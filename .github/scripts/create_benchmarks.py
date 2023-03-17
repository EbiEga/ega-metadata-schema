import argparse
import os
from utils.validation_statistics import JSONBatchValidationStats

# Script used to record validation parameters of JSON documents. For further details, please check:
#   https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/biovalidator_benchmarks

# --- #
# Initial arguments
# --- #
parser = argparse.ArgumentParser(
    description="Create benchmarks for a Biovalidator server. Check details at https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/biovalidator_benchmarks."
)
parser.add_argument(
    "--endpoint",
    type=str,
    required=True,
    help='The endpoint of the Biovalidator server. Example: "http://localhost:3020/validate"',
)
parser.add_argument(
    "--input_directory",
    type=str,
    required=True,
    help='The filepath to a directory that contains the JSON documents to validate. Example: "examples/json_validation_tests/"',
)
parser.add_argument(
    "--output_directory",
    type=str,
    default="./",
    help='The filepath to a directory in which the results will be stored. Example: "2023_benchmarks/". Default value: "./"',
)
parser.add_argument(
    "--number_of_iterations",
    type=int,
    default=1,
    help="The amount of iterations of validation of each JSON document within the input directory. Example: 10. Default value: 1",
)
parser.add_argument(
    "--n_parallel_threads",
    type=int,
    default=1,
    help="The amount of parallel threads for each validation iteration. Example: 5. Default value: 1",
)
parser.add_argument(
    "--stop_at_errors",
    action="store_true",
    default=False,
    help="A boolean switch by which we tell the script to stop the execution when a validation error is raised.",
)
parser.add_argument(
    "--not_just_summary_df",
    action="store_true",
    default=False,
    help="A boolean switch by which we tell the script to not just print the summary dataframe with parameters, but instead save the parameters in files and generate a README.",
)
parser.add_argument(
    "--only_print_complete_df",
    action="store_true",
    default=False,
    help="A boolean switch by which we tell the script that we do not want any files to be saved and, instead, we just want the complete table of parameters to be printed.",
)
args = parser.parse_args()

# Check the integrity of the given arguments
if not isinstance(args.endpoint, str):
    raise ValueError("endpoint must be a string.")
if not isinstance(args.input_directory, str):
    raise ValueError("input_directory must be a string.")
if not os.path.exists(args.input_directory) or not os.path.isdir(args.input_directory):
    raise ValueError(
        f"The provided directory path '{args.input_directory}' does not exist or it's not a directory"
    )
if not isinstance(args.output_directory, str):
    raise ValueError("output_directory must be a string.")
if not isinstance(args.number_of_iterations, int):
    raise ValueError("number_of_iterations must be an integer.")
if not args.number_of_iterations > 0:
    raise ValueError("number_of_iterations must be an integer greater than 0.")
if not isinstance(args.n_parallel_threads, int):
    raise ValueError("n_parallel_threads must be an integer.")
if not args.n_parallel_threads > 0:
    raise ValueError("n_parallel_threads must be an integer greater than 0.")
if not isinstance(args.stop_at_errors, bool):
    raise ValueError("stop_at_errors must be a boolean.")
if not isinstance(args.not_just_summary_df, bool):
    raise ValueError("not_just_summary_df must be a boolean.")
if not isinstance(args.only_print_complete_df, bool):
    raise ValueError("only_print_complete_df must be a boolean.")

# --- #
# Stats collection
# --- #
batch_validator = JSONBatchValidationStats(
    input_directory=args.input_directory,
    output_directory=args.output_directory,
    endpoint=args.endpoint,
    stop_at_errors=args.stop_at_errors
)

# We validate all files "number_of_iterations" times, with "n_parallel_threads" parallel threads,
#   populating the "batch_validator.complete_df" dataframe
batch_validator.iterate_over_dir(
    n_iterations=args.number_of_iterations,
    n_parallel_threads=args.n_parallel_threads
)

# We get the populated complete dataframe and generate the summary one
batch_validator.join_validation_stats()

# We save the dataframes if applicable
if args.only_print_complete_df:
    print(batch_validator.complete_df.to_string(index=False))
    exit(0)

elif not args.not_just_summary_df:
    print(batch_validator.summary_df.to_string(index=False))
    exit(0)

# If we reached this point, we create all files and save them
batch_validator.create_output_dir()
batch_validator.save_dataframe_csv(
    dataframe=batch_validator.complete_df, 
    ilename="complete_df.csv"
)
batch_validator.save_dataframe_csv(
    dataframe=batch_validator.summary_df, 
    filename="summary_df.csv"
)

batch_validator.create_3d_scatter_plot()
batch_validator.create_2d_density_graphs()
batch_validator.create_2d_scatter_graphs()
batch_validator.create_summary_readme()
