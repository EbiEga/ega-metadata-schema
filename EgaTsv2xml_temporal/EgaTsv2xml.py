#!/usr/bin/env python3

"""
Programme:  EgaTsv2xml
File:       EgaTsv2xml.py
Version:    1
Date:       2021-01-26
Function:   A script to generate EGA submission XML files from structured input file (.csv, .tsv, .xlsx)
Copyright:  EMBL-EBI, 2021
Author:     Marcos Casado Barbero
Address:    EMBL-EBI
            Wellcome Genome Campus
            Hinxton
            Cambridgeshire, CB10 1SD, UK
--------------------------------------------------------------------------
#! Released under ¿2-clause BSD license?
--------------------------------------------------------------------------
Description:
============
The script takes an input file (.csv, .tsv or .xlsx) containing the metadata of
an object (e.g. Sample or Run) required for an EGA submission and generates
a correctly formatted XML file (following the structure displayed in a schema.yaml
file) that can be used in the EGA's programmatic submission
(https://ega-archive.org/submission/sequence/programmatic_submissions).

This script is based on work from an older project:
    - https://github.com/EBIvariation/amp-t2d-submissions/tree/master/xls2xml
--------------------------------------------------------------------------
Usage:
======
This script was written and tested using python 3.8, functionality with
older versions of python have not been tested and are not guaranteed.
--------------------------------------------------------------------------
Revision History:
================
1  21.01.28    By: MCB
"""

from Input_reader import Input_reader
from XML_creator import XML_creator
from validation_scripts import list_web_FullDirectory, download_files, check_xml_is_valid

#! _______________________________
#! The following parts are fixed and only has 2 examples, but in the next step I will add the given arguments from the command line
#! _______________________________

url = 'http://ftp.ebi.ac.uk/pub/databases/ena/doc/xsd/sra_1_5/'
ext = '.xsd'

# --- #
# For Sample
# --- #

# - Reading input into dataframe
xml_input = Input_reader(input_file = "final_templates/xlsx_templates/Filled_examples/Sample.xlsx",
                         conf_file = "xml_configuration.yaml",
                         conf_key = "sample")

# - Creating the XML
xml_creation = XML_creator(schema_filename = "xml_schema.yaml",
                           input_dataframe = xml_input.input_dataframe,
                           schema_key = "sample",
                           output_xml = "Sample_output_xml.xml",
                           verbose = True,
                           debug_mode = False)

xml_creation.construct_xml()
xml_creation.save_xml()

# - Validating the XML against the schema (XSD)

file_list = list_web_FullDirectory(url, ext)

download_files(file_list = file_list, output_dir = "XSD_schemas_downloaded/")

xml_is_valid = check_xml_is_valid(xml_tree = xml_creation.xmlVar_SAMPLE_SET,
                                  schema_file = "XSD_schemas_downloaded/SRA.sample.xsd")

print("----------------!!!! Created Sample xml is vali?", xml_is_valid)


# --- #
# For RUN
# --- #

# - Reading input into dataframe
xml_input = Input_reader(input_file = "final_templates/xlsx_templates/Filled_examples/run_template.xlsx",
                         conf_file = "xml_configuration.yaml",
                         conf_key = "run")

# - Creating the XML
xml_creation = XML_creator(schema_filename = "xml_schema.yaml",
                           input_dataframe = xml_input.input_dataframe,
                           schema_key = "run",
                           output_xml = "Run_output_xml.xml",
                           verbose = True,
                           debug_mode = False)

xml_creation.construct_xml()
xml_creation.save_xml()

# - Validating the XML against the schema (XSD)

file_list = list_web_FullDirectory(url, ext)

download_files(file_list = file_list, output_dir = "XSD_schemas_downloaded/")

xml_is_valid = check_xml_is_valid(xml_tree = xml_creation.xmlVar_RUN_SET,
                                  schema_file = "XSD_schemas_downloaded/SRA.run.xsd")

print("----------------!!!! Created Run xml is vali?", xml_is_valid)
