#!/usr/bin/env python3

"""
Programme:  star2xml
File:       star2xml.py
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
    $ ./star2xml.py "study,sample,analysis,experiment,run,dataset,submission,dac,policy" "../templates/sequence-based-metadata/whole_submission_template.xlsx" --validate

======
This script was written and tested using python 3.8, functionality with
older versions of python have not been tested and are not guaranteed.
"""

import argparse
import sys
import os
from datetime import datetime

# -------- #
# Parsing given arguments
# -------- #
arg_parser = argparse.ArgumentParser(prog = "star2xml.py",
                                     description = """A script to transform an input file (.csv, .tsv or .xlsx) into one (or more) dataframe(s), and
                                                    then build one (or more) XML(s) with its information following the XML structure described in a YAML file""",
                                     epilog = """Example of usage: $ ./star2xml.py "study,sample,analysis,experiment,run,dataset,submission,dac,policy" 
                                     "../templates/sequence-based-metadata/EGA_metadata_submission_template_v1.xlsx" --validate""")

arg_parser.add_argument('schema_keys',
                        help = """Schema keys for the metadata object. Can be a single key (e.g. "sample", "run", "experiment"...), 
                                or several keys separated by commas (e.g. "sample,run,experiment")""")

arg_parser.add_argument('input_file',
                        help = """Input file (.csv, .tsv or .xlsx) with metadata information to be transformed into a dataframe 
                                (e.g. "sample.xlsx"). If several schema keys are given, the input spreadsheet is expected to have
                                a separated tab named after each schema key.""")

arg_parser.add_argument('--output_xmls',
                        dest = 'output_xmls',
                        default = 'output_xmls/',
                        help = """Output XML filepaths, i.e. file(s) that will contain the generated XML(s). [OUTPUT_XMLS] can be 
                        (1) a single filepath (e.g. "sample.xml"), (2) several filepaths separated by commas (e.g. "sample.xml,run.xml,experiment.xml" 
                        - in the same order as the schema keys), (3) or a directory (default: "output_xmls/") where all XMLs will be saved with their 
                        corresponding schema keys as their names (with the time-stamp if needed to avoid overwritting files).""")

arg_parser.add_argument('--schema-file',
                        dest = 'schema_file',
                        nargs = '?', # 0 or 1 arguments
                        default = 'configuration_files/xml_schema.yaml',
                        help = """YAML file containing the schema for the metadata object(s) (default: "xml_schema.yaml")""")

arg_parser.add_argument('--configuration-file',
                        dest = 'conf_file',
                        nargs = '?', # 0 or 1 arguments
                        default = 'configuration_files/input_configuration.yaml',
                        help = """YAML file containing the configuration (i.e. required fields) of the input file (default: 
                        "input_configuration.yaml")""")

arg_parser.add_argument('--verbose',
                        action='store_true',
                        default = False,
                        help="""A boolean switch to add verbosity to the function (printing initial parameters, final XML...)""")

arg_parser.add_argument('--debug',
                        action='store_true',
                        default = False,
                        help="""A boolean switch to set the functions in "debug" mode, which will add even more verbosity to the 
                                function (printing every step of the XML creation...)""")

arg_parser.add_argument('--validate',
                        action='store_true',
                        default = False,
                        help="""A boolean switch that will enable the validation of the scripts right after its creation. Thus, the
                                function will call validateXML.py (in verbose mode) after it has finished creating the XMLs.""")

arguments = arg_parser.parse_args()
input_file = arguments.input_file
output_xmls = arguments.output_xmls.split(',')
schema_keys = arguments.schema_keys.lower().split(',')
schema_file = arguments.schema_file
conf_file = arguments.conf_file
is_verbose = arguments.verbose
is_debug = arguments.debug
also_validate = arguments.validate

if len(output_xmls) == 1 and not os.path.splitext(output_xmls[0])[1]:
    # We check if we were given one or several output-XMLs and if it's a directory (has a file extension)
    output_isFiles = False

elif all([os.path.splitext(x)[1] == ".xml" for x in output_xmls]):
    # If not a directory, we might have been given a list of filepaths, but all their file extensions have to match ".xml", or else there was an error
    output_isFiles = True

else:
    # If none of the above conditions were satisfied, there was a mistake (several directories, or incorrect filepaths...)
    print("ERROR in star2xml.py: given 'output_xmls' argument was not a single directory or a list of filenames with '.xml' as their extension:\n\t- Given output_xmls: %s" \
            % output_xmls, file=sys.stderr)
    sys.exit()

if output_isFiles:
    # Assert a possible common mistake
    assert len(schema_keys) == len(output_xmls), "Error: the given schema keys '{}' and output XMLs '{}' do not match in length".format(schema_keys, output_xmls)

# -------- #
# Reading given input file into a dataframe(s)
# -------- #
from Input_reader import Input_reader
def deal_with_one_schema_key(schemaKey, output_xml):
    """
    Function to deal with a single schema key given to star2xml.py
        The function will read the given input file, create a dataframe with its data, and iterate over a YAML schema to
        construct an XML using values from the dataframe. 

    Parameters:
        - schemaKey (string): schema key (e.g. "sample", "run", etc.) of the metadata object. It will be used to index the metadata
                              object within the configuration files, as well as the tab within the input file (if applicable).
        - output_xml (string): filepath (e.g. "output_folder/sample.xml") where the output XML will be saved. 
    """
    xml_input = Input_reader(input_file = input_file,
                            conf_file = conf_file,
                            conf_key = schemaKey)

    # -------- #
    # Creation of the XML following a YAML schema and using the input dataframe
    # -------- #
    from XML_creator import XML_creator
    xml_creation = XML_creator(schema_filename = schema_file,
                            input_dataframe = xml_input.input_dataframe,
                            schema_key = schemaKey,
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
            print("- The generated XML resides in: ", output_xml)

        else:
            print("ERROR in star2xml.py: unknown error in the generation of the XML: output_xml '%s' it is not a file or does not contain bytes" \
                % output_xml, file=sys.stderr)

# We iterate over all the given schema keys
loop_counter = 0

if also_validate:
    xmls_for_validation = []

for schemaKey in schema_keys:
    schemaKey = schemaKey.strip()
    if not output_isFiles:
        # If output_xmls was a directory, we construct a default output_xml filename with its schemaKey
        schemaKey_filename = schemaKey + ".xml"
        output_xml = os.path.join(output_xmls[0], schemaKey_filename)

        if os.path.exists(output_xml) and os.path.getsize(output_xml) > 0:
            # If the file already exists and has some information, we avoid overwritting it using the datetime
            date_time = datetime.now().isoformat(timespec='minutes').replace(":", "_")
            schemaKey_filename = date_time + "_" + schemaKey + ".xml"
            output_xml = os.path.join(output_xmls[0], schemaKey_filename)
    
    else:
        # If the output_xmls were a list of filenames, we get their corresponding file
        output_xml = output_xmls[loop_counter]

    if also_validate:
        # If we will validate the XMLs we append their names
        xmls_for_validation.append(output_xml)

    # We call the function to deal with 
    deal_with_one_schema_key(schemaKey = schemaKey, 
                             output_xml = output_xml)

    # We add 1 to the counter to extract the proper output XML name
    loop_counter += 1

# In case we also want the validation step, we call ./validateXML.py: 
if also_validate:
    os.system('./validateXML.py --schema-file "%s" --download_xsd --verbose "%s" "%s"' \
                % (schema_file, ",".join(x.strip() for x in schema_keys), ",".join(xmls_for_validation)))
                
