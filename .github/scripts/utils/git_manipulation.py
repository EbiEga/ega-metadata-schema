# ------ #
# Utils for Git Manipulation
# ------ #
# In this file there are functions, classes or variables that are used widely
#   in the GitHub actions of this repository and imported accordingly in other
#   scripts.

# - #
# System imports
# - #
import git
import os
import requests
from typing import Union
import urllib.request

# -#
# Helper functions
# -#
def get_current_branch(directory_path: str) -> Union[str, None]:
    """
    Returns the name of the active branch of a given directory.
    """
    try:
        repo = git.Repo(directory_path, search_parent_directories=True)
        return repo.active_branch.name

    except git.InvalidGitRepositoryError:
        print(f"The given directory ('{directory_path}') is neither a valid Git repository nor has a parent directory that is.")
        return None
    

def load_main_json(file_path: str, base_url: str = None) -> dict:
    """
    Given a file path, returns the loaded JSON file of its version of the "main" branch of the ega-metadata-schema repository
    """
    if base_url is None:
        base_url = os.getenv('BASE_URL')
        if base_url is None:
            raise EnvironmentError(
                "The environment variable 'BASE_URL' is not set. "
                "Please set this variable to the base URL for your repository, e.g., "
                "'https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main'"
            )

    file_extension = os.path.splitext(file_path)[1].lower()
    if not file_extension == ".json":
        raise ValueError(f"Given file path is not of a JSON file: {file_path}")

    url = f"{base_url}/{file_path}"
    response = requests.get(url)
    if not response.status_code == requests.codes.ok:
        error_message = (
            f"The GET request was not successful: the status code was '{response.status_code}' when trying to"
            f" fetch file '{os.path.basename(file_path)}' from the repository at the given URL: {url}"
        )
        raise requests.HTTPError(error_message)
    return response.json()

def fetch_and_copy_files(
    directory_to_copy: str,
    destination_directory_name: str = "./",
    repository_url: str = "https://api.github.com/repos/EbiEga/ega-metadata-schema",
    verbose: bool = False,
    branch: str = "main"
    ):
    """
    Given a repository URL and its directory to copy, it copies the contents to another given destination directory.
    """
    # Fetch the contents of the directory from the GitHub API
    api_url = f"{repository_url}/contents/{directory_to_copy}?ref={branch}"
    response = requests.get(api_url)
    if response.status_code == 200:
        files = response.json()
        for file in files:
            filename = file["name"]
            download_url = file["download_url"]
            destination_file = os.path.join(destination_directory_name, filename)
            
            try:
                with urllib.request.urlopen(download_url) as response:
                    with open(destination_file, 'wb') as output_file:
                        output_file.write(response.read())
                if verbose:
                    print(f"File '{filename}' copied successfully.")
            except urllib.error.HTTPError as e:
                raise RuntimeError(f"Error copying file '{filename}': {e}")
            except Exception as e:
                raise RuntimeError(f"An error occurred while copying file '{filename}': {e}")
    else:
        raise RuntimeError(f"Failed to fetch directory contents from '{repository_url}': {response.status_code} - {response.text}")
