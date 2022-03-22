# EGA study metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Study metadata object. This object is intended to contain metadata about the compilation of examinations, analyses or critical inspection of a particular subject. In other words, a Study is a container of experiments and analyses of any nature (including Array data) grouped by a common goal or investigation. They often draw together data from a range of datasets and are represented in publication. For instance, an example would be a case-control study on cancer patients and healthy individuals. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/studies>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.study.json](../out/EGA.study.json "open original schema") |

## EGA study metadata schema Type

`object` ([EGA study metadata schema](ega-18.md))

# EGA study metadata schema Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                 |
| :------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object_id](#object_id)                     | Merged   | Required | cannot be null | [EGA study metadata schema](ega-18-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/object_id")                 |
| [schema_descriptor](#schema_descriptor)     | `object` | Optional | cannot be null | [EGA study metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/schema_descriptor")        |
| [object_title](#object_title)               | `string` | Required | cannot be null | [EGA study metadata schema](ega-18-properties-title-of-the-study.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/object_title")             |
| [object_description](#object_description)   | `string` | Optional | cannot be null | [EGA study metadata schema](ega-18-properties-description-of-the-study.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/object_description") |
| [study_types](#study_types)                 | `array`  | Optional | cannot be null | [EGA study metadata schema](ega-18-properties-study-types-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_types")               |
| [study_designs](#study_designs)             | `array`  | Required | cannot be null | [EGA study metadata schema](ega-18-properties-study-designs-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_designs")           |
| [study_relationships](#study_relationships) | `array`  | Optional | cannot be null | [EGA study metadata schema](ega-18-properties-study-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_relationships")     |
| [study_attributes](#study_attributes)       | `array`  | Optional | cannot be null | [EGA study metadata schema](ega-18-properties-study-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_attributes")    |

## object_id

Node containing the main identifiers of the object (e.g. alias, center_name...), inherited from the common definitions. #! We extend the core object (object_core_id) by adding a pattern check based on this schema's nature: a study (by using EGA-study-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-18-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-18-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/object_id")

### object_id Type

`object` ([Object's IDs block](ega-18-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that study EGA ID (EGAS) is correct](ega-18-properties-objects-ids-block-allof-check-that-study-ega-id-egas-is-correct.md "check type definition")

## schema_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/schema_descriptor")

### schema_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object_title

Short free-form text that can be used to call out study records in searches or displays.

`object_title`

*   is required

*   Type: `string` ([Title of the study](ega-18-properties-title-of-the-study.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-18-properties-title-of-the-study.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/object_title")

### object_title Type

`string` ([Title of the study](ega-18-properties-title-of-the-study.md))

### object_title Examples

```json
"EBI test case-control study for cancer"
```

## object_description

An in-depth description of the study, including its overall purpose, goals, scope or nature.

`object_description`

*   is optional

*   Type: `string` ([Description of the study](ega-18-properties-description-of-the-study.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-18-properties-description-of-the-study.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/object_description")

### object_description Type

`string` ([Description of the study](ega-18-properties-description-of-the-study.md))

### object_description Examples

```json
"EBI genome-wide case-control association study for Hypertension (HT) using seven disease collections together with the 1958 Spanish Birth Cohort and the EU National Blood Service collections as controls."
```

## study_types

List of study types. Contains specific keywords (e.g. 'COVID-19') as items that can be associated to the study, providing an overall view of its purpose.

`study_types`

*   is optional

*   Type: `string[]` ([Study type](ega-18-properties-study-types-array-study-type.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-18-properties-study-types-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_types")

### study_types Type

`string[]` ([Study type](ega-18-properties-study-types-array-study-type.md))

### study_types Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## study_designs

List of study designs (a.k.a. experimental designs). Contains specific keywords (e.g. 'RNA stability design') as items that can be associated to the study, providing an overall view of the method of investigating particular types of research questions or solving particular types of problems.

`study_designs`

*   is required

*   Type: `string[]` ([Enumeration of design keywords](ega-12-definitions-enumeration-of-design-keywords.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-18-properties-study-designs-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_designs")

### study_designs Type

`string[]` ([Enumeration of design keywords](ega-12-definitions-enumeration-of-design-keywords.md))

### study_designs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## study_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an ArrayExperiment being linked to a study) the EGA.

`study_relationships`

*   is optional

*   Type: `object[]` ([EGA Relationships object](ega-12-definitions-ega-relationships-object.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-18-properties-study-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_relationships")

### study_relationships Type

`object[]` ([EGA Relationships object](ega-12-definitions-ega-relationships-object.md))

### study_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## study_attributes

Custom attributes of a study: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`study_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-18-properties-study-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_attributes")

### study_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### study_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
