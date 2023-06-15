import os
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
    "--git_var_name",
    type=str,
    default=None,
    help='The variable name (e.g. "VERSION_CHANGE") to which the output of this script will be associated. This variable will be written within the GitHub environment, so this option should only be used in a GitHub environment (e.g. in a GH workflow). Default: None',
)
parser.add_argument(
    "--verbose",
    action="store_true",
    default=False,
    help="A boolean switch by which we tell the script to print more information along the way.",
)
args = parser.parse_args()

# Check the integrity of the given arguments
if not isinstance(args.version_manifest_dir, str):
    raise ValueError(f"Version manifest directory (--version_manifest_dir) must be a string.")
if args.new_release_version:
    if not is_semantic_version(args.new_release_version):
        raise ValueError(f"The given new release version ('{args.new_release_version}') does not follow semantic versioning.")

def print_verbose(text: str, verbose: bool):
    """
    Function that prints messages based on the script's verbose level
    """
    if verbose:
        print(text)

# --------- #
# Main function for the check
# --------- #
def main(args: argparse.Namespace) -> bool:
    # Hardcoded values
    schema_repo_filepath = "."
    releases_array_keyword = "releases"
    version_keyword = "version"
    version_manifest_file = f"{args.version_manifest_dir}/version_manifest.json"

    # We get the new version of the project
    if not args.new_release_version:
        new_version = get_current_branch(directory_path = schema_repo_filepath)
        if new_version.startswith("v"):
            # We get rid of the "v" string that represents the "version"
            new_version = new_version[1:]
        if not is_semantic_version(new_version):
            raise ValueError(f"The current branch name ('{new_version}') does not follow semantic versioning.")
    else:
        new_version = args.new_release_version


    main_version_manifest_json = load_main_json(file_path = version_manifest_file)

    # We get the highest version of all the releases within the manifest file
    highest_version_index = get_highest_version_index(version_manifest_json=main_version_manifest_json)
    highest_version = main_version_manifest_json[releases_array_keyword][highest_version_index][version_keyword]
    print_verbose(
        f"- Comparison of versions:"
        f"\tThe new version is '{new_version}'"
        f"\tThe highest existing version in the version manifest is '{highest_version}'",
        args.verbose
    )

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
    
    print_verbose(
        f"- The change type is '{change_type}'",
        args.verbose
    )

    return change_type

if __name__ == "__main__":
    version_check_type = main(args)
    if not args.git_var_name:
        print(version_check_type)
    else:
        # If we were given the variable name for the Github env, we associate
        #   the value to it by writting it to the GitHub env. file
        #   See: https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/
        with open(os.getenv('GITHUB_ENV'), 'a') as env_file:
            env_file.write(f"{args.git_var_name}={version_check_type}\n")

