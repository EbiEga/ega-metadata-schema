# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- Added all versions of the Array templates (reside within ``ega-metadata-schema/templates/array-based-metadata/deprecated_versions``). Taken from their [previous location](https://www.ebi.ac.uk/seqdb/confluence/display/EGA/EGA+AF+templates).

## [1.0.0] - 2021-04-26
### Added
- [ega-metadata-schema/README.md](README.md) - Main README of the project with all its related information.
- [Star2xml/README.md](Star2xml/README.md) - Secondary README of the project, containing all the information related to the star2xml tool (usage, prerequisites, scripts...).
- LICENSE - License applied to the [ega-metadata-schema](https://github.com/EbiEga/ega-metadata-schema) project.
- [Descriptive XMLs](examples/sequence-based-metadata/XML/XMLs_examples-descriptive) - Folder containing (at least) one descriptive XML (with instructions on what information corresponds to which nodes of the XML) for each metadata object.
- [True XMLs](examples/sequence-based-metadata/XML/XMLs_examples-true_values) - Folder containing (at least) one "true" XML (with fabricated values an little to no comments to see what an XML ready to be submitted would look like) for each metadata object.
- [EGA_Array_based_Format_V4.3.xlsx](templates/array-based-metadata/EGA_Array_based_Format_V4.3.xlsx) - Spreadsheet used as template to store and submit Array Format (AF) metadata.
- [EGA_metadata_submission_template_v1.xlsx](templates/sequence-based-metadata/EGA_metadata_submission_template_v1.xlsx) - Spreadsheet used as template to store metadata related to Sequence data. Such spreadsheet can be used as input of the [star2xml](Star2xml/) tool.
- [star2xml.py](Star2xml/star2xml.py) - Main wrapper (Python script) to call the project. Can either generate XMLs based on a given tabular input, or both create them and call the secondary wrapper [validateXML.py](Star2xml/validateXML.py) to validate them.
- [validateXML.py](Star2xml/validateXML.py) - Secondary wrapper (Python script) of the project. Will validate the given XMLs against the given XML schemas (.xsd files). 
- [requirements.txt](Star2xml/requirements.txt) - Text file containing all required packages (with their teste versions) to run the project.
- [input_configuration.yaml](Star2xml/configuration_files/input_configuration.yaml) - Configuration file (Yaml) containing the required fields (column names) that shall appear in the input file.
- [xml_schema.yaml](Star2xml/configuration_files/xml_schema.yaml) - Configuration file (Yaml) containing general information about the project (e.g. ENA's GitHub) and the structure of each metadata object's XML, upon which [XML_creator.py](Star2xml/XML_creator.py) will iterate to construct XMLs. 
- [Input_reader.py](Star2xml/Input_reader.py) - Python script to transform given input file into a dataframe.
- [XML_creator.py](Star2xml/XML_creator.py) - Python script to construct an XML based on the given input dataframe and the XML structure from [xml_schemas.yaml](Star2xml/configuration_files/xml_schema.yaml). 
- [ftp_downloader.py](Star2xml/ftp_downloader.py) - Python script with the required tools to download ENA's XML schemas (.xsd files) from their [FTP server](http://ftp.ebi.ac.uk/pub/databases/ena/doc/xsd/sra_1_6/).
- [git_downloader.py](Star2xml/git_downloader.py) - Python script with the required tools to download ENA's XML schemas (.xsd files) from their [GitHub repository](https://github.com/enasequence/schema/tree/master/src/main/resources/uk/ac/ebi/ena/sra/schema).
- [scripts_for_validation.py](Star2xml/scripts_for_validation.py) - Python script with the required tools to validate an XML against a given XML schema (.xsd file).
- [utils.py](Star2xml/utils.py) - Python script with diverse functions used by other scripts (e.g. ``report_error_messages()``)
- Several images within [miscellaneous/](Star2xml/miscellaneous/) to be referenced by star2xml's [README](Star2xml/README.md).
- Two mock example XMLs ([``test_run.xml``](Star2xml/test_data/XML_examples/test_run.xml) and [``test_sample.xml``](Star2xml/test_data/XML_examples/test_sample.xml)) to check what the output of the tool could be.
