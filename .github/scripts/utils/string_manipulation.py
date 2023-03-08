# ------ #
# Utils for String Manipulation
# ------ #
# In this file there are functions, classes or variables that are used widely
#   in the GitHub actions of this repository and imported accordingly in other
#   scripts.

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