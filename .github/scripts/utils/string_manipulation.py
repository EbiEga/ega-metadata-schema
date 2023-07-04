# ------ #
# Utils for String Manipulation
# ------ #
# In this file there are functions, classes or variables that are used widely
#   in the GitHub actions of this repository and imported accordingly in other
#   scripts.

# - #
# System imports
# - #
import os
from typing import Union
import semver

# -#
# Helper functions
# -#
def add_newlines(current_value, str_length: int = 80, newline_character: str = "\\n"):
    """
    Recursive function that iterates over a given value (e.g. a loaded JSON) and
        changes the values of all strings whose lenght is above the given maximum
        string length (str_length).

    In our use-case, it is used to add new lines for the graphs to be readable in case
        some strings (e.g. 'description' fields) are way too long.
    """
    if isinstance(current_value, dict):
        new_dict = {}
        for key, value in current_value.items():
            new_dict[key] = add_newlines(
                current_value=value,
                str_length=str_length,
                newline_character=newline_character
            )
        return new_dict

    elif isinstance(current_value, list):
        new_list = []
        for item in current_value:
            item_content = add_newlines(
                current_value=item,
                str_length=str_length,
                newline_character=newline_character
            )
            new_list.append(item_content)
        return new_list

    elif isinstance(current_value, str):
        if len(current_value) > str_length:
            current_value = add_char_to_str(
                string=current_value,
                str_length=str_length,
                new_character=newline_character
            )

        return current_value

    else:
        return current_value

def remove_char_from_list(input_list: list, char: str) -> list:
    """
    Removes a given character (char) from a given list (input_list)
    """
    updated_list = list(item.replace(char, "") for item in input_list)
    return updated_list


def create_highlights_liner(json_path_str: str) -> str:
    """
    Formats the JSON Path with the preffix and newline for PlantUML
    """
    return "#highlight " + json_path_str + "\n"


def add_char_to_list(input_list: list, char: str) -> list:
    """
    Adds a given character (char) at the beginning and end of a given list (input_list)
    """
    updated_list = list(char + item + char for item in input_list)
    return updated_list


def add_char_to_str(
    string: str, str_length: int = 80, new_character: str = "\\n"
) -> str:
    """
    Function that, given a string, splits it into words and inserts a new character (new_character)
        the the character count of the words is above the given maximum string length (str_length)
    """
    assert isinstance(
        string, str
    ), f"The given string '{string}' is not of string type."
    words = string.split()
    new_string = ""
    line_length = 0
    for word in words:
        if line_length + len(word) > str_length:
            if not len(word) > str_length:
                # We don't want new lines at the beginning in words that are too long (e.g. '$ref')
                new_string += new_character
            line_length = 0
        new_string += word + " "
        line_length += len(word) + 1

    updated_string = new_string.strip()

    return updated_string

def is_semantic_version(version_string: str) -> bool:
    """
    Checks whether a given string matches semantic versioning pattern (e.g. "1.1.1" is correct; "hello-world" is not).
    The pattern is defined by semver module (https://github.com/python-semver/python-semver) and allows for the three
    main elements (major, minor, and patch) as well as optional additions like Pre-release and Build metadata.
    """
    try:
        # Raises a ValueError if not following semantic versioning
        semver.parse_version_info(version_string)
        return True
    except ValueError:
        return False
    
def get_keys_for_diff_values(dict1, dict2):
    """
    Returns a list containing the keys whose values differed in the two given dictionaries
    """
    if not isinstance(dict1, dict):
        err_type = type(dict1)
        raise TypeError(
                f"The given 'dict1' (type: {err_type}) needs to be dictionary type."
            )
    if not isinstance(dict2, dict):
        err_type = type(dict2)
        raise TypeError(
                f"The given 'dict2' (type: {err_type}) needs to be dictionary type."
            )
    if set(dict1.keys()) != set(dict2.keys()):
        raise ValueError("The two dictionaries have different keys.")
    keys_with_diff_values = []
    for key in dict1.keys():
        if dict1[key] != dict2[key]:
            keys_with_diff_values.append(key)
    return keys_with_diff_values


def replace_after_string_in_url(url: str, new_str: str, previous_str: str = "ega-metadata-schema") -> str:
    """
    Replaces the string following "previous_str" with the "new_str" in the given "url",
        after splitting the "url" by "/".
        Example URL:
            "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json"
    There are two main use-cases:
        1. Modifying the branch name in a GitHub URL with a new branch name by giving the repo name
            (e.g. "ega-metadata-schema") as the "previous_str" and another branch name as "new_str" (e.g. "v1.0.0")
        2. Modifying the owner of a repository (e.g. in a forked repo) by giving "raw.githubusercontent.com"
            as the "previous_str" and another username as "new_str" (e.g. M-casado).
    """
    parts = url.split("/")
    new_parts = []
    if not previous_str in parts:
        raise ValueError(
            f"The given 'previous_str' ('{previous_str}') was not found as an element within the given URL ('{url}'). Amend this issue"
            f" by providing an existing string within the url.."
            f"\n\tFull list of URL elements: {parts}"
        )
    elif previous_str == "":
        raise ValueError(
            f"The given 'new_str' ('{previous_str}') is an empty string."
        )
    for part in parts:
        if new_parts and new_parts[-1] == previous_str:
            # If the previous item was the "previous_str", we don't get this "part", but the new string instead
            new_parts.append(new_str)
        else:
            new_parts.append(part)
    
    return "/".join(new_parts)


def validate_json_file_path(file_path: str) -> None:
    """
    Validates if a file exists and is a JSON file
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    file_extension = os.path.splitext(file_path)[1].lower()
    if not file_extension == ".json":
        raise ValueError(f"File is not a JSON file: {file_path}")
    

def compare_semantic_versions(old_version: str, new_version: str) -> Union[bool, str]:
    """
    Compares two given semantic versions and returns a tuple with a boolean indicating if the new version is higher
    and the type of change (Major, Minor, Patch, or Invalid) between them.
    
    Args:
        old_version (str): The old version string to be compared, following semantic versioning.
        new_version (str): The new version string to be compared, following semantic versioning.
    
    Returns:
        Tuple[bool, str]: A tuple containing:
            - A boolean value indicating if the new version is higher than the old version.
            - A string representing the type of change between the versions: "Major", "Minor", "Patch", or "Invalid".
            
    Raises:
        ValueError: If either the old_version or new_version does not follow the semantic versioning format.
    """
    if not is_semantic_version(old_version):
        raise ValueError(f"The given old version ('{old_version}') does not follow semantic versioning.")
    if not is_semantic_version(new_version):
        raise ValueError(f"The given new version ('{new_version}') does not follow semantic versioning.")
    
    # Semver.compare output:
    #   0 if the versions are equal; a negative integer if the first version is smaller; a positive integer if the first version is bigger.
    is_higher = semver.compare(new_version, old_version) > 0
    version_change = "Invalid"

    if is_higher:
        old_ver_info = semver.parse_version_info(old_version)
        new_ver_info = semver.parse_version_info(new_version)

        if new_ver_info.major > old_ver_info.major:
            version_change = "Major"
        elif new_ver_info.minor > old_ver_info.minor:
            version_change = "Minor"
        elif new_ver_info.patch > old_ver_info.patch:
            version_change = "Patch"

    return is_higher, version_change
