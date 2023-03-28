# ------ #
# Utils for String Manipulation
# ------ #
# In this file there are functions, classes or variables that are used widely
#   in the GitHub actions of this repository and imported accordingly in other
#   scripts.

# - #
# System imports
# - #
import re


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
    The pattern allows for the three main elements: major version; minor version; and patch version; as well
        as optional additions like: Pre-release version and Build metadata.
    """
    semver_regex = r'^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$'
    match = re.match(semver_regex, version_string)
    there_was_match = match is not None
    return there_was_match


def is_higher_version(o_lower_version: str, o_higher_version:str) -> bool:
    """
    Compare two strings that follow the semantic versioning specification.
    Returns:
        - True if "o_higher_version" is greater than "o_lower_version".
        - False otherwise.
    """
    # Double check that they do follow semantic versioning
    if not is_semantic_version(o_lower_version):
        raise ValueError(
            f"The given lower version ('{o_lower_version}') does not follow semantic versioning."
        )
    if not is_semantic_version(o_higher_version):
        raise ValueError(
            f"The given higher version ('{o_higher_version}') does not follow semantic versioning."
        )

    # Strip off any pre-release version and build metadata
    lower_version = o_lower_version.split('+')[0].split('-')[0]
    higher_version = o_higher_version.split('+')[0].split('-')[0]

    # Split the version strings into their components (major, minor, patch)
    higher_version_l = [int(v) for v in higher_version.split('.')]
    lower_version_l = [int(v) for v in lower_version.split('.')]

    # Compare the major version numbers
    if higher_version_l[0] > lower_version_l[0]:
        return True
    elif higher_version_l[0] < lower_version_l[0]:
        return False

    # Compare the minor version numbers
    if higher_version_l[1] > lower_version_l[1]:
        return True
    elif higher_version_l[1] < lower_version_l[1]:
        return False

    # Compare the patch version numbers
    if higher_version_l[2] > lower_version_l[2]:
        return True
    elif higher_version_l[2] < lower_version_l[2]:
        return False

    # The versions are identical
    return False