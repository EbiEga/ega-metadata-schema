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
    

def load_main_json_schema(file_path: str) -> dict:
    """
    Given a file path, returns the loaded JSON file of its version of the "main" branch of the ega-metadata-schema repository
    """
    file_extension = os.path.splitext(file_path)[1].lower()
    if not file_extension == ".json":
        raise ValueError(f"Given file path is not of a JSON file: {file_path}")
    file_name = os.path.basename(file_path)
    url = f"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/{file_name}"
    response = requests.get(url)
    if response.status_code != 200:
        raise FileNotFoundError(f"Given file was not found in the repository's main branch (https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas): {file_name}")
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
