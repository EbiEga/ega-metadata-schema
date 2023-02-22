# ------ #
# Utils for PlantUML format
# ------ #
# In this file there are functions, classes or variables that are used widely
#   in the GitHub actions of this repository and imported accordingly in other
#   scripts.

# - #
# System imports
# - #
import json
import os
from typing import Union
from .json_manipulation import create_parent_json_paths, \
    find_json_paths

from .string_manipulation import remove_char_from_list, \
    add_char_to_list, \
    create_highlights_liner

# -#
# Hardcoded values
# -#
plantUML_format_dictionary = {
    "strings_to_strip": ["[", "]"],
    "property_quote": '"',
    "highlight_separator": " / "
}

# -#
# Helper functions
# -#


# -#
# Class definition
# -#
class PlantUMLFormatter:
    """
    PlantUMLFormatter - a class for for converting JSON objects to PlantUML syntax.

    Arguments:
    - json_filepath (str): a string representing the path to the JSON file to be loaded.
        The file must be of type .json. The file is only used if "json_data" was not given.
    - json_data (dict): a dictionary representing the JSON data to be used.
    """

    def __init__(self, json_filepath: str = "", json_data: Union[dict, None] = None):

        self.load_json_data(json_filepath=json_filepath, json_data=json_data)
        self.empty_jsonpath_list()
        self.empty_highlight_header_list()
        self.highlights_header = ""

    def load_json_data(self, json_filepath: str = "", json_data: Union[bool, None] = None) -> dict:
        """
        Loads JSON data from either a file or a dictionary.
            It's used not only at the definition of the class, but also can be used later on
            to modify the original JSON once the highlight header has been created. This allows to
            highlight a reduced version of a JSON object

            For example: if we highlight by 'termId' as property name, but want to highlight a
                smaller JSON object, we could create the header with the full JSON object, and then
                replace the saved JSON as a smaller version of it.
        """
        # We either take the given JSON data or load the given JSON file
        if isinstance(json_data, dict):
            self.original_json = json_data

        elif json_filepath:
            file_extension = os.path.splitext(json_filepath)[1].lower()
            if not os.path.isfile(json_filepath) or not file_extension == ".json":
                raise ValueError(
                    f"The given JSON filepath ('{json_filepath}') was not a file or is not a JSON file (*.json)."
                )
            self.json_filepath = json_filepath
            with open(json_filepath, "r", encoding="utf-8") as json_file:
                self.original_json = json.load(json_file)

        else:
            raise TypeError(
                f"Expected either a JSON file ({json_filepath}) or JSON data and neither of them were provided."
            )

    def empty_jsonpath_list(self) -> None:
        """
        Empties the JSON Paths list (self.jsonpaths_list)
        """
        self.jsonpaths_list = []

    def empty_highlight_header_list(self) -> None:
        """
        Empties the list with JSON Paths in highlight format (self.highlight_header_list)
        """
        self.highlight_header_list = []

    def add_jsonpaths(self, condition_dict: dict) -> list:
        """
        Adds to the list of JSON Paths (self.jsonpaths_list) new paths based on given conditions
            from a condition dictionary.
        """
        new_json_paths = find_json_paths(
            json_data=self.original_json, condition_dict=condition_dict
        )

        # Avoid duplication of JSON Paths
        for new_json_path in new_json_paths:
            if new_json_path not in self.jsonpaths_list:
                self.jsonpaths_list.append(new_json_path)

        return self.jsonpaths_list

    def format_json_paths(
        self, plantUML_format_dictionary: dict, add_parent_properties: bool = True
    ) -> list:
        """
        Formats the list of JSON Paths (self.jsonpaths_list) into PlantUML syntax, populating the list
            of formatted JSON paths for highlights (self.highlight_header_list)
        """
        # We get the parameters of the plantUML format dictionary
        try:
            strings_to_strip = plantUML_format_dictionary["strings_to_strip"]  # e.g. ["[", "]"]
            property_quote = plantUML_format_dictionary["property_quote"]      # e.g. '"'
            separator = plantUML_format_dictionary["highlight_separator"]      # e.g. " / "

        except KeyError as e:
            raise KeyError( f"KeyError: {e}" )

        if len(self.jsonpaths_list) == 0:
            self.highlight_header_list = []
            return self.highlight_header_list

        # We separate each item of the JSON path
        paths = list(path.split(".") for path in self.jsonpaths_list)

        # And now format them in the correct PlantUML highlighting syntax
        if strings_to_strip is not None and isinstance(strings_to_strip, list):
            for string in strings_to_strip:
                paths = list(remove_char_from_list(path, string) for path in paths)

        if add_parent_properties:
            # Now we are going to add the parental paths so that they are also highlighted
            #   instead of just having the leaves highlighted
            for path in paths:
                full_path_list = create_parent_json_paths(path)
                for n_path in full_path_list:
                    if n_path not in paths:
                        paths.append(n_path)

        paths = list(add_char_to_list(path, property_quote) for path in paths)
        paths = list(separator.join(path) for path in paths)
        self.highlight_header_list = paths

        return self.highlight_header_list

    def create_highlights_header(self) -> str:
        """
        Creates the header based on the list of one-liners for the PlantUML highlights
        """
        self.highlights_header = "".join(
            create_highlights_liner(json_path_str)
            for json_path_str in self.highlight_header_list
        )
        return self.highlights_header

    def save_all(self, output_filepath: str, overwrite: bool = False) -> None:
        """
        Saves the JSON object with the correct start and end of file and its header
            Example: PlantUMLFormatter.save_all()
        """
        if os.path.isfile(output_filepath) and not overwrite:
            raise ValueError(
                f"File '{output_filepath}' already exists and 'overwrite' was set to False.\n "
                f"\tChoose a different filename or set overwrite to True."
            )

        with open(output_filepath, "w", encoding="utf-8") as f:
            # Move the file pointer to the beginning of the file and we add the PlantUML syntax one-liner
            f.seek(0, 0)
            f.write("@startjson\n")

            # We then add the header
            f.write(self.highlights_header)
            f.write("\n")

            # Then the JSON file per se
            f.write(json.dumps(self.original_json, indent=4))

            # And finally "@endjson" to the end of the file
            f.write("\n@endjson")
