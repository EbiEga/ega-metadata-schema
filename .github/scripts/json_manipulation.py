#!/usr/bin/env python
# coding: utf-8

import json
import os
import jsonref
from pathlib import Path
import json

# ------#
# JSONManipulationFormatter Class
# ------#

# -#
# Hardcoded values
# -#
# Used to simplify the graph based on depth
mapping_property_names = {
    "list": "[ ... ]",
    "dict": "{ ... }",
}

# Different condition_dict dictionaries for filtering a JSON object
conditions_cardinality = { "property_names": [ "objectId", "rSource", "rTarget", "rType" ] }

conditions_controlled_vocabulary = { "property_names": [ "enum" ] }

conditions_ontology_validation = { "property_names": [ "termId" ] }

# -#
# Helper functions
# -#
def max_depth(json_obj: dict) -> int:
    """
    Function to find the maximum depth of a JSON object
    """
    if isinstance(json_obj, dict):
        return 1 + max(max_depth(v) for v in json_obj.values())
    elif isinstance(json_obj, list):
        return 1 + max(max_depth(v) for v in json_obj)
    else:
        return 0

def new_dict_depth(json_object_value: dict, depth: int, mapping_property_names: dict):
    """
    Recursive function to create, based on a given dictionary, a shorter version of it based on its depth.
    """
    property_type = type(json_object_value)
    if property_type == dict and depth > 0:
        new_dict = {}
        for key, value in json_object_value.items():
            new_dict[key] = new_dict_depth(
                json_object_value=value,
                depth=depth - 1,
                mapping_property_names=mapping_property_names
            )

        return new_dict

    elif property_type == list and depth > 0:
        new_list = []
        for item in json_object_value:
            item_content = new_dict_depth(
                json_object_value=item,
                depth=depth - 1,
                mapping_property_names=mapping_property_names
            )
            new_list.append(item_content)
        return new_list

    elif property_type == str or property_type == bool or property_type == int:
        return json_object_value

    else:
        property_type = type(json_object_value).__name__
        if property_type in mapping_property_names.keys():
            property_type = mapping_property_names[property_type]

        return property_type

def check_condition_dict(original_key, original_value, condition_dict:dict) -> bool:
    """
    Function that checks if a given key and value of a dictionary satisfy conditions based
        on a dictionary with conditions (condition_dict)

    Stablished conditions:
        - { "property_names": [...] } --> If any item in the list ([...]) matches a property name.
                Can be used, for example, to check if the given key matches any of the strings
                within the given list.
    """
    satsified_conditions = False
    for key, value in condition_dict.items():
        # The syntax of the condition_dict is made-up
        if key == "property_names":
            if not isinstance(value, list):
                raise ValueError(
                    f"The value for the key 'property_names' in the 'condition_dict' needs to be of type list"
                    f"\n\tGiven value: {value}"
                )
            for property_name in value:
                if original_key == property_name:
                    satsified_conditions = True
                    return satsified_conditions
        else:
            raise TypeError(
                    f"The given dictionary containing the conditions to check has an unexpected syntax."
                    f"\n\tCheck the possibilities in function 'check_condition_dict()' and add yours"
                    f"\n\tif it is not an expected error."
                )


def filter_dict(original_dict: dict, condition_dict: dict) -> dict:
    """
    Recursive function that, given a dictionary to filter (original_dict) and a dictionary
        with conditions for the former to satisfy (condition_dict), iterates over the
        original_dict to create a subset of the original dictionary based on conditions
        to match within the condition_dict.
    """
    current_dict = {}
    for key, value in original_dict.items():
        condition_matches = check_condition_dict(
            original_key=key,
            original_value=value,
            condition_dict=condition_dict
        )

        if condition_matches:
            # keep only branches that satisfy the conditions
            current_dict[key] = value

        elif isinstance(value, dict):
            # recursively filter sub-dictionaries
            filtered = filter_dict(value, condition_dict)
            if filtered:
                current_dict[key] = filtered

        elif isinstance(value, list):
            # recursively filter each element of the list
            filtered_list = []
            for item in value:
                if isinstance(item, dict):
                    filtered = filter_dict(item, condition_dict)
                    if filtered:
                        filtered_list.append(filtered)

                # For now we haven't encountered a use-case where an item is not a dict
                #   and we are still interested. But if that use-case appears, add here
                #   how to satisfy the condition of those items based on the use-case

            # If the list exists, containing some matching branches
            if filtered_list:
                current_dict[key] = filtered_list

    return current_dict

def add_char_to_str(string: str, str_length: int = 80, new_character: str = "\\n") -> str:
    """
    Function that, given a string, splits it into words and inserts a new character (new_character)
        the the character count of the words is above the given maximum string length (str_length)
    """
    assert isinstance(string, str), f"The given string '{string}' is not of string type."
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

# -#
# Class definition
# -#
class JSONManipulationFormatter:
    """
    JSONManipulationFormatter - a class for formatting JSON data to be used in graphing software. Examples
        of formatting include: reducing the depth of a JSON object, resolving its references,
        filtering the JSON object based on set of conditions, etc.

    Arguments:
    - json_filepath (str): a string representing the path to the JSON file to be loaded. The file must be of type .json.
    - json_data (dict): a dictionary representing the JSON data to be used.
    - is_schema (bool): a boolean flag that specifies whether the given JSON is a schema or not.
    """

    def __init__(
        self, json_filepath: str = None, json_data: dict = None, is_schema: bool = None
    ):

        # We either take the given JSON data or load the given JSON file
        if json_data:
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
                f"Class JSONManipulationFormatter expects either a JSON file or JSON data and neither of them were provided."
            )

        self.current_json = self.original_json.copy()

        # Whether the given JSON is a schema or the data
        if is_schema is None:
            self.identify_schema_or_data()
        elif is_schema:
            self.is_schema = True
        elif not is_schema:
            self.is_schema = False

    def prettify(self) -> str:
        """
        Returns a string representation of the current JSON object formatted as a string in
            a more human-readable way: with newlines and indentation.
            Example: JSONManipulationFormatter.prettify()
        """
        return json.dumps(self.current_json, indent=4)

    def max_depth(self) -> int:
        """
        Returns an integer that represents the maximum depth of the current JSON object.
            Example: JSONManipulationFormatter.max_depth()
        """
        return max_depth(self.current_json)

    def identify_schema_or_data(self) -> bool:
        """
        Determines whether the loaded JSON data is a JSON schema or JSON data. It is based on the
            top-level properties of the JSON object:
            - If the JSON data has the properties "data" and "schema" at the top-level, it is
                considered a data object.
            - If it has any other properties, it is considered a schema object.
        """
        properties_at_root = list(self.current_json.keys())
        if properties_at_root == ["data", "schema"]:
            self.is_schema = False
        else:
            self.is_schema = True

        return self.is_schema

    def restart_json(self) -> dict:
        """
        Restarts the current JSON to the original JSON.
            Example: JSONManipulationFormatter.restart_json()
        """
        self.current_json = self.original_json.copy()

        return self.current_json

    def resolve_json_references(
        self, json_filepath: str = None, resolve_schema_prop: bool = False
    ) -> dict:
        """
        Replaces all references ('$ref') in the JSON with their resolved values using the jsonref library.
            If the JSON has inter-file references, the json_filepath argument must be provided.
            If 'resolve_schema_prop' is True, it will resolve also the 'schema' property within a JSON data.

            Example: JSONManipulationFormatter.resolve_json_references(json_filepath="/path/to/file.json")
        """
        # We need the absolute path for jsonref to be able to resolve inter-file references
        #   See https://jsonref.readthedocs.io/en/v1.0.0b1/#a-note-on-base-uri
        if isinstance(json_filepath, str):
            absolute_file_path = Path(json_filepath).absolute()
        elif isinstance(self.json_filepath, str):
            absolute_file_path = Path(self.json_filepath).absolute()
        else:
            raise TypeError(
                f"In order to resolve references it is necessary to know the filepath of the used file "
                f"(in case of inter-file references), but none was given.\nProvide it with 'json_filepath' "
                f"or initialise the class again providing a 'json_filepath'."
            )

        base_uri = absolute_file_path.as_uri()

        if not type(self.current_json) == dict:
            raise ValueError(
                f"The pre-loaded JSON data for file '{absolute_file_path}' is not of type dictionary."
            )

        # If the JSON is not a schema, it's better to empty the whole "schema" property.
        #    otherwise, it provides the whole referenced schema, being too much information
        self.identify_schema_or_data()
        if not self.is_schema and not resolve_schema_prop:
            schema_property_content = self.current_json["schema"]
            self.current_json["schema"] = ""

        resolved_json_data = jsonref.replace_refs(self.current_json, base_uri=base_uri)
        self.current_json = resolved_json_data

        # We give the content of "schema" back
        if not self.is_schema and not resolve_schema_prop:
            self.current_json["schema"] = schema_property_content

        return self.current_json

    def reduce_depth(self, desired_depth: int) -> dict:
        """
        Reduces the current JSON object to the desired amount of depth.
            Example: JSONManipulationFormatter.reduce_depth(desired_depth=3)
        """
        current_depth = max_depth(self.current_json)
        if current_depth < desired_depth:
            self.restart_json()
        self.current_json = new_dict_depth(
            json_object_value=self.current_json,
            depth=desired_depth,
            mapping_property_names=mapping_property_names
        )

        return self.current_json

    def subset_json(self, condition_dict: dict) -> dict:
        """
        Subsets the current JSON object based on a set of conditions given in the condition_dict.
            Example: JSONManipulationFormatter.subset_json(condition_dict=cardinality_dict)
            Example of cardinality_dict:
                cardinality_dict = { "property_names": [ "objectId", "rSource", "rTarget", "rType" ] }
        """
        self.current_json = filter_dict(
            original_dict=self.current_json, condition_dict=condition_dict
        )
        return self.current_json

    def add_newlines(
        self, str_length: int = 80, newline_character: str = "\\n"
    ) -> dict:
        """
        Adds newlines ('\\n') to long strings in the JSON object so that it is easier to interpret.
            Example: JSONManipulationFormatter.add_newlines(str_length=80, newline_character="\\n")
        """
        self.current_json = add_newlines(
            current_value=self.current_json,
            str_length=str_length,
            newline_character=newline_character
        )

        return self.current_json

    def save_json(
        self,
        output_filepath: str,
        overwrite: bool = False
    ) -> None:
        """
        Saves the JSON object to a file.
            Example: JSONManipulationFormatter.save_json()
        """
        if os.path.isfile(output_filepath) and not overwrite:
            raise ValueError(
                f"File '{output_filepath}' already exists and 'overwrite' was set to False.\n "
                f"\tChoose a different filename or set overwrite to True."
            )

        with open(output_filepath, "w", encoding="utf-8") as outfile:
            json.dump(self.current_json, outfile, indent=4)

# -#
# Examples of usage
# -#

# formatter = JSONManipulationFormatter(json_filepath="../../examples/json_validation_tests/sample_valid-1.json")
# null = formatter.resolve_json_references()
# formatter.subset_json(condition_dict=conditions_cardinality)
# print(formatter.prettify())

# formatter.restart_json()
# formatter.reduce_depth(2)
# print(formatter.prettify())

# formatter.restart_json()
# formatter.subset_json(condition_dict=conditions_cardinality)
# print(formatter.prettify())

# formatter.restart_json()
# formatter.subset_json(condition_dict=conditions_controlled_vocabulary)
# print(formatter.prettify())

# formatter.restart_json()
# formatter.subset_json(condition_dict=conditions_ontology_validation)
# print(formatter.prettify())

# formatter.restart_json()
# formatter.add_newlines()
# print(formatter.prettify())
