# EGA sample metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its sample metadata object. This object is intended to contain metadata about the physical sample \[OBI:0000747] used in the experiment. A sample is defined as a limited quantity of something (e.g. a portion of a substance or individual) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. It is a material which is collected with the intention of being representative of a greater whole. A sample shall not be confused with the individual (i.e. a person or donor) such sample derives from, for 'individual' is its own metadata object (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json>). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json](../../../schemas/EGA.sample.json "open original schema") |

## EGA sample metadata schema Type

`object` ([EGA sample metadata schema](ega-10.md))

# EGA sample metadata schema Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                         |
| :------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                       | Merged   | Required | cannot be null | [EGA sample metadata schema](ega-10-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/objectId")                              |
| [schemaDescriptor](#schemadescriptor)       | `object` | Optional | cannot be null | [EGA sample metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/schemaDescriptor")                      |
| [objectTitle](#objecttitle)                 | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-title-of-the-sample.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/objectTitle")                         |
| [objectDescription](#objectdescription)     | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-description-of-the-sample.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/objectDescription")             |
| [organismDescriptor](#organismdescriptor)   | `object` | Required | cannot be null | [EGA sample metadata schema](ega-4-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/organismDescriptor") |
| [sampleCollection](#samplecollection)       | Merged   | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection")           |
| [sampleGrouping](#samplegrouping)           | Merged   | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-group-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping")                  |
| [sampleTypes](#sampletypes)                 | `array`  | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-array-of-sample-types.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleTypes")                       |
| [cellTypes](#celltypes)                     | `array`  | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-array-of-cell-types.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes")                           |
| [sampleStatus](#samplestatus)               | `array`  | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-array-of-sample-statuses.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus")                   |
| [sampleRelationships](#samplerelationships) | `array`  | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleRelationships")                |
| [sampleAttributes](#sampleattributes)       | `array`  | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-sample-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleAttributes")               |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions. #! We extend the core object (objectCoreId) by adding a pattern check based on this schema's nature: a sample (by using EGASampleIdPattern)

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-10-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-10-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that sample EGA ID (EGAN) is correct](ega-10-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

## objectTitle

An informative sample title that should serve as an overview (e.g. sample tag, pseudonyms, sample type, sample groups, purpose...) of the sample and differentiate it from others. This short text can be used to call out sample records in searches or in displays.

`objectTitle`

*   is optional

*   Type: `string` ([Title of the sample](ega-10-properties-title-of-the-sample.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-title-of-the-sample.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the sample](ega-10-properties-title-of-the-sample.md))

### objectTitle Examples

```json
"Buccal swab from COVID+ patient NM305004"
```

## objectDescription

An informative sample description that describes the sample and differentiates it from others.

`objectDescription`

*   is optional

*   Type: `string` ([Description of the sample](ega-10-properties-description-of-the-sample.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-description-of-the-sample.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/objectDescription")

### objectDescription Type

`string` ([Description of the sample](ega-10-properties-description-of-the-sample.md))

### objectDescription Examples

```json
"Buccal swab from COVID positive patient (NM305004) was taken on a sunny morning, had a lower volume than expected, then was sent to..."
```

## organismDescriptor

This property describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or, like humans, made up of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance.

`organismDescriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-4-definitions-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-4-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/organismDescriptor")

### organismDescriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-4-definitions-organism-obi0100026-descriptor-block.md))

## sampleCollection

Node containing the provenance details (when and where) of the sample. This information does not include the whole sample collection protocol (expected at experiment's protocols), only the sampling date (when the sample was taken from the individual) and site (where was it taken within the individual).

`sampleCollection`

*   is optional

*   Type: `object` ([Sample collection descriptor](ega-10-properties-sample-collection-descriptor.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-collection-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection")

### sampleCollection Type

`object` ([Sample collection descriptor](ega-10-properties-sample-collection-descriptor.md))

any of

*   [Either the collection date is required](ega-10-properties-sample-collection-descriptor-anyof-either-the-collection-date-is-required.md "check type definition")

*   [Or the age at collection is required](ega-10-properties-sample-collection-descriptor-anyof-or-the-age-at-collection-is-required.md "check type definition")

*   [Or the sampling site is required](ega-10-properties-sample-collection-descriptor-anyof-or-the-sampling-site-is-required.md "check type definition")

## sampleGrouping

Node describing whether the sample object is: (1) a single physical sample (a single blood sample), collected individually through its corresponding protocol; or (2) corresponds to a set of samples that, after being individually collected, was grouped together (e.g. blood samples from different donors) physically or during the experimentation and analysis. One sample corresponds to one biological replicate \[EFO:0002091] (e.g. genetic content from a single cell, a tissue, buccal swab, etc.) from a single individual or from several individuals. Shall not be mistaken for technical replicates \[EFO:0002090] being used several times (see <https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/miscellaneous/sample_replicate.jpg>).

`sampleGrouping`

*   is optional

*   Type: `object` ([Sample group descriptor](ega-10-properties-sample-group-descriptor.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-group-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleGrouping")

### sampleGrouping Type

`object` ([Sample group descriptor](ega-10-properties-sample-group-descriptor.md))

one (and only one) of

*   [Either the sampleNumber is present and above 1](ega-10-properties-sample-group-descriptor-oneof-either-the-samplenumber-is-present-and-above-1.md "check type definition")

*   [Or the sampleGroupBoolean is 'false', hence an individual sample with sampleNumber being '1' or no sampleNumber](ega-10-properties-sample-group-descriptor-oneof-or-the-samplegroupboolean-is-false-hence-an-individual-sample-with-samplenumber-being-1-or-no-samplenumber.md "check type definition")

## sampleTypes

Array of sample types: the material entity (e.g. DNA) that is this sample. Use this property as tags that befit your sample, picking as many as needed. Choose the specific terms if possible (e.g. if the assayed molecule is cDNA, add 'cDNA' instead of just 'DNA'). This property should not be confused with the sample collection protocols: regardless of the procedure to collect the sample, this property specifies what this sample is representing.

`sampleTypes`

*   is optional

*   Type: `string[]` ([Type of sample](ega-10-properties-array-of-sample-types-type-of-sample.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-array-of-sample-types.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleTypes")

### sampleTypes Type

`string[]` ([Type of sample](ega-10-properties-array-of-sample-types-type-of-sample.md))

### sampleTypes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## cellTypes

Array of cell types, in case the sample is composed of cells (e.g. cell culture) or the cells from which the genetic material derived are known (e.g. extract DNA from astrocytes). Use this property as tags that befit your sample, picking as many cell types as your sample contains or may contain.

`cellTypes`

*   is optional

*   Type: `object[]` ([Cell type](ega-10-properties-array-of-cell-types-cell-type.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-array-of-cell-types.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/cellTypes")

### cellTypes Type

`object[]` ([Cell type](ega-10-properties-array-of-cell-types-cell-type.md))

### cellTypes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## sampleStatus

Array of statuses of the sample. Used to specify the condition(s) under study **if** the diagnosis of the individual is not enough to describe the status of the sample. In other words, if the differenciation between affected and unaffected groups is done at the sample level and not at the individual level. This differentiation exists when the study design is of case-control \[[EFO:0001427](http://www.ebi.ac.uk/efo/EFO_0001427)].
For example, if two samples derive from an individual with 'renal cell carcinoma', one deriving from the affected tissue and the other from an unaffected tissue, this node can be used to specify whether the sample belongs to the unaffected group (i.e. control) or the affected one (i.e. case). On the other hand, if two samples derived from different probands each, one person being affected and the other unaffected by the condition under study, this node **is not** required.
Same could be applied, for instance, for treated or untreated samples, but not for treated or untreated individuals.

`sampleStatus`

*   is optional

*   Type: `object[]` ([Sample status item](ega-10-properties-array-of-sample-statuses-sample-status-item.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-array-of-sample-statuses.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus")

### sampleStatus Type

`object[]` ([Sample status item](ega-10-properties-array-of-sample-statuses-sample-status-item.md))

### sampleStatus Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## sampleRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. a viral sample from BioSamples being linked to a blood sample within the EGA) and within (e.g. a sample being linked to a sequencing run) the EGA.

`sampleRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-10-properties-sample-relationships-items.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleRelationships")

### sampleRelationships Type

an array of merged types ([Details](ega-10-properties-sample-relationships-items.md))

### sampleRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## sampleAttributes

Custom attributes of a sample: reusable attributes to encode tag-value pairs (e.g. Tag being 'age' and its Value '30') with optional units (e.g. 'years'). Its properties are inherited from the common-definitions.json schema.

`sampleAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-sample-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleAttributes")

### sampleAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

### sampleAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
