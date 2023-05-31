import os
import argparse

from utils.string_manipulation import validate_json_file_path, \
    compare_semantic_versions
from utils.json_manipulation import JSONManipulationFormatter
from utils.git_manipulation import load_main_json_schema

# Script used to check whether the change in version of the JSON schemas (compared to branch 'main') complies with semantic versioning
# For further details, please check:
#   https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/releases

# --------- #
# Handling arguments
# --------- #
parser = argparse.ArgumentParser(
    description="Checks that the given 'JSON Schemas' change in version, with respect to the 'main' branch, complying with semantic versioning. Check details at https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/releases",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    "--files",
    nargs='+',
    help='List of modified JSON file paths',
)
parser.add_argument(
    "--strict_mode",
    action="store_true",
    default=False,
    help="A boolean switch that, if present, will make the script raise issues when JSON Schema files with non-compliant semantic versionings are found.",
)
parser.add_argument(
    "--set_output_gh_action",
    type=str,
    required=False,
    help='The variable name that is used to set the output of the script. Only used if present, and should only be present if the script is being used in a GitHub workflow, so that this one can use the output for other jobs/steps. Example: "version_needs_to_be_checked"',
)
args = parser.parse_args()

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


# --------- #
# Main function for the check
# --------- #
def main(args: argparse.Namespace) -> bool:
    """
    Performs the check to determine whether the change in version of the JSON schemas (compared to branch 'main') complies with semantic versioning.

    Args:
        args (argparse.Namespace): Command-line arguments passed to the script.

    Returns:
        version_needs_to_be_checked: boolean value that will determine whether one of the files complying with semantic versioning (i.e. its version
            is higher in the new file) has a minor/patch change, and thus should trigger a validation step of all the files just to be sure
            about backwards compatibility.
    """
    files = args.files
    strict_mode = args.strict_mode
    version_needs_to_be_checked = False

    for file_path in files:
        file_name = os.path.basename(file_path)
        try:
            # Load new and old JSON and compare their versions
            validate_json_file_path(file_path)
            new_json_formatter = JSONManipulationFormatter(json_filepath=file_path)

            old_json = load_main_json_schema(file_path)
            old_json_formatter = JSONManipulationFormatter(json_data=old_json)

            is_higher, expected_diff = compare_semantic_versions(
                old_version=old_json_formatter.version,
                new_version=new_json_formatter.version
            )
            if not is_higher:                
                raise ValueError(
                    f"Found issue when comparing two versions of the JSON schema ({file_name}): the newer version is not higher than older version."
                    f"\n\t- Newer version found in the PR:\t\t{new_json_formatter.version}"
                    f"\n\t- Existing version in the 'main' branch:\t{old_json_formatter.version}"
                )

            print(f"For file '{file_name}' the version change is {old_json_formatter.version} -> {new_json_formatter.version}")
            # If the change is not "Major", we need to check the combinations: New Schemas-Old examples and New examples-Old Schemas
            if expected_diff in ["Minor", "Patch"]:
                version_needs_to_be_checked = True

        except Exception as e:
            if strict_mode:
                raise e
            else:
                print(f"Warning: {e}")

    return version_needs_to_be_checked

if __name__ == "__main__":
    version_check_required = main(args)
    if args.set_output_gh_action:
        # We set the output for the GitHub workflow
        set_output(name=args.set_output_gh_action, value=version_check_required)
    else:
        print(version_check_required)

