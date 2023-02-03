# EGA study metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Study metadata object. This object is intended to contain metadata about the compilation of examinations, analyses or critical inspection of a particular subject. In other words, a Study is a container of experiments and analyses of any nature (including Array data) grouped by a common goal or investigation. They often draw together data from a range of datasets and are represented in publication. For instance, an example would be a case-control study on cancer patients and healthy individuals. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/studies>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.study.json](../../../schemas/EGA.study.json "open original schema") |

## EGA study metadata schema Type

`object` ([EGA study metadata schema](ega-11.md))

# EGA study metadata schema Properties

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                          |
| :---------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                     | Merged   | Required | cannot be null | [EGA study metadata schema](ega-11-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/objectId")                 |
| [schemaDescriptor](#schemadescriptor)     | `object` | Optional | cannot be null | [EGA study metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/schemaDescriptor")         |
| [objectTitle](#objecttitle)               | `string` | Required | cannot be null | [EGA study metadata schema](ega-11-properties-title-of-the-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/objectTitle")             |
| [objectDescription](#objectdescription)   | `string` | Optional | cannot be null | [EGA study metadata schema](ega-11-properties-description-of-the-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/objectDescription") |
| [studyTypes](#studytypes)                 | `array`  | Required | cannot be null | [EGA study metadata schema](ega-11-properties-studytypes-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyTypes")                |
| [studyDesigns](#studydesigns)             | `array`  | Required | cannot be null | [EGA study metadata schema](ega-11-properties-studydesigns-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyDesigns")            |
| [studyRelationships](#studyrelationships) | `array`  | Optional | cannot be null | [EGA study metadata schema](ega-11-properties-study-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyRelationships")     |
| [studyAttributes](#studyattributes)       | `array`  | Optional | cannot be null | [EGA study metadata schema](ega-11-properties-study-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyAttributes")    |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions. #! We extend the core object (objectCoreId) by adding a pattern check based on this schema's nature: a study (by using EGAStudyIdPattern)

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-11-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-11-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-11-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that study EGA ID (EGAS) is correct](ega-11-properties-objects-ids-block-allof-check-that-study-ega-id-egas-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

## objectTitle

Short free-form text that can be used to call out study records in searches or displays.

`objectTitle`

*   is required

*   Type: `string` ([Title of the study](ega-11-properties-title-of-the-study.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-11-properties-title-of-the-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the study](ega-11-properties-title-of-the-study.md))

### objectTitle Examples

```json
"EBI test case-control study for cancer"
```

## objectDescription

An in-depth description of the study, including its overall purpose, goals, scope or nature.

`objectDescription`

*   is optional

*   Type: `string` ([Description of the study](ega-11-properties-description-of-the-study.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-11-properties-description-of-the-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/objectDescription")

### objectDescription Type

`string` ([Description of the study](ega-11-properties-description-of-the-study.md))

### objectDescription Examples

```json
"EBI genome-wide case-control association study for Hypertension (HT) using seven disease collections together with the 1958 Spanish Birth Cohort and the EU National Blood Service collections as controls."
```

## studyTypes

List of study types. Contains specific keywords (e.g. 'COVID-19') as items that can be associated to the study, providing an overall view of its purpose.

`studyTypes`

*   is required

*   Type: `string[]` ([Study type](ega-11-properties-studytypes-array-study-type.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-11-properties-studytypes-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyTypes")

### studyTypes Type

`string[]` ([Study type](ega-11-properties-studytypes-array-study-type.md))

### studyTypes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## studyDesigns

List of study designs (a.k.a. experimental designs). Contains specific keywords (e.g. 'RNA stability design') as items that can be associated to the study, providing an overall view of the method of investigating particular types of research questions or solving particular types of problems.

`studyDesigns`

*   is required

*   Type: `string[]` ([Enumeration of design keywords](ega-4-definitions-enumeration-of-design-keywords.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-11-properties-studydesigns-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyDesigns")

### studyDesigns Type

`string[]` ([Enumeration of design keywords](ega-4-definitions-enumeration-of-design-keywords.md))

### studyDesigns Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## studyRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. an ArrayExperiment being linked to a study) the EGA.

`studyRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-11-properties-study-relationships-items.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-11-properties-study-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyRelationships")

### studyRelationships Type

an array of merged types ([Details](ega-11-properties-study-relationships-items.md))

### studyRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## studyAttributes

Custom attributes of a study: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`studyAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA study metadata schema](ega-11-properties-study-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.study.json#/properties/studyAttributes")

### studyAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

### studyAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
