# EGA analysis metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its analysis metadata object. This object is intended to contain metadata about a detailed examination of data (mainly data processing protocols) in order to come to some conclusion. It can be of different types (e.g. sequence variation, sequence alignment, phenotype characterization, gene expression, etc.) that will mainly differ in the protocols used to achieve the processed data of the analysis. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.analysis.json](../../../schemas/EGA.analysis.json "open original schema") |

## EGA analysis metadata schema Type

`object` ([EGA analysis metadata schema](ega-2.md))

# EGA analysis metadata schema Properties

| Property                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                            |
| :-------------------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                                     | Merged   | Required | cannot be null | [EGA analysis metadata schema](ega-2-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectId")                              |
| [schemaDescriptor](#schemadescriptor)                     | `object` | Optional | cannot be null | [EGA analysis metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/schemaDescriptor")                     |
| [objectTitle](#objecttitle)                               | `string` | Optional | cannot be null | [EGA analysis metadata schema](ega-2-properties-title-of-the-analysis.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectTitle")                       |
| [objectDescription](#objectdescription)                   | `string` | Optional | cannot be null | [EGA analysis metadata schema](ega-2-properties-description-of-the-analysis.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectDescription")           |
| [targetedLoci](#targetedloci)                             | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-2-properties-loci-of-the-targeted-genomic-feature.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/targetedLoci")       |
| [typesOfInputData](#typesofinputdata)                     | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-2-properties-types-of-input-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/typesOfInputData")                    |
| [typesOfOutputData](#typesofoutputdata)                   | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-2-properties-types-of-output-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/typesOfOutputData")                  |
| [analysisTypeSpecifications](#analysistypespecifications) | `object` | Required | cannot be null | [EGA analysis metadata schema](ega-2-properties-analysis-type-specifications.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisTypeSpecifications") |
| [analysisFiles](#analysisfiles)                           | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-2-properties-files-of-the-analysis.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisFiles")                     |
| [analysisRelationships](#analysisrelationships)           | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-2-properties-analysis-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisRelationships")            |
| [analysisAttributes](#analysisattributes)                 | `array`  | Optional | cannot be null | [EGA analysis metadata schema](ega-2-properties-analysis-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisAttributes")           |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions.

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-2-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-2-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that analysis EGA ID (EGAZ) is correct](ega-2-properties-objects-ids-block-allof-check-that-analysis-ega-id-egaz-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

## objectTitle

An informative analysis title that should serve as an overview of the analysis, including: performed analysis, samples, purpose... (e.g. 'Variant calling analysis of tumor repressed cells'). This short text can be used to call out analyses records in searches or in displays.

`objectTitle`

*   is optional

*   Type: `string` ([Title of the analysis](ega-2-properties-title-of-the-analysis.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-title-of-the-analysis.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the analysis](ega-2-properties-title-of-the-analysis.md))

### objectTitle Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### objectTitle Examples

```json
"Variant calling analysis of tumor repressed cells"
```

## objectDescription

An in-depth description of the biological relevance and intent of the analysis, including its workflow.

`objectDescription`

*   is optional

*   Type: `string` ([Description of the analysis](ega-2-properties-description-of-the-analysis.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-description-of-the-analysis.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectDescription")

### objectDescription Type

`string` ([Description of the analysis](ega-2-properties-description-of-the-analysis.md))

### objectDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### objectDescription Examples

```json
"The analysis was conducted with the objective of... ...and for that purpose we compared untreated controls against..."
```

## targetedLoci

Array of items that unambiguously define the loci of targeted genomic features in the analysis. For example, if the aim of the analysis was to detect variants in the human gene TAF1 and TP53, their identifiers will be expected in two items of this array.

`targetedLoci`

*   is optional

*   Type: `object[]` ([Locus identifier](ega-4-definitions-locus-identifier.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-loci-of-the-targeted-genomic-feature.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/targetedLoci")

### targetedLoci Type

`object[]` ([Locus identifier](ega-4-definitions-locus-identifier.md))

### targetedLoci Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## typesOfInputData

Types of input data the analysis uses to obtain the processed files.

`typesOfInputData`

*   is optional

*   Type: `string[]` ([Type of data](ega-2-properties-types-of-input-data-type-of-data.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-types-of-input-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/typesOfInputData")

### typesOfInputData Type

`string[]` ([Type of data](ega-2-properties-types-of-input-data-type-of-data.md))

### typesOfInputData Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## typesOfOutputData

Types of output data the analysis uses to obtain the processed files.

`typesOfOutputData`

*   is optional

*   Type: `string[]` ([Type of data](ega-2-properties-types-of-output-data-type-of-data.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-types-of-output-data.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/typesOfOutputData")

### typesOfOutputData Type

`string[]` ([Type of data](ega-2-properties-types-of-output-data-type-of-data.md))

### typesOfOutputData Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## analysisTypeSpecifications

Node containing different sets of fields that depend on the specific analysis type. Depending on the analysis types different metadata will be required.

`analysisTypeSpecifications`

*   is required

*   Type: `object` ([Analysis type specifications](ega-2-properties-analysis-type-specifications.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-analysis-type-specifications.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisTypeSpecifications")

### analysisTypeSpecifications Type

`object` ([Analysis type specifications](ega-2-properties-analysis-type-specifications.md))

## analysisFiles

This property contains the files derived from performing any processing or analysis over raw data (e.g. VCF, aligned BAM...) and those that add context to it (e.g. CSV, TXT...).

`analysisFiles`

*   is optional

*   Type: `object[]` ([EGA File object](ega-4-definitions-ega-file-object.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-files-of-the-analysis.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisFiles")

### analysisFiles Type

`object[]` ([EGA File object](ega-4-definitions-ega-file-object.md))

### analysisFiles Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## analysisRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an analysis being linked to a Sample) the EGA.

`analysisRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-2-properties-analysis-relationships-items.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-analysis-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisRelationships")

### analysisRelationships Type

an array of merged types ([Details](ega-2-properties-analysis-relationships-items.md))

### analysisRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## analysisAttributes

Custom attributes of an analysis: reusable attributes to encode tag-value pairs (e.g. Tag being 'internal tag' and its Value 'this analysis is corresponds to internal tag XYZ') with optional units. Its properties are inherited from the common-definitions.json schema.

`analysisAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-analysis-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisAttributes")

### analysisAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

### analysisAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
