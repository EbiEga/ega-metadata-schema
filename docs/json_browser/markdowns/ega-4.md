# EGA sample metadata schema v0.0.1 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its sample metadata object. This object is intended to contain metadata about the physical sample used in the experiment. A sample is defined as a limited quantity of something (e.g. a portion of a substance or individual) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample shall not be confused with the individual (i.e. a person or donor) such sample derives from, for 'individual' is its own metadata object (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json>). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json](../out/EGA.sample.json "open original schema") |

## EGA sample metadata schema v0.0.1 Type

`object` ([EGA sample metadata schema v0.0.1](ega-4.md))

# EGA sample metadata schema v0.0.1 Properties

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                     |
| :------------------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object_id](#object_id)                                 | Merged   | Required | cannot be null | [EGA sample metadata schema v0.0.1](ega-4-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_id")                                             |
| [object_title](#object_title)                           | `string` | Optional | cannot be null | [EGA sample metadata schema v0.0.1](ega-4-properties-title-of-the-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_title")                                        |
| [object_description](#object_description)               | `string` | Optional | cannot be null | [EGA sample metadata schema v0.0.1](ega-4-properties-description-of-the-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_description")                            |
| [organism_descriptor](#organism_descriptor)             | Merged   | Required | cannot be null | [EGA sample metadata schema v0.0.1](ega-4-properties-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/organism_descriptor")                |
| [minimal_public_attributes](#minimal_public_attributes) | `object` | Required | cannot be null | [EGA sample metadata schema v0.0.1](ega-4-properties-minimal-public-attributes-describing-a-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/minimal_public_attributes") |
| [sample_collection_date](#sample_collection_date)       | `string` | Optional | cannot be null | [EGA sample metadata schema v0.0.1](ega-2-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection_date")           |
| [sample_grouping](#sample_grouping)                     | Merged   | Optional | cannot be null | [EGA sample metadata schema v0.0.1](ega-4-properties-sample-group-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping")                                 |
| [sample_relationships](#sample_relationships)           | `array`  | Optional | cannot be null | [EGA sample metadata schema v0.0.1](ega-4-properties-sample-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_relationships")                               |
| [sample_attributes](#sample_attributes)                 | `array`  | Optional | cannot be null | [EGA sample metadata schema v0.0.1](ega-4-properties-sample-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_attributes")                              |

## object_id

Node containing the main identifiers of the object (e.g. alias, center_name...), inherited from the common definitions. #! We extend the core object (object_core_id) by adding a pattern check based on this schema's nature: a sample (by using EGA-sample-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-4-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA sample metadata schema v0.0.1](ega-4-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_id")

### object_id Type

`object` ([Object's IDs block](ega-4-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that sample EGA ID (EGAN) is correct](ega-4-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-is-correct.md "check type definition")

## object_title

An informative sample title that should serve as an overview (e.g. sample tag, pseudonyms, sample type, sample groups, purpose...) of the sample and differentiate it from others. This short text can be used to call out sample records in searches or in displays.

`object_title`

*   is optional

*   Type: `string` ([Title of the sample](ega-4-properties-title-of-the-sample.md))

*   cannot be null

*   defined in: [EGA sample metadata schema v0.0.1](ega-4-properties-title-of-the-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_title")

### object_title Type

`string` ([Title of the sample](ega-4-properties-title-of-the-sample.md))

### object_title Examples

```json
"Buccal swab from COVID+ patient NM305004"
```

## object_description

An informative sample descripotion that describes the sample and differentiates it from others.

`object_description`

*   is optional

*   Type: `string` ([Description of the sample](ega-4-properties-description-of-the-sample.md))

*   cannot be null

*   defined in: [EGA sample metadata schema v0.0.1](ega-4-properties-description-of-the-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_description")

### object_description Type

`string` ([Description of the sample](ega-4-properties-description-of-the-sample.md))

### object_description Examples

```json
"Buccal swab from COVID positive patient (NM305004) was taken on a sunny morning, had a lower volume than expected, then was sent to..."
```

## organism_descriptor

This node describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance by default.

`organism_descriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-4-properties-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA sample metadata schema v0.0.1](ega-4-properties-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/organism_descriptor")

### organism_descriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-4-properties-organism-obi0100026-descriptor-block.md))

any of

*   [Either the taxon ID is provided](ega-4-properties-organism-obi0100026-descriptor-block-anyof-either-the-taxon-id-is-provided.md "check type definition")

*   [Or the scientific name is provided](ega-4-properties-organism-obi0100026-descriptor-block-anyof-or-the-scientific-name-is-provided.md "check type definition")

## minimal_public_attributes

Among all fields describing a sample, some may contain identifiable metadata and thus be private. Nevertheless, there are three basic attributes that every sample should contain (even if they are unknown): subject id (sample donor id), biological sex and phenotype. These shall be displayed and queryable.

`minimal_public_attributes`

*   is required

*   Type: `object` ([Minimal public attributes describing a sample](ega-4-properties-minimal-public-attributes-describing-a-sample.md))

*   cannot be null

*   defined in: [EGA sample metadata schema v0.0.1](ega-4-properties-minimal-public-attributes-describing-a-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/minimal_public_attributes")

### minimal_public_attributes Type

`object` ([Minimal public attributes describing a sample](ega-4-properties-minimal-public-attributes-describing-a-sample.md))

## sample_collection_date

ISO date (format YYYY-MM-DD - e.g. '2021-05-15') when the sample was collected. If the protocols are long enough, the date shall be the day the collection concluded.

`sample_collection_date`

*   is optional

*   Type: `string` ([Pattern of an EGA ISO date (YYYY-MM-DD)](ega-2-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md))

*   cannot be null

*   defined in: [EGA sample metadata schema v0.0.1](ega-2-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection_date")

### sample_collection_date Type

`string` ([Pattern of an EGA ISO date (YYYY-MM-DD)](ega-2-definitions-pattern-of-an-ega-iso-date-yyyy-mm-dd.md))

### sample_collection_date Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[0-9]{4}-(0[0-9]|1[0-2])-([012][0-9]|3[01])$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B4%7D-\(0%5B0-9%5D%7C1%5B0-2%5D\)-\(%5B012%5D%5B0-9%5D%7C3%5B01%5D\)%24 "try regular expression with regexr.com")

### sample_collection_date Examples

```json
"2021-04-30"
```

## sample_grouping

Node describing whether the sample object is: (1) a single physical sample (a single blood sample), collected individually through its corresponding protocol; or (2) corresponds to a set of samples that, after being individually collected, was grouped together (e.g. blood samples from different donors) physically or during the experimentation and analysis. One sample corresponds to one biological replicate \[EFO:0002091] (it could be the genetic content from a single cell, a tissue… from a single individual or from several individuals). Shall not be mistaken for technical replicates \[EFO:0002090] being used several times (see <https://www.ebi.ac.uk/seqdb/confluence/pages/viewpage.action?spaceKey=EGA&title=Sample+Representation>).

`sample_grouping`

*   is optional

*   Type: `object` ([Sample group descriptor](ega-4-properties-sample-group-descriptor.md))

*   cannot be null

*   defined in: [EGA sample metadata schema v0.0.1](ega-4-properties-sample-group-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping")

### sample_grouping Type

`object` ([Sample group descriptor](ega-4-properties-sample-group-descriptor.md))

one (and only one) of

*   [Either the sample_number is present and above 1](ega-4-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1.md "check type definition")

*   [Or the sample_group_boolean is 'false', hence an individual sample with sample_number being '1' or no sample_number](ega-4-properties-sample-group-descriptor-oneof-or-the-sample_group_boolean-is-false-hence-an-individual-sample-with-sample_number-being-1-or-no-sample_number.md "check type definition")

## sample_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. a viral sample from BioSamples being linked to a blood sample within the EGA) and within (e.g. a sample being linked to a sequencing run) the EGA.

`sample_relationships`

*   is optional

*   Type: `object[]` ([EGA Relationships object](ega-2-definitions-ega-relationships-object.md))

*   cannot be null

*   defined in: [EGA sample metadata schema v0.0.1](ega-4-properties-sample-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_relationships")

### sample_relationships Type

`object[]` ([EGA Relationships object](ega-2-definitions-ega-relationships-object.md))

### sample_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## sample_attributes

Custom attributes of a sample: reusable attributes to encode tag-value pairs (e.g. Tag being 'age' and its Value '30') with optional units (e.g. 'years'). Its properties are inherited from the common-definitions.json schema.

`sample_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA sample metadata schema v0.0.1](ega-4-properties-sample-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_attributes")

### sample_attributes Type

`object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

### sample_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
