#!/usr/bin/env python
# coding: utf-8

import json
import os
import json
import jsonpath_ng

# # Only for the examples in the end:
# from json_manipulation import JSONManipulationFormatter
# from json_manipulation import conditions_ontology_validation

# ------#
# PlantUMLFormatter Class
# ------#

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
def jsonexpression_condition_dict(condition_dict: dict) -> jsonpath_ng.jsonpath.Descendants:
    """
    Function that generates a JSON expression for 'jsonjsonpath_ng' based on a given
        dictionary with conditions (condition_dict).

    Expression purpose based on the given dict:
        - { "property_names": [...] } --> the expression will match properties named as every item in the list.
    """
    for key, value in condition_dict.items():
        # The syntax of the condition_dict is made-up
        if key == "property_names":
            if not isinstance(value, list):
                raise ValueError(
                    f"The value for the key 'property_names' in the 'condition_dict' needs to be of type list"
                    f"\n\tGiven value: {value}"
                )

            # We create the JSON path expression based on the syntax, giving the whole list (value) as property names
            jsonpath_expression = jsonpath_ng.parse(f"$..{value}")

            return jsonpath_expression

        else:
            raise TypeError(
                f"The given dictionary containing the conditions to check has an unexpected syntax."
                f"\n\tCheck the possibilities in function 'jsonexpression_condition_dict()' and add yours"
                f"\n\tif it is not an expected error."
            )

def create_parent_json_paths(input_list: list) -> list:
    """
    From a given input list whose items are JSON Paths, returns a list with both the given
        JSON Paths and an extra JSON path for depth level in the JSON object.

    Example: from an 'input_list' ["data.cellTypes.cellType"], it would return an updated_list
        being ["data.cellTypes.cellType", "data.cellTypes", "data"]

    Intended purpose: to add all parent-properties JSON paths of a given JSON path leaf.
    """
    n_items = len(input_list)
    updated_list = []
    for i in range(n_items + 1):
        list_index = i + 1
        # We iterate over the list and create a new list (path)
        #   with all items (properties) up to the range.
        updated_list.append(input_list[0:list_index])

    return updated_list

def find_json_paths(json_data: dict, condition_dict: dict) -> list:
    """
    Find all JSON paths in a JSON object that match a set of conditions. The set of conditions
        is a dictionary with a syntax specific to function 'jsonexpression_condition_dict()'
    """
    jsonpath_expression = jsonexpression_condition_dict(condition_dict)
    matches = jsonpath_expression.find(json_data)
    list_of_paths = list(str(match.full_path) for match in matches)
    return list_of_paths

def create_highlights_liner(json_path_str: str) -> str:
    """
    Formats the JSON Path with the preffix and newline for PlantUML
    """
    return "#highlight " + json_path_str + "\n"

def remove_char_from_list(input_list: list, char: str) -> list:
    """
    Removes a given character (char) from a given list (input_list)
    """
    updated_list = list(item.replace(char, "") for item in input_list)
    return updated_list

def add_char_to_list(input_list: list,  char: str) -> list:
    """
    Adds a given character (char) at the beginning and end of a given list (input_list)
    """
    updated_list = list(char + item + char for item in input_list)
    return updated_list

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

    def __init__(
        self, json_filepath: str = None, json_data: dict = None
    ):

        self.load_json_data(json_filepath=json_filepath, json_data=json_data)
        self.empty_jsonpath_list()
        self.empty_highlight_header_list()
        self.highlights_header = ""

    def load_json_data(self, json_filepath: str = None, json_data: dict = None) -> dict:
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
            raise KeyError(
                f"KeyError: {e}"
            )

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

    def save_all(
        self, output_filepath: str, overwrite: bool = False
    ) -> None:
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

# -#
# Examples of usage
# -#
# formatter = JSONManipulationFormatter(json_filepath="../../examples/json_validation_tests/sample_valid-1.json")
# json_data = formatter.current_json

# header = PlantUMLFormatter(json_data=json_data)
# header.add_jsonpaths(condition_dict=conditions_ontology_validation)
# header.format_json_paths(plantUML_format_dictionary=plantUML_format_dictionary)
# header.create_highlights_header()
# header.save_all(output_filepath="output_sample.json", overwrite=True)

# # Example of usage: reducing the JSON object after creating the header:
# formatter.reduce_depth(desired_depth=2)
# json_data = formatter.current_json

# header.load_json_data(json_data=json_data)
# header.save_all(output_filepath="reduced_output_sample.json", overwrite=True)
