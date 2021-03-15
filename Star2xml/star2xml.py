#!/usr/bin/env python3

"""
Programme:  star2xml
File:       star2xml.py
Version:    1
Date:       2021-01-26
Function:   A script to generate EGA submission XML files from structured input
            file (.csv, .tsv, .xlsx)
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
The script takes an input file (.csv, .tsv or .xlsx) containing the metadata of
an object (e.g. Sample or Run) required for an EGA submission and generates
a correctly formatted XML file (following the structure displayed in a schema.yaml
file) that can be used in the EGA's programmatic submission.
(https://ega-archive.org/submission/sequence/programmatic_submissions).

This script is based on work from an older project:
    - https://github.com/EBIvariation/amp-t2d-submissions/tree/master/xls2xml
--------------------------------------------------------------------------
For further information run:
    $ ./star2xml.py -h
Example:
    $ ./star2xml.py 'sample' 'sample.xlsx' 'sample.xml' --schema-file 'xml_schema.yaml' --configuration-file 'input_configuration.yaml'

======
This script was written and tested using python 3.8, functionality with
older versions of python have not been tested and are not guaranteed.
"""

import argparse
import sys
import os.path

# -------- #
# Parsing given arguments
# -------- #

program_description = """A script to transform an input file (.csv, .tsv or .xlsx) into a dataframe, and
then build an XML (which will be validated against ENA's schemas .XSD) with
its information following the XML structure described in a YAML file
"""

arg_parser = argparse.ArgumentParser(prog = "star2xml.py",
                                     description = program_description,
                                     epilog = "Example of usage: $ star2xml.py --schema-file 'xml_schema.yaml' --configuration-file 'input_configuration.yaml' 'sample' 'sample.xlsx' 'sample.xml'")

arg_parser.add_argument('schema_key',
                        help = 'Schema key for the metadata object (e.g. "sample", "run", "experiment"...)')

arg_parser.add_argument('input_file',
                        help = 'Input file (.csv, .tsv or .xlsx) with metadata information to be transformed into a dataframe (e.g. "sample.xlsx")')

arg_parser.add_argument('output_xml',
                        help = 'Output XML filepath, i.e. file that will contain the generated XML (e.g. "sample.xml")')


arg_parser.add_argument('--schema-file',
                        dest = 'schema_file',
                        nargs = '?', # 0 or 1 arguments
                        default = 'configuration_files/xml_schema.yaml',
                        help = 'YAML file containing the schema for the metadata object(s) (e.g. "xml_schema.yaml")')

arg_parser.add_argument('--configuration-file',
                        dest = 'conf_file',
                        nargs = '?', # 0 or 1 arguments
                        default = 'configuration_files/input_configuration.yaml',
                        help = 'YAML file containing the configuration (i.e. required fields) of the input file (e.g. "input_configuration.yaml")')

arg_parser.add_argument('--verbose',
                        action='store_true',
                        default = False,
                        help='A boolean switch to add verbosity to the function (printing initial parameters, final XML...)')

arg_parser.add_argument('--debug',
                        action='store_true',
                        default = False,
                        help='A boolean switch to set the functions in "debug" mode, which will add even more verbosity to the function (printing every step of the XML creation...)')

arguments = arg_parser.parse_args()
input_file = arguments.input_file
output_xml = arguments.output_xml
schema_key = arguments.schema_key.lower()
schema_file = arguments.schema_file
conf_file = arguments.conf_file
is_verbose = arguments.verbose
is_debug = arguments.debug

# -------- #
# Reading given input file into a dataframe
# -------- #
from Input_reader import Input_reader
xml_input = Input_reader(input_file = input_file,
                         conf_file = conf_file,
                         conf_key = schema_key)

# -------- #
# Creation of the XML following a YAML schema and using the input dataframe
# -------- #
from XML_creator import XML_creator
xml_creation = XML_creator(schema_filename = schema_file,
                           input_dataframe = xml_input.input_dataframe,
                           schema_key = schema_key,
                           output_xml = output_xml,
                           verbose = is_verbose,
                           debug_mode = is_debug)

if is_verbose or is_debug:
    xml_creation.print_basic_info()
xml_creation.construct_xml()
xml_creation.save_xml()

# If the output XML was generated and has some Bytes
if is_verbose or is_debug:
    if os.path.exists(output_xml) and os.path.getsize(output_xml) > 0:
        print("- star2xml.py finished. XML generation completed!")
        print("- The generated XML is: ", output_xml)

    else:
        print("ERROR in star2xml.py: unknown error in the generation of the XML: output_xml '%s' it is not a file or does not contain bytes" \
              % output_xml, file=sys.stderr)
