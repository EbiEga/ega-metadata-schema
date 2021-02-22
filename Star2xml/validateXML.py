#!/usr/bin/env python3

"""
Programme:  validateXML
File:       validateXML.py
Version:    1
Date:       2021-02-05
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

program_description = """A script to validate one (or more) input XML files based
on some XML schemas (.xsd files). If schemas are missing, it downloads them
from a given FTP server. The function returns a list full of boolean values
defined by the outcome of the validation (e.g. [False, True, True] if only the
last 2 XMLs were correctly validated)
"""

arg_parser = argparse.ArgumentParser(prog = "validateXML.py",
                                     description = program_description,
                                     epilog = "Schema keys and their input XMLs have to be given in the same order!")

arg_parser.add_argument('schema_keys',
                        help = 'Schema key(s) (comma delimited) for the metadata object(s) (e.g. "sample,run" or "experiment"...)')

arg_parser.add_argument('input_xmls',
                        help = 'Input XML(s) (comma delimited) with metadata information to be validated (e.g. "sample.xml,run.xml")')

arg_parser.add_argument('--schemas-dir',
                        dest = 'schema_dir',
                        nargs = '?', # 0 or 1 arguments
                        default = 'downloaded_schemasXSD/',
                        help = 'Directory containing all the XSD schema files (e.g. "downloaded_schemasXSD/"). If --download-xsd is given, the XSD files will be downloaded into this directory.')

arg_parser.add_argument('--schema-file',
                        dest = 'schema_file',
                        nargs = '?', # 0 or 1 arguments
                        default = 'configuration_files/xml_schema.yaml',
                        help = 'YAML file containing the schema for the metadata object(s) (e.g. "xml_schema.yaml")')

arg_parser.add_argument('--download_xsd',
                        action='store_true',
                        default = False,
                        help='A boolean switch to give if you want the schemas (.xsd files) to be downloaded instead of providing them')

arg_parser.add_argument('--verbose',
                        action='store_true',
                        default = False,
                        help='A boolean switch to add verbosity to the function (will print into the terminal extra information, as well as the validation errors and results with a friendlier format)')


arguments = arg_parser.parse_args()
input_xmls = arguments.input_xmls.split(',')
schema_keys = arguments.schema_keys.lower().split(',')
schema_file = arguments.schema_file
schema_dir = arguments.schema_dir
is_xsd_missing = arguments.download_xsd
is_verbose = arguments.verbose

# Assert a possible common mistake
assert len(schema_keys) == len(input_xmls), "Error: the given schema keys '{}' and input XMLs '{}' do not match in length".format(schema_keys, input_xmls)

# We load the information (like a dictionary) from the YAML file
from yaml import safe_load
with open(schema_file, "r") as schema_file:
    schema_general_dict = safe_load(schema_file)


# -------- #
# Download of XML schemas (.xsd files) if --download-xsd was given
# -------- #
if is_xsd_missing:
    # Import the downloading function
    from ftp_downloader import download_files

    if is_verbose:
        print("# Download mode enable, XSD files will be downloaded to the directory '%s'" % schema_dir)

    # Assign the server's information from the YAML file
    file_extension = schema_general_dict["XML_schemas_info"]["file_extension"]
    ftp_server = schema_general_dict["XML_schemas_info"]["ftp_server"]
    schemas_dir = schema_general_dict["XML_schemas_info"]["schemas_dir"]

    # Download the XSD files into the given schema directory
    download_files(download_directory = schemas_dir,
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
                                      schema_key = schema_key)

    # Based on the returned boolean of xml_is_valid() we append a different result
    outcome_result.append(xml_is_valid)

# We finally print the outcome list (which can be redirected to a variable, text file, pipeline...):
print(outcome_result)
