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
- Added [``sample``](schemas/EGA.sample.json) and [``individual``](schemas/EGA.individual.json) JSON schemas [[PR#27](https://github.com/EbiEga/ega-metadata-schema/pull/27)]
- Added [``object-set``](schemas/EGA.object-set.json) schema to contain grouped objects in sets [[PR#30](https://github.com/EbiEga/ega-metadata-schema/pull/30)].
- Added remaining schemas (some empty for the moment) [[PR#30](https://github.com/EbiEga/ega-metadata-schema/pull/30)].
- Added PR and issue templates [[PR#40](https://github.com/EbiEga/ega-metadata-schema/pull/40)].
- Added example XML to JSON documents (see [README.md](examples/xml-json-same-objects/README.md)) [[PR#35](https://github.com/EbiEga/ega-metadata-schema/pull/35)].
- Added [contributing documentation](./docs/contributing.md) [[PR#41](https://github.com/EbiEga/ega-metadata-schema/pull/41)]
- Added GH [workflow](./.github/workflows/super_linter.yml) to lint code and documentation of the repository [[PR#42](https://github.com/EbiEga/ega-metadata-schema/pull/42)].
- Added GH [workflow](./.github/workflows/json_validation.yml) to validate JSON examples automatically on PRs [[PR#42](https://github.com/EbiEga/ega-metadata-schema/pull/42)].
- Added GH [workflow](./.github/workflows/markdown_creation.yml) to generate automatically the JSON browser's markdown documentation when changes are pushed to "main" (a PR is closed) [[PR#42](https://github.com/EbiEga/ega-metadata-schema/pull/42)].
- Added GH [workflow diagram](./docs/gh_workflows/) [[PR#42](https://github.com/EbiEga/ega-metadata-schema/pull/42)].
- Added new attributes to samples and individuals, aligning with phenopackets but with the least overlapping fields [[PR#45](https://github.com/EbiEga/ega-metadata-schema/pull/45)].
- Added "resources" (ontologies) property to the submission object to handle ontology versions [[PR#48](https://github.com/EbiEga/ega-metadata-schema/pull/48)].

### Modified
- [star2xml](https://github.com/EGA-archive/star2xml) - Moved tool star2xml to its own repository: "https://github.com/EGA-archive/star2xml".
- [JSON schemas](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas) - improved drafted JSON schemas for AF (Array Format) Array and Experiment metadata.
- Modified the relationships node so that the target and source are of type ``object_core_id`` (being able to reference non-registered objects). [[PR#26](https://github.com/EbiEga/ega-metadata-schema/pull/26)]
- Updated markdown documentation of the schemas (see [README](docs/json_browser/markdowns/README.md)) [[PR#27](https://github.com/EbiEga/ega-metadata-schema/pull/27)]
- Updated JSON schemas ([``common definitions``](schemas/EGA.common-definitions.json), [``ArrayAssay``](schemas/EGA.ArrayAssay.json) and [``ArrayExperiment``](schemas/EGA.ArrayExperiment.json)) [[PR#27](https://github.com/EbiEga/ega-metadata-schema/pull/27)]
- Removed Jupyter-notebook for validation and added instructions in [README.md](schemas/README.md) to validate through AJV [[PR#30](https://github.com/EbiEga/ega-metadata-schema/pull/30)].
- Replaced [``ArrayAssay``](schemas/EGA.ArrayAssay.json) with [``Assay``](schemas/EGA.assay.json), fusing "Run" object (from previous model) and Array Assays [[PR#34](https://github.com/EbiEga/ega-metadata-schema/pull/34)]
- Added the [``Experiment``](schemas/EGA.experiment.json) object, and fused ArrayExperiment with it, removing the latter [[PR#34](https://github.com/EbiEga/ega-metadata-schema/pull/34)]
- Added the [``Analysis``](schemas/EGA.analysis.json) object [[PR#34](https://github.com/EbiEga/ega-metadata-schema/pull/34)]
- Added loci descriptor node to common definitions (inherited by other objects) [[PR#34](https://github.com/EbiEga/ega-metadata-schema/pull/34)]
- Updated protocols object [[PR#34](https://github.com/EbiEga/ega-metadata-schema/pull/34)]
- Added folder ``controlled_vocabulary_schemas`` with JSON documents containing controlled vocabulary for specific fields. These are inherited in the common definitions mainly [[PR#34](https://github.com/EbiEga/ega-metadata-schema/pull/34)]
- All external accessions are now required to follow a CURIE format (e.g. ``ncbigene:100010``) [[PR#34](https://github.com/EbiEga/ega-metadata-schema/pull/34)]
- Updated JSON markdowns [[PR#34](https://github.com/EbiEga/ega-metadata-schema/pull/34)]
- Added example XML to JSON documents (see [README.md](examples/xml-json-same-objects/README.md)) [[PR#35](https://github.com/EbiEga/ega-metadata-schema/pull/35)].
- Modified relationship nodes so that only one end of the relationship is allowed [[PR#39](https://github.com/EbiEga/ega-metadata-schema/pull/39)].
- Modified relationship nodes to accept only specific combinations per object [[PR#39](https://github.com/EbiEga/ega-metadata-schema/pull/39)].
- Moved and renamed the validation examples from [schemas/validation_tests](./schemas/validation_tests) to [examples/json_validation_tests](./examples/json_validation_tests/) [[PR#42](https://github.com/EbiEga/ega-metadata-schema/pull/42)].
- Changed cross-schema absolute references to relative ones [PR#44](https://github.com/EbiEga/ega-metadata-schema/pull/44)]
- Modified all JSON schema pointers (``$ids``) for them to point to the raw text version of each file [PR#46](https://github.com/EbiEga/ega-metadata-schema/pull/46)].
- Transformed the protocols properties of experiments and analyses into an object on its own [PR#47](https://github.com/EbiEga/ega-metadata-schema/pull/47)].

## [0.0.0] - 2021-04-26
### Added [2021-04-26]
- [ega-metadata-schema/README.md](README.md) - Main README of the project with all its related information.
- LICENSE - License applied to the [ega-metadata-schema](https://github.com/EbiEga/ega-metadata-schema) project.
- [Descriptive XMLs](examples/sequence-based-metadata/XML/XMLs_examples-descriptive) - Folder containing (at least) one descriptive XML (with instructions on what information corresponds to which nodes of the XML) for each metadata object.
- [True XMLs](examples/sequence-based-metadata/XML/XMLs_examples-true_values) - Folder containing (at least) one "true" XML (with fabricated values an little to no comments to see what an XML ready to be submitted would look like) for each metadata object.
- [EGA_Array_based_Format_V4.3.xlsx](templates/array-based-metadata/EGA_Array_based_Format_V4.3.xlsx) - Spreadsheet used as template to store and submit Array Format (AF) metadata.
- [EGA_metadata_submission_template_v1.xlsx](templates/sequence-based-metadata/EGA_metadata_submission_template_v1.xlsx) - Spreadsheet used as template to store metadata related to Sequence data. Such spreadsheet can be used as input of the [star2xml](https://github.com/EGA-archive/star2xml) tool.