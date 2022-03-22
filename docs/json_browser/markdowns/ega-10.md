# EGA analysis metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json
```

Empty for the moment.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.analysis.json](../out/EGA.analysis.json "open original schema") |

## EGA analysis metadata schema Type

`object` ([EGA analysis metadata schema](ega-10.md))

# EGA analysis metadata schema Properties

| Property                                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                     |
| :------------------------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object_id](#object_id)                                       | Merged   | Required | cannot be null | [EGA analysis metadata schema](ega-10-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/object_id")                               |
| [schema_descriptor](#schema_descriptor)                       | `object` | Optional | cannot be null | [EGA analysis metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/schema_descriptor")                      |
| [object_title](#object_title)                                 | `string` | Optional | cannot be null | [EGA analysis metadata schema](ega-10-properties-title-of-the-analysis.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/object_title")                        |
| [object_description](#object_description)                     | `string` | Optional | cannot be null | [EGA analysis metadata schema](ega-10-properties-description-of-the-analysis.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/object_description")            |
| [analysis_protocols](#analysis_protocols)                     | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-10-properties-protocols-related-to-an-analysis.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_protocols")       |
| [targeted_loci](#targeted_loci)                               | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-10-properties-loci-of-the-targeted-genomic-feature.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/targeted_loci")        |
| [types_of_input_data](#types_of_input_data)                   | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-10-properties-types-of-input-data.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/types_of_input_data")                   |
| [types_of_output_data](#types_of_output_data)                 | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-10-properties-types-of-output-data.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/types_of_output_data")                 |
| [analysis_type_specifications](#analysis_type_specifications) | `object` | Required | cannot be null | [EGA analysis metadata schema](ega-10-properties-analysis-type-specifications.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_type_specifications") |
| [analysis_files](#analysis_files)                             | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-10-properties-files-of-the-analysis.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_files")                      |
| [analysis_relationships](#analysis_relationships)             | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-10-properties-analysis-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_relationships")             |
| [analysis_attributes](#analysis_attributes)                   | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-10-properties-analysis-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_attributes")            |

## object_id

Node containing the main identifiers of the object (e.g. alias, center_name...), inherited from the common definitions.

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-10-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/object_id")

### object_id Type

`object` ([Object's IDs block](ega-10-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that analysis EGA ID (EGAZ) is correct](ega-10-properties-objects-ids-block-allof-check-that-analysis-ega-id-egaz-is-correct.md "check type definition")

## schema_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/schema_descriptor")

### schema_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object_title

An informative analysis title that should serve as an overview of the analysis, including: performed analysis, samples, purpose... (e.g. 'Variant calling analysis of tumor repressed cells'). This short text can be used to call out analyses records in searches or in displays.

`object_title`

*   is optional

*   Type: `string` ([Title of the analysis](ega-10-properties-title-of-the-analysis.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-title-of-the-analysis.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/object_title")

### object_title Type

`string` ([Title of the analysis](ega-10-properties-title-of-the-analysis.md))

### object_title Examples

```json
"Variant calling analysis of tumor repressed cells"
```

## object_description

An in-depth description of the biological relevance and intent of the analysis, including its workflow.

`object_description`

*   is optional

*   Type: `string` ([Description of the analysis](ega-10-properties-description-of-the-analysis.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-description-of-the-analysis.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/object_description")

### object_description Type

`string` ([Description of the analysis](ega-10-properties-description-of-the-analysis.md))

### object_description Examples

```json
"The analysis was conducted with the objective of... ...and for that purpose we compared untreated controls against..."
```

## analysis_protocols

Comprises metadata (e.g. Type of protocol) of a plan specification executed during an analysis. It shall have a sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents.

`analysis_protocols`

*   is optional

*   Type: `object[]` ([EGA Protocols object](ega-12-definitions-ega-protocols-object.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-protocols-related-to-an-analysis.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_protocols")

### analysis_protocols Type

`object[]` ([EGA Protocols object](ega-12-definitions-ega-protocols-object.md))

### analysis_protocols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## targeted_loci

Array of items that unambiguously define the loci of targeted genomic features in the analysis. For example, if the aim of the analysis was to detect variants in the human gene TAF1 and TP53, their identifiers will be expected in two items of this array.

`targeted_loci`

*   is optional

*   Type: `object[]` ([Locus identifier](ega-12-definitions-locus-identifier.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-loci-of-the-targeted-genomic-feature.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/targeted_loci")

### targeted_loci Type

`object[]` ([Locus identifier](ega-12-definitions-locus-identifier.md))

### targeted_loci Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## types_of_input_data

Types of input data the analysis uses to obtain the processed files.

`types_of_input_data`

*   is optional

*   Type: `string[]` ([Type of data](ega-10-properties-types-of-input-data-type-of-data.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-types-of-input-data.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/types_of_input_data")

### types_of_input_data Type

`string[]` ([Type of data](ega-10-properties-types-of-input-data-type-of-data.md))

### types_of_input_data Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## types_of_output_data

Types of output data the analysis uses to obtain the processed files.

`types_of_output_data`

*   is optional

*   Type: `string[]` ([Type of data](ega-10-properties-types-of-output-data-type-of-data.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-types-of-output-data.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/types_of_output_data")

### types_of_output_data Type

`string[]` ([Type of data](ega-10-properties-types-of-output-data-type-of-data.md))

### types_of_output_data Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## analysis_type_specifications

Node containing different sets of fields that depend on the specific analysis type. Depending on the analysis types different metadata will be required.

`analysis_type_specifications`

*   is required

*   Type: `object` ([Analysis type specifications](ega-10-properties-analysis-type-specifications.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-analysis-type-specifications.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_type_specifications")

### analysis_type_specifications Type

`object` ([Analysis type specifications](ega-10-properties-analysis-type-specifications.md))

## analysis_files

This property contains the files derived from performing any processing or analysis over raw data (e.g. VCF, aligned BAM...) and those that add context to it (e.g. CSV, TXT...).

`analysis_files`

*   is optional

*   Type: `object[]` ([EGA File object](ega-12-definitions-ega-file-object.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-files-of-the-analysis.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_files")

### analysis_files Type

`object[]` ([EGA File object](ega-12-definitions-ega-file-object.md))

### analysis_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## analysis_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an analysis being linked to a Sample) the EGA.

`analysis_relationships`

*   is optional

*   Type: `object[]` ([EGA Relationships object](ega-12-definitions-ega-relationships-object.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-analysis-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_relationships")

### analysis_relationships Type

`object[]` ([EGA Relationships object](ega-12-definitions-ega-relationships-object.md))

### analysis_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## analysis_attributes

Custom attributes of an analysis: reusable attributes to encode tag-value pairs (e.g. Tag being 'internal tag' and its Value 'this analysis is corresponds to internal tag XYZ') with optional units. Its properties are inherited from the common-definitions.json schema.

`analysis_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-10-properties-analysis-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_attributes")

### analysis_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### analysis_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
