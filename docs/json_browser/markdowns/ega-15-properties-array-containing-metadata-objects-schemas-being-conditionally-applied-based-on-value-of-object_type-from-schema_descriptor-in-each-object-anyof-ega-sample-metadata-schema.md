# EGA sample metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_array/items/anyOf/2
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its sample metadata object. This object is intended to contain metadata about the physical sample used in the experiment. A sample is defined as a limited quantity of something (e.g. a portion of a substance or individual) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample shall not be confused with the individual (i.e. a person or donor) such sample derives from, for 'individual' is its own metadata object (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json>). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.object-set.json\*](../../../schemas/EGA.object-set.json "open original schema") |

## 2 Type

`object` ([EGA sample metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-sample-metadata-schema.md))

# 2 Properties

| Property                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                               |
| :-------------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id)                                  | Merged   | Required | cannot be null | [EGA sample metadata schema](ega-17-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_id")                                             |
| [schema\_descriptor](#schema_descriptor)                  | `object` | Optional | cannot be null | [EGA sample metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/schema_descriptor")                                    |
| [object\_title](#object_title)                            | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-title-of-the-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_title")                                        |
| [object\_description](#object_description)                | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-description-of-the-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_description")                            |
| [organism\_descriptor](#organism_descriptor)              | `object` | Required | cannot be null | [EGA sample metadata schema](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/organism_descriptor")               |
| [minimal\_public\_attributes](#minimal_public_attributes) | `object` | Required | cannot be null | [EGA sample metadata schema](ega-17-properties-minimal-public-attributes-describing-a-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/minimal_public_attributes") |
| [sample\_collection](#sample_collection)                  | Merged   | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-collection-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection")                          |
| [sample\_grouping](#sample_grouping)                      | Merged   | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-group-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping")                                 |
| [sample\_relationships](#sample_relationships)            | `array`  | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_relationships")                               |
| [sample\_attributes](#sample_attributes)                  | `array`  | Optional | cannot be null | [EGA sample metadata schema](ega-17-properties-sample-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_attributes")                              |

## object\_id

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions. #! We extend the core object (object\_core\_id) by adding a pattern check based on this schema's nature: a sample (by using EGA-sample-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-17-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_id")

### object\_id Type

`object` ([Object's IDs block](ega-17-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that sample EGA ID (EGAN) is correct](ega-17-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-is-correct.md "check type definition")

## schema\_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/schema_descriptor")

### schema\_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object\_title

An informative sample title that should serve as an overview (e.g. sample tag, pseudonyms, sample type, sample groups, purpose...) of the sample and differentiate it from others. This short text can be used to call out sample records in searches or in displays.

`object_title`

*   is optional

*   Type: `string` ([Title of the sample](ega-17-properties-title-of-the-sample.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-title-of-the-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_title")

### object\_title Type

`string` ([Title of the sample](ega-17-properties-title-of-the-sample.md))

### object\_title Examples

```json
"Buccal swab from COVID+ patient NM305004"
```

## object\_description

An informative sample description that describes the sample and differentiates it from others.

`object_description`

*   is optional

*   Type: `string` ([Description of the sample](ega-17-properties-description-of-the-sample.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-description-of-the-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/object_description")

### object\_description Type

`string` ([Description of the sample](ega-17-properties-description-of-the-sample.md))

### object\_description Examples

```json
"Buccal swab from COVID positive patient (NM305004) was taken on a sunny morning, had a lower volume than expected, then was sent to..."
```

## organism\_descriptor

This node describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance by default.

`organism_descriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/organism_descriptor")

### organism\_descriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

## minimal\_public\_attributes

Among all fields describing a sample, some may contain identifiable metadata and thus be private. Nevertheless, there are three basic attributes that every sample should contain (even if they are unknown): subject id (sample donor id), biological sex and phenotype. These shall be displayed and queryable.

`minimal_public_attributes`

*   is required

*   Type: `object` ([Minimal public attributes describing a sample](ega-17-properties-minimal-public-attributes-describing-a-sample.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-minimal-public-attributes-describing-a-sample.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/minimal_public_attributes")

### minimal\_public\_attributes Type

`object` ([Minimal public attributes describing a sample](ega-17-properties-minimal-public-attributes-describing-a-sample.md))

## sample\_collection

Node containing the provenance details (when and where) of the sample. This information does not include the whole sample collection protocol (expected at experiment's protocols), only the sampling date (when the sample was taken from the individual) and site (where was it taken within the individual).

`sample_collection`

*   is optional

*   Type: `object` ([Sample collection descriptor](ega-17-properties-sample-collection-descriptor.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-collection-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_collection")

### sample\_collection Type

`object` ([Sample collection descriptor](ega-17-properties-sample-collection-descriptor.md))

any of

*   [Either the collection date is required](ega-17-properties-sample-collection-descriptor-anyof-either-the-collection-date-is-required.md "check type definition")

*   [Or the collection site is required](ega-17-properties-sample-collection-descriptor-anyof-or-the-collection-site-is-required.md "check type definition")

## sample\_grouping

Node describing whether the sample object is: (1) a single physical sample (a single blood sample), collected individually through its corresponding protocol; or (2) corresponds to a set of samples that, after being individually collected, was grouped together (e.g. blood samples from different donors) physically or during the experimentation and analysis. One sample corresponds to one biological replicate \[EFO:0002091] (e.g. genetic content from a single cell, a tissue, buccal swab, etc.) from a single individual or from several individuals. Shall not be mistaken for technical replicates \[EFO:0002090] being used several times (see <https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/miscellaneous/sample_replicate.jpg>).

`sample_grouping`

*   is optional

*   Type: `object` ([Sample group descriptor](ega-17-properties-sample-group-descriptor.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-group-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_grouping")

### sample\_grouping Type

`object` ([Sample group descriptor](ega-17-properties-sample-group-descriptor.md))

one (and only one) of

*   [Either the sample_number is present and above 1](ega-17-properties-sample-group-descriptor-oneof-either-the-sample_number-is-present-and-above-1.md "check type definition")

*   [Or the sample_group_boolean is 'false', hence an individual sample with sample_number being '1' or no sample_number](ega-17-properties-sample-group-descriptor-oneof-or-the-sample_group_boolean-is-false-hence-an-individual-sample-with-sample_number-being-1-or-no-sample_number.md "check type definition")

## sample\_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. a viral sample from BioSamples being linked to a blood sample within the EGA) and within (e.g. a sample being linked to a sequencing run) the EGA.

`sample_relationships`

*   is optional

*   Type: an array of merged types ([Details](ega-17-properties-sample-relationships-items.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_relationships")

### sample\_relationships Type

an array of merged types ([Details](ega-17-properties-sample-relationships-items.md))

### sample\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## sample\_attributes

Custom attributes of a sample: reusable attributes to encode tag-value pairs (e.g. Tag being 'age' and its Value '30') with optional units (e.g. 'years'). Its properties are inherited from the common-definitions.json schema.

`sample_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-17-properties-sample-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_attributes")

### sample\_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### sample\_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
