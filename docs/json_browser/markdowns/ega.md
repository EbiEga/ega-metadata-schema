# EGA DAC metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Data Access Committee (DAC) metadata object. This object is intended to contain metadata about the body of one or more named individuals who are responsible for data release to external requestors based on consent and/or National Research Ethics terms. A DAC is typically formed, but not necessarily, from the same organization that collected the samples and generated any associated files/analyses. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/submission/data_access_committee>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.DAC.json](../../../schemas/EGA.DAC.json "open original schema") |

## EGA DAC metadata schema Type

`object` ([EGA DAC metadata schema](ega.md))

# EGA DAC metadata schema Properties

| Property                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                 |
| :-------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                   | Merged   | Required | cannot be null | [EGA DAC metadata schema](ega-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/objectId")               |
| [schemaDescriptor](#schemadescriptor)   | `object` | Optional | cannot be null | [EGA DAC metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/schemaDescriptor")    |
| [objectTitle](#objecttitle)             | `string` | Optional | cannot be null | [EGA DAC metadata schema](ega-properties-title-of-the-dac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/objectTitle")             |
| [objectDescription](#objectdescription) | `string` | Optional | cannot be null | [EGA DAC metadata schema](ega-properties-description-of-the-dac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/objectDescription") |
| [dacContacts](#daccontacts)             | `object` | Required | cannot be null | [EGA DAC metadata schema](ega-properties-dac-contacts-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts")         |
| [dacRelationships](#dacrelationships)   | `array`  | Optional | cannot be null | [EGA DAC metadata schema](ega-properties-dac-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacRelationships")       |
| [dacAttributes](#dacattributes)         | `array`  | Optional | cannot be null | [EGA DAC metadata schema](ega-properties-dac-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacAttributes")      |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions. #! We extend the core object (objectCoreId) by adding a pattern check based on this schema's nature: an DAC (by using EGADACIdPattern)

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that DAC EGA ID (EGAC) is correct](ega-properties-objects-ids-block-allof-check-that-dac-ega-id-egac-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

## objectTitle

Short free-form text that can be used to call out DAC records in searches or displays.

`objectTitle`

*   is optional

*   Type: `string` ([Title of the DAC](ega-properties-title-of-the-dac.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-properties-title-of-the-dac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the DAC](ega-properties-title-of-the-dac.md))

### objectTitle Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### objectTitle Examples

```json
"EBI Consortium Data Access Committee"
```

## objectDescription

An in-depth description of the DAC, including its overall purpose or nature of studies it governs.

`objectDescription`

*   is optional

*   Type: `string` ([Description of the DAC](ega-properties-description-of-the-dac.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-properties-description-of-the-dac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/objectDescription")

### objectDescription Type

`string` ([Description of the DAC](ega-properties-description-of-the-dac.md))

### objectDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### objectDescription Examples

```json
"EBI DAC governing data from projects related to human microbiome with data provenance..."
```

## dacContacts

Object containing the main contact's and optional additional contact's details.

`dacContacts`

*   is required

*   Type: `object` ([DAC contacts' details](ega-properties-dac-contacts-details.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-properties-dac-contacts-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts")

### dacContacts Type

`object` ([DAC contacts' details](ega-properties-dac-contacts-details.md))

## dacRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a DAC) the EGA.

`dacRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-properties-dac-relationships-items.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-properties-dac-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacRelationships")

### dacRelationships Type

an array of merged types ([Details](ega-properties-dac-relationships-items.md))

### dacRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## dacAttributes

Custom attributes of a DAC: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`dacAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-properties-dac-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacAttributes")

### dacAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

### dacAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
