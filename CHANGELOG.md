# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Added all versions of the Array templates (reside within ``ega-metadata-schema/templates/array-based-metadata/deprecated_versions``). Taken from their [previous location](https://www.ebi.ac.uk/seqdb/confluence/display/EGA/EGA+AF+templates).
- Added [docs](docs/) folder [[PR#26](https://github.com/EbiEga/ega-metadata-schema/pull/26)]
- Added [metadata model diagram](docs/metadata_model/README.md) [[PR#26](https://github.com/EbiEga/ega-metadata-schema/pull/26)]
- Added markdown documentation (json_browser) explaining the schemas (see [README](docs/json_browser/README.md)) [[PR#26](https://github.com/EbiEga/ega-metadata-schema/pull/26)]
- Added ``titles`` and ``descriptions`` to several constraints within the schemas (for the markdowns to have a better explanation) [[PR#26](https://github.com/EbiEga/ega-metadata-schema/pull/26)]
- Added ``examples`` and ``meta:enum`` keywords within the schemas for them to appear in the markdowns. [[PR#26](https://github.com/EbiEga/ega-metadata-schema/pull/26)]
### Modified
- [star2xml](https://github.com/EGA-archive/star2xml) - Moved tool star2xml to its own repository: https://github.com/EGA-archive/star2xml. 
- [JSON schemas](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas) - improved drafted JSON schemas for AF (Array Format) Array and Experiment metadata.
- Modified the relationships node so that the target and source are of type ``object_core_id`` (being able to reference non-registered objects). [[PR#26](https://github.com/EbiEga/ega-metadata-schema/pull/26)]

## [0.0.0] - 2021-04-26
### Added
- [ega-metadata-schema/README.md](README.md) - Main README of the project with all its related information.
- LICENSE - License applied to the [ega-metadata-schema](https://github.com/EbiEga/ega-metadata-schema) project.
- [Descriptive XMLs](examples/sequence-based-metadata/XML/XMLs_examples-descriptive) - Folder containing (at least) one descriptive XML (with instructions on what information corresponds to which nodes of the XML) for each metadata object.
- [True XMLs](examples/sequence-based-metadata/XML/XMLs_examples-true_values) - Folder containing (at least) one "true" XML (with fabricated values an little to no comments to see what an XML ready to be submitted would look like) for each metadata object.
- [EGA_Array_based_Format_V4.3.xlsx](templates/array-based-metadata/EGA_Array_based_Format_V4.3.xlsx) - Spreadsheet used as template to store and submit Array Format (AF) metadata.
- [EGA_metadata_submission_template_v1.xlsx](templates/sequence-based-metadata/EGA_metadata_submission_template_v1.xlsx) - Spreadsheet used as template to store metadata related to Sequence data. Such spreadsheet can be used as input of the [star2xml](https://github.com/EGA-archive/star2xml) tool.