# ------ #
# Utils for JSON Manipulation
# ------ #
# In this file there are functions, classes or variables that are used widely
#   in the GitHub actions of this repository and imported accordingly in other
#   scripts.

# - #
# System imports
# - #
import json
import os
import jsonref
import jsonpath_ng
import warnings

from pathlib import Path
from typing import Union
from .string_manipulation import add_newlines, \
    is_semantic_version, \
    is_higher_version

# - #
# Hardcoded values
# - #
# Used to simplify the graph based on depth
mapping_property_names = {
    "list": "[ ... ]",
    "dict": "{ ... }",
}

# Different condition_dict dictionaries for filtering a JSON object
conditions_cardinality = {"property_names": [ "objectId", "rSource", "rTarget", "rType" ]}
conditions_controlled_vocabulary = {"property_names": [ "enum" ]}
conditions_ontology_validation = {"property_names": [ "termId" ]}

# - #
# Helper functions
# - #
def jsonexpression_condition_dict(
    condition_dict: dict
) -> jsonpath_ng.jsonpath.Descendants:
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


def check_condition_dict(original_key: str, original_value, condition_dict: dict) -> bool:
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


def find_json_paths(json_data: dict, condition_dict: dict) -> list:
    """
    Find all JSON paths in a JSON object that match a set of conditions. The set of conditions
        is a dictionary with a syntax specific to function 'jsonexpression_condition_dict()'
    """
    jsonpath_expression = jsonexpression_condition_dict(condition_dict)
    matches = jsonpath_expression.find(json_data)
    list_of_paths = list(str(match.full_path) for match in matches)
    return list_of_paths


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
            original_key=key, original_value=value, condition_dict=condition_dict
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


def new_dict_depth(json_object_value: dict, depth: int, mapping_property_names: dict):
    """
    Recursive function to create, based on a given dictionary, a shorter version of it based on a given depth.
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


def load_json(json_filepath: str) -> dict:
    """
    Function to load a JSON file and returns it as a python dictionary.
    """
    file_extension = os.path.splitext(json_filepath)[1].lower()
    if not os.path.isfile(json_filepath) or not file_extension == ".json":
        raise ValueError(
            f"File '{json_filepath}' does not exist, is not a file, or is not a JSON file"
        )
    with open(json_filepath, "r") as json_file:
        json_data = json.load(json_file)
    return json_data


def empty_json_values(json_data, root_level: bool = False):
    """
    Function to empty all values within a given JSON object (dictionary), but keeping its structure.
        Alternatively, "root_level" can be True so that the "schema" property is not erased at root level.
    """
    if isinstance(json_data, dict):
        for key in json_data:
            if root_level and key == "schema":
                # We don't want to get rid of the "$ref" within the schema
                continue
            json_data[key] = empty_json_values(json_data[key])
    elif isinstance(json_data, list):
        for i in range(len(json_data)):
            json_data[i] = empty_json_values(json_data[i])
    elif isinstance(json_data, str):
        json_data = ""
    elif isinstance(json_data, int):
        json_data = 0

    return json_data


def check_previous_project_versions(version_manifest_json: dict, new_version: str, strict_mode: bool = False) -> bool:
    """
    Given a newer version string (e.g. '1.0.0'), checks that it is higher than all existing project versions
        in the given version_manifest_json file.
    """
    if not isinstance(version_manifest_json, dict):
        err_type = type(version_manifest_json)
        raise TypeError(
                f"The given Version Manifest JSON (type: {err_type}) needs to be dictionary type."
            )
    if not is_semantic_version(new_version):
        raise ValueError(
            f"The given version ('{new_version}') does not follow the expected semantic versioning."
        )

    # We iterate over each release within the version manifest
    for release in version_manifest_json["releases"]:
        existing_release_version = release["version"]
        if not is_semantic_version(existing_release_version):
            raise ValueError(
                f"Found issue when parsing the version manifest: one of the versions ('{existing_release_version}') does not follow the expected semantic versioning."
                f"\n\t- Release:\n{release}"
            )
            
        if not is_higher_version(o_lower_version=existing_release_version, o_higher_version=new_version):
            if strict_mode:
                raise ValueError(
                    f"Found issue when comparing the version manifest and the newer version: one of the versions is higher than or equal to the newer version."
                    f"\n\t- Given newer version: {new_version}"
                    f"\n\t- Existing version that is higher: {existing_release_version}"
                    f"\n\t- Full existing release details:\n{release}"
                )
            return False
    
    # If all were lower than the newer one
    return True


def find_same_version(version_manifest_json: dict, new_version: str) -> Union[int, None]:
    """
    Returns the index of the release in the Version Manifest whose "version" matches the
        given "new_version". Returns None otherwise.
    """
    if not isinstance(version_manifest_json, dict):
        err_type = type(version_manifest_json)
        raise TypeError(
                f"The given Version Manifest JSON (type: {err_type}) needs to be dictionary type."
            )
    if not is_semantic_version(new_version):
        raise ValueError(
            f"The given version ('{new_version}') does not follow the expected semantic versioning."
        )

    releases = version_manifest_json["releases"]
    for i in range(len(releases)):
        if releases[i]['version'] == new_version:
            return i
        
    return None


# - #
# Class definition
# - #
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
        self, json_filepath: str = "", json_data: dict = {}, is_schema: Union[bool, None] = None 
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
        elif is_schema == True:
            self.is_schema = True
        elif not is_schema == False:
            self.is_schema = False
        else:
            raise ValueError(
                f"The given 'is_schema' value ({is_schema}) was not None, True or False."
            )

        # We extract the Schema version
        self.add_version()

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
            - If the JSON data has property "$id" at its root, it is considered data.
            - If it has any other properties, it is considered a schema object.
        """
        properties_at_root = list(self.current_json.keys())
        if "$id" in properties_at_root:
            self.is_schema = True
        else:
            self.is_schema = False

        return self.is_schema

    def restart_json(self) -> dict:
        """
        Restarts the current JSON to the original JSON.
            Example: JSONManipulationFormatter.restart_json()
        """
        self.current_json = self.original_json.copy()

        return self.current_json

    def resolve_json_references(
        self, json_filepath: str = "", resolve_schema_prop: bool = False
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
    
    def add_version(self, version_keyword: str = "meta:version"):
        """
        Finds the version of the JSON object if it is a schema.
        """
        if self.is_schema:
            self.version = self.current_json[version_keyword]
            if not is_semantic_version(self.version):
                raise ValueError(
                    f"The found version of the JSON object does not follow semantic versioning.\n"
                    f"\t- Found version: '{self.version}'\n"
                    f"\t- Used keyword to get the version: '{version_keyword}'"
                )

    def save_json(self, output_filepath: str, overwrite: bool = False) -> None:
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


class CreateObjectSet:
    """
    The CreateObjectSet class is used to create a new JSON object set by using an existing JSON file as a template.
        The new object set can have new JSON objects added to it, and can also have the values of its properties cleared.
        The idea is to use one of the object-sets in the 'example/json_validation_tests' directory as a template for a new object-set.

    For further details, please check:
        https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/biovalidator_benchmarks
    """
    def __init__(
        self,
        template_doc: str
    ):
        """
        Initialize the class with the path to a template JSON file.

            :param template_doc: str : path to the template JSON file
        """
        self.template_doc = template_doc
        self.data_name = "data"
        self.objectArray_name = "objectArray"

        # Load the template object-set file
        self.template_json_obj = load_json(self.template_doc)

    def empty_objectArray(self):
        """
        Empties the "objectArray" list in the template JSON object. Used prior new additions to an existing template
        """
        self.template_json_obj[self.data_name][self.objectArray_name].clear()

    def empty_all_properties(self):
        """
        Will empty the objectArray property and all other properties in the template will lose their values
        """
        self.empty_objectArray()
        self.template_json_obj = empty_json_values(
            self.template_json_obj, root_level=True
        )

    def add_new_json(
        self,
        new_json: Union[str,dict]
    ):
        """
        Adds a new JSON object to the "objectArray" list of the template JSON object.

            :param new_json: [str,dict] : either the path to the template JSON file or the loaded JSON file
        """
        if isinstance(new_json, str):
            new_data = load_json(new_json)
        elif isinstance(new_json, dict):
            new_data = new_json
        else:
            raise ValueError(
                f"New JSON to be added '{new_json}' must be either the filepath to a JSON document or the loaded dictionary of a JSON"
            )

        # If we are using a JSON with the "data" and "schema" structure, we only keep the data
        if "schema" in new_data and "data" in new_data:
            new_data = new_data["data"]

        self.template_json_obj[self.data_name][self.objectArray_name].append(new_data)

    def count_n_objects(self):
        """
        Returns the number of objects (i.e. items) in the 'objectArray' array of the template JSON
        """
        n_of_objects = len(
            self.template_json_obj[self.data_name][self.objectArray_name]
        )
        return n_of_objects

    def save_json(
        self,
        output_filepath: str = "new_object-set.json",
        add_suffix: bool = False,
        overwrite: bool = False
    ):
        """
        Saves the JSON object to a file.

            :param output_filepath: str : the filepath that the saved file will have
            :param add_suffix: bool : whether the new filepath will have an added suffix with the number of objects it contains
            :param overwrite: bool : whether the saved file is allowed to overwrite an existing file or not
        """
        if add_suffix:
            split_filename = os.path.splitext(output_filepath)
            suffix = "_" + str(self.count_n_objects())
            output_filepath = split_filename[0] + suffix + split_filename[1]

        if os.path.isfile(output_filepath) and not overwrite:
            warnings.warn(
                f"File '{output_filepath}' already exists and 'overwrite' was set to False. Choose a different filename or set overwrite to True.",
                UserWarning
            )
            return

        with open(output_filepath, "w") as outfile:
            json.dump(self.template_json_obj, outfile, indent=4)
