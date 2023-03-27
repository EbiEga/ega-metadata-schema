import os
from datetime import datetime
import argparse

from utils.git_manipulation import get_current_branch
from utils.json_manipulation import JSONManipulationFormatter, \
    check_previous_project_versions, \
    find_same_version
from utils.string_manipulation import is_semantic_version
from utils.json_validation import validate_json

# Script used to update the version manifest (./docs/releases) with the versions of the JSON schemas. For further details, please check:
#   https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/biovalidator_benchmarks

# --------- #
# Handling arguments
# --------- #
parser = argparse.ArgumentParser(
    description="Updates the version manifest file with the version of the project (i.e. branch name) and the version of each JSON schema. Check details at https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/releases."
)
parser.add_argument(
    "--schemas_dir",
    type=str,
    default="./schemas",
    help='The path to the schema directory. Default: "./schemas"',
)
parser.add_argument(
    "--version_manifest_dir",
    type=str,
    default="./docs/releases",
    help='The path to the version manifest directory. Default: "./docs/releases"',
)
parser.add_argument(
    "--new_release_version",
    type=str,
    default=None,
    help='Semantic version of the new project release version to use instead of the current branch name. Do NOT use unless you know exactly what you are doing: to comply with the release workflow, the version should normally be taken from the branch name. Default: None',
)
parser.add_argument(
    "--overwrite_mode",
    action="store_true",
    default=False,
    help="A boolean switch by which we tell the script to overwrite an existing release if found with the same name. Only use this option if you know for a fact that you want to overwrite an existing version (e.g. one that was created at the start of a PR that you want to overwrite manually at the end of the PR review)",
)
args = parser.parse_args()

# Check the integrity of the given arguments
if not isinstance(args.schemas_dir, str):
    raise ValueError(f"Schemas directory (--schemas_dir) must be a string.")
if not os.path.exists(args.schemas_dir) or not os.path.isdir(args.schemas_dir):
    raise ValueError(
        f"The provided directory path '{args.schemas_dir}' does not exist or it's not a directory."
    )
if not isinstance(args.version_manifest_dir, str):
    raise ValueError(f"Version manifest directory (--version_manifest_dir) must be a string.")
if not os.path.exists(args.version_manifest_dir) or not os.path.isdir(args.version_manifest_dir):
    raise ValueError(
        f"The provided directory path '{args.version_manifest_dir}' does not exist or it's not a directory."
    )

# - #
# Hardcoded values
# - #
version_manifest_file = f"{args.version_manifest_dir}/version_manifest.json"
version_manifest_schemafile = f"{args.version_manifest_dir}/VM_schema.json"
f_extension = ".json"

# --------- #
# Running update of the version file
# --------- #
if not args.new_release_version:
    current_branch_name = get_current_branch(".")
else:
    current_branch_name = args.new_release_version
today = datetime.today().strftime('%Y-%m-%d')
version_dict = {}

# We check that the branch name complies with semantic versioning
if current_branch_name.startswith("v"):
    # We get rid of the "v" string that represents the "version", since this won't go into the version manifest
    current_branch_name = current_branch_name[1:]
if not is_semantic_version(current_branch_name):
    raise ValueError(
        f"The current branch ('{current_branch_name}') does not follow the expected semantic versioning (e.g. 2.0.1)."
    )

# Load the version manifest
version_obj = JSONManipulationFormatter(json_filepath=version_manifest_file)

# If overwrite_mode is True, we pop out the existing release with the same version
if args.overwrite_mode:
    # There shouldn't be more than one duplicate, so no need for a "while" loop here, technically
    same_version_index = find_same_version(
        version_manifest_json=version_obj.current_json,
        new_version=current_branch_name
    )
    # If the same project release version was found, we remove it
    if same_version_index:
        releases = version_obj.current_json["releases"]    
        del releases[same_version_index]
        version_obj.current_json["releases"] = releases

# We check that the new version (e.g. 2.0.1) is higher than the existing ones (e.g. 2.0.0)
new_is_higher = check_previous_project_versions(version_manifest_json=version_obj.current_json, new_version=current_branch_name)
if not new_is_higher:
    raise ValueError(
        f"The version represented by the branch name ({current_branch_name}) was lower or equal than one in the existing "
        f"version manifest. In order to comply with semantic versioning, new ones should always be higher."
        f"\n\tTo raise an issue when this happens, you can add 'strict_mode=True' to check_previous_project_versions()."
    )

# We collect all the versions from the existing releases
for file in os.scandir(args.schemas_dir):
    if not file.path.endswith(f_extension):
        continue
    found_files = True
    file_basename = os.path.splitext(file.name)[0]
    object_name = file_basename.replace("EGA.", "")
    
    json_obj = JSONManipulationFormatter(json_filepath=file.path)
    version_dict[object_name] = json_obj.version

# If the dict is empty
if not version_dict:
    raise ValueError(
        f"There were no '{f_extension}' files to get versions from in the given schema directory ('{args.schemas_dir}')."
    )

# We create the dictionary of the property for the new release
new_release_dict = {}
new_release_dict["version"] = current_branch_name
new_release_dict["date"] = today
new_release_list = []

for obj_name, obj_version in version_dict.items():
    obj_dir = {}
    obj_dir["schemaName"] = obj_name
    obj_dir["version"] = obj_version
    new_release_list.append(obj_dir)
new_release_dict["jsonSchemas"] = new_release_list

# We add the new release to the version manifest and validate it
version_obj.current_json["releases"].append(new_release_dict)
json_schema = JSONManipulationFormatter(json_filepath=version_manifest_schemafile)
validation_result = validate_json(json_obj=version_obj.current_json, json_schema=json_schema.current_json, strict_mode=True)

# Finally, we save it
if validation_result:
    version_obj.save_json(output_filepath=version_manifest_file, overwrite=True)