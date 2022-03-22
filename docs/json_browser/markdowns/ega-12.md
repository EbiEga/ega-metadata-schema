# EGA common metadata definitions Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to store common definitions for other metadata objects. Basically, we are defining here common properties (e.g. instances' aliases) that other metadata objects (e.g. sample) may use. The way we refer to them is by using this object's '$id' field, referencing it in other files (with '$ref' and the relative path of the property - e.g. '$ref': '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id>'). See structuring documentation (<https://json-schema.org/understanding-json-schema/structuring.html>). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract               | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                               |
| :--------------------- | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------- |
| Cannot be instantiated | Yes        | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json](../out/EGA.common-definitions.json "open original schema") |

## EGA common metadata definitions Type

`object` ([EGA common metadata definitions](ega-12.md))

# EGA common metadata definitions Definitions

## Definitions group object_core_id

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id"}
```

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                           |
| :------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [alias](#alias)                             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/alias")                      |
| [center_name](#center_name)                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/center_name")      |
| [ega_accession](#ega_accession)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/ega_accession")    |
| [external_accessions](#external_accessions) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions") |

### alias

Submitter designated name (e.g. 'my_sample_J13') for the object (e.g. Sample). The name must be unique within the submission account (e.g. 'ega-box-79'), since the aliases and submission accounts are concatenated within our database to obtain the unique alias (e.g. 'ega-box-79::my_sample_J13').

`alias`

*   is optional

*   Type: `string` ([Alias of an object](ega-12-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/alias")

#### alias Type

`string` ([Alias of an object](ega-12-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

#### alias Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### alias Examples

```json
"my_sample_J13"
```

### center_name

Center name (e.g. 'EBI-TEST') associated to the submitter. In other words, it is the acronym of the submitter's account (provided by the HelpDesk team).

`center_name`

*   is optional

*   Type: `string` ([Center name of the submitter](ega-12-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/center_name")

#### center_name Type

`string` ([Center name of the submitter](ega-12-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

#### center_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### center_name Examples

```json
"EBI-TEST"
```

### ega_accession

The object accession (i.e. unique identifier) assigned by the archive (EGA). Object accessions can be found in the 'Identifiers' section of the EGA-archive website (<https://ega-archive.org/metadata/how-to-use-the-api>) and commonly start with EGA, followed by the distinctive letter of the object and finally the numeric ID of the instance.

`ega_accession`

*   is optional

*   Type: `string` ([EGA's accession of the object](ega-12-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/ega_accession")

#### ega_accession Type

`string` ([EGA's accession of the object](ega-12-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

#### ega_accession Examples

```json
"EGAN00003245489"
```

### external_accessions

External accession node to reference objects in other archives (e.g. an already existing sample at BioSamples).

`external_accessions`

*   is optional

*   Type: `object[]` ([Object of external accession of the object](ega-12-definitions-object-of-external-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions")

#### external_accessions Type

`object[]` ([Object of external accession of the object](ega-12-definitions-object-of-external-accession-of-the-object.md))

#### external_accessions Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## Definitions group custom_attribute

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute"}
```

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                   |
| :-------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tag](#tag)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/tag")     |
| [value](#value) | Multiple | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/value") |
| [units](#units) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/units") |

### tag

The name of the attribute (e.g. 'Age').

`tag`

*   is required

*   Type: `string` ([Tag of the custom attribute](ega-12-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/tag")

#### tag Type

`string` ([Tag of the custom attribute](ega-12-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md))

#### tag Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### tag Examples

```json
"age"
```

### value

The value of the attribute (e.g. '40').

`value`

*   is required

*   Type: any of the folllowing: `string` or `number` ([Value of the custom attribute](ega-12-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/value")

#### value Type

any of the folllowing: `string` or `number` ([Value of the custom attribute](ega-12-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md))

#### value Examples

```json
"smoker"
```

```json
40
```

### units

The optional units of the attribute (e.g. 'years').

`units`

*   is optional

*   Type: `string` ([Units of the custom attribute](ega-12-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/units")

#### units Type

`string` ([Units of the custom attribute](ega-12-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md))

#### units Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### units Examples

```json
"years"
```

## Definitions group file_object

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object"}
```

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :-------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filename](#filename)                         | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filename.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")                                                |
| [filetype](#filetype)                         | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")                                                |
| [checksum_method](#checksum_method)           | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-method-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")                               |
| [unencrypted_checksum](#unencrypted_checksum) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum") |
| [encrypted_checksum](#encrypted_checksum)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")     |

### filename

The full name of a file, including all of their file extensions (e.g. .gpg, .md5...), that identifies the file (e.g. 'my-bam-file.bam.gpg').

`filename`

*   is required

*   Type: `string` ([Filename](ega-12-definitions-ega-file-object-properties-filename.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filename.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")

#### filename Type

`string` ([Filename](ega-12-definitions-ega-file-object-properties-filename.md))

#### filename Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[^<>:;,?"*|]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22\*%7C%5D%2B%24 "try regular expression with regexr.com")

#### filename Examples

```json
"my-bam-file.bam.gpg"
```

### filetype

The nature of the content stored in an electronic file. The string corresponds to the ID or name (e.g. FASTA or TSV), chosen from a list of controlled vocabulary (CV), associated with the given filetype. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`filetype`

*   is required

*   Type: `string` ([Filetype](ega-12-definitions-ega-file-object-properties-filetype.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")

#### filetype Type

`string` ([Filetype](ega-12-definitions-ega-file-object-properties-filetype.md))

#### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"CEL"`   |             |
| `"TSV"`   |             |
| `"ADF"`   |             |
| `"FASTQ"` |             |
| `"FASTA"` |             |
| `"SDRF"`  |             |
| `"IDF"`   |             |
| `"VCF"`   |             |
| `"SRA"`   |             |
| `"SRF"`   |             |
| `"SFF"`   |             |
| `"BAM"`   |             |
| `"CRAM"`  |             |
| `"XLSX"`  |             |
| `"CSV"`   |             |
| `"BED"`   |             |
| `"IDAT"`  |             |
| `"MAP"`   |             |
| `"PED"`   |             |
| `"BIM"`   |             |
| `"FAM"`   |             |
| `"TXT"`   |             |
| `"EXP"`   |             |
| `"GPR"`   |             |
| `"PY"`    |             |
| `"SH"`    |             |

### checksum_method

Node containing both the ID (MD5 or SHA-256), describing the method which yields the checksum from a data input for the purpose of detecting errors. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`checksum_method`

*   is required

*   Type: `string` ([Checksum method ID](ega-12-definitions-ega-file-object-properties-checksum-method-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-method-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")

#### checksum_method Type

`string` ([Checksum method ID](ega-12-definitions-ega-file-object-properties-checksum-method-id.md))

#### checksum_method Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"MD5"`     |             |
| `"SHA-256"` |             |

### unencrypted_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the unencrypted files.

`unencrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum")

#### unencrypted_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

#### unencrypted_checksum Examples

```json
"46798b5cfca45c46a84b7419f8b74735"
```

### encrypted_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the encrypted files.

`encrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")

#### encrypted_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

#### encrypted_checksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```

## Definitions group relationship_object

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object"}
```

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r_type](#r_type)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-relationship-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")            |
| [r_source](#r_source) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source") |
| [r_target](#r_target) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target") |

### r_type

ID (e.g. same_as) of the type of the relationship. To be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`r_type`

*   is required

*   Type: `string` ([Relationship type](ega-12-definitions-ega-relationships-object-properties-relationship-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-relationship-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")

#### r_type Type

`string` ([Relationship type](ega-12-definitions-ega-relationships-object-properties-relationship-type.md))

#### r_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                        | Explanation |
| :--------------------------- | :---------- |
| `"referenced_by"`            |             |
| `"develops_from"`            |             |
| `"same_as"`                  |             |
| `"member_of"`                |             |
| `"grouped_with"`             |             |
| `"family_relationship_with"` |             |
| `"child_of"`                 |             |
| `"parent_of"`                |             |
| `"is_after"`                 |             |
| `"published_in"`             |             |
| `"submitted_by"`             |             |
| `"contact_of"`               |             |
| `"main_contact_of"`          |             |

#### r_type Examples

```json
"referenced_by"
```

### r_source

Object reference of the relationship's source. In other words, the starting point of the relationship: in 'sample_A develops_from sample_B' the source is 'sample_A'.

`r_source`

*   is required

*   Type: `object` ([Source of the relationship](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source")

#### r_source Type

`object` ([Source of the relationship](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

        *   [External accession: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

        *   [Experiment: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

        *   [Study: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

        *   [Sample: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

        *   [Submission: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

        *   [Assay: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-assay-object_id-and-object_type-check.md "check type definition")

        *   [Dataset: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

        *   [Analysis: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

        *   [Policy: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

        *   [DAC: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

        *   [Individual: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")

### r_target

Object reference of the relationship's target. In other words, the ending point of the relationship: in 'sample_A develops_from sample_B' the target is 'sample_B'.

`r_target`

*   is required

*   Type: `object` ([Target of the relationship](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target")

#### r_target Type

`object` ([Target of the relationship](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

        *   [External accession: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

        *   [Experiment: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

        *   [Study: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

        *   [Sample: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

        *   [Submission: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

        *   [Assay: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-assay-object_id-and-object_type-check.md "check type definition")

        *   [Dataset: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

        *   [Analysis: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

        *   [Policy: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

        *   [DAC: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

        *   [Individual: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")

## Definitions group protocols_object

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object"}
```

| Property                                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                |
| :------------------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [protocol_name](#protocol_name)                               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")                        |
| [protocol_step_index](#protocol_step_index)                   | `number` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_step_index")                   |
| [previous_protocol_step_index](#previous_protocol_step_index) | `number` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/previous_protocol_step_index") |
| [protocol_type_descriptor](#protocol_type_descriptor)         | `object` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor")         |
| [protocol_performers](#protocol_performers)                   | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_performers")             |
| [protocol_instrument](#protocol_instrument)                   | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_instrument")             |
| [protocol_software](#protocol_software)                       | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-software-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_software")                 |
| [protocol_description](#protocol_description)                 | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description")          |

### protocol_name

Name of the protocol (e.g. 'myProtocol-13'). To be defined by the user.

`protocol_name`

*   is optional

*   Type: `string` ([Name of the protocol](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name")

#### protocol_name Type

`string` ([Name of the protocol](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md))

#### protocol_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### protocol_name Examples

```json
"myProtocol-13"
```

```json
"Treatment for leukemia patients C30"
```

```json
"Sample collection from infected patients"
```

### protocol_step_index

Lexically ordered value (greater than 0) that allows for the protocol section to be sequentially ordered. The float primitive data type is used to allow for pipe sections to be inserted later on. In other words, adding a new intermediate step 1.1 between steps 1 and 2 afterwards. For example, in an experiment where we treated samples before its DNA extraction, the sample treatment protocol would have a lower 'protocol_step_index' than the DNA extraction.

`protocol_step_index`

*   is required

*   Type: `number` ([Protocol step index](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_step_index")

#### protocol_step_index Type

`number` ([Protocol step index](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md))

#### protocol_step_index Examples

```json
0.5
```

```json
1
```

```json
2.5
```

```json
2
```

```json
30
```

### previous_protocol_step_index

The 'protocol_step_index' of the previous protocol, if hierarchically ordered. Set to '0' if this protocol is the first step. In case several protocols are not sequential, both can share the same 'previous_protocol_step_index'.

`previous_protocol_step_index`

*   is required

*   Type: `number` ([Previous protocol step index](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/previous_protocol_step_index")

#### previous_protocol_step_index Type

`number` ([Previous protocol step index](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md))

#### previous_protocol_step_index Examples

```json
0
```

```json
0.5
```

```json
1
```

```json
2.5
```

```json
2
```

```json
30
```

### protocol_type_descriptor

Node to contain the information about the type and subtype of the protocol. References to ontologies allow for a clear provenance and documentation of the protocol type, and hence we highly recommend their usage.

`protocol_type_descriptor`

*   is required

*   Type: `object` ([Protocol type descriptor](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_type_descriptor")

#### protocol_type_descriptor Type

`object` ([Protocol type descriptor](ega-12-definitions-ega-protocols-object-properties-protocol-type-descriptor.md))

### protocol_performers

Array of performers' descriptions of those individuals, groups, or institutions that executed the protocol.

`protocol_performers`

*   is optional

*   Type: `string[]` ([Performer of the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array-performer-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_performers")

#### protocol_performers Type

`string[]` ([Performer of the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-performers-array-performer-of-the-protocol.md))

#### protocol_performers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### protocol_instrument

Array of instruments used in the protocol.

`protocol_instrument`

*   is optional

*   Type: `string[]` ([Instrument used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array-instrument-used-in-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_instrument")

#### protocol_instrument Type

`string[]` ([Instrument used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array-instrument-used-in-the-protocol.md))

#### protocol_instrument Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### protocol_software

Array of software descriptions used in the protocol.

`protocol_software`

*   is optional

*   Type: `string[]` ([Software descriptions used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-protocol-software-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_software")

#### protocol_software Type

`string[]` ([Software descriptions used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

#### protocol_software Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### protocol_description

Description of the protocol (e.g. 'First tilt the cell culture flask... ...and finally let it still for 2 hours.'), being descriptive enough to be replicated between institutions or performers.

`protocol_description`

*   is required

*   Type: `string` ([Description of the protocol](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_description")

#### protocol_description Type

`string` ([Description of the protocol](ega-12-definitions-ega-protocols-object-properties-description-of-the-protocol.md))

#### protocol_description Examples

```json
"First tilt the cell culture flask... ...and finally let it still for 2 hours."
```

```json
"Patients were given a ketogenic diet for 3 weeks at intervals consisting in..."
```

## Definitions group array_label

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label"}
```

| Property                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                            |
| :-------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [array_label_id](#array_label_id)       | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")             |
| [array_label_curie](#array_label_curie) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie")       |
| [label_description](#label_description) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/label_description") |

### array_label_id

ID/name (e.g. 'Cy3 dye' or 'Biotin') of the Array label used for the experiment.

`array_label_id`

*   is required

*   Type: `string` ([Array label of the array experiment - ID](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")

#### array_label_id Type

`string` ([Array label of the array experiment - ID](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md))

#### array_label_id Examples

```json
"Cy3 dye"
```

### array_label_curie

CURIE (i.e. ontologized term - e.g. 'CHEBI:37987' or 'CHEBI:15956') of the Array label used for the experiment. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index).

`array_label_curie`

*   is optional

*   Type: `string` ([Array label of the array experiment - CURIE](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie")

#### array_label_curie Type

`string` ([Array label of the array experiment - CURIE](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie-allof-compact-uri-curie-pattern.md "check type definition")

#### array_label_curie Examples

```json
"CHEBI:37987"
```

### label_description

Additional description of the used label, indicating further details: context, purpose of the label, description of the label in the absence of an ontologized term, etc.

`label_description`

*   is optional

*   Type: `string` ([Array label of the array experiment - Description](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/label_description")

#### label_description Type

`string` ([Array label of the array experiment - Description](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md))

#### label_description Examples

```json
"This label was use to dye the control samples"
```

```json
"This newly discovered label (yet to be added to an ontology) consists in a compound of type X..."
```

```json
"The label ID is unknown because we were given the RNA already dyed..."
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

## Definitions group EGA-assay-id-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/EGA-assay-id-pattern"}
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

## Definitions group txt-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/txt-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group exp-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/exp-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group gpr-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/gpr-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group py-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/py-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sh-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sh-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group object_external_accession

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession"}
```

| Property                                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                              |
| :---------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [external_accession_curie](#external_accession_curie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession_curie") |
| [accession_label](#accession_label)                   | Multiple | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")          |

### external_accession_curie

Unique identifier of an external, to EGA, object. It shall follow CURIE format (`prefix`:`accession`): prefix assigned to the archive (e.g. biosample - search for yours at identifiers.org) and the unique accession of the object (e.g. SAMEA7616999).

`external_accession_curie`

*   is required

*   Type: `string` ([CURIE of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession_curie")

#### external_accession_curie Type

`string` ([CURIE of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession-allof-compact-uri-curie-pattern.md "check type definition")

#### external_accession_curie Examples

```json
"biosample:SAMEA7616999"
```

```json
"arrayexpress:E-MEXP-1712"
```

### accession_label

Optional label (e.g. 'taken from biosample temporarily') of the external accession, used to add extra information to the identifier.

`accession_label`

*   is optional

*   Type: any of the folllowing: `string` or `number` ([Label of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")

#### accession_label Type

any of the folllowing: `string` or `number` ([Label of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

#### accession_label Examples

```json
"taken from biosample temporarily"
```

```json
"Ensembl's part of the accessions"
```

```json
"first"
```

```json
2
```

## Definitions group sample-label-association

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association"}
```

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                  |
| :---------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [label](#label)         | `object` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/label")                                   |
| [object_id](#object_id) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id") |

### label

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node corresponds to the basic description of one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described. Its basic structure is a label ID and its optional CURIE.

`label`

*   is required

*   Type: `object` ([Repeatable array_label node](ega-12-definitions-repeatable-array_label-node.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/label")

#### label Type

`object` ([Repeatable array_label node](ega-12-definitions-repeatable-array_label-node.md))

### object_id



`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id")

#### object_id Type

`object` ([Object's IDs block](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that sample EGA ID (EGAN) pattern is correct](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-pattern-is-correct.md "check type definition")

## Definitions group one-relationship-end

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end"}
```

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                               |
| :-------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object_id](#object_id-1)   | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")    |
| [object_type](#object_type) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type") |

### object_id

Node containing the main identifiers of the relationship's object (e.g. alias, center_name...), inherited from the common definitions (#/definitions/object_core_id).

`object_id`

*   is required

*   Type: `object` ([Relationship's object's IDs block](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")

#### object_id Type

`object` ([Relationship's object's IDs block](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

### object_type

Type of the relationship's object, chosen from a list of CV (e.g. experiment, dataset, external_URL...). Both the source or target types can be: (1) the object tag of one of EGA's object (e.g. file, sample…); (2) an 'external_accession'; (3) or an 'external_URL'. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`object_type`

*   is required

*   Type: `string` ([Type of the relationship's object](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type")

#### object_type Type

`string` ([Type of the relationship's object](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

#### object_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation |
| :--------------------- | :---------- |
| `"experiment"`         |             |
| `"study"`              |             |
| `"sample"`             |             |
| `"individual"`         |             |
| `"submission"`         |             |
| `"assay"`              |             |
| `"dataset"`            |             |
| `"analysis"`           |             |
| `"policy"`             |             |
| `"DAC"`                |             |
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

| Property                                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                               |
| :------------------------------------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [experimental_condition_term](#experimental_condition_term)               | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")               |
| [experimental_condition_curie](#experimental_condition_curie)             | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")             |
| [experimental_condition_description](#experimental_condition_description) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description") |

### experimental_condition_term

Term that specifies the experimental condition (e.g. 'fibroadenoma').

`experimental_condition_term`

*   is required

*   Type: `string` ([Experimental condition term](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")

#### experimental_condition_term Type

`string` ([Experimental condition term](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md))

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

Curie (i.e. ontologised term - e.g. 'EFO:0001461') of the experimental condition. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index).

`experimental_condition_curie`

*   is optional

*   Type: `string` ([Experimental condition curie](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")

#### experimental_condition_curie Type

`string` ([Experimental condition curie](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-experimental-condition-properties-experimental-condition-curie-allof-compact-uri-curie-pattern.md "check type definition")

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

*   Type: `string` ([Experimental condition description](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description")

#### experimental_condition_description Type

`string` ([Experimental condition description](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md))

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

| Property                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                        |
| :---------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [taxon_id](#taxon_id)               | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id")                                      |
| [scientific_name](#scientific_name) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name") |
| [common_name](#common_name)         | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")         |

### taxon_id

Taxonomy Identifier (e.g. '9606' for humans) curated by the NCBI Taxonomy (search for your sample's here: <https://www.ncbi.nlm.nih.gov/taxonomy>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

`taxon_id`

*   is required

*   Type: `string` ([Taxon identifier](ega-12-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id")

#### taxon_id Type

`string` ([Taxon identifier](ega-12-definitions-organism-obi0100026-descriptor-block-properties-taxon-identifier.md))

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

*   Type: `string` ([Biologic entity classification scientific name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name")

#### scientific_name Type

`string` ([Biologic entity classification scientific name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md))

#### scientific_name Examples

```json
"homo sapiens"
```

### common_name

Common name (e.g. 'human') used to designate a plant, animal or other organism, as opposed to the scientific name.

`common_name`

*   is optional

*   Type: `string` ([Biologic entity classification common name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")

#### common_name Type

`string` ([Biologic entity classification common name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

#### common_name Examples

```json
"human"
```

## Definitions group schema_descriptor

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor"}
```

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                   |
| :-------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object_type](#object_type-1)                       | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-type-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_type")                                 |
| [described_by_schema_uri](#described_by_schema_uri) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/described_by_schema_uri")                      |
| [object_schema_version](#object_schema_version)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_schema_version")            |
| [common_schema_version](#common_schema_version)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/common_schema_version") |

### object_type

Type of the object (e.g. 'sample') the JSON document describes.

`object_type`

*   is required

*   Type: `string` ([Type of the object](ega-12-definitions-schema-descriptor-properties-type-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-type-of-the-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_type")

#### object_type Type

`string` ([Type of the object](ega-12-definitions-schema-descriptor-properties-type-of-the-object.md))

#### object_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"experiment"` |             |
| `"study"`      |             |
| `"sample"`     |             |
| `"individual"` |             |
| `"submission"` |             |
| `"assay"`      |             |
| `"dataset"`    |             |
| `"analysis"`   |             |
| `"policy"`     |             |
| `"DAC"`        |             |
| `"object-set"` |             |

### described_by_schema_uri

URI of the schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json>') that describes the JSON document (e.g. 'my_sample.json')

`described_by_schema_uri`

*   is required

*   Type: `string` ([URI of the schema](ega-12-definitions-schema-descriptor-properties-uri-of-the-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/described_by_schema_uri")

#### described_by_schema_uri Type

`string` ([URI of the schema](ega-12-definitions-schema-descriptor-properties-uri-of-the-schema.md))

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

*   Type: `string` ([Version of the object's schema](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_schema_version")

#### object_schema_version Type

`string` ([Version of the object's schema](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

all of

*   [Semantic versioning pattern](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema-allof-semantic-versioning-pattern.md "check type definition")

### common_schema_version

The version of the common definition's schema, the one containing all shared definitions (i.e. 'EGA.common-definitions.json'), not the one specific to the object described by the JSON document (e.g. 'EGA.sample.json').

`common_schema_version`

*   is required

*   Type: `string` ([Version of the common definition's schema](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/common_schema_version")

#### common_schema_version Type

`string` ([Version of the common definition's schema](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

all of

*   [Semantic versioning pattern](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema-allof-semantic-versioning-pattern.md "check type definition")

## Definitions group semantic-versioning-pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/semantic-versioning-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group contact_details

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details"}
```

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                |
| :-------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [individual_full_name](#individual_full_name) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/individual_full_name") |
| [institution_name](#institution_name)         | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-institution-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/institution_name")               |
| [email_address](#email_address)               | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-email-address.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/email_address")                     |
| [phone_number](#phone_number)                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-phone-number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/phone_number")                       |

### individual_full_name

A full set of all personal names by which an individual is known and that can be recited as a word-group, with the understanding that, taken together, they all relate to that one individual. In case there are several, separate them with semicolons (;).

`individual_full_name`

*   is optional

*   Type: `string` ([Full name of an individual](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/individual_full_name")

#### individual_full_name Type

`string` ([Full name of an individual](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md))

#### individual_full_name Examples

```json
"Wayne Jr., Bruce"
```

### institution_name

The full name of an institution the contact belongs to. In case there are several, separate them with semicolons (;).

`institution_name`

*   is optional

*   Type: `string` ([Institution name](ega-12-definitions-contact-details-properties-institution-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-institution-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/institution_name")

#### institution_name Type

`string` ([Institution name](ega-12-definitions-contact-details-properties-institution-name.md))

#### institution_name Examples

```json
"European Genome-phenome Archive (EGA)"
```

### email_address

Current email address that would be used in case the contact needs to be reached. Its expected format is of a local-part (e.g. 'myname'), followed by an 'at' sign (i.e. '@') and the domain of the address (e.g. 'gmail.com' or 'ebi.ac.uk').

`email_address`

*   is required

*   Type: `string` ([Email address](ega-12-definitions-contact-details-properties-email-address.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-email-address.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/email_address")

#### email_address Type

`string` ([Email address](ega-12-definitions-contact-details-properties-email-address.md))

#### email_address Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Ba-zA-Z0-9\_%5C-%5C.%5D%2B\)%40\(%5Ba-zA-Z0-9\_%5C-%5C.%5D%2B\)%5C.\(%5Ba-zA-Z%5D%7B2%2C5%7D\)%24 "try regular expression with regexr.com")

#### email_address Examples

```json
"myname@ebi.ac.uk"
```

### phone_number

Current phone number that would be used in case the contact needs to be reached. Theoretically would only be used in case the email address was not provided, does not exist or is unresponsive.

`phone_number`

*   is optional

*   Type: `string` ([Phone number](ega-12-definitions-contact-details-properties-phone-number.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-phone-number.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/phone_number")

#### phone_number Type

`string` ([Phone number](ega-12-definitions-contact-details-properties-phone-number.md))

#### phone_number Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^\+?\(?[0-9]{1,4}\)?[-\s\./0-9]+$
```

[try pattern](https://regexr.com/?expression=%5E%5C%2B%3F%5C\(%3F%5B0-9%5D%7B1%2C4%7D%5C\)%3F%5B-%5Cs%5C.%2F0-9%5D%2B%24 "try regular expression with regexr.com")

#### phone_number Examples

```json
"+44 7427512529"
```

## Definitions group study-design-keywords

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/study-design-keywords"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group locus_identifier

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier"}
```

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                     |
| :------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [organism_descriptor](#organism_descriptor) | `object` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/organism_descriptor")       |
| [loci_descriptor](#loci_descriptor)         | `array`  | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-locus-identifier-properties-loci-context-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor") |

### organism_descriptor

This node describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance by default.

`organism_descriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/organism_descriptor")

#### organism_descriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

### loci_descriptor

Array of locus context items. Multiple loci can be described in the array if the organism remains the same.

`loci_descriptor`

*   is required

*   Type: `object[]` ([Locus context item](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-locus-identifier-properties-loci-context-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor")

#### loci_descriptor Type

`object[]` ([Locus context item](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

#### loci_descriptor Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## Definitions group gene_descriptor

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor"}
```

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                            |
| :------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [gene_symbol](#gene_symbol)     | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-symbol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_symbol")     |
| [gene_id_curie](#gene_id_curie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_id_curie") |

### gene_symbol

The official gene symbol. It is typically derived from the gene name. This optional field exists to provide the common identifier of the gene. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: (1) in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature; (2) while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

`gene_symbol`

*   is optional

*   Type: `string` ([Gene Symbol](ega-12-definitions-gene-descriptor-properties-gene-symbol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-symbol.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_symbol")

#### gene_symbol Type

`string` ([Gene Symbol](ega-12-definitions-gene-descriptor-properties-gene-symbol.md))

#### gene_symbol Examples

```json
"TAF1"
```

```json
"TP53"
```

```json
"BRAF"
```

```json
"16S"
```

### gene_id_curie

A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol (e.g. HGNC:11535 for gene TAF1). The identifier has to follow CURIE format. Additionally, there are 2 types of allowed databases to reference: NCBIGene and HGNC. Other archives' accessions (e.g. ensembl:ENSDARG00000035330) can be cross referenced with NCBIGene to obtain its gene ID (e.g. ncbigene:555452).

`gene_id_curie`

*   is required

*   Type: `string` ([Gene CURIE ID](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_id_curie")

#### gene_id_curie Type

`string` ([Gene CURIE ID](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md))

one (and only one) of

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-ncbi-gene-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-hgnc-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

#### gene_id_curie Examples

```json
"HGNC:11535"
```

```json
"hgnc:11998"
```

```json
"HGNC:1097"
```

```json
"ncbigene:100010"
```

```json
"ncbigene:6872"
```

## Definitions group ncbi_assembly_descriptor

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor"}
```

| Property                                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assembly_name](#assembly_name)                               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_name")                        |
| [ncbi_assembly_accession](#ncbi_assembly_accession)           | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_accession")           |
| [assembly_unit_name](#assembly_unit_name)                     | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_unit_name")              |
| [ncbi_assembly_unit_accession](#ncbi_assembly_unit_accession) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_unit_accession") |

### assembly_name

A free-text common name (e.g. 'GRCh38') that is used to denote the sequence assembly.

`assembly_name`

*   is optional

*   Type: `string` ([Assembly common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_name")

#### assembly_name Type

`string` ([Assembly common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md))

#### assembly_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### assembly_name Examples

```json
"GRCh38.p14"
```

```json
"GRCh38"
```

```json
"GRCh37.p13"
```

```json
"GRCh37"
```

### ncbi_assembly_accession

Assembly's identifier (e.g. GCF\_000001405.26) of the assembly. For example, the assembly accession for the GenBank version of the public human reference assembly (GRCh38.p14) is GCA\_000001405.29. See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbi_assembly_accession`

*   is optional

*   Type: `string` ([NCBI Assembly accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_accession")

#### ncbi_assembly_accession Type

`string` ([NCBI Assembly accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md))

all of

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-ncbi-assembly-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

#### ncbi_assembly_accession Examples

```json
"assembly:GCF_000001405.26"
```

```json
"assembly:GCA_000001405.1"
```

```json
"assembly:GCF_000005845.2"
```

### assembly_unit_name

A free-text common name (e.g. 'chr17') that is used to denote the sequence assembly unit.

`assembly_unit_name`

*   is optional

*   Type: `string` ([Assembly unit common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_unit_name")

#### assembly_unit_name Type

`string` ([Assembly unit common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md))

#### assembly_unit_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### assembly_unit_name Examples

```json
"Chromosome 2"
```

```json
"MT"
```

```json
"chr17"
```

```json
"chr20"
```

```json
"18"
```

### ncbi_assembly_unit_accession

NCBI's identifier (e.g. ) of the assembly unit. An assembly unit is defined as the collection of sequences used to define discrete parts of an assembly. Commonly assembly units are entire chromosomes (e.g. Chromosome 1 of human genome), scaffolds or different types of sequences (e.g. Mitochondrial DNA). For example, GenBank's accession: (1) for the assembly unit of the human chromosome 1 is [NC\_000001.11](https://www.ncbi.nlm.nih.gov/nuccore/NC\_000001.11) (for the human reference assembly GRCh38.p14); (2) and for the complete mitochondrion genome of a human it is [NC\_012920.1](https://www.ncbi.nlm.nih.gov/nuccore/NC\_012920.1). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbi_assembly_unit_accession`

*   is optional

*   Type: `string` ([NCBI Assembly unit accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_unit_accession")

#### ncbi_assembly_unit_accession Type

`string` ([NCBI Assembly unit accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md))

all of

*   one (and only one) of

    *   [NC - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nc---molecule-type-dna.md "check type definition")

    *   [AC - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-ac---molecule-type-dna.md "check type definition")

    *   [NZ - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nz---molecule-type-dna.md "check type definition")

    *   [NT - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nt---molecule-type-dna.md "check type definition")

    *   [NW - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nw---molecule-type-dna.md "check type definition")

    *   [NG - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-ng---molecule-type-dna.md "check type definition")

    *   [NM - Molecule type: mRNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nm---molecule-type-mrna.md "check type definition")

    *   [XM - Molecule type: mRNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-xm---molecule-type-mrna.md "check type definition")

    *   [NR - Molecule type: RNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nr---molecule-type-rna.md "check type definition")

    *   [XR - Molecule type: RNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-xr---molecule-type-rna.md "check type definition")

    *   [NP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-np---molecule-type-protein.md "check type definition")

    *   [AP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-ap---molecule-type-protein.md "check type definition")

    *   [XP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-xp---molecule-type-protein.md "check type definition")

    *   [YP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-yp---molecule-type-protein.md "check type definition")

    *   [WP - Molecule type: protein](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-wp---molecule-type-protein.md "check type definition")

#### ncbi_assembly_unit_accession Examples

```json
"refseq:NC_000001.11"
```

```json
"refseq:NC_012920.1"
```

## Definitions group genomic_sequence_descriptor

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor"}
```

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assembly_descriptor](#assembly_descriptor)     | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/assembly_descriptor")                                      |
| [sequence_coordinates](#sequence_coordinates)   | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-sequence-coordinates.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/sequence_coordinates")                                          |
| [dna_sequence_strand](#dna_sequence_strand)     | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-genomic-sequence-descriptor-properties-dna-sequence-strand.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/dna_sequence_strand")     |
| [nucleic_acid_sequence](#nucleic_acid_sequence) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/nucleic_acid_sequence") |

### assembly_descriptor

Node describing a sequence assembly referenced in [NCBI's Assembly database](https://www.ncbi.nlm.nih.gov/assembly). Assembly is a database providing information on the structure of assembled genomes, assembly names and other meta-data, statistical reports, and links to genomic sequence data. An assembly is defined as the set of chromosomes, unlocalized and unplaced (sometimes called 'random') and alternate sequences used to represent an organism's genome. Assemblies are constructed from 1 or more assembly units.

`assembly_descriptor`

*   is optional

*   Type: `object` ([NCBI's Assembly descriptor](ega-12-definitions-ncbis-assembly-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/assembly_descriptor")

#### assembly_descriptor Type

`object` ([NCBI's Assembly descriptor](ega-12-definitions-ncbis-assembly-descriptor.md))

any of

*   [Or the Assembly accession is required](ega-12-definitions-ncbis-assembly-descriptor-anyof-or-the-assembly-accession-is-required.md "check type definition")

*   [Or the Assembly unit accession is required](ega-12-definitions-ncbis-assembly-descriptor-anyof-or-the-assembly-unit-accession-is-required.md "check type definition")

### sequence_coordinates

A position in a map (for example a genetic map), either a single position (e.g. 71366222) or a region interval (e.g. 71366222-71532374). Used to define coordinates within an assembly unit.

`sequence_coordinates`

*   is optional

*   Type: `object` ([Sequence coordinates](ega-12-definitions-sequence-coordinates.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-sequence-coordinates.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/sequence_coordinates")

#### sequence_coordinates Type

`object` ([Sequence coordinates](ega-12-definitions-sequence-coordinates.md))

any of

*   [Either a single position is given](ega-12-definitions-sequence-coordinates-anyof-either-a-single-position-is-given.md "check type definition")

*   [Or the whole sequence interval](ega-12-definitions-sequence-coordinates-anyof-or-the-whole-sequence-interval.md "check type definition")

### dna_sequence_strand

DNA sequence is double-stranded. By convention, for a reference chromosome, one whole strand is designated the 'forward strand' and the other the 'reverse strand'. This designation is arbitrary and sometimes the terms 'plus strand' and 'minus strand', respectively, are used instead. A genomic feature can live on a DNA strand in one of two orientations. For instance, a gene is said to have a coding strand (also known as its 'sense strand'), and a template strand (also known as its 'antisense strand'), which can be forward or reverse strands depending on which contain the nucleotide sequence the RNA polymerase reads to create its RNA product. Annotations such as Ensembl and UCSC are concerned with the coding sequences of genes, so when they say a gene is on the forward strand, it means the gene's coding sequence is on the forward strand. To follow through again, that means that during transcription of this forward-strand gene, the gene's template sequence is read from the reverse strand, producing an mRNA that matches the sequence on the forward strand. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`dna_sequence_strand`

*   is optional

*   Type: `string` ([DNA Sequence strand](ega-12-definitions-genomic-sequence-descriptor-properties-dna-sequence-strand.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-genomic-sequence-descriptor-properties-dna-sequence-strand.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/dna_sequence_strand")

#### dna_sequence_strand Type

`string` ([DNA Sequence strand](ega-12-definitions-genomic-sequence-descriptor-properties-dna-sequence-strand.md))

#### dna_sequence_strand Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation                          |
| :---------- | :----------------------------------- |
| `"forward"` |                                      |
| `"reverse"` | function reverse() { [native code] } |

### nucleic_acid_sequence

Sequence of characters representing a specific nucleic (i.e. molecular species - e.g. Adenine) or groupings of these (through ambiguity codes), using [one-letter IUPAC abbreviations](https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry#Amino_acid_and_nucleotide_base_codes).

`nucleic_acid_sequence`

*   is optional

*   Type: `string` ([Nucleic acid sequence](ega-12-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/nucleic_acid_sequence")

#### nucleic_acid_sequence Type

`string` ([Nucleic acid sequence](ega-12-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md))

#### nucleic_acid_sequence Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^([\.-]*[ACGTURYKMSWBDHVNX]+[\.-]*)+$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B%5C.-%5D\*%5BACGTURYKMSWBDHVNX%5D%2B%5B%5C.-%5D\*\)%2B%24 "try regular expression with regexr.com")

#### nucleic_acid_sequence Examples

```json
"ACTGCCG"
```

```json
"CTGCGCGCGCT"
```

```json
"KM-AGT-X-N"
```

## Definitions group sequence_coordinates

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates"}
```

| Property                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                   |
| :-------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [single_position](#single_position)     | `number` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-single-sequence-position.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/single_position") |
| [sequence_interval](#sequence_interval) | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval")      |

### single_position

A single 1-based (first base of the assembly unit is 1, not 0) sequence coordinate, inclusive. It can be used to describe the start or end coordinates of a sequence interval, or directly a single coordinate within a sequence.

`single_position`

*   is optional

*   Type: `number` ([Single sequence position](ega-12-definitions-sequence-coordinates-properties-single-sequence-position.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-single-sequence-position.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/single_position")

#### single_position Type

`number` ([Single sequence position](ega-12-definitions-sequence-coordinates-properties-single-sequence-position.md))

#### single_position Examples

```json
71366222
```

```json
36592394
```

```json
1
```

### sequence_interval

The location of a sequence feature in a genome, defined by its start (e.g. 71366222) and end (e.g. 71532374) position on some reference genomic coordinate system. Positions are always represented by contiguous spans using interbase coordinates or coordinate ranges. Both coordinates are inclusive: the sequence bounds are included in the described genomic feature. In other words, if the sequence interval is 71366222-71532374, both 71366222 and 71532374 coordinates are included in the feature.

`sequence_interval`

*   is optional

*   Type: `object` ([Sequence interval](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval")

#### sequence_interval Type

`object` ([Sequence interval](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md))

## Definitions group dna_sequence_strand

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/dna_sequence_strand"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group nucleic_acid_sequence

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/nucleic_acid_sequence"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group single_sequence_position

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/single_sequence_position"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie_general_pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/curie_general_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie_refseq_pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/curie_refseq_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie_hgnc_symbol_pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/curie_hgnc_symbol_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie_hgnc_identifier_pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/curie_hgnc_identifier_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie_ncbi_gene_identifier_pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/curie_ncbi_gene_identifier_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie_ncbi_assembly_pattern

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/curie_ncbi_assembly_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group assay_technology_descriptor

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor"}
```

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                              |
| :------------------------------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay_instrument](#assay_instrument)                   | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assays-instrument-category.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument")      |
| [assay_instrument_platform](#assay_instrument_platform) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assay-instrument-label.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument_platform") |

### assay_instrument

The general categories (e.g. sequencers) in which assay instruments are categorized. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`assay_instrument`

*   is required

*   Type: `string` ([Assay's instrument category](ega-12-definitions-assay-technology-properties-assays-instrument-category.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assays-instrument-category.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument")

#### assay_instrument Type

`string` ([Assay's instrument category](ega-12-definitions-assay-technology-properties-assays-instrument-category.md))

#### assay_instrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation |
| :------------ | :---------- |
| `"array"`     |             |
| `"sequencer"` |             |

### assay_instrument_platform

Label (e.g. 'Illumina HiSeq 2500'), chosen from a list of controlled vocabulary (CV), of the technology used at the experiment. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`assay_instrument_platform`

*   is required

*   Type: `string` ([Assay instrument label](ega-12-definitions-assay-technology-properties-assay-instrument-label.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assay-instrument-label.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument_platform")

#### assay_instrument_platform Type

`string` ([Assay instrument label](ega-12-definitions-assay-technology-properties-assay-instrument-label.md))

#### assay_instrument_platform Examples

```json
"Illumina HiSeq 2500"
```

```json
"[HuGene-1_1-st] Affymetrix Human Gene 1.1 ST Array [probe set (exon) version]"
```

```json
"DNBSEQ-G400 FAST"
```

## Definitions group library_layout

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/library_layout"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group spot_descriptor

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group type_of_data

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/type_of_data"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group reference_alignment_details

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/reference_alignment_details"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group uberon-anatomical-entity

Reference this group by using

```json
{"$ref":"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/uberon-anatomical-entity"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
