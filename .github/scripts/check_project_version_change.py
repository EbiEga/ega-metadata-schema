import argparse

from utils.git_manipulation import get_current_branch, \
    load_main_json
from utils.json_manipulation import get_highest_version_index
from utils.string_manipulation import is_semantic_version, \
    compare_semantic_versions

# Script used to check whether the change in version of the project is major or 
#   not.
# For further details, please check:
#   https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/releases

# --------- #
# Handling arguments
# --------- #
parser = argparse.ArgumentParser(
    description="Checks whether the change in version of the project is major (returning 'Major') or not (returning either 'Minor' or 'Patch'). The version change is defined as the difference in semantic versionings between the 'current branch' (e.g. '1.0.0') and the highest version within the version_manifest file (e.g. '0.0.0'). The script can be used to check whether backwards compatibility needs to be test: only if a non-major change occurs in the project. Check further details at https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/releases."
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
    "--set_output_gh_action",
    type=str,
    required=False,
    help='The variable name that is used to set the output of the script. Only used if present, and should only be present if the script is being used in a GitHub workflow, so that this one can use the output for other jobs/steps. Example: "version_change_type"',
)
args = parser.parse_args()

# Check the integrity of the given arguments
if not isinstance(args.version_manifest_dir, str):
    raise ValueError(f"Version manifest directory (--version_manifest_dir) must be a string.")
if args.new_release_version:
    if not is_semantic_version(args.new_release_version):
        raise ValueError(f"The given new release version ('{args.new_release_version}') does not follow semantic versioning.")

# --------- #
# Main function for the check
# --------- #
def set_output(name: str, value):
    """
    Function to set the output of the script within the environment of a GitHub workflow, for the variable (i.e. name
        and value) to be used by other jobs/runs/steps.
    """
    try:
        output_file = os.environ['GITHUB_OUTPUT']
    except KeyError:
        raise KeyError("The 'GITHUB_OUTPUT' environment variable is not set. Perhaps you are running option '--set_output_gh_action' outside of a GitHub workflow.")
    
    with open(output_file, 'a') as fh:
        print(f'{name}={value}', file=fh)

def main(args: argparse.Namespace) -> bool:
    # Hardcoded values
    schema_repo_filepath = "."
    releases_array_keyword = "releases"
    version_keyword = "version"
    version_manifest_file = f"{args.version_manifest_dir}/version_manifest.json"

    # We get the new version of the project
    if not args.new_release_version:
        new_version = get_current_branch(directory_path = schema_repo_filepath)
        if not is_semantic_version(new_version):
            raise ValueError(f"The current branch name ('{new_version}') does not follow semantic versioning.")
    else:
        new_version = args.new_release_version

    main_version_manifest_json = load_main_json(file_path = version_manifest_file)

    # We get the highest version of all the releases within the manifest file
    highest_version_index = get_highest_version_index(version_manifest_json=main_version_manifest_json)
    highest_version = main_version_manifest_json[releases_array_keyword][highest_version_index][version_keyword]

    # Time to compare the new and old versions, to assert that the new is higher
    new_is_higher, change_type = compare_semantic_versions(
        old_version=highest_version,
        new_version=new_version
    )
    if not new_is_higher:
        raise ValueError(
            f"The version represented by the branch name ({new_version}) was lower or equal than one in the existing "
            f"version manifest ({highest_version}). In order to comply with semantic versioning, new ones should always be higher."
        )
    
    return change_type

if __name__ == "__main__":
    version_check_type = main(args)
    if args.set_output_gh_action:
        # We set the output for the GitHub workflow
        set_output(name=args.set_output_gh_action, value=version_check_type)
    else:
        print(version_check_type)
