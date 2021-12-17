# EGA ArrayExperiment metadata schema v0.0.1 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its ArrayExperiment metadata object. This objects is intended to be similar to the Experiment metadata object from ENA, but containing metadata from an Array Format (AF) submission. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.ArrayExperiment.json](../out/EGA.ArrayExperiment.json "open original schema") |

## EGA ArrayExperiment metadata schema v0.0.1 Type

`object` ([EGA ArrayExperiment metadata schema v0.0.1](ega-1.md))

# EGA ArrayExperiment metadata schema v0.0.1 Properties

| Property                                                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                         |
| :---------------------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object_id](#object_id)                                           | Merged    | Required | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_id")                                               |
| [object_title](#object_title)                                     | `string`  | Optional | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-title-of-the-arrayexperiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_title")                                 |
| [object_description](#object_description)                         | `string`  | Optional | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-description-of-the-arrayexperiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_description")                     |
| [technology](#technology)                                         | `object`  | Required | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology")        |
| [array_label](#array_label)                                       | `array`   | Required | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-array-label-of-the-arrayexperiment-efo0000562.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_label")                 |
| [experimental_design](#experimental_design)                       | `object`  | Required | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/experimental_design") |
| [array_type](#array_type)                                         | `object`  | Required | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_type")                   |
| [assayed_molecule](#assayed_molecule)                             | `object`  | Required | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/assayed_molecule")       |
| [adf_files](#adf_files)                                           | `array`   | Optional | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-array-design-format-adf-ncitc172213-file-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/adf_files")                  |
| [sample_number](#sample_number)                                   | `integer` | Optional | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-number-of-samples-of-the-arrayexperiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/sample_number")                    |
| [array_experiment_relationships](#array_experiment_relationships) | `array`   | Optional | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-arrayexperiment-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_relationships")              |
| [array_experiment_attributes](#array_experiment_attributes)       | `array`   | Optional | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-arrayexperiment-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_attributes")             |
| [array_experiment_protocols](#array_experiment_protocols)         | `array`   | Optional | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-protocols-related-to-an-arrayexperiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_protocols")        |

## object_id

Node containing the main identifiers of the object (e.g. alias, center_name...), inherited from the common definitions. #! We extend the core object (object_core_id) by adding a pattern check based on this schema's nature: an ArrayExperiment (by using EGA-ArrayExperiment-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-1-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_id")

### object_id Type

`object` ([Object's IDs block](ega-1-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that ArrayExperiment EGA ID (EGAE) is correct](ega-1-properties-objects-ids-block-allof-check-that-arrayexperiment-ega-id-egae-is-correct.md "check type definition")

## object_title

An informative experiment title that should serve as an overview of the experiment, including: used technology, samples, purpose... (e.g. 'Affymetrix-X microarray of human breast cancer cell line MCF-7 treated with tamoxifen compared with untreated controls'). This short text can be used to call out ArrayExperiment records in searches or in displays.

`object_title`

*   is optional

*   Type: `string` ([Title of the ArrayExperiment](ega-1-properties-title-of-the-arrayexperiment.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-title-of-the-arrayexperiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_title")

### object_title Type

`string` ([Title of the ArrayExperiment](ega-1-properties-title-of-the-arrayexperiment.md))

### object_title Examples

```json
"Affymetrix-X microarray of human breast cancer cell line MCF-7 treated with tamoxifen compared with untreated controls"
```

## object_description

An in-depth description of the biological relevance and intent of the ArrayExperiment, including the experimental workflow.

`object_description`

*   is optional

*   Type: `string` ([Description of the ArrayExperiment](ega-1-properties-description-of-the-arrayexperiment.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-description-of-the-arrayexperiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_description")

### object_description Type

`string` ([Description of the ArrayExperiment](ega-1-properties-description-of-the-arrayexperiment.md))

### object_description Examples

```json
"The experiment was conducted with the objective of... ...and obtained positive results at..."
```

## technology

Microarray technology applicable for the ArrayExperiment. It contains both the ID  (e.g. One-colour microarray) and the CURIE  (e.g. EFO:0010939) of the technology.

`technology`

*   is required

*   Type: `object` ([Microarray technology of the ArrayExperiment \[EFO:0002698\]](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/technology")

### technology Type

`object` ([Microarray technology of the ArrayExperiment \[EFO:0002698\]](ega-1-properties-microarray-technology-of-the-arrayexperiment-efo0002698.md))

## array_label

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. Can be repeated so that dual labelled arrays can be taken into account.

`array_label`

*   is required

*   Type: `object[]` ([Repeatable array_label node](ega-2-definitions-repeatable-array_label-node.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-array-label-of-the-arrayexperiment-efo0000562.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_label")

### array_label Type

`object[]` ([Repeatable array_label node](ega-2-definitions-repeatable-array_label-node.md))

### array_label Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## experimental_design

Experimental factor describing the method of investigating particular types of research questions or solving particular types of problems. It contains both the human readable ID (e.g. RNA stability design) and CURIE (e.g. EFO:0001783) of the experimental design.

`experimental_design`

*   is required

*   Type: `object` ([Experimental design of the ArrayExperiment \[EFO:0001426\]](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/experimental_design")

### experimental_design Type

`object` ([Experimental design of the ArrayExperiment \[EFO:0001426\]](ega-1-properties-experimental-design-of-the-arrayexperiment-efo0001426.md))

## array_type

Type of array (not its purpose per se) providing a glimpse of the used technology. It contains both the human readable ID (e.g. Proteomic profiling by array) and CURIE (e.g. EFO:0002765) of the array type.

`array_type`

*   is required

*   Type: `object` ([Array type of the ArrayExperiment \[EFO:0002696\]](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_type")

### array_type Type

`object` ([Array type of the ArrayExperiment \[EFO:0002696\]](ega-1-properties-array-type-of-the-arrayexperiment-efo0002696.md))

## assayed_molecule

Type of molecule assayed. It contains both the human readable ID (e.g. DNA assay) and CURIE (e.g. EFO:0001456) of the assayed molecule.

`assayed_molecule`

*   is required

*   Type: `object` ([Assayed molecule in the ArrayExperiment \[EFO:0002772\]](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/assayed_molecule")

### assayed_molecule Type

`object` ([Assayed molecule in the ArrayExperiment \[EFO:0002772\]](ega-1-properties-assayed-molecule-in-the-arrayexperiment-efo0002772.md))

## adf_files

The array design format (ADF) \[NCIT:C172213] is the unique set of probes (with their coordinates) found on the microarray chip. They can be standard (sold by a company) or custom. Its format is of a spreadsheet-like tab-delimited text file with metadata header rows, followed by a multi-column table of probe information. This object shall only be used if the EGA is the one storing such file. Otherwise, the Relationships object shall be used to point from the ArrayExperiment to the ADF submitted elsewhere.

`adf_files`

*   is optional

*   Type: `object[]` ([EGA File object](ega-2-definitions-ega-file-object.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-array-design-format-adf-ncitc172213-file-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/adf_files")

### adf_files Type

`object[]` ([EGA File object](ega-2-definitions-ega-file-object.md))

### adf_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## sample_number

Number of samples included in the experiment. One sample corresponds to one biological replicate \[EFO:0002091] (it could be the genetic content from a single cell, a tissue… from a single individual or from several individuals). Shall not be mistaken for technical replicates \[CHEBI:24432] being used several times (see <https://www.ebi.ac.uk/seqdb/confluence/pages/viewpage.action?spaceKey=EGA&title=Sample+Representation>).

`sample_number`

*   is optional

*   Type: `integer` ([Number of samples of the ArrayExperiment](ega-1-properties-number-of-samples-of-the-arrayexperiment.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-number-of-samples-of-the-arrayexperiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/sample_number")

### sample_number Type

`integer` ([Number of samples of the ArrayExperiment](ega-1-properties-number-of-samples-of-the-arrayexperiment.md))

### sample_number Examples

```json
30
```

## array_experiment_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an ArrayExperiment being linked to a Sample) the EGA.

`array_experiment_relationships`

*   is optional

*   Type: `object[]` ([EGA Relationships object](ega-2-definitions-ega-relationships-object.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-arrayexperiment-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_relationships")

### array_experiment_relationships Type

`object[]` ([EGA Relationships object](ega-2-definitions-ega-relationships-object.md))

### array_experiment_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## array_experiment_attributes

Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`array_experiment_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-arrayexperiment-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_attributes")

### array_experiment_attributes Type

`object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

### array_experiment_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## array_experiment_protocols

Comprises metadata (e.g. Type of protocol) of a plan specification related to an ArrayExperiment, with sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents.

`array_experiment_protocols`

*   is optional

*   Type: `object[]` ([EGA Protocols object](ega-2-definitions-ega-protocols-object.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-protocols-related-to-an-arrayexperiment.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_protocols")

### array_experiment_protocols Type

`object[]` ([EGA Protocols object](ega-2-definitions-ega-protocols-object.md))

### array_experiment_protocols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
