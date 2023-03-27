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
from typing import Union


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