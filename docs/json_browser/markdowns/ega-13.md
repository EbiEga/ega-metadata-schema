# EGA dataset metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Dataset metadata object. This object is intended to contain metadata about the collection of file-containing objects (ArrayAssay, runs or analyses) subject to controlled access. In other words, a dataset encompasses a set of objects to which access is granted as a whole, since access given to a data requester is access to a dataset, and fall under the same Policy. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/studies>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.dataset.json](../out/EGA.dataset.json "open original schema") |

## EGA dataset metadata schema Type

`object` ([EGA dataset metadata schema](ega-13.md))

# EGA dataset metadata schema Properties

| Property                                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                          |
| :---------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [object_id](#object_id)                               | Merged   | Required | cannot be null | [EGA dataset metadata schema](ega-13-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/object_id")                                      |
| [schema_descriptor](#schema_descriptor)               | `object` | Optional | cannot be null | [EGA dataset metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/schema_descriptor")                             |
| [object_title](#object_title)                         | `string` | Required | cannot be null | [EGA dataset metadata schema](ega-13-properties-title-of-the-dataset.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/object_title")                                |
| [object_description](#object_description)             | `string` | Optional | cannot be null | [EGA dataset metadata schema](ega-13-properties-description-of-the-dataset.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/object_description")                    |
| [dataset_type](#dataset_type)                         | `string` | Required | cannot be null | [EGA dataset metadata schema](ega-13-properties-dataset-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/dataset_type")                                        |
| [approximate_release_date](#approximate_release_date) | Merged   | Optional | cannot be null | [EGA dataset metadata schema](ega-13-properties-approximate-release-date-of-the-dataset.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/approximate_release_date") |
| [dataset_relationships](#dataset_relationships)       | `array`  | Optional | cannot be null | [EGA dataset metadata schema](ega-13-properties-dataset-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/dataset_relationships")                      |
| [dataset_attributes](#dataset_attributes)             | `array`  | Optional | cannot be null | [EGA dataset metadata schema](ega-13-properties-dataset-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/dataset_attributes")                     |

## object_id

Node containing the main identifiers of the object (e.g. alias, center_name...), inherited from the common definitions. #! We extend the core object (object_core_id) by adding a pattern check based on this schema's nature: an dataset (by using EGA-dataset-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-13-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-13-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/object_id")

### object_id Type

`object` ([Object's IDs block](ega-13-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that dataset EGA ID (EGAD) is correct](ega-13-properties-objects-ids-block-allof-check-that-dataset-ega-id-egad-is-correct.md "check type definition")

## schema_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/schema_descriptor")

### schema_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object_title

Free-form title of the Dataset. It should be the first picture of the dataset content and not contain more than 30 words. It can be used to call out dataset records in searches or displays.

`object_title`

*   is required

*   Type: `string` ([Title of the dataset](ega-13-properties-title-of-the-dataset.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-13-properties-title-of-the-dataset.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/object_title")

### object_title Type

`string` ([Title of the dataset](ega-13-properties-title-of-the-dataset.md))

### object_title Examples

```json
"EBI colon cancer dataset"
```

## object_description

More extensive free-form description of the Dataset. It should include the content of the dataset (number of samples, file types, technology/protocol used to obtain the data…) and not extend more than 4 sentences.

`object_description`

*   is optional

*   Type: `string` ([Description of the dataset](ega-13-properties-description-of-the-dataset.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-13-properties-description-of-the-dataset.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/object_description")

### object_description Type

`string` ([Description of the dataset](ega-13-properties-description-of-the-dataset.md))

### object_description Examples

```json
"This dataset is related to Project X by grant Y and encompasses samples from group Z, whose DNA was hybridized against a microarray designed for SNPs."
```

## dataset_type

Type of the dataset, expressing the overall purpose of the dataset. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition. The CV was inherited from ENA's dataset types.

`dataset_type`

*   is required

*   Type: `string` ([Dataset type](ega-13-properties-dataset-type.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-13-properties-dataset-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/dataset_type")

### dataset_type Type

`string` ([Dataset type](ega-13-properties-dataset-type.md))

### dataset_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                                               | Explanation |
| :------------------------------------------------------------------ | :---------- |
| `"whole genome sequencing"`                                         |             |
| `"exome sequencing"`                                                |             |
| `"genotyping by array"`                                             |             |
| `"transcriptome profiling by high-throughput sequencing"`           |             |
| `"transcriptome profiling by array"`                                |             |
| `"amplicon sequencing"`                                             |             |
| `"methylation binding domain sequencing"`                           |             |
| `"methylation profiling by high-throughput sequencing"`             |             |
| `"phenotype information"`                                           |             |
| `"genomic variant calling"`                                         |             |
| `"chromatin accessibility profiling by high-throughput sequencing"` |             |
| `"histone modification profiling by high-throughput sequencing"`    |             |
| `"chip-Seq"`                                                        |             |
| `"study summary information"`                                       |             |

### dataset_type Examples

```json
"whole genome sequencing"
```

## approximate_release_date

An approximate date of the desired release of the dataset. Bare in mind that this will NOT automatically release the dataset, but instead may be used to set a reminder to the submitter (and EGA's HelpDesk team) in case the dataset was not released by this time. This would help in cases where this step was forgotten by the submitter or release was stalled for some reason.

`approximate_release_date`

*   is optional

*   Type: `string` ([Approximate release date of the dataset](ega-13-properties-approximate-release-date-of-the-dataset.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-13-properties-approximate-release-date-of-the-dataset.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/approximate_release_date")

### approximate_release_date Type

`string` ([Approximate release date of the dataset](ega-13-properties-approximate-release-date-of-the-dataset.md))

all of

*   [Pattern of an EGA ISO date (YYYY-MM-DD)](ega-12-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md "check type definition")

*   [We cap the reminder up to 3 years](ega-13-properties-approximate-release-date-of-the-dataset-allof-we-cap-the-reminder-up-to-3-years.md "check type definition")

### approximate_release_date Examples

```json
"2023-12-01"
```

```json
"2024-01-10"
```

## dataset_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a dataset) the EGA.

`dataset_relationships`

*   is optional

*   Type: `object[]` ([EGA Relationships object](ega-12-definitions-ega-relationships-object.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-13-properties-dataset-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/dataset_relationships")

### dataset_relationships Type

`object[]` ([EGA Relationships object](ega-12-definitions-ega-relationships-object.md))

### dataset_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## dataset_attributes

Custom attributes of a dataset: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`dataset_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-13-properties-dataset-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.dataset.json#/properties/dataset_attributes")

### dataset_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### dataset_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
