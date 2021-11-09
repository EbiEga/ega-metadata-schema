# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

# [0.0.0] 
## 2021-11-05
### Modified
- [star2xml](https://github.com/EGA-archive/star2xml) - Moved tool star2xml to its own repository: https://github.com/EGA-archive/star2xml. 

## 2021-04-26
### Added
- [ega-metadata-schema/README.md](README.md) - Main README of the project with all its related information.
- LICENSE - License applied to the [ega-metadata-schema](https://github.com/EbiEga/ega-metadata-schema) project.
- [Descriptive XMLs](examples/sequence-based-metadata/XML/XMLs_examples-descriptive) - Folder containing (at least) one descriptive XML (with instructions on what information corresponds to which nodes of the XML) for each metadata object.
- [True XMLs](examples/sequence-based-metadata/XML/XMLs_examples-true_values) - Folder containing (at least) one "true" XML (with fabricated values an little to no comments to see what an XML ready to be submitted would look like) for each metadata object.
- [EGA_Array_based_Format_V4.3.xlsx](templates/array-based-metadata/EGA_Array_based_Format_V4.3.xlsx) - Spreadsheet used as template to store and submit Array Format (AF) metadata.
- [EGA_metadata_submission_template_v1.xlsx](templates/sequence-based-metadata/EGA_metadata_submission_template_v1.xlsx) - Spreadsheet used as template to store metadata related to Sequence data. Such spreadsheet can be used as input of the [star2xml](https://github.com/EGA-archive/star2xml) tool.