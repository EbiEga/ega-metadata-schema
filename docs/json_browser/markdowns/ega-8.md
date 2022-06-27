# EGA DAC metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its Data Access Committee (DAC) metadata object. This object is intended to contain metadata about the body of one or more named individuals who are responsible for data release to external requestors based on consent and/or National Research Ethics terms. A DAC is typically formed, but not necessarily, from the same organization that collected the samples and generated any associated files/analyses. Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/submission/data_access_committee>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.DAC.json](../../../schemas/EGA.DAC.json "open original schema") |

## EGA DAC metadata schema Type

`object` ([EGA DAC metadata schema](ega-8.md))

# EGA DAC metadata schema Properties

| Property                                   | Type     | Required | Nullable       | Defined by                                                                                                                                                                                    |
| :----------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id)                   | Merged   | Required | cannot be null | [EGA DAC metadata schema](ega-8-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/object_id")               |
| [schema\_descriptor](#schema_descriptor)   | `object` | Optional | cannot be null | [EGA DAC metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/schema_descriptor")     |
| [object\_title](#object_title)             | `string` | Optional | cannot be null | [EGA DAC metadata schema](ega-8-properties-title-of-the-dac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/object_title")             |
| [object\_description](#object_description) | `string` | Optional | cannot be null | [EGA DAC metadata schema](ega-8-properties-description-of-the-dac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/object_description") |
| [dac\_contacts](#dac_contacts)             | `object` | Required | cannot be null | [EGA DAC metadata schema](ega-8-properties-dac-contacts-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dac_contacts")         |
| [dac\_relationships](#dac_relationships)   | `array`  | Optional | cannot be null | [EGA DAC metadata schema](ega-8-properties-dac-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dac_relationships")       |
| [dac\_attributes](#dac_attributes)         | `array`  | Optional | cannot be null | [EGA DAC metadata schema](ega-8-properties-dac-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dac_attributes")      |

## object\_id

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions. #! We extend the core object (object\_core\_id) by adding a pattern check based on this schema's nature: an DAC (by using EGA-DAC-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-8-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-8-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/object_id")

### object\_id Type

`object` ([Object's IDs block](ega-8-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that DAC EGA ID (EGAC) is correct](ega-8-properties-objects-ids-block-allof-check-that-dac-ega-id-egac-is-correct.md "check type definition")

## schema\_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/schema_descriptor")

### schema\_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object\_title

Short free-form text that can be used to call out DAC records in searches or displays.

`object_title`

*   is optional

*   Type: `string` ([Title of the DAC](ega-8-properties-title-of-the-dac.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-8-properties-title-of-the-dac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/object_title")

### object\_title Type

`string` ([Title of the DAC](ega-8-properties-title-of-the-dac.md))

### object\_title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### object\_title Examples

```json
"EBI Consortium Data Access Committee"
```

## object\_description

An in-depth description of the DAC, including its overall purpose or nature of studies it governs.

`object_description`

*   is optional

*   Type: `string` ([Description of the DAC](ega-8-properties-description-of-the-dac.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-8-properties-description-of-the-dac.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/object_description")

### object\_description Type

`string` ([Description of the DAC](ega-8-properties-description-of-the-dac.md))

### object\_description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### object\_description Examples

```json
"EBI DAC governing data from projects related to human microbiome with data provenance..."
```

## dac\_contacts

Object containing the main contact's and optional additional contact's details.

`dac_contacts`

*   is required

*   Type: `object` ([DAC contacts' details](ega-8-properties-dac-contacts-details.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-8-properties-dac-contacts-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dac_contacts")

### dac\_contacts Type

`object` ([DAC contacts' details](ega-8-properties-dac-contacts-details.md))

## dac\_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a DAC) the EGA.

`dac_relationships`

*   is optional

*   Type: an array of merged types ([Details](ega-8-properties-dac-relationships-items.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-8-properties-dac-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dac_relationships")

### dac\_relationships Type

an array of merged types ([Details](ega-8-properties-dac-relationships-items.md))

### dac\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## dac\_attributes

Custom attributes of a DAC: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`dac_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-8-properties-dac-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dac_attributes")

### dac\_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### dac\_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
