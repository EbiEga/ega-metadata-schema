import os
import argparse

from utils.git_manipulation import fetch_and_copy_files

# Script used to copy all files within a GitHub directory to a local directory.
#   Example: to download JSON Examples from "main" during a GitHub workflow.

# --- #
# Initial arguments
# --- #
parser = argparse.ArgumentParser(
    description="Copies all files from within a directory of a GitHub repository into a local directory (e.g. all JSON files from within './examples/json_validation_tests').",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    "--input_directory",
    type=str,
    required=True,
    help='The path to a directory within the GitHub repository whose files will be copied. Example: "./examples/json_validation_tests"',
)
parser.add_argument(
    "--destination_directory",
    type=str,
    required=True,
    help='The path to the local directory to which all files will be copied. Example: "./"',
)
parser.add_argument(
    "--branch",
    type=str,
    required=False,
    default="main",
    help='The branch of the GitHub repository to use. Default: "main"',
)
args = parser.parse_args()

# # Check the integrity of the given arguments
if not isinstance(args.input_directory, str):
    raise ValueError("input_directory must be a string.")
if not isinstance(args.destination_directory, str):
    raise ValueError("destination_directory must be a string.")
if not isinstance(args.branch, str):
    raise ValueError("branch must be a string.")

# --- #
# Copying the files
# --- #
def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")

create_directory(args.destination_directory)
fetch_and_copy_files(
    destination_directory_name=args.destination_directory,
    directory_to_copy=args.input_directory,
    verbose=True
)