import os
from datetime import datetime
import argparse
import warnings

from utils.git_manipulation import get_current_branch
from utils.json_manipulation import JSONManipulationFormatter, \
    check_previous_project_versions, \
    find_same_version, \
    get_highest_version_index
from utils.string_manipulation import is_semantic_version, \
    get_keys_for_diff_values, \
    compare_semantic_versions
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

# We collect all the versions from the existing objects
for file in os.scandir(args.schemas_dir):
    if not file.path.endswith(f_extension):
        continue
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
new_release_dict["allJsonSchemas"] = version_dict

# We create the "changedJsonSchemas" by comparing the existing highest version and the new one
existing_releases = version_obj.current_json["releases"]
highest_version_index = get_highest_version_index(version_manifest_json=version_obj.current_json)
if highest_version_index is not None:
    highest_release = existing_releases[highest_version_index]
    try:
        highest_allJsonSchemas = highest_release["allJsonSchemas"]
    except:
        raise Exception(
            f"The project release of the highest version ({highest_release['version']}) did not have 'allJsonSchemas' as its keyword."
            f" This may suggest that there was something wrong with the way the last release was written into the version manifest."
            f" The new release will have nothing to compare to when checking what object versions changed between releases."
        )
    # We get the objects that differ in versions
    new_allJsonSchemas = new_release_dict["allJsonSchemas"]
    diff_keys_list = get_keys_for_diff_values(dict1=highest_allJsonSchemas, dict2=new_allJsonSchemas)

    if len(diff_keys_list) == 0:
        warnings.warn(
                f"WARNING: When comparing releases {new_release_dict['version']} and {highest_release['version']},"
                f" there were no differences in the individual object schema versions."
                f" This could reflect an issue in the individual object versions, unless the project new"
                f" version was pushed to change something that is not related to the JSON schemas.",
                UserWarning
            )

    # We iterate over the objects with diff. versions, creating "changedJsonSchemas"
    changed_version_dict = {}
    for object_name in diff_keys_list:
        new_is_higher, version_change = compare_semantic_versions(
            old_version=highest_allJsonSchemas[object_name],
            new_version=new_allJsonSchemas[object_name]
        )
        if not new_is_higher:
            raise ValueError(
                f"When comparing releases {new_release_dict['version']} and {highest_release['version']}, the version of the object '{object_name}' was"
                f" not complying with the project release (i.e. the new object version was not higher):\n"
                f"\t- Project version {new_release_dict['version']}: '{object_name}' {new_allJsonSchemas[object_name]}\n"
                f"\t- Project version {highest_release['version']}: '{object_name}' {highest_allJsonSchemas[object_name]}"
            )
        changed_version_dict[object_name] = new_allJsonSchemas[object_name]
        
    new_release_dict["changedJsonSchemas"] = changed_version_dict

    # We remove the "allJsonSchemas" from the last release: only the new one will keep this property
    del highest_release['allJsonSchemas']
    existing_releases[highest_version_index] = highest_release
else:
    new_release_dict["changedJsonSchemas"] = version_dict

# We add the new release to the version manifest (on the top - position 0, to be easier to read and parse) and validate it
version_obj.current_json["releases"].insert(0, new_release_dict)
json_schema = JSONManipulationFormatter(json_filepath=version_manifest_schemafile)
validation_result = validate_json(json_obj=version_obj.current_json, json_schema=json_schema.current_json, strict_mode=True)

# Finally, we save it
if validation_result:
    version_obj.save_json(output_filepath=version_manifest_file, overwrite=True)