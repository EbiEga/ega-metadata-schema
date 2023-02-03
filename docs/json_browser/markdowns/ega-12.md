# EGA submission metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Submission (also known as submission project) metadata object. This object is intended to be an object that others can reference, grouping them by submission details. An EGA user can submit metadata comprising thousands of objects, or just a few that suffice the bare minimum of a comprehensive submission: at least one dataset, with its proper links to other objects. A submission JSON document hold little details, mainly the basic descriptive fields and collaborators array, but its main use is for other objects to reference it. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.submission.json](../../../schemas/EGA.submission.json "open original schema") |

## EGA submission metadata schema Type

`object` ([EGA submission metadata schema](ega-12.md))

# EGA submission metadata schema Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                  |
| :-------------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                               | Merged   | Required | cannot be null | [EGA submission metadata schema](ega-12-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectId")                               |
| [schemaDescriptor](#schemadescriptor)               | `object` | Optional | cannot be null | [EGA submission metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/schemaDescriptor")                       |
| [objectTitle](#objecttitle)                         | `string` | Optional | cannot be null | [EGA submission metadata schema](ega-12-properties-title-of-the-submission-project.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectTitle")              |
| [objectDescription](#objectdescription)             | `string` | Optional | cannot be null | [EGA submission metadata schema](ega-12-properties-description-of-the-submissions-project.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectDescription") |
| [resources](#resources)                             | `array`  | Optional | cannot be null | [EGA submission metadata schema](ega-12-properties-resources-ontologies.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources")                           |
| [additionalCollaborators](#additionalcollaborators) | `array`  | Optional | cannot be null | [EGA submission metadata schema](ega-12-properties-submission-collaborator-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators")  |
| [submissionRelationships](#submissionrelationships) | `array`  | Optional | cannot be null | [EGA submission metadata schema](ega-12-properties-submission-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/submissionRelationships")         |
| [submissionAttributes](#submissionattributes)       | `array`  | Optional | cannot be null | [EGA submission metadata schema](ega-12-properties-submission-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/submissionAttributes")        |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions. #! We extend the core object (objectCoreId) by adding a pattern check based on this schema's nature: a submission (by using EGASubmissionIdPattern)

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-12-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-12-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that Submission EGA ID (EGAB) is correct](ega-12-properties-objects-ids-block-allof-check-that-submission-ega-id-egab-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

## objectTitle

Short free-form text that can be used to call out submission project records in searches or displays.

`objectTitle`

*   is optional

*   Type: `string` ([Title of the submission project](ega-12-properties-title-of-the-submission-project.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-title-of-the-submission-project.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the submission project](ega-12-properties-title-of-the-submission-project.md))

### objectTitle Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### objectTitle Examples

```json
"Submission XF40"
```

## objectDescription

An in-depth description of the submission, including its overall purpose or nature of studies it governs.

`objectDescription`

*   is optional

*   Type: `string` ([Description of the submissions project](ega-12-properties-description-of-the-submissions-project.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-description-of-the-submissions-project.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectDescription")

### objectDescription Type

`string` ([Description of the submissions project](ega-12-properties-description-of-the-submissions-project.md))

### objectDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### objectDescription Examples

```json
"EBI submission project XF40 of 1000 samples and its 1500 sequencing runs"
```

## resources

An array containing metadata of all the ontologies used in the submission. Its only purpose is to enhance traceability of the used ontologies in the future. For example, if an individual's phenotype is diabetes mellitus (which corresponds to curie EFO:0000400), one of the used ontologies would be EFO. Now, if in the future the term EFO:0000400 is changed in a new release of EFO, it's imperative to keep track of what version of EFO the submitter was referring to when it was referenced. Since most submitters would normally use the latest version of the ontologies at the time of the submission, these resources are intended to be automatically populated at every submission (and thus are not required) to ease the process; nonetheless, if provided, they should not be overwritten by that process. Bear in mind that there is only one 'resources' array per submission, and the items need to be unique, which means that different versions of the same ontologies will not be allowed.

`resources`

*   is optional

*   Type: `object[]` ([Resource](ega-12-properties-resources-ontologies-resource.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-resources-ontologies.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources")

### resources Type

`object[]` ([Resource](ega-12-properties-resources-ontologies-resource.md))

### resources Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## additionalCollaborators

Object containing optional collaborators of the submission project, who shall have different capabilities granted by the owner: 'read' or 'read and write' rights.

`additionalCollaborators`

*   is optional

*   Type: `object[]` ([Collaborator](ega-12-properties-submission-collaborator-details-collaborator.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-submission-collaborator-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/additionalCollaborators")

### additionalCollaborators Type

`object[]` ([Collaborator](ega-12-properties-submission-collaborator-details-collaborator.md))

### additionalCollaborators Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## submissionRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a submission) the EGA.

`submissionRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-12-properties-submission-relationships-items.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-submission-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/submissionRelationships")

### submissionRelationships Type

an array of merged types ([Details](ega-12-properties-submission-relationships-items.md))

### submissionRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## submissionAttributes

Custom attributes of a submission: reusable attributes to encode tag-value pairs (e.g. Tag being 'internal identifier' and its Value 'XF40') with optional units. Its properties are inherited from the common-definitions.json schema.

`submissionAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-submission-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/submissionAttributes")

### submissionAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

### submissionAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
