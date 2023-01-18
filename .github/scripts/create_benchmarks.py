import os
import json
import requests
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from typing import Tuple

# Module used to record validation parameters of JSON documents. For further details, please check:
#   https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/biovalidator_benchmarks

#---#
# Initial arguments
#---#
parser = argparse.ArgumentParser(description='Create benchmarks for a Biovalidator server. Check details at https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/biovalidator_benchmarks.')
parser.add_argument('--endpoint', type=str, required=True, help='The endpoint of the Biovalidator server. Example: "http://localhost:3020/validate"')
parser.add_argument('--input_directory', type=str, required=True, help='The filepath to a directory that contains the JSON documents to validate. Example: "examples/json_validation_tests/"')
parser.add_argument('--output_directory', type=str, default='./', help='The filepath to a directory in which the results will be stored. Example: "2023_benchmarks/". Default value: "./"')
parser.add_argument('--number_of_iterations', type=int, default=1, help='The amount of iterations of validation of each JSON document within the input directory. Example: 10. Default value: 1')
parser.add_argument('--stop_at_errors', action='store_true', default=False, help='A boolean switch by which we tell the script to stop the execution when a validation error is raised.')
parser.add_argument('--not_just_summary_df', action='store_true', default=False, help='A boolean switch by which we tell the script to not just print the summary dataframe with parameters, but instead save the parameters in files and generate a README.')
parser.add_argument('--only_print_complete_df', action='store_true', default=False, help='A boolean switch by which we tell the script that we do not want any files to be saved and, instead, we just want the complete table of parameters to be printed.')

args = parser.parse_args()

# Check the integrity of the given arguments
if not isinstance(args.endpoint, str):
    raise ValueError("endpoint must be a string.")
if not isinstance(args.input_directory, str):
    raise ValueError("input_directory must be a string.")
if not os.path.exists(args.input_directory) or not os.path.isdir(args.input_directory):
    raise ValueError(f"The provided directory path '{args.input_directory}' does not exist or it's not a directory")
if not isinstance(args.output_directory, str):
    raise ValueError("output_directory must be a string.")
if not isinstance(args.number_of_iterations, int):
    raise ValueError("number_of_iterations must be an integer.")
if not args.number_of_iterations > 0:
    raise ValueError("number_of_iterations must be an integer greater than 0.")
if not isinstance(args.stop_at_errors, bool):
    raise ValueError("stop_at_errors must be a boolean.")
if not isinstance(args.not_just_summary_df, bool):
    raise ValueError("not_just_summary_df must be a boolean.")
if not isinstance(args.only_print_complete_df, bool):
    raise ValueError("only_print_complete_df must be a boolean.")

#---#
# Functions
#---#
def get_current_timestamp() -> str:
    """
    Returns the current timestamp in the format of 'year-month-day hour:minute:second' (e.g. '2022-06-23 12:34:56')
    """
    current_time = datetime.now()
    formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_timestamp


def df_to_markdown_table(dataframe: pd.DataFrame) -> str:
    """
    Returns a markdown formatted table from a dataframe
    """
    markdown_params = {"showindex": False, "tablefmt": "pipe"}
    table = dataframe.to_markdown(**markdown_params)
    return table

#---#
# Classes
#---#
class JSONDocValidationStats:
    """
    A class used to send a JSON document against an validation endpoint.
    
    This class takes in a JSON document filepath and an endpoint, and uses methods to send the JSON document and record certain parameters (e.g. validation time).
    
    Attributes:
        json_doc (str): the JSON document filepath to validate (e.g. 'dataset-valid-1.json').
        endpoint (str): the endpoint to which the JSON document will be sent to be validated (e.g. 'http://biovalidator.ega.ebi.ac.uk/validate')
        stop_at_errors (bool): whether the class should raise an exception when the endpoint response contains an error or not.
    
    Example:
        validate = JSONDocValidationStats(
            json_doc='dataset-valid-1.json',
            endpoint='http://localhost:3020/validate',
            stop_at_errors=False)

        useful_parameters = [validate.passed_validation, validate.validation_time, validate.n_data_properties, validate.n_ontology_properties, validate.validation_outcome]
    """
    def __init__(self, json_doc:str, endpoint:str = "http://biovalidator.ega.ebi.ac.uk/validate", stop_at_errors:bool = False):
        self.endpoint = endpoint
        self.initiate_json_tree = True
        with open(json_doc) as json_file:
            self.json_dict = json.load(json_file)
        
        self.validate_json()
        if self.validation_outcome == []:
            self.passed_validation = True
        else:
            self.passed_validation = False
            if stop_at_errors:
                self.prettified_validation_outcome = json.dumps(self.validation_outcome, indent=4)
                raise Exception(f"JSON file '{json_doc}' did not pass validation. Reported errors:\n{self.prettified_validation_outcome}")        
        
        self.n_data_properties, self.n_ontology_properties = self.count_properties(json_dict=self.json_dict)
        
    def validate_json(self):
        """ 
        Validates a json document by sending a post request to the specified endpoint, the json document is passed as the json payload and saves the response in json format as well as the time it took to get the response
        """
        start_time = datetime.now()
        response = requests.post(self.endpoint, json=self.json_dict)
        end_time = datetime.now()

        self.validation_outcome = response.json()
        self.validation_time = (end_time - start_time).total_seconds()

    def count_properties(self, json_dict: dict) -> Tuple[int,int]:
        """
        Counts all the keys in a JSON object including nested keys and properties with the name "termId".
            Properties named "termId" denote that the parent property is an ontologyTerm following EGA's JSON schemas and allows us to count them.
        """
        term_id_count = 0
        count = 0
        root_level = False
        
        if self.initiate_json_tree:
            json_dict = self.json_dict
            root_level = True
            self.initiate_json_tree = False
        
        if type(json_dict) == dict:        
            for key in json_dict:
                if key == "schema" and root_level:
                    # We avoid counting the properties of the "schema" at root level
                    continue
                    
                if key == "termId":
                    term_id_count += 1

                sub_count, sub_term_id_count = self.count_properties(json_dict[key])
                count += sub_count
                term_id_count += sub_term_id_count

                count += 1        
        
        elif type(json_dict) == list:
            # Cases in which the content is an array (list)
            for item in json_dict:
                sub_count, sub_term_id_count = self.count_properties(item)
                count += sub_count
                term_id_count += sub_term_id_count
            
        else:
            # Cases like "str", "bool", "None", etc.
            return 0, 0
            
        return count, term_id_count

class JSONBatchValidationStats:
    """
    A class that makes use of JSONDocValidationStats class to validate in batch all JSON files in a directory and record useful parameters of it for display.
    
    This class takes in some input data and performs some action on it. It has a few methods that can be used to process the data in different ways.
    
    Attributes:
        input_data (str): The input data that the class will process.
    
    Example:
        my_class = MyClass("some input data")
        my_class.process_data()
    """
    def __init__(self, 
                 input_directory:str,
                 output_directory:str = "output",
                 endpoint:str = "http://biovalidator.ega.ebi.ac.uk/validate",
                 stop_at_errors:bool = False):
        
        self.input_directory = input_directory
        self.output_directory = output_directory
        self.endpoint = endpoint
        self.stop_at_errors = stop_at_errors
        self.complete_df_csv_filepath = os.path.join(self.output_directory, "complete_df.csv")
        self.summary_df_csv_filepath = os.path.join(self.output_directory, "summary_df.csv")

        if not os.path.exists(input_directory) or not os.path.isdir(input_directory):
            raise ValueError(f"The provided directory path '{input_directory}' does not exist or it's not a directory")
        
        self.complete_df_columns = ["filepath", "passed_validation", "validation_time", "n_data_properties", "n_ontology_properties", "timestamp", "validation_outcome"]
        self.complete_df = pd.DataFrame(columns=self.complete_df_columns)

    def iterate_over_dir(self) -> pd.DataFrame:
        """ 
        Iterates over all JSON documents within the directory, loads them and calls JSONDocValidationStats(), populating with one validation round the self.complete_df
        """
        rows = []
        for file in os.scandir(self.input_directory):
            if file.name.endswith('.json') and file.is_file():
                filepath = file.path
                validator = JSONDocValidationStats(json_doc=filepath,
                                                endpoint=self.endpoint,
                                                stop_at_errors=self.stop_at_errors)
                timestamp = get_current_timestamp()
                rows.append({
                    "filepath": filepath,
                    "passed_validation": validator.passed_validation, 
                    "validation_time": validator.validation_time, 
                    "n_data_properties": validator.n_data_properties, 
                    "n_ontology_properties": validator.n_ontology_properties,
                    "timestamp": timestamp,
                    "validation_outcome": validator.validation_outcome
                })

        self.complete_df = self.complete_df.append(rows, ignore_index=True)

        return self.complete_df

    def save_dataframe_csv(self, dataframe: pd.DataFrame, filename: str):
        """
        Saves a dataframe as a CSV file
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Given 'dataframe' must be of type pd.DataFrame.")
        filepath = os.path.join(self.output_directory, filename)
        dataframe.to_csv(filepath, index=False)
        
    def join_validation_stats(self) -> pd.DataFrame:
        """
        Uses the self.complete_df dataframe to generate a summary of it (self.summary_df), grouping parameters by the "filepath" (i.e. grouping parameters by filename)
        """
        if not hasattr(self, 'complete_df') or self.complete_df.empty:
            raise ValueError("complete_df has not been initialized or is empty. Use method 'iterate_over_dir()' at least once before trying to create the summary dataframe.")

        summary_df = self.complete_df.groupby("filepath").agg(
            {
                "filepath": "first", # First occurence of filepath
                "passed_validation": all, # Only True if "all" are True in the complete df
                "validation_time": "mean", # The mean of all validation times in the complete df
                "n_data_properties": "first", # First occurence of n_data_properties
                "n_ontology_properties": "first" # First occurence of n_ontology_properties
            }
        )
        summary_df.rename(
            columns={
                "passed_validation": "Passed validation",
                "validation_time": "Average validation time",
                "n_data_properties": "Number of JSON properties per file",
                "n_ontology_properties": "Number of ontology validations per file"
            },
            inplace=True,
        )
        
        summary_df["Number of validations"] = self.complete_df.groupby("filepath").size()
        self.summary_df = summary_df

        return self.summary_df
        
    def create_3d_scatter_plot(self, filename:str = "3D_scatterPlot.png"):
        """
        Creates a 3D scatter plot using the complete dataframe, representing n_data_properties, n_ontology_properties and validation_time. Then saves it.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(            
            self.complete_df["n_data_properties"], 
            self.complete_df["n_ontology_properties"],
            self.complete_df["validation_time"]
        )
        ax.set_xlabel('n_data_properties')
        ax.set_ylabel('n_ontology_properties')
        ax.set_zlabel('validation_time')
        
        self.filepath_3d_scatter_plot = os.path.join(self.output_directory, filename)
        fig.savefig(self.filepath_3d_scatter_plot)        
        
    def create_2d_scatter_graphs(self, filename:str = "2D_scatterPlot.png"):
        """
        Creates twi 2D scatter plot using the complete dataframe, representing n_data_properties and n_ontology_properties versus validation_time. Then saves it.
        """
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        
        axs[0].scatter(self.complete_df["n_data_properties"], self.complete_df["validation_time"], c='r', marker='o')
        axs[0].set_xlabel("n_data_properties")
        axs[0].set_ylabel("validation_time")

        axs[1].scatter(self.complete_df["n_ontology_properties"], self.complete_df["validation_time"], c='b', marker='o')
        axs[1].set_xlabel("n_ontology_properties")
        
        self.filepath_2d_scatter_plot = os.path.join(self.output_directory, filename)
        fig.savefig(self.filepath_2d_scatter_plot)
        
    def create_2d_density_graphs(self, filename:str = "2D_densityPlots.png"):
        """
        Creates twi 2D density plot using the complete dataframe, representing n_data_properties and n_ontology_properties versus validation_time. Then saves it.
        """
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        # Plotting density plot for n_data_properties and validation_time
        x = self.complete_df["n_data_properties"]
        y = self.complete_df["validation_time"]
        axs[0].set_xlabel("n_data_properties")
        axs[0].set_ylabel("validation_time")
        axs[0].hist2d(x, y, bins=30, cmap="Blues")

        # Plotting density plot for n_ontology_properties and validation_time
        x = self.complete_df["n_ontology_properties"]
        y = self.complete_df["validation_time"]
        axs[1].set_xlabel("n_ontology_properties")
        axs[1].hist2d(x, y, bins=30, cmap="Blues")

        # Adding a colorbar to show the density
        cbar = fig.colorbar(axs[0].get_children()[0], ax=axs, shrink=0.5)
        cbar.set_label("Density (Nº validations)")

        self.filepath_2d_density_plot = os.path.join(self.output_directory, filename)
        fig.savefig(self.filepath_2d_density_plot)
                       
    def create_output_dir(self):
        """
        Creates a directory to store the outputs at. If it already exists, adds/changes a suffix to make the output directory name unique.
        """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
            
        else:
            base_path = self.output_directory.rstrip("_0123456789")
            suffix = self.output_directory[len(base_path):]
            if suffix == "":
                self.output_directory = base_path + "_1"
                # We add the suffix and try again
                self.create_output_dir()
                
            else:
                try:
                    suffix_num = int(suffix.lstrip("_"))
                    suffix_num += 1
                    self.output_directory = base_path + "_" + str(suffix_num)
                    # We sum 1 to the suffix and try again
                    self.create_output_dir()

                except ValueError:
                    raise ValueError("The directory name format is not correct. It should end with an underscore and a number.")
    
    def create_run_parameters_df(self):   
        """
        Creates a dataframe with overall parameters of the JSONBatchValidationStats() instance
        """     
        param_df = {
            "Date": get_current_timestamp(),
            "Passed validation": [self.complete_df.all(axis='rows')["passed_validation"]],
            "Validation time (s)": [round(self.complete_df['validation_time'].sum(), 2)],
            "Input directory": self.input_directory,
            "Used endpoint": self.endpoint,
            "Nº of executions": [self.summary_df["Number of validations"][0]],
            "Nº of files": [len(self.summary_df.index)],
            "Nº of properties": [self.complete_df['n_data_properties'].sum()],
            "Nº of ontology validations": [self.complete_df['n_ontology_properties'].sum()]
        }

        # Create the pandas DataFrame with column name is provided explicitly
        self.param_df = pd.DataFrame(param_df)
    
    def create_summary_readme(self):
        """
        Creates a summary README in markdown format, compiling the parameters along the generated graphs and summary table.
        """
        self.readme_filepath = os.path.join(self.output_directory, "README.md")
        
        self.create_run_parameters_df()
        param_table = df_to_markdown_table(self.param_df)
        
        summary_table = df_to_markdown_table(self.summary_df)        
        
        readme_content = (
            f"# JSON validation summary\n"
            f"The script [``create_benchmarks.py``](https://github.com/EbiEga/ega-metadata-schema/blob/main/.github/scripts/create_benchmarks.py) validated all JSON files in a directory against a validation server endpoint, recording valuable parameters of its execution.\n"
            f"Overall execution parameters:\n"
            f"{param_table}"
            f"\n\nAll files generated in this execution are stored in this directory (``{self.output_directory}``) with this same README. These files are:"
            f"\n1. Two CSV files: the complete set of validation parameters for each file and validation attempt ([``{self.complete_df_csv_filepath}``]({os.path.basename(self.summary_df_csv_filepath)}))"
            f" and a summary of those ([``{self.summary_df_csv_filepath}``]({os.path.basename(self.summary_df_csv_filepath)})), also displayed below."
            f"\n2. Two graphs (both inserted below) of the full set of parameters: a 3D graph ([``{self.filepath_3d_scatter_plot}``]({os.path.basename(self.filepath_3d_scatter_plot)})) of the validation time, number of properties, and number of ontology validations;"
            f" and a 2D density plot ([``{self.filepath_2d_density_plot}``]({os.path.basename(self.filepath_2d_density_plot)})) containing 2 subplots: one for each variable versus the validation time"
            f"\n\n"
            f"Graphical representations:\n"
            f"\n![3D Scatter plot]({os.path.basename(self.filepath_3d_scatter_plot)})\n"
            f"![2D Density plot]({os.path.basename(self.filepath_2d_density_plot)})\n"
            f"\nSummary table:\n"
            f"{summary_table}"
        )

        with open(self.readme_filepath, "w") as file:
            file.write(readme_content)


#---#
# Stats collection
#---#
batch_validator = JSONBatchValidationStats(
    input_directory=args.input_directory,
    output_directory=args.output_directory,
    endpoint=args.endpoint,
    stop_at_errors=args.stop_at_errors
    )

for i in range(args.number_of_iterations):
    # We validate all files "number_of_iterations" times, populating the "batch_validator.complete_df" dataframe
    batch_validator.iterate_over_dir()

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
batch_validator.save_dataframe_csv(dataframe=batch_validator.complete_df, filename="complete_df.csv")
batch_validator.save_dataframe_csv(dataframe=batch_validator.summary_df, filename="summary_df.csv")

batch_validator.create_3d_scatter_plot()
batch_validator.create_2d_density_graphs()
batch_validator.create_summary_readme()