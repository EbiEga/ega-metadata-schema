# EGA assay metadata schema Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to validate its assay metadata object. This object is intended to contain metadata about the raw qualitative or quantitative test performed to determine any kind of biological property of a biological sample. It can be of different types: (1) sequencing assay \[EFO:0003740] (e.g. sequence CRAM or FastQ files); and an (2) array assay \[EFO:0002696] (e.g. intensity CEL files). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                               |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.assay.json](../../../schemas/EGA.assay.json "open original schema") |

## EGA assay metadata schema Type

`object` ([EGA assay metadata schema](ega-11.md))

all of

*   [If the files are aligned reads, the reference alignment details are expected](ega-11-allof-if-the-files-are-aligned-reads-the-reference-alignment-details-are-expected.md "check type definition")

*   [Allowed filetypes for a sequencing assay](ega-11-allof-allowed-filetypes-for-a-sequencing-assay.md "check type definition")

*   [Allowed filetypes for an array assay](ega-11-allof-allowed-filetypes-for-an-array-assay.md "check type definition")

# EGA assay metadata schema Properties

| Property                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                   |
| :-------------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id)                                  | Merged   | Required | cannot be null | [EGA assay metadata schema](ega-11-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/object_id")                         |
| [schema\_descriptor](#schema_descriptor)                  | `object` | Optional | cannot be null | [EGA assay metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/schema_descriptor")                |
| [object\_title](#object_title)                            | `string` | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-title-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/object_title")                     |
| [object\_description](#object_description)                | `string` | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-description-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/object_description")         |
| [assay\_center](#assay_center)                            | `string` | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-centername-that-performed-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_center")    |
| [assay\_date](#assay_date)                                | `string` | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-pattern-of-ega-iso-8601-date.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_date")             |
| [assay\_type\_specifications](#assay_type_specifications) | Merged   | Required | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-type-specifications.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_type_specifications") |
| [assay\_relationships](#assay_relationships)              | `array`  | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_relationships")             |
| [assay\_files](#assay_files)                              | `array`  | Required | cannot be null | [EGA assay metadata schema](ega-11-properties-data-files-produced-from-an-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_files")       |
| [assay\_attributes](#assay_attributes)                    | `array`  | Optional | cannot be null | [EGA assay metadata schema](ega-11-properties-assay-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_attributes")            |

## object\_id

Node containing the main identifiers of the object (e.g. alias, center\_name...), inherited from the common definitions. #! We extend the core object (object\_core\_id) by adding a pattern check based on this schema's nature: an assay (by using EGA-assay-id-pattern)

`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-11-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/object_id")

### object\_id Type

`object` ([Object's IDs block](ega-11-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that assay's EGA ID (EGAR) is correct](ega-11-properties-objects-ids-block-allof-check-that-assays-ega-id-egar-is-correct.md "check type definition")

## schema\_descriptor

This node is intended to be used to describe the schemas and standards that a JSON document was based on. For instance, if a sample.json document was created to be validated against EGA.sample.json schema version 1.0.0, such information should be reflected in this block. This way, both a human and a machine can interpret and validate the JSON document efficiently, without the need of guessing versions.

`schema_descriptor`

*   is optional

*   Type: `object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-12-definitions-schema-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/schema_descriptor")

### schema\_descriptor Type

`object` ([Schema descriptor](ega-12-definitions-schema-descriptor.md))

## object\_title

An informative assay title that should serve as an overview of the assay and differentiate it from others. This short text can be used to call out assay records in searches or in displays.

`object_title`

*   is optional

*   Type: `string` ([Title of the assay](ega-11-properties-title-of-the-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-title-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/object_title")

### object\_title Type

`string` ([Title of the assay](ega-11-properties-title-of-the-assay.md))

### object\_title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### object\_title Examples

```json
"Ilumina sequencing assay 3409 - Cancer genomics"
```

## object\_description

An in-depth description (e.g. used technology, sample groups, purpose...) of the assay.

`object_description`

*   is optional

*   Type: `string` ([Description of the assay](ega-11-properties-description-of-the-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-description-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/object_description")

### object\_description Type

`string` ([Description of the assay](ega-11-properties-description-of-the-assay.md))

### object\_description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### object\_description Examples

```json
"Sequencing assay number 3409 of 4000. Sequenced through Illumina MiSeq to find SNPs of colorectal cancer samples..."
```

## assay\_center

The name of the center (e.g. 'EBI-TEST') responsible for performing assay, if applicable, in case it's different from the center submitting metadata).

`assay_center`

*   is optional

*   Type: `string` ([Centername that performed the assay](ega-11-properties-centername-that-performed-the-assay.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-centername-that-performed-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_center")

### assay\_center Type

`string` ([Centername that performed the assay](ega-11-properties-centername-that-performed-the-assay.md))

### assay\_center Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### assay\_center Examples

```json
"EBI-TEST"
```

## assay\_date

Regular expression to check the syntax of a date following 'ISO 8601 date' format. Notice that the Time (denoted by 'T...') is optional. So is the time zone, specified at the end of the string (e.g. 'Z', '+01:00'...). See more detail at '<https://regexpattern.com/iso-8601-dates-times/>'.

`assay_date`

*   is optional

*   Type: `string` ([Pattern of EGA ISO 8601 date](ega-11-properties-pattern-of-ega-iso-8601-date.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-pattern-of-ega-iso-8601-date.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_date")

### assay\_date Type

`string` ([Pattern of EGA ISO 8601 date](ega-11-properties-pattern-of-ega-iso-8601-date.md))

### assay\_date Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])(T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?)?$
```

[try pattern](https://regexr.com/?expression=%5E\(-%3F\(%3F%3A%5B1-9%5D%5B0-9%5D*\)%3F%5B0-9%5D%7B4%7D\)-\(1%5B0-2%5D%7C0%5B1-9%5D\)-\(3%5B01%5D%7C0%5B1-9%5D%7C%5B12%5D%5B0-9%5D\)\(T\(2%5B0-3%5D%7C%5B01%5D%5B0-9%5D\)%3A\(%5B0-5%5D%5B0-9%5D\)%3A\(%5B0-5%5D%5B0-9%5D\)\(%5C.%5B0-9%5D%2B\)%3F\(Z%7C%5B%2B-%5D\(%3F%3A2%5B0-3%5D%7C%5B01%5D%5B0-9%5D\)%3A%5B0-5%5D%5B0-9%5D\)%3F\)%3F%24 "try regular expression with regexr.com")

### assay\_date Examples

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

## assay\_type\_specifications

Node containing different sets of fields that depend on the specific assay type. The main categories of assay types follow a similar pattern as the used technology: either array assays (those in which an [array instrument \[EFO:0002698\]](http://www.ebi.ac.uk/efo/EFO_0002698) was used) or sequencing assays (those in which a [sequencing instrument \[EFO:0003739\]](http://www.ebi.ac.uk/efo/EFO_0003739) was used). Depending on the used technology, different types of fields will be required. For example, if an array was used, its sample\_array\_labels will be expected. Having this modular assay type-related node allows for easy additions of new technology-specific requirements.

`assay_type_specifications`

*   is required

*   Type: `object` ([Assay type specifications](ega-11-properties-assay-type-specifications.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-type-specifications.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_type_specifications")

### assay\_type\_specifications Type

`object` ([Assay type specifications](ega-11-properties-assay-type-specifications.md))

all of

*   [If the assay is of type array its specifications will be expected](ega-11-properties-assay-type-specifications-allof-if-the-assay-is-of-type-array-its-specifications-will-be-expected.md "check type definition")

## assay\_relationships

Comprises metadata (e.g. Source or Target) of a directional association between two entities, one of which shall be the current assay.

`assay_relationships`

*   is optional

*   Type: an array of merged types ([Details](ega-11-properties-assay-relationships-items.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-relationships.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_relationships")

### assay\_relationships Type

an array of merged types ([Details](ega-11-properties-assay-relationships-items.md))

### assay\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## assay\_files

This property contains the specific files (e.g. raw CRAM files) derived from performing the sequencing or hybridization and scanning with the sampled material.

`assay_files`

*   is required

*   Type: an array of merged types ([Details](ega-11-properties-data-files-produced-from-an-assay-items.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-data-files-produced-from-an-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_files")

### assay\_files Type

an array of merged types ([Details](ega-11-properties-data-files-produced-from-an-assay-items.md))

### assay\_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## assay\_attributes

Custom attributes of an assay: reusable attributes to encode tag-value pairs (e.g. Tag being 'additional context' and its Value 'this specific assay was stored mistakenly for longer periods of time, so its data could be misleading...') with optional units. Its properties are inherited from the common-definitions.json schema.

`assay_attributes`

*   is optional

*   Type: `object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

*   cannot be null

*   defined in: [EGA assay metadata schema](ega-11-properties-assay-custom-attributes.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.assay.json#/properties/assay_attributes")

### assay\_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

### assay\_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
