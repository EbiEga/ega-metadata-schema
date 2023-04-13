import argparse
import os
from utils.json_manipulation import JSONManipulationFormatter

# Script used to modify the static pointers (e.g. "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json")
#   of the JSON schemas and documents. For further details, please check: https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/releases

# --- #
# Initial arguments
# --- #
parser = argparse.ArgumentParser(
    description="Modifies the static pointers of JSON schemas and documents in a given directory, following EGA's format. Check main use-case at https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/releases."
)
parser.add_argument(
    "--input_directory",
    type=str,
    required=True,
    help='The filepath to a directory that contains the JSON documents or schemas to modify. Example: "examples/json_validation_tests/"',
)
parser.add_argument(
    "--output_directory",
    type=str,
    help='The filepath to a directory in which the modified JSON files will be stored. If missing, the original ones will be overwritten. Example: "examples/modified_jsons/".',
)
parser.add_argument(
    "--new_str",
    type=str,
    required=True,
    help='The string that will be replacing the element right after the "previous_str" in the static pointers. Examples: "v1.0.0" or "M-casado"',
)
parser.add_argument(
    "--previous_str",
    type=str,
    default="ega-metadata-schema",
    help='The string that will be used to locate what is replaced: the element that comes right after this "previous_str" in the static pointers. Example: "ega-metadata-schema" when changing branch names, or "EbiEga" when changing owners of the repository.',
)
args = parser.parse_args()

# Check the integrity of the given arguments
if not isinstance(args.input_directory, str):
    raise ValueError("input_directory must be a string.")
if not os.path.exists(args.input_directory) or not os.path.isdir(args.input_directory):
    raise ValueError(
        f"The provided directory path '{args.input_directory}' does not exist or it's not a directory"
    )
if not isinstance(args.new_str, str):
    raise ValueError("new_str must be a string.")
if not isinstance(args.previous_str, str):
    raise ValueError("previous_str must be a string.")

# If the output directory was not given, we use the input and overwrite them
if args.output_directory:
    if not isinstance(args.output_directory, str):
        raise ValueError("output_directory must be a string.")
    if not os.path.exists(args.output_directory):
            os.makedirs(args.output_directory)
else:
    args.output_directory = args.input_directory

# --- #
# JSON file modification
# --- #
for file in os.scandir(args.input_directory):
    if file.name.endswith(".json") and file.is_file():
        filepath = file.path
        formatter = JSONManipulationFormatter(json_filepath=filepath)
        formatter.modify_static_pointers(
            new_str=args.new_str,
            previous_str=args.previous_str
        )
        new_filename = os.path.join(args.output_directory, file.name)
        formatter.save_json(output_filepath=new_filename, overwrite=True)