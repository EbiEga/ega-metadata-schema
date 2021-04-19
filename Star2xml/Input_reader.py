import sys
import pandas as pd
#! Also need to install "openpyxl" package if you don't have it installed along pandas.
import os
import yaml
from utils import report_error_messages

# Headers that define attributes within the YAML configuration file
required_headers_key = "required"

# The range of rows that are descriptive and shall be removed (can be a list of tuples or a single tuple)
#     In this case we have (0,1) since the 2 first rows are descriptive
descriptive_rows_range = [(0,1)]
# This string will be placed above the real data to indicate submitters where to put it.
#     If we don't want the descriptive string, simply use 'descriptive_string = ""'
descriptive_string = "Provide your real metadata below this row (each row under this one will account for one metadata instance)"
descriptive_row = 1
descriptive_col = 0

class Input_reader():
    """
    Reader for CSV / TSV / XLSX (excel) input that contains the metadata information
    """
    def __init__(self, input_file, conf_file, conf_key):
        """
        Initialization (constructor) of an instance.

        Parameters:
            - self: not given, it's the instance itself.
            - input_file (str): file path to the input file (.tsv, .csv or .xlsx | e.g. samples.tsv)
            - conf_file (str): file path to the configuration file (e.g. conf.yaml)
            - conf_key (str): key string that defines the metadata object (e.g. "sample" or "run")
        """

        self.conf_key = conf_key
        # We load the YAML file, creating a dictionary (of dictionaries) with its content.
        #     e.g. self.conf_dict = {'worksheets': ['Sample'], 'Sample': {'required': ['Sample_ID'], 'optional': ['Sample_title']}}
        try:
            with open(conf_file, "r") as f:
                self.conf_dict = yaml.safe_load(f)

        except yaml.scanner.ScannerError as ScannerError:
            print("ERROR in Input_reader(): in the given configuration file '%s' there was a scanning issue." \
                  % conf_file, file=sys.stderr)
            print("\t - Problem: %s" \
                  % ScannerError.problem, file=sys.stderr)
            print("\t - Problem's location: %s" \
                  % ScannerError.context_mark, file=sys.stderr)
            sys.exit()

        except:
            print("ERROR in Input_reader(): given configuration filepath '%s' could not be read" \
                  % conf_file, file=sys.stderr)
            report_error_messages(sys.exc_info()[0], sys.exc_info()[1])
            sys.exit()

        # We save the basename and file extension of the input file for future checks
        self.input_file = input_file
        self.input_file_basename = os.path.basename(self.input_file)
        self.input_filetype = os.path.splitext(self.input_file)[1]

        # We generate the dataframe containing the metadata
        self.generate_dataframe()

        # We check if the input file meets the requirements (i.e. contains the required fields)
        if not self.check_if_valid():
            print("ERROR in Input_reader(): given input file (%s) does not contain the required fields for '%s' object:\n\t- Required fields: %s\n\t- Input fields: %s" \
                  % (self.input_file_basename, self.conf_key, self.required_headers, self.input_file_headers), file=sys.stderr)
            print("- Missing headers:\n%s" % self.missing_headers, file=sys.stderr)
            sys.exit()

    def generate_dataframe(self):
        """
        Transforms the input file into a dataframe ("self.input_dataframe"), converging from different input file
            types (.csv, .tsv and .xlsx) into a unified format.

        Regarding datatypes (dtype), we choose to preserve data as stored in the input file (dtype = "object") instead
            of letting pandas interpret it or giving a dictionary with datatypes. This approach advocates for a higher
            flexibility.
        """

        # We check the given filepath exists and is a file
        if not os.path.isfile(self.input_file):
            print("ERROR in Input_reader(): given input filepath '%s' does not exist" % self.input_file, file=sys.stderr)
            sys.exit()

        try:
            # Depending on what filetype it is, we read it with different pandas' methods
            if self.input_filetype == ".csv":
                 self.input_dataframe = pd.read_csv(filepath_or_buffer = self.input_file, sep = ",", dtype = "object")

            elif self.input_filetype == ".tsv":
                self.input_dataframe = pd.read_csv(filepath_or_buffer = self.input_file, sep = "\t", dtype = "object")

            elif self.input_filetype == ".xlsx":
                self.input_dataframe = pd.read_excel(io = self.input_file, dtype = "object", engine='openpyxl', sheet_name = self.conf_key)

            else:
                # If given a filetype that we didn't expect
                print("ERROR in Input_reader() - generate_dataframe(): given input file (%s) has extension '%s', while the allowed file types are [.csv | .tsv | .xlsx]" \
                      % (self.input_file_basename, self.input_filetype), file=sys.stderr)
                sys.exit()
        except ValueError:
            print("ERROR in Input_reader() - generate_dataframe(): given input file (%s) did not have a tab named '%s'" \
                      % (self.input_file_basename, self.conf_key), file=sys.stderr)
            sys.exit()
            
        except:
            print("ERROR in Input_reader(): given input filepath '%s' could not be read. Check that the given schema keys (e.g. 'sample') are correct" % self.input_file, file=sys.stderr)
            report_error_messages(sys.exc_info()[0], sys.exc_info()[1])
            sys.exit()
        
        if descriptive_string != "":
            try:
                # We check that the descriptive string is there
                description_is_there = self.check_row_value(row_to_look = descriptive_row,
                                                            column_to_look = descriptive_col, 
                                                            value = descriptive_string)
                
            # It could also be the case that the user removed all rows and only added one or two, for which we will
            #     receive an index error, and we'll report it the same way. 
            except IndexError:
                description_is_there = False
                
            if not description_is_there:
                print("ERROR in Input_reader() - generate_dataframe(): a descriptive row was supposed to be at row %s and column %s, but it was not found. It may lead to real data being skipped.\n\t- Descriptive string: %s" \
                  % (descriptive_row, descriptive_col, descriptive_string), file=sys.stderr)
                sys.exit()
            
        
        # We call the function to remove descriptive rows
        self.peel_off_rows(row_ranges = descriptive_rows_range)
        
    def check_row_value(self, row_to_look, column_to_look, value):
        """
        Function to check that a value is at dataframe[column_to_look][row_to_look] (returns True if so, False otherwise).
            It can be used, for instance, to check that the descriptive row above real data exists.
            
        Parameters:
            - row_to_look (int): row of the dataframe corresponding to the value.
            - column_to_look (int): column of the dataframe corresponding to the value.
            - value (undetermined): value that should correspond to dataframe[column_to_look][row_to_look]
        """
        # If the value is empty or does not contain information
        if not value:
            return False
        
        if self.input_dataframe[self.input_dataframe.columns[column_to_look]][self.input_dataframe.index[row_to_look]] == value:
            return True
        else:
            return False        
    
    def peel_off_rows(self, row_ranges):
        """
        Function that will get rid off descriptive rows from the range given by row_ranges. For instance,
            if row_ranges is [(0,1), (3,5)], the function will remove the first 2 rows and rows from the 4th to the 6th.
            
        Parameters:
            - row_ranges (list of tuples): contains a tuple for each range to remove from the dataframe.
        """
        # We check that the row range is indeed a list
        if not isinstance(row_ranges, list):
            print("ERROR in Input_reader() - peel_off_rows(): given row ranges to remove from the input dataframe is not a list: \n\t- Row ranges to remove: %s" \
                  % [row_ranges], file=sys.stderr)
            sys.exit()
            
        for tuple_i in row_ranges:
            # We check that we are using a tuple
            if not isinstance(tuple_i, tuple):
                print("ERROR in Input_reader() - peel_off_rows(): given row ranges (list) to remove from the input dataframe contains elements that are not tuples: \n\t- Row ranges to remove: %s\n\t- Element that is not a tuple: %s" \
                      % (row_ranges, tuple_i), file=sys.stderr)
                sys.exit()
            
            # We remove the given row range
            self.input_dataframe.drop(self.input_dataframe.index[[tuple_i[0], tuple_i[1]]], inplace = True)        

        # We then reset the rows index (so that the dataframe row indexes don't start at the Nth row after the ones we removed)
        self.input_dataframe.reset_index(inplace=True)

    def check_if_valid(self):
        """
        Checks if the input file contains all the required fields (for that metadata object),
            which are described in the configuration file (indexing the corresponding object).

        Return:
            - self.is_valid (boolean): "True" if all required fields are present in the input file.
                                       "False" otherwise.
        """

        # We index the dictionary we created from the conf.yaml file (self.conf_dict) with its configuration key (e.g. Sample)
        self.required_headers = self.conf_dict[self.conf_key][required_headers_key]

        # Get the input_file headers and then compare the two
        #     (">=" so that we allow additional headers in the input file besides the required)
        self.input_file_headers = list(self.input_dataframe.columns.values)
        self.is_valid = set(self.input_file_headers) >= set(self.required_headers)

        if not self.is_valid:
            # We get which ones are required but not in the input:
            self.missing_headers = set(self.required_headers) - set(self.input_file_headers)
            
        return self.is_valid