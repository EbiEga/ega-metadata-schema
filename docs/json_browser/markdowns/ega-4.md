# EGA common metadata definitions Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to store common definitions for other metadata objects. Basically, we are defining here common properties (e.g. instances' aliases) that other metadata objects (e.g. sample) may use. The way we refer to them is by using this object's '$id' field, referencing it in other files (with '$ref' and the relative path of the property - e.g. '$ref': '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id>'). See structuring documentation (<https://json-schema.org/understanding-json-schema/structuring.html>). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract               | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                               |
| :--------------------- | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------- |
| Cannot be instantiated | Yes        | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json](../out/EGA.common-definitions.json "open original schema") |

## EGA common metadata definitions Type

`object` ([EGA common metadata definitions](ega-4.md))

# EGA common metadata definitions Definitions

## Definitions group object_core_id

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id"}
```

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                          |
| :------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [alias](#alias)                             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/alias")                      |
| [center_name](#center_name)                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/center_name")      |
| [ega_accession](#ega_accession)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/ega_accession")    |
| [external_accessions](#external_accessions) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions") |

### alias

Submitter designated name (e.g. 'my_sample_J13') for the object (e.g. Sample). The name must be unique within the submission account (e.g. 'ega-box-79'), since the aliases and submission accounts are concatenated within our database to obtain the unique alias (e.g. 'ega-box-79::my_sample_J13').

`alias`

*   is optional

*   Type: `string` ([Alias of an object](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/alias")

#### alias Type

`string` ([Alias of an object](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

#### alias Examples

```json
"my_sample_J13"
```

### center_name

Center name (e.g. 'EBI-TEST') associated to the submitter. In other words, it is the acronym of the submitter's account (provided by the HelpDesk team).

`center_name`

*   is optional

*   Type: `string` ([Center name of the submitter](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/center_name")

#### center_name Type

`string` ([Center name of the submitter](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

#### center_name Examples

```json
"EBI-TEST"
```

### ega_accession

The object accession (i.e. unique identifier) assigned by the archive (EGA). Object accessions can be found in the 'Identifiers' section of the EGA-archive website (<https://ega-archive.org/metadata/how-to-use-the-api>) and commonly start with EGA, followed by the distinctive letter of the object and finally the numeric ID of the instance.

`ega_accession`

*   is optional

*   Type: `string` ([EGA's accession of the object](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/ega_accession")

#### ega_accession Type

`string` ([EGA's accession of the object](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

#### ega_accession Examples

```json
"EGAN00003245489"
```

### external_accessions

Custom attributes of an ArrayExperiment: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

`external_accessions`

*   is optional

*   Type: `object[]` ([Object of external accession of the object](ega-4-definitions-object-of-external-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions")

#### external_accessions Type

`object[]` ([Object of external accession of the object](ega-4-definitions-object-of-external-accession-of-the-object.md))

#### external_accessions Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## Definitions group custom_attribute

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute"}
```

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                  |
| :-------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tag](#tag)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/tag")     |
| [value](#value) | Multiple | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/value") |
| [units](#units) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/units") |

### tag

The name of the attribute (e.g. 'Age').

`tag`

*   is required

*   Type: `string` ([Tag of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/tag")

#### tag Type

`string` ([Tag of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md))

#### tag Examples

```json
"age"
```

### value

The value of the attribute (e.g. '40').

`value`

*   is required

*   Type: any of the folllowing: `string` or `number` ([Value of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/value")

#### value Type

any of the folllowing: `string` or `number` ([Value of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md))

#### value Examples

```json
"40"
```

### units

The optional units of the attribute (e.g. 'years').

`units`

*   is optional

*   Type: `string` ([Units of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/units")

#### units Type

`string` ([Units of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md))

#### units Examples

```json
"years"
```

## Definitions group file_object

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object"}
```

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                            |
| :-------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [filename](#filename)                         | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-filename-data1050.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")                                       |
| [filetype](#filetype)                         | `object` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-filetype-ncitc172272.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")                                    |
| [checksum_method](#checksum_method)           | `object` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")                |
| [unencrypted_checksum](#unencrypted_checksum) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum") |
| [encrypted_checksum](#encrypted_checksum)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")     |

### filename

The full name of a file, including all of their file extensions (e.g. .gpg, .md5...), that identifies the file (e.g. 'my-bam-file.bam.gpg').

`filename`

*   is required

*   Type: `string` ([Filename \[data:1050\]](ega-4-definitions-ega-file-object-properties-filename-data1050.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-filename-data1050.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")

#### filename Type

`string` ([Filename \[data:1050\]](ega-4-definitions-ega-file-object-properties-filename-data1050.md))

#### filename Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[^<>:;,?"*|/]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22\*%7C%2F%5D%2B%24 "try regular expression with regexr.com")

#### filename Examples

```json
"my-bam-file.bam.gpg"
```

### filetype

The nature of the content stored in an electronic file. Contains up to two properties, the name (e.g. CEL or TSV) and the CURIE (e.g. EFO:0005630 or NCIT:C164049), chosen from a list of CVs.

`filetype`

*   is required

*   Type: `object` ([Filetype \[NCIT:C172272\]](ega-4-definitions-ega-file-object-properties-filetype-ncitc172272.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-filetype-ncitc172272.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")

#### filetype Type

`object` ([Filetype \[NCIT:C172272\]](ega-4-definitions-ega-file-object-properties-filetype-ncitc172272.md))

### checksum_method

Node containing both the ID (MD5 or SHA-256) and the CURIE (NCIT:C171276 or NCIT:C80226), describing the method which yields the checksum from a data input for the purpose of detecting errors.

`checksum_method`

*   is required

*   Type: `object` ([Checksum method \[ChecksumAlgorithm\]](ega-4-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")

#### checksum_method Type

`object` ([Checksum method \[ChecksumAlgorithm\]](ega-4-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md))

### unencrypted_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the unencrypted files.

`unencrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum")

#### unencrypted_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

#### unencrypted_checksum Examples

```json
"46798b5cfca45c46a84b7419f8b74735"
```

### encrypted_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the encrypted files.

`encrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")

#### encrypted_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

#### encrypted_checksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```

## Definitions group relationship_object

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object"}
```

| Property              | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                |
| :-------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [r_type](#r_type)     | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")     |
| [r_source](#r_source) | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source") |
| [r_target](#r_target) | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target") |

### r_type

The Type of the relationship, containing both its ID (e.g. same_as and the CURIE (e.g. NCIT:C64637), that summarises its purpose. #! The list of CV shall be agreed on, improved and enlarged.

`r_type`

*   is required

*   Type: `object` ([Type of the relationship](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")

#### r_type Type

`object` ([Type of the relationship](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship.md))

any of

*   [Check that r_type is present](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship-anyof-check-that-r_type-is-present.md "check type definition")

*   [Check that r_type_curie is present](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship-anyof-check-that-r_type_curie-is-present.md "check type definition")

### r_source

Object reference of the relationship’s source. In other words, the starting point of the relationship: in 'sample_A develops_from sample_B' the source is 'sample_A'.

`r_source`

*   is required

*   Type: `object` ([Source of the relationship](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source")

#### r_source Type

`object` ([Source of the relationship](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

        *   [External accession: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

        *   [Experiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

        *   [Study: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

        *   [Sample: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

        *   [Submission: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

        *   [Run: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-run-object_id-and-object_type-check.md "check type definition")

        *   [Dataset: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

        *   [Analysis: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

        *   [Policy: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

        *   [DAC: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

        *   [ArrayExperiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayexperiment-object_id-and-object_type-check.md "check type definition")

        *   [ArrayAssay: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayassay-object_id-and-object_type-check.md "check type definition")

        *   [Individual: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")

### r_target

Object reference of the relationship’s target. In other words, the ending point of the relationship: in 'sample_A develops_from sample_B' the target is 'sample_B'.

`r_target`

*   is required

*   Type: `object` ([Target of the relationship](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target")

#### r_target Type

`object` ([Target of the relationship](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

        *   [External accession: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

        *   [Experiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

        *   [Study: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

        *   [Sample: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

        *   [Submission: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

        *   [Run: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-run-object_id-and-object_type-check.md "check type definition")

        *   [Dataset: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

        *   [Analysis: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

        *   [Policy: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

        *   [DAC: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

        *   [ArrayExperiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayexperiment-object_id-and-object_type-check.md "check type definition")

        *   [ArrayAssay: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayassay-object_id-and-object_type-check.md "check type definition")

        *   [Individual: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")

## Definitions group protocols_object

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object"}
```

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                 |
| :-------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocol_name](#protocol_name)               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-ncitc42614.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")               |
| [protocol_type](#protocol_type)               | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-type-of-protocol-obi0000272-.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type")                  |
| [protocol_curie](#protocol_curie)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-type-ncitc21270.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_curie")         |
| [protocol_description](#protocol_description) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-description-of-the-protocol-ncitc25365.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description") |

### protocol_name

Name of the protocol (e.g. 'myProtocol-13'). To be defined by the user.

`protocol_name`

*   is optional

*   Type: `string` ([Name of the protocol \[NCIT:C42614\]](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-ncitc42614.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-ncitc42614.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")

#### protocol_name Type

`string` ([Name of the protocol \[NCIT:C42614\]](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-ncitc42614.md))

#### protocol_name Examples

```json
"myProtocol-13"
```

### protocol_type

Classification by type of the protocol (e.g. 'Sample collection'), to be chosen from a controlled vocabulary list (to be upgraded on demand).

`protocol_type`

*   is required

*   Type: `string` ([Type of protocol \[OBI:0000272\] ](ega-4-definitions-ega-protocols-object-properties-type-of-protocol-obi0000272-.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-type-of-protocol-obi0000272-.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type")

#### protocol_type Type

`string` ([Type of protocol \[OBI:0000272\] ](ega-4-definitions-ega-protocols-object-properties-type-of-protocol-obi0000272-.md))

#### protocol_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                     | Explanation |
| :---------------------------------------- | :---------- |
| `"Sample collection"`                     |             |
| `"Nucleic acid extraction"`               |             |
| `"Nucleic acid labeling"`                 |             |
| `"Nucleic acid hybridization to array"`   |             |
| `"Array scanning and feature extraction"` |             |
| `"Nucleic acid library construction"`     |             |
| `"Growth"`                                |             |
| `"Dissociation"`                          |             |
| `"Enrichment"`                            |             |
| `"Treatment"`                             |             |
| `"Conversion"`                            |             |
| `"Clinical treatment"`                    |             |
| `"Dissection"`                            |             |
| `"Gene expression"`                       |             |

#### protocol_type Examples

```json
"Sample collection"
```

### protocol_curie

Ontology term (e.g. 'EFO:0005518') of the Type of protocol.

`protocol_curie`

*   is optional

*   Type: `string` ([Name of the protocol type \[NCIT:C21270\]](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-type-ncitc21270.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-type-ncitc21270.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_curie")

#### protocol_curie Type

`string` ([Name of the protocol type \[NCIT:C21270\]](ega-4-definitions-ega-protocols-object-properties-name-of-the-protocol-type-ncitc21270.md))

#### protocol_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"EFO:0005518"` |             |
| `"EFO:0002944"` |             |
| `"EFO:0003813"` |             |
| `"EFO:0003815"` |             |
| `"EFO:0003814"` |             |
| `"EFO:0004184"` |             |
| `"EFO:0003789"` |             |
| `"EFO:0009088"` |             |
| `"EFO:0009089"` |             |
| `"EFO:0003969"` |             |
| `"EFO:0005520"` |             |
| `"EFO:0000355"` |             |
| `"EFO:0005519"` |             |
| `"EFO:0003788"` |             |

#### protocol_curie Examples

```json
"EFO:0005518"
```

### protocol_description

Description of the protocol (e.g. 'First tilt the cell culture flask... ...and finally let it still for 2 hours.'), being descriptive enough to be replicated by anyone who is granted access.

`protocol_description`

*   is required

*   Type: `string` ([Description of the protocol \[NCIT:C25365\]](ega-4-definitions-ega-protocols-object-properties-description-of-the-protocol-ncitc25365.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-protocols-object-properties-description-of-the-protocol-ncitc25365.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description")

#### protocol_description Type

`string` ([Description of the protocol \[NCIT:C25365\]](ega-4-definitions-ega-protocols-object-properties-description-of-the-protocol-ncitc25365.md))

#### protocol_description Examples

```json
"First tilt the cell culture flask... ...and finally let it still for 2 hours."
```

## Definitions group array_label

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label"}
```

| Property                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                    |
| :-------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [array_label_id](#array_label_id)       | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")       |
| [array_label_curie](#array_label_curie) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie") |

### array_label_id

Human readable ID/name (e.g. 'Cy3 dye' or 'Biotin') of the Array label used for the experiment.

`array_label_id`

*   is required

*   Type: `string` ([Array label of the ArrayExperiment - ID](ega-4-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")

#### array_label_id Type

`string` ([Array label of the ArrayExperiment - ID](ega-4-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---id.md))

#### array_label_id Examples

```json
"Cy3 dye"
```

### array_label_curie

CURIE (i.e. ontologized term - e.g. 'CHEBI:37987' or 'CHEBI:15956') of the Array label used for the experiment.

`array_label_curie`

*   is required

*   Type: `string` ([Array label of the ArrayExperiment - CURIE](ega-4-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie")

#### array_label_curie Type

`string` ([Array label of the ArrayExperiment - CURIE](ega-4-definitions-repeatable-array_label-node-properties-array-label-of-the-arrayexperiment---curie.md))

#### array_label_curie Examples

```json
"CHEBI:37987"
```

## Definitions group object-id-and-object-type-check

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group checksum-pattern-check

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group md5-checksum-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/md5-checksum-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group SHA-256-checksum-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/SHA-256-checksum-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-experiment-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-experiment-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-study-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-study-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-sample-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-sample-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-submission-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-submission-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-run-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-run-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-dataset-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-dataset-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-analysis-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-analysis-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-policy-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-policy-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-DAC-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-DAC-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-ArrayExperiment-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-ArrayExperiment-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-ArrayAssay-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-ArrayAssay-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-individual-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-individual-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-ISO-date-YYYY-MM-DD-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-ISO-date-YYYY-MM-DD-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group filename-filetype-pattern-check

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cel-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/cel-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group tsv-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/tsv-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group adf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/adf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fastq-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/fastq-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fasta-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/fasta-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sdrf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sdrf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group idf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/idf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group vcf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/vcf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sra-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sra-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group srf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/srf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sff-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sff-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bam-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/bam-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cram-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/cram-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group xlsx-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/xlsx-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group csv-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/csv-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bed-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/bed-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group idat-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/idat-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group map-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/map-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group ped-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ped-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bim-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/bim-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fam-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/fam-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group object_external_accession

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession"}
```

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                        |
| :---------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [external_accession](#external_accession) | Multiple | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-of-external-accession-of-the-object-properties-external-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession") |
| [accession_archive](#accession_archive)   | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-of-external-accession-of-the-object-properties-name-of-the-archive.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_archive")               |
| [accession_label](#accession_label)       | Multiple | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")     |

### external_accession

Unique identifier of the object (e.g. SAMEA7616999), assigned by other archives (e.g. biosample).

`external_accession`

*   is required

*   Type: any of the folllowing: `string` or `number` ([External accession of the object](ega-4-definitions-object-of-external-accession-of-the-object-properties-external-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-of-external-accession-of-the-object-properties-external-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession")

#### external_accession Type

any of the folllowing: `string` or `number` ([External accession of the object](ega-4-definitions-object-of-external-accession-of-the-object-properties-external-accession-of-the-object.md))

#### external_accession Examples

```json
"SAMEA7616999"
```

### accession_archive

Name of the archive (e.g. biosample) from which the external accession is taken.

`accession_archive`

*   is required

*   Type: `string` ([Name of the archive](ega-4-definitions-object-of-external-accession-of-the-object-properties-name-of-the-archive.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-of-external-accession-of-the-object-properties-name-of-the-archive.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_archive")

#### accession_archive Type

`string` ([Name of the archive](ega-4-definitions-object-of-external-accession-of-the-object-properties-name-of-the-archive.md))

#### accession_archive Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"ensembl"`         |             |
| `"ena"`             |             |
| `"pubmed"`          |             |
| `"protein"`         |             |
| `"nuccore"`         |             |
| `"ipg"`             |             |
| `"nucleotide"`      |             |
| `"structure"`       |             |
| `"genome"`          |             |
| `"annotinfo"`       |             |
| `"assembly"`        |             |
| `"bioproject"`      |             |
| `"biosample"`       |             |
| `"blastdbinfo"`     |             |
| `"books"`           |             |
| `"cdd"`             |             |
| `"clinvar"`         |             |
| `"gap"`             |             |
| `"gapplus"`         |             |
| `"grasp"`           |             |
| `"dbvar"`           |             |
| `"gene"`            |             |
| `"gds"`             |             |
| `"geoprofiles"`     |             |
| `"homologene"`      |             |
| `"medgen"`          |             |
| `"mesh"`            |             |
| `"ncbisearch"`      |             |
| `"nlmcatalog"`      |             |
| `"omim"`            |             |
| `"orgtrack"`        |             |
| `"pmc"`             |             |
| `"popset"`          |             |
| `"proteinclusters"` |             |
| `"pcassay"`         |             |
| `"protfam"`         |             |
| `"biosystems"`      |             |
| `"pccompound"`      |             |
| `"pcsubstance"`     |             |
| `"seqannot"`        |             |
| `"snp"`             |             |
| `"sra"`             |             |
| `"taxonomy"`        |             |
| `"biocollections"`  |             |
| `"gtr"`             |             |

#### accession_archive Examples

```json
"biosample"
```

### accession_label

Optional label (e.g. 'taken from biosample temporarily') of the external accession, used to add extra information to the identifier.

`accession_label`

*   is optional

*   Type: any of the folllowing: `string` or `number` ([Label of the external accession](ega-4-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")

#### accession_label Type

any of the folllowing: `string` or `number` ([Label of the external accession](ega-4-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

#### accession_label Examples

```json
"taken from biosample temporarily"
```

## Definitions group sample-label-association

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association"}
```

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [label](#label)         | `object` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-array_label-node.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/label")                                   |
| [object_id](#object_id) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id") |

### label

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node corresponds to the basic description of one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described. Its basic structure is a label ID and its optional CURIE.

`label`

*   is required

*   Type: `object` ([Repeatable array_label node](ega-4-definitions-repeatable-array_label-node.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-array_label-node.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/label")

#### label Type

`object` ([Repeatable array_label node](ega-4-definitions-repeatable-array_label-node.md))

### object_id



`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id")

#### object_id Type

`object` ([Object's IDs block](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that sample EGA ID (EGAN) pattern is correct](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-pattern-is-correct.md "check type definition")

## Definitions group one-relationship-end

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end"}
```

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                              |
| :-------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [object_id](#object_id-1)   | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")    |
| [object_type](#object_type) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type") |

### object_id

Node containing the main identifiers of the relationship's object (e.g. alias, center_name...), inherited from the common definitions (#/definitions/object_core_id).

`object_id`

*   is required

*   Type: `object` ([Relationship's object's IDs block](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")

#### object_id Type

`object` ([Relationship's object's IDs block](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

### object_type

Type of the relationship's object, chosen from a list of CV (e.g. arrayExperiment, dataset, external_URL...). Both the source or target types can be: (1) the object tag of one of EGA’s object (e.g. file, sample…); (2) an 'external_accession'; (3) or an 'external_URL'.

`object_type`

*   is required

*   Type: `string` ([Type of the relationship's object](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type")

#### object_type Type

`string` ([Type of the relationship's object](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

#### object_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation |
| :--------------------- | :---------- |
| `"experiment"`         |             |
| `"study"`              |             |
| `"sample"`             |             |
| `"individual"`         |             |
| `"submission"`         |             |
| `"run"`                |             |
| `"dataset"`            |             |
| `"analysis"`           |             |
| `"policy"`             |             |
| `"DAC"`                |             |
| `"ArrayExperiment"`    |             |
| `"ArrayAssay"`         |             |
| `"external_accession"` |             |
| `"external_URL"`       |             |

#### object_type Examples

```json
"sample"
```

## Definitions group subject_id

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/subject_id"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group biological_sex

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/biological_sex"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group experimental_condition_descriptor

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor"}
```

| Property                                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                         |
| :------------------------------------------------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [experimental_condition_term](#experimental_condition_term)               | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-term.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")               |
| [experimental_condition_curie](#experimental_condition_curie)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")             |
| [experimental_condition_description](#experimental_condition_description) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description") |

### experimental_condition_term

Human-readable term that specifies the experimental condition (e.g. 'fibroadenoma').

`experimental_condition_term`

*   is required

*   Type: `string` ([Experimental condition term](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-term.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")

#### experimental_condition_term Type

`string` ([Experimental condition term](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-term.md))

#### experimental_condition_term Examples

```json
"control"
```

```json
"fibroadenoma"
```

```json
"osteonecrosis"
```

### experimental_condition_curie

Curie (i.e. ontologised term - e.g. 'EFO:0001461') of the experimental condition.

`experimental_condition_curie`

*   is optional

*   Type: `string` ([Experimental condition curie](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")

#### experimental_condition_curie Type

`string` ([Experimental condition curie](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-curie.md))

#### experimental_condition_curie Examples

```json
"EFO:0001461"
```

```json
"EFO:1000254"
```

```json
"EFO:0004259"
```

### experimental_condition_description

Broad description of the experimental condition, providing further details and context over the ontologised term.

`experimental_condition_description`

*   is optional

*   Type: `string` ([Experimental condition description](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description")

#### experimental_condition_description Type

`string` ([Experimental condition description](ega-4-definitions-experimental-condition-xco0000000-properties-experimental-condition-description.md))

#### experimental_condition_description Examples

```json
"A control role is borne by a material in a process in which results obtained from an experimental sample and a control sample are compared."
```

```json
"A benign tumor of the breast characterized by the presence of stromal and epithelial elements."
```

```json
"A none disease characterized by death of bone tissue due to a lack of blood supply."
```

## Definitions group organism_descriptor

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor"}
```

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                  |
| :---------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [taxon_id](#taxon_id)               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier-apollo_sv00000203.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id")                               |
| [scientific_name](#scientific_name) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name-ncitc43459.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name") |
| [common_name](#common_name)         | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name-ncitc164690.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")        |

### taxon_id

Taxonomy Identifier (e.g. '9606' for humans) curated by the NCBI Taxonomy (search for your sample's here: <https://www.ncbi.nlm.nih.gov/taxonomy>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

`taxon_id`

*   is optional

*   Type: `string` ([Taxon identifier \[APOLLO_SV:00000203\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier-apollo_sv00000203.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier-apollo_sv00000203.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id")

#### taxon_id Type

`string` ([Taxon identifier \[APOLLO_SV:00000203\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier-apollo_sv00000203.md))

#### taxon_id Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[0-9]{1,7}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%7B1%2C7%7D%24 "try regular expression with regexr.com")

#### taxon_id Examples

```json
"9606"
```

### scientific_name

The name applied to a plant, animal, or other organism, according to the Codes of Nomenclature, consisting of a Genus and species (e.g. 'homo sapiens').

`scientific_name`

*   is optional

*   Type: `string` ([Biologic entity classification scientific name \[NCIT:C43459\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name-ncitc43459.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name-ncitc43459.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name")

#### scientific_name Type

`string` ([Biologic entity classification scientific name \[NCIT:C43459\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name-ncitc43459.md))

#### scientific_name Examples

```json
"homo sapiens"
```

### common_name

Common name (e.g. 'human') used to designate a plant, animal or other organism, as opposed to the scientific name.

`common_name`

*   is optional

*   Type: `string` ([Biologic entity classification common name \[NCIT:C164690\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name-ncitc164690.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name-ncitc164690.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")

#### common_name Type

`string` ([Biologic entity classification common name \[NCIT:C164690\]](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name-ncitc164690.md))

#### common_name Examples

```json
"human"
```

## Definitions group schema_descriptor

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor"}
```

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                  |
| :-------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [object_type](#object_type-1)                       | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_type")                                 |
| [described_by_schema_uri](#described_by_schema_uri) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/described_by_schema_uri")                      |
| [object_schema_version](#object_schema_version)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_schema_version")            |
| [common_schema_version](#common_schema_version)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/common_schema_version") |

### object_type

Type of the object (e.g. 'sample') the JSON document describes.

`object_type`

*   is required

*   Type: `string` ([Type of the object](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_type")

#### object_type Type

`string` ([Type of the object](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md))

#### object_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | :---------- |
| `"experiment"`      |             |
| `"study"`           |             |
| `"sample"`          |             |
| `"individual"`      |             |
| `"submission"`      |             |
| `"run"`             |             |
| `"dataset"`         |             |
| `"analysis"`        |             |
| `"policy"`          |             |
| `"DAC"`             |             |
| `"ArrayExperiment"` |             |
| `"ArrayAssay"`      |             |
| `"object-set"`      |             |

### described_by_schema_uri

URI of the schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json>') that describes the JSON document (e.g. 'my_sample.json')

`described_by_schema_uri`

*   is required

*   Type: `string` ([URI of the schema](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/described_by_schema_uri")

#### described_by_schema_uri Type

`string` ([URI of the schema](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md))

#### described_by_schema_uri Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^https://github\.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA\..+\.json$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3A%2F%2Fgithub%5C.com%2FEbiEga%2Fega-metadata-schema%2Ftree%2Fmain%2Fschemas%2FEGA%5C..%2B%5C.json%24 "try regular expression with regexr.com")

#### described_by_schema_uri Examples

```json
"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json"
```

### object_schema_version

The version of the object's schema, the one specific for the object the JSON document corresponds to (e.g. 'EGA.sample.json'), not the common definitions schema's version (i.e. 'EGA.common-definitions.json').

`object_schema_version`

*   is required

*   Type: `string` ([Version of the object's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_schema_version")

#### object_schema_version Type

`string` ([Version of the object's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

all of

*   [Semantic versioning pattern](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema-allof-semantic-versioning-pattern.md "check type definition")

### common_schema_version

The version of the common definition's schema, the one containing all shared definitions (i.e. 'EGA.common-definitions.json'), not the one specific to the object described by the JSON document (e.g. 'EGA.sample.json').

`common_schema_version`

*   is required

*   Type: `string` ([Version of the common definition's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/common_schema_version")

#### common_schema_version Type

`string` ([Version of the common definition's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

all of

*   [Semantic versioning pattern](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema-allof-semantic-versioning-pattern.md "check type definition")

## Definitions group semantic-versioning-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/semantic-versioning-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
