# EGA assay metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its assay metadata object. This object is intended to contain metadata about the raw qualitative or quantitative test performed to determine any kind of biological property of a biological sample. It can be of different types: (1) sequencing assay \[EFO:0003740] (e.g. sequence CRAM or FastQ files); and an (2) array assay \[EFO:0002696] (e.g. intensity CEL files). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.assay.json](../../../schemas/EGA.assay.json "open original schema") |

## EGA assay metadata schema Type

`object` ([EGA assay metadata schema](ega-3.md))

all of

*   [If the files are aligned reads, the reference alignment details are expected](ega-3-allof-if-the-files-are-aligned-reads-the-reference-alignment-details-are-expected.md "check type definition")

*   [Allowed filetypes for a sequencing assay](ega-3-allof-allowed-filetypes-for-a-sequencing-assay.md "check type definition")

*   [Allowed filetypes for an array assay](ega-3-allof-allowed-filetypes-for-an-array-assay.md "check type definition")

# EGA assay metadata schema Properties

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                |
| :-------------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)                               | Merged   | Required | cannot be null | [EGA assay metadata schema](ega-3-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/objectId")                        |
| [schemaDescriptor](#schemadescriptor)               | `object` | Optional | cannot be null | [EGA assay metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/schemaDescriptor")               |
| [objectTitle](#objecttitle)                         | `string` | Optional | cannot be null | [EGA assay metadata schema](ega-3-properties-title-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/objectTitle")                    |
| [objectDescription](#objectdescription)             | `string` | Optional | cannot be null | [EGA assay metadata schema](ega-3-properties-description-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/objectDescription")        |
| [assayCenter](#assaycenter)                         | `string` | Optional | cannot be null | [EGA assay metadata schema](ega-3-properties-centername-that-performed-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayCenter")   |
| [assayDate](#assaydate)                             | `string` | Optional | cannot be null | [EGA assay metadata schema](ega-3-properties-pattern-of-ega-iso-8601-date.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayDate")            |
| [assayTypeSpecifications](#assaytypespecifications) | Merged   | Required | cannot be null | [EGA assay metadata schema](ega-3-properties-assay-type-specifications.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications") |
| [assayRelationships](#assayrelationships)           | `array`  | Optional | cannot be null | [EGA assay metadata schema](ega-3-properties-assay-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayRelationships")            |
| [assayFiles](#assayfiles)                           | `array`  | Required | cannot be null | [EGA assay metadata schema](ega-3-properties-data-files-produced-from-an-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayFiles")      |
| [assayAttributes](#assayattributes)                 | `array`  | Optional | cannot be null | [EGA assay metadata schema](ega-3-properties-assay-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayAttributes")           |

## objectId

Node containing the main identifiers of the object (e.g. alias, centerName...), inherited from the common definitions. #! We extend the core object (objectCoreId) by adding a pattern check based on this schema's nature: an assay (by using EGAAssayIdPattern)

`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-3-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/objectId")

### objectId Type

`object` ([Object's IDs block](ega-3-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that assay's EGA ID (EGAR) is correct](ega-3-properties-objects-ids-block-allof-check-that-assays-ega-id-egar-is-correct.md "check type definition")

## schemaDescriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schemaDescriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-4-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/schemaDescriptor")

### schemaDescriptor Type

`object` ([Schema descriptor](ega-4-definitions-schema-descriptor.md))

## objectTitle

An informative assay title that should serve as an overview of the assay and differentiate it from others. This short text can be used to call out assay records in searches or in displays.

`objectTitle`

*   is optional

*   Type: `string` ([Title of the assay](ega-3-properties-title-of-the-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-title-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/objectTitle")

### objectTitle Type

`string` ([Title of the assay](ega-3-properties-title-of-the-assay.md))

### objectTitle Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### objectTitle Examples

```json
"Ilumina sequencing assay 3409 - Cancer genomics"
```

## objectDescription

An in-depth description (e.g. used technology, sample groups, purpose...) of the assay.

`objectDescription`

*   is optional

*   Type: `string` ([Description of the assay](ega-3-properties-description-of-the-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-description-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/objectDescription")

### objectDescription Type

`string` ([Description of the assay](ega-3-properties-description-of-the-assay.md))

### objectDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### objectDescription Examples

```json
"Sequencing assay number 3409 of 4000. Sequenced through Illumina MiSeq to find SNPs of colorectal cancer samples..."
```

## assayCenter

The name of the center (e.g. 'EBI-TEST') responsible for performing assay, if applicable, in case it's different from the center submitting metadata).

`assayCenter`

*   is optional

*   Type: `string` ([Centername that performed the assay](ega-3-properties-centername-that-performed-the-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-centername-that-performed-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayCenter")

### assayCenter Type

`string` ([Centername that performed the assay](ega-3-properties-centername-that-performed-the-assay.md))

### assayCenter Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### assayCenter Examples

```json
"EBI-TEST"
```

## assayDate

Regular expression to check the syntax of a date following 'ISO 8601 date' format. Notice that the Time (denoted by 'T...') is optional. So is the time zone, specified at the end of the string (e.g. 'Z', '+01:00'...). See more detail at '<https://regexpattern.com/iso-8601-dates-times/>'.

`assayDate`

*   is optional

*   Type: `string` ([Pattern of EGA ISO 8601 date](ega-3-properties-pattern-of-ega-iso-8601-date.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-pattern-of-ega-iso-8601-date.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayDate")

### assayDate Type

`string` ([Pattern of EGA ISO 8601 date](ega-3-properties-pattern-of-ega-iso-8601-date.md))

### assayDate Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])(T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?)?$
```

[try pattern](https://regexr.com/?expression=%5E\(-%3F\(%3F%3A%5B1-9%5D%5B0-9%5D*\)%3F%5B0-9%5D%7B4%7D\)-\(1%5B0-2%5D%7C0%5B1-9%5D\)-\(3%5B01%5D%7C0%5B1-9%5D%7C%5B12%5D%5B0-9%5D\)\(T\(2%5B0-3%5D%7C%5B01%5D%5B0-9%5D\)%3A\(%5B0-5%5D%5B0-9%5D\)%3A\(%5B0-5%5D%5B0-9%5D\)\(%5C.%5B0-9%5D%2B\)%3F\(Z%7C%5B%2B-%5D\(%3F%3A2%5B0-3%5D%7C%5B01%5D%5B0-9%5D\)%3A%5B0-5%5D%5B0-9%5D\)%3F\)%3F%24 "try regular expression with regexr.com")

### assayDate Examples

```json
"2021-04-30"
```

```json
"2020-12-29T19:30:45.123Z"
```

```json
"2020-12-29"
```

```json
"2020-12-29T19:30:45"
```

```json
"2021-10-13T04:13:00+01:00"
```

```json
"2021-10-13T12:13:00-08:00"
```

```json
"2021-10-13T12:13:00"
```

## assayTypeSpecifications

Node containing different sets of fields that depend on the instrument used for the assay: either array assays (those in which an [array instrument \[EFO:0002698\]](http://www.ebi.ac.uk/efo/EFO_0002698) was used) or sequencing assays (those in which a [sequencing instrument \[EFO:0003739\]](http://www.ebi.ac.uk/efo/EFO_0003739) was used). Depending on the used technology, different types of fields will be required. For example, if an array was used, its arraySampleLabels will be expected. Having this modular assay type-related node allows for easy additions of new technology-specific requirements.

`assayTypeSpecifications`

*   is required

*   Type: `object` ([Assay type specifications](ega-3-properties-assay-type-specifications.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-assay-type-specifications.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayTypeSpecifications")

### assayTypeSpecifications Type

`object` ([Assay type specifications](ega-3-properties-assay-type-specifications.md))

all of

*   [If the assay is of type array its specifications will be expected](ega-3-properties-assay-type-specifications-allof-if-the-assay-is-of-type-array-its-specifications-will-be-expected.md "check type definition")

## assayRelationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities, one of which shall be the current assay.

`assayRelationships`

*   is optional

*   Type: an array of merged types ([Details](ega-3-properties-assay-relationships-items.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-assay-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayRelationships")

### assayRelationships Type

an array of merged types ([Details](ega-3-properties-assay-relationships-items.md))

### assayRelationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## assayFiles

This property contains the specific files (e.g. raw CRAM files) derived from performing the sequencing or hybridization and scanning with the sampled material.

`assayFiles`

*   is required

*   Type: an array of merged types ([Details](ega-3-properties-data-files-produced-from-an-assay-items.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-data-files-produced-from-an-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayFiles")

### assayFiles Type

an array of merged types ([Details](ega-3-properties-data-files-produced-from-an-assay-items.md))

### assayFiles Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## assayAttributes

Custom attributes of an assay: reusable attributes to encode tag-value pairs (e.g. Tag being 'additional context' and its Value 'this specific assay was stored mistakenly for longer periods of time, so its data could be misleading...') with optional units. Its properties are inherited from the common-definitions.json schema.

`assayAttributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-3-properties-assay-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assayAttributes")

### assayAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

### assayAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
