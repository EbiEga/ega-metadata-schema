import json
import os
import warnings
from typing import Union

# Module used to create custom Object-sets. For further details, please check:
#   https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/biovalidator_benchmarks


def keep_data_prop(new_json: dict) -> dict:
    """
    Function to only keep the property "data" at root level, and nothing else of the loaded JSON dict
    """
    data_property_name = "data"
    if not isinstance(new_json, dict):
        raise ValueError(
            "new_json must be a loaded JSON object (i.e. dictionary)."
        )
    if not data_property_name in new_json:
        raise ValueError(
            f"new_json does not contain '{data_property_name}' property at root level"
        )
    modified_json = new_json.pop(data_property_name, None)

    return modified_json

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


class CreateObjectSet:
    """
    The CreateObjectSet class is used to create a new JSON object set by using an existing JSON file as a template.
        The new object set can have new JSON objects added to it, and can also have the values of its properties cleared.
        The idea is to use one of the object-sets in the 'example/json_validation_tests' directory as a template for a new object-set.
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
            new_data = keep_data_prop(new_data)

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
