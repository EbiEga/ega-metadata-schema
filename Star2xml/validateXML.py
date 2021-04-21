#!/usr/bin/env python3

"""
Programme:  validateXML
File:       validateXML.py
Function:   A script to validate a given XML against a given schema (.xsd)
Copyright:  EMBL-EBI, 2021
Address:    EMBL-EBI
            Wellcome Genome Campus
            Hinxton
            Cambridgeshire, CB10 1SD, UK
--------------------------------------------------------------------------
# Released under Apache License Version 2.0, January 2004, http://www.apache.org/licenses/
--------------------------------------------------------------------------
Description:
============
The script takes an input XML file containing metadata information of one or more
ENA metadata objects (e.g. sample, run, experiment...) and validates them against
their corresponding schema (.xsd). If such schemas are missing, it downloads them
from the ENA's source of truth. Thus, such XML files should be ready for
programmatic submission to the ENA
(https://ega-archive.org/submission/sequence/programmatic_submissions).

This script is based on work from an older project:
    - https://github.com/EBIvariation/amp-t2d-submissions/tree/master/xls2xml
--------------------------------------------------------------------------
For further information run:
    $ ./validateXML.py -h
Example:
    $ ./validateXML.py "sample,run" "sample.xml,run.xml" --schemas-dir "XSD_schemas_directory/" --schema-file "xml_schema.yaml" --download_xsd --verbose
======
This script was written and tested using python 3.8, functionality with
older versions of python have not been tested and are not guaranteed.
"""

# -------- #
# Parsing given arguments
# -------- #
import argparse

arg_parser = argparse.ArgumentParser(prog = "validateXML.py",
                                    epilog = "Schema keys (e.g. 'sample,run') and their input XMLs (e.g. 'sample.xml,run.xml') have to be given in the same order!",
                                    description = """A script to validate one (or more) input XML(s) based
                                                    on some XML schemas (.xsd files). If schemas are missing, it downloads them
                                                    from its GH repository (or FTP server) (specified within the configuration files). 
                                                    The function returns a list of boolean values defined by the outcome of the 
                                                    validation (e.g. [False, True, True] if only the last 2 XMLs were correctly validated)
                                                    """)

arg_parser.add_argument('schema_keys',
                        help = """Schema key(s) (comma delimited) for the metadata object(s) (e.g. "sample,run" or "experiment"...)""")

arg_parser.add_argument('input_xmls',
                        help = """Input XML(s) (comma delimited) with metadata information to be validated (e.g. "sample.xml,run.xml" or "experiment.xml")""")

arg_parser.add_argument('--schemas-dir',
                        dest = 'schema_dir',
                        nargs = '?', # 0 or 1 arguments
                        default = 'downloaded_schemasXSD/',
                        help = """Directory containing all the XSD schema files (default: "downloaded_schemasXSD/"). If 
                                --download-xsd is given, the XSD files will be downloaded into this directory.""")

arg_parser.add_argument('--schema-file',
                        dest = 'schema_file',
                        nargs = '?', # 0 or 1 arguments
                        default = 'configuration_files/xml_schema.yaml',
                        help = """YAML file containing the schema for the metadata object(s) (default: "configuration_files/xml_schema.yaml")""")

arg_parser.add_argument('--download_xsd',
                        action='store_true',
                        default = False,
                        help="""A boolean switch that will enable the download of the XML schemas (.xsd files) instead of having to provide them manually.""")

arg_parser.add_argument('--ftp_downloader',
                        action='store_false',
                        default = True,
                        help="""A boolean switch to use the ftp downloader instead of the default request.get() 
                                downloader for the ENA schemas (in GitHub), which is the main source of truth for ENA schemas. We advise you not to use this 
                                option unless you know for sure that the version of the schemas within the configuration files (e.g. 'pub/databases/ena/doc/xsd/sra_1_6/') 
                                is the proper one.""")

arg_parser.add_argument('--verbose',
                        action='store_true',
                        default = False,
                        help="""A boolean switch to add verbosity to the function (will print into the terminal extra information, 
                                as well as the validation errors and results with a friendlier format). Highly recommended.""")

arg_parser.add_argument('--dont_stop_parsing',
                        action='store_true',
                        default = False,
                        help="""A boolean switch that, if given, will make the validation continue if an error is raised when parsing
                                one of the given XMLs. Such file with errors will be reported as not validated, but the function will not stop,
                                validating other files. The error will be displayed excplicitly as a warning if '--verbose' is also given.""")



arguments = arg_parser.parse_args()
input_xmls = arguments.input_xmls.split(',')
schema_keys = arguments.schema_keys.lower().split(',')
schema_file = arguments.schema_file
schema_dir = arguments.schema_dir
is_xsd_missing = arguments.download_xsd
git_downloader_method = arguments.ftp_downloader
is_verbose = arguments.verbose
dontExitOn_ParsingErrors = arguments.dont_stop_parsing

# Assert a possible common mistake
assert len(schema_keys) == len(input_xmls), "Error: the given schema keys '{}' and input XMLs '{}' do not match in length".format(schema_keys, input_xmls)

# We load the information (like a dictionary) from the YAML file
from yaml import safe_load
try:
    with open(schema_file, "r") as schema_file:
        schema_general_dict = safe_load(schema_file)

except FileNotFoundError:
    print("ERROR in validateXML.py: given schema filepath '%s' does not exist or could not be found." \
          % schema_file, file=sys.stderr)
    sys.exit()

except yaml.scanner.ScannerError as ScannerError:
    print("ERROR in validateXML.py: in the given schema '%s' there was a scanning issue." \
          % schema_file, file=sys.stderr)
    print("\t - Problem: %s" \
          % ScannerError.problem, file=sys.stderr)
    print("\t - Problem's location: %s" \
          % ScannerError.context_mark, file=sys.stderr)
    sys.exit()

except:
    print("ERROR in validateXML.py: unknown error happened trying to yaml.safe_load() the given schema filepath '%s'." \
          % schema_file, file=sys.stderr)
    sys.exit()


# -------- #
# Download of XML schemas (.xsd files) if --download-xsd was given
# -------- #
if is_xsd_missing:
    if is_verbose:
            print("# Download mode enable, XSD files will be downloaded to the directory '%s' if not found already there." % schema_dir)
            
    if git_downloader_method:
        if is_verbose:
            print("# Download function used is download_files_git() from git_downloader.py")

        # We import the downloading function
        from git_downloader import download_files_git

        download_file_dict = schema_general_dict["XML_schemas_info"]["download_files_git"]

        if isinstance(download_file_dict, dict):
            # We transform the dictionary into the list we use as input
            download_file_list = list(download_file_dict.values())
        
        elif isinstance(download_file_dict, list):
            download_file_list = download_file_dict

        else:
            # If it's not a dictionary nor a list, we did something wrong
            print("ERROR in validateXML.py: the information extracted from the yaml schema file (%s) with the keys 'XML_schemas_info' and 'download_files_git' did not return a dictionary nor a list.\n\t- Returned information: %s" \
                    % (schema_file, download_file_dict), file=sys.stderr)
            sys.exit()

        # We retrieve the information for the download from the configuration file (xml_schema.yaml)
        download_files_git(output_dir = schema_dir,
                           raw_file_url_list = download_file_list)

    else:
        # Import the downloading function
        from ftp_downloader import download_files_ftp

        if is_verbose:
            print("# Download function used is download_files_ftp() from ftp_downloader.py")

        # Assign the server's information from the YAML file
        file_extension = schema_general_dict["XML_schemas_info"]["file_extension"]
        ftp_server = schema_general_dict["XML_schemas_info"]["ftp_server"]
        schemas_dir = schema_general_dict["XML_schemas_info"]["schemas_dir"]

        # Download the XSD files into the given schema directory
        download_files_ftp(download_directory = schemas_dir,
                           server = ftp_server,
                           output_dir = schema_dir,
                           file_extension = file_extension)
else:
    if is_verbose:
        print("# Download mode disabled, XSD files will be expected to be at '%s'" % schema_dir)

# -------- #
# Validation of the output_xml against XML schemas (.xsd - and their download if missing)
# -------- #
from scripts_for_validation import check_xml_is_valid
import os.path
import sys
outcome_result = []
num_validations = len(schema_keys)
if is_verbose:
    print("# Number of given schema keys (along their XMLs): %s" % num_validations)
# We iterate over the given list of schema_keys and xml_inputs
for index in range(num_validations):
    # We save the information for this schema_key that resides in the YAML file
    schema_key = schema_keys[index]
    schema_xsd_filename = os.path.basename(schema_general_dict["XML_schemas_info"]["object_schemas"][schema_key])
    local_xsd_file = os.path.join(schema_dir, schema_xsd_filename)
    input_xml = input_xmls[index]
    xml_is_valid = check_xml_is_valid(xml_tree = input_xml,
                                      schema_file = local_xsd_file,
                                      verbose = is_verbose,
                                      schema_key = schema_key,
                                      dontExitOn_ParsingErrors = dontExitOn_ParsingErrors)

    # Based on the returned boolean of xml_is_valid() we append a different result
    outcome_result.append(xml_is_valid)

# We finally print the outcome list (which can be redirected to a variable, text file, pipeline...):
print(outcome_result)
