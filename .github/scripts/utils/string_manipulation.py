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
