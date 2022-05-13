# EGA submission metadata schema Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/object_array/items/anyOf/4
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Submission (also known as submission project) metadata object. This object is intended to be an object that others can reference, grouping them by submission details. An EGA user can submit metadata comprising thousands of objects, or just a few that suffice the bare minimum of a comprehensive submission: at least one dataset, with its proper links to other objects. A submission JSON document hold little details, mainly the basic descriptive fields and collaborators array, but its main use is for other objects to reference it. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.object-set.json\*](../../../schemas/EGA.object-set.json "open original schema") |

## 4 Type

`object` ([EGA submission metadata schema](ega-15-properties-array-containing-metadata-objects-schemas-being-conditionally-applied-based-on-value-of-object_type-from-schema_descriptor-in-each-object-anyof-ega-submission-metadata-schema.md))

# 4 Properties

| Property                                               | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                         |
| :----------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id)                               | Merged   | Required | cannot be null | [EGA submission metadata schema](ega-19-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/object_id")                               |
| [schema\_descriptor](#schema_descriptor)               | `object` | Optional | cannot be null | [EGA submission metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/schema_descriptor")                      |
| [object\_title](#object_title)                         | `string` | Optional | cannot be null | [EGA submission metadata schema](ega-19-properties-title-of-the-submission-project.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/object_title")              |
| [object\_description](#object_description)             | `string` | Optional | cannot be null | [EGA submission metadata schema](ega-19-properties-description-of-the-submissions-project.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/object_description") |
| [additional\_collaborators](#additional_collaborators) | `array`  | Optional | cannot be null | [EGA submission metadata schema](ega-19-properties-submission-collaborator-details.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/additional_collaborators")  |
| [submission\_relationships](#submission_relationships) | `array`  | Optional | cannot be null | [EGA submission metadata schema](ega-19-properties-submission-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/submission_relationships")         |
| [submission\_attributes](#submission_attributes)       | `array`  | Optional | cannot be null | [EGA submission metadata schema](ega-19-properties-submission-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/submission_attributes")        |

## object\_id

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions. #! We extend the core object (object\_core\_id) by adding a pattern check based on this schema's nature: a submission (by using EGA-submission-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-19-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-19-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/object_id")

### object\_id Type

`object` ([Object's IDs block](ega-19-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that Submission EGA ID (EGAB) is correct](ega-19-properties-objects-ids-block-allof-check-that-submission-ega-id-egab-is-correct.md "check type definition")

## schema\_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-definitions-schema-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/schema_descriptor")

### schema\_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object\_title

Short free-form text that can be used to call out submission project records in searches or displays.

`object_title`

*   is optional

*   Type: `string` ([Title of the submission project](ega-19-properties-title-of-the-submission-project.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-19-properties-title-of-the-submission-project.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/object_title")

### object\_title Type

`string` ([Title of the submission project](ega-19-properties-title-of-the-submission-project.md))

### object\_title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### object\_title Examples

```json
"Submission XF40"
```

## object\_description

An in-depth description of the submission, including its overall purpose or nature of studies it governs.

`object_description`

*   is optional

*   Type: `string` ([Description of the submissions project](ega-19-properties-description-of-the-submissions-project.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-19-properties-description-of-the-submissions-project.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/object_description")

### object\_description Type

`string` ([Description of the submissions project](ega-19-properties-description-of-the-submissions-project.md))

### object\_description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### object\_description Examples

```json
"EBI submission project XF40 of 1000 samples and its 1500 sequencing runs"
```

## additional\_collaborators

Object containing optional collaborators of the submission project, who shall have different capabilities granted by the owner: 'read' or 'read and write' rights.

`additional_collaborators`

*   is optional

*   Type: `object[]` ([Collaborator](ega-19-properties-submission-collaborator-details-collaborator.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-19-properties-submission-collaborator-details.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/additional_collaborators")

### additional\_collaborators Type

`object[]` ([Collaborator](ega-19-properties-submission-collaborator-details-collaborator.md))

### additional\_collaborators Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## submission\_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a submission) the EGA.

`submission_relationships`

*   is optional

*   Type: an array of merged types ([Details](ega-19-properties-submission-relationships-items.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-19-properties-submission-relationships.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/submission_relationships")

### submission\_relationships Type

an array of merged types ([Details](ega-19-properties-submission-relationships-items.md))

### submission\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## submission\_attributes

Custom attributes of a submission: reusable attributes to encode tag-value pairs (e.g. Tag being 'internal identifier' and its Value 'XF40') with optional units. Its properties are inherited from the common-definitions.json schema.

`submission_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-19-properties-submission-custom-attributes.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/submission_attributes")

### submission\_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### submission\_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
