# EGA common metadata definitions Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to store common definitions for other metadata objects. Basically, we are defining here common properties (e.g. instances' aliases) that other metadata objects (e.g. sample) may use. The way we refer to them is by using this object's '$id' field, referencing it in other files (with '$ref' and the relative path of the property - e.g. '$ref': '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id>'). See structuring documentation (<https://json-schema.org/understanding-json-schema/structuring.html>). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract               | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                         |
| :--------------------- | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------- |
| Cannot be instantiated | Yes        | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json](../../../schemas/EGA.common-definitions.json "open original schema") |

## EGA common metadata definitions Type

`object` ([EGA common metadata definitions](ega-12.md))

# EGA common metadata definitions Definitions

## Definitions group object\_core\_id

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_core_id"}
```

| Property                                     | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                     |
| :------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [alias](#alias)                              | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/alias")                      |
| [center\_name](#center_name)                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/center_name")      |
| [ega\_accession](#ega_accession)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/ega_accession")    |
| [external\_accessions](#external_accessions) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions") |

### alias

Submitter designated name (e.g. 'my\_sample\_J13') for the object (e.g. Sample). The name must be unique within the submission account (e.g. 'ega-box-79'), since the aliases and submission accounts are concatenated within our database to obtain the unique alias (e.g. 'ega-box-79::my\_sample\_J13').

`alias`

*   is optional

*   Type: `string` ([Alias of an object](ega-12-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/alias")

#### alias Type

`string` ([Alias of an object](ega-12-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

#### alias Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### alias Examples

```json
"my_sample_J13"
```

### center\_name

Center name (e.g. 'EBI-TEST') associated to the submitter. In other words, it is the acronym of the submitter's account (provided by the HelpDesk team).

`center_name`

*   is optional

*   Type: `string` ([Center name of the submitter](ega-12-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/center_name")

#### center\_name Type

`string` ([Center name of the submitter](ega-12-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

#### center\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### center\_name Examples

```json
"EBI-TEST"
```

### ega\_accession

The object accession (i.e. unique identifier) assigned by the archive (EGA). Object accessions can be found in the 'Identifiers' section of the EGA-archive website (<https://ega-archive.org/metadata/how-to-use-the-api>) and commonly start with EGA, followed by the distinctive letter of the object and finally the numeric ID of the instance.

`ega_accession`

*   is optional

*   Type: `string` ([EGA's accession of the object](ega-12-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/ega_accession")

#### ega\_accession Type

`string` ([EGA's accession of the object](ega-12-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

#### ega\_accession Examples

```json
"EGAN00003245489"
```

### external\_accessions

External accession node to reference objects in other archives (e.g. an already existing sample at BioSamples).

`external_accessions`

*   is optional

*   Type: `object[]` ([Object of external accession of the object](ega-12-definitions-object-of-external-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/external_accessions")

#### external\_accessions Type

`object[]` ([Object of external accession of the object](ega-12-definitions-object-of-external-accession-of-the-object.md))

#### external\_accessions Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## Definitions group custom\_attribute

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute"}
```

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :-------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tag](#tag)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/tag")     |
| [value](#value) | Multiple | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/value") |
| [units](#units) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/units") |

### tag

The name of the attribute (e.g. 'Age').

`tag`

*   is required

*   Type: `string` ([Tag of the custom attribute](ega-12-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/tag")

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

*   defined in: [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/value")

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

*   defined in: [EGA common metadata definitions](ega-12-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/units")

#### units Type

`string` ([Units of the custom attribute](ega-12-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md))

#### units Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### units Examples

```json
"years"
```

## Definitions group file\_object

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object"}
```

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                       |
| :------------------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filename](#filename)                                   | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filename.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")                                                |
| [filetype](#filetype)                                   | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")                                                |
| [checksum\_method](#checksum_method)                    | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-method-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")                               |
| [unencrypted\_checksum](#unencrypted_checksum)          | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum") |
| [encrypted\_checksum](#encrypted_checksum)              | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")     |
| [sequence\_quality\_details](#sequence_quality_details) | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details")                |

### filename

The full name of a file, including all of their file extensions (e.g. .gpg, .md5...), that identifies the file (e.g. 'my-bam-file.bam.gpg').

`filename`

*   is required

*   Type: `string` ([Filename](ega-12-definitions-ega-file-object-properties-filename.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filename.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")

#### filename Type

`string` ([Filename](ega-12-definitions-ega-file-object-properties-filename.md))

#### filename Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>:;,?"*|]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22*%7C%5D%2B%24 "try regular expression with regexr.com")

#### filename Examples

```json
"my-bam-file.bam.gpg"
```

### filetype

The nature of the content stored in an electronic file. The string corresponds to the ID or name (e.g. FASTA or TSV), chosen from a list of controlled vocabulary (CV), associated with the given filetype. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`filetype`

*   is required

*   Type: `string` ([Filetype](ega-12-definitions-ega-file-object-properties-filetype.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")

#### filetype Type

`string` ([Filetype](ega-12-definitions-ega-file-object-properties-filetype.md))

#### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation                                                                                                                                                                                                                                                                                                                                       |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"CEL"`   | \[EFO:0005630]                                                                                                                                                                                                                                                                                                                                    |
| `"TSV"`   | \[NCIT:C164049]: Tab delimited text file commonly used to deliver certain phenotype or auxiliary data along with sequencing submissions (only needed for certain use cases). The first line is normally devoted to column headers. When used along sequencing files in a sequencing assay, each column is dedicated to an INDSC data series type. |
| `"ADF"`   | \[NCIT:C172213]                                                                                                                                                                                                                                                                                                                                   |
| `"FASTQ"` | \[EFO:0004155]                                                                                                                                                                                                                                                                                                                                    |
| `"FASTA"` | \[NCIT:C47845]                                                                                                                                                                                                                                                                                                                                    |
| `"SDRF"`  | \[NCIT:C172211]                                                                                                                                                                                                                                                                                                                                   |
| `"IDF"`   | \[NCIT:C172212]                                                                                                                                                                                                                                                                                                                                   |
| `"VCF"`   | \[NCIT:C172216]                                                                                                                                                                                                                                                                                                                                   |
| `"SRA"`   | \[format:3698]                                                                                                                                                                                                                                                                                                                                    |
| `"SRF"`   | \[EFO:0004154]                                                                                                                                                                                                                                                                                                                                    |
| `"SFF"`   | \[EFO:0004156]                                                                                                                                                                                                                                                                                                                                    |
| `"BAM"`   | \[EFO:0004157]                                                                                                                                                                                                                                                                                                                                    |
| `"CRAM"`  | \[format:3462]                                                                                                                                                                                                                                                                                                                                    |
| `"XLSX"`  | \[format:3620]                                                                                                                                                                                                                                                                                                                                    |
| `"CSV"`   | \[format:3752]                                                                                                                                                                                                                                                                                                                                    |
| `"BED"`   | \[format:3003]                                                                                                                                                                                                                                                                                                                                    |
| `"IDAT"`  | \[format:3578]                                                                                                                                                                                                                                                                                                                                    |
| `"MAP"`   | \[format:3285]                                                                                                                                                                                                                                                                                                                                    |
| `"PED"`   | \[format:3286]                                                                                                                                                                                                                                                                                                                                    |
| `"BIM"`   |                                                                                                                                                                                                                                                                                                                                                   |
| `"FAM"`   |                                                                                                                                                                                                                                                                                                                                                   |
| `"TXT"`   |                                                                                                                                                                                                                                                                                                                                                   |
| `"EXP"`   | \[format:1631]                                                                                                                                                                                                                                                                                                                                    |
| `"GPR"`   | \[format:3829]                                                                                                                                                                                                                                                                                                                                    |
| `"PY"`    | \[format:3996]                                                                                                                                                                                                                                                                                                                                    |
| `"SH"`    | Bash scripts                                                                                                                                                                                                                                                                                                                                      |

### checksum\_method

Node containing both the ID (MD5 or SHA-256), describing the method which yields the checksum from a data input for the purpose of detecting errors. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`checksum_method`

*   is required

*   Type: `string` ([Checksum method ID](ega-12-definitions-ega-file-object-properties-checksum-method-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-method-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")

#### checksum\_method Type

`string` ([Checksum method ID](ega-12-definitions-ega-file-object-properties-checksum-method-id.md))

#### checksum\_method Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation     |
| :---------- | :-------------- |
| `"MD5"`     | \[NCIT:C171276] |
| `"SHA-256"` | \[NCIT:C80226]  |

### unencrypted\_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the unencrypted files.

`unencrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum")

#### unencrypted\_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

#### unencrypted\_checksum Examples

```json
"46798b5cfca45c46a84b7419f8b74735"
```

### encrypted\_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the encrypted files.

`encrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")

#### encrypted\_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

#### encrypted\_checksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```

### sequence\_quality\_details

Sequencing quality scores measure the probability that a base is called (i.e. sequenced) incorrectly. New sequencing technologies assign a quality score to each of the bases in the sequence.

`sequence_quality_details`

*   is optional

*   Type: `object` ([Sequence quality details](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details")

#### sequence\_quality\_details Type

`object` ([Sequence quality details](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md))

## Definitions group relationship\_object

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationship_object"}
```

| Property               | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                |
| :--------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-relationship-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")                 |
| [r\_source](#r_source) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source")      |
| [r\_target](#r_target) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target")      |
| [r\_label](#r_label)   | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_label") |

### r\_type

ID (e.g. same\_as) of the type of the relationship. To be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`r_type`

*   is required

*   Type: `string` ([Relationship type](ega-12-definitions-ega-relationships-object-properties-relationship-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-relationship-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")

#### r\_type Type

`string` ([Relationship type](ega-12-definitions-ega-relationships-object-properties-relationship-type.md))

#### r\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                        | Explanation    |
| :--------------------------- | :------------- |
| `"referenced_by"`            | \[SIO:000252]  |
| `"develops_from"`            | \[RO:0002202]  |
| `"same_as"`                  | \[NCIT:C64637] |
| `"member_of"`                | \[RO:0002350]  |
| `"grouped_with"`             |                |
| `"family_relationship_with"` | \[EFO:0004424] |
| `"child_of"`                 | \[GSSO:000728] |
| `"is_after"`                 | \[SIO:000211]  |
| `"published_in"`             | \[EFO:0001796] |
| `"submitted_by"`             | \[NCIT:C25695] |
| `"contact_of"`               | \[NCIT:C25461] |
| `"main_contact_of"`          |                |

#### r\_type Examples

```json
"referenced_by"
```

### r\_source

Object reference of the relationship's source. In other words, the starting point of the relationship: in 'sample\_A develops\_from sample\_B' the source is 'sample\_A'.

`r_source`

*   is optional

*   Type: `object` ([Source of the relationship](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source")

#### r\_source Type

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

        *   [Protocol: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-protocol-object_id-and-object_type-check.md "check type definition")

### r\_target

Object reference of the relationship's target. In other words, the ending point of the relationship: in 'sample\_A develops\_from sample\_B' the target is 'sample\_B'.

`r_target`

*   is optional

*   Type: `object` ([Target of the relationship](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target")

#### r\_target Type

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

        *   [Protocol: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-protocol-object_id-and-object_type-check.md "check type definition")

### r\_label

Custom free-form label of the relationship, used to add extra details of the relationship if needed.

`r_label`

*   is optional

*   Type: `string` ([Custom label of the relationship](ega-12-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_label")

#### r\_label Type

`string` ([Custom label of the relationship](ega-12-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md))

#### r\_label Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### r\_label Examples

```json
"Source individual is the third child of the target individual"
```

```json
"Grouped samples by colour of the medium"
```

```json
"Both samples are the same because of an error in the submission at..."
```

## Definitions group array\_label

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/array_label"}
```

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                      |
| :---------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [array\_label\_id](#array_label_id)       | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")             |
| [array\_label\_curie](#array_label_curie) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie")       |
| [label\_description](#label_description)  | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/label_description") |

### array\_label\_id

ID/name (e.g. 'Cy3 dye' or 'Biotin') of the Array label used for the experiment.

`array_label_id`

*   is required

*   Type: `string` ([Array label of the array experiment - ID](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_id")

#### array\_label\_id Type

`string` ([Array label of the array experiment - ID](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---id.md))

#### array\_label\_id Examples

```json
"Cy3 dye"
```

### array\_label\_curie

CURIE (i.e. ontologized term - e.g. 'CHEBI:37987' or 'CHEBI:15956') of the Array label used for the experiment. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index).

`array_label_curie`

*   is optional

*   Type: `string` ([Array label of the array experiment - CURIE](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/array_label_curie")

#### array\_label\_curie Type

`string` ([Array label of the array experiment - CURIE](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---curie-allof-compact-uri-curie-pattern.md "check type definition")

#### array\_label\_curie Examples

```json
"CHEBI:37987"
```

### label\_description

Additional description of the used label, indicating further details: context, purpose of the label, description of the label in the absence of an ontologized term, etc.

`label_description`

*   is optional

*   Type: `string` ([Array label of the array experiment - Description](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/array_label/properties/label_description")

#### label\_description Type

`string` ([Array label of the array experiment - Description](ega-12-definitions-repeatable-array_label-node-properties-array-label-of-the-array-experiment---description.md))

#### label\_description Examples

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
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group checksum-pattern-check

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group md5-checksum-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/md5-checksum-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group SHA-256-checksum-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/SHA-256-checksum-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-experiment-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-experiment-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-study-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-study-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-sample-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-sample-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-submission-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-submission-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-assay-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-assay-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-dataset-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-dataset-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-analysis-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-analysis-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-policy-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-policy-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-DAC-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-DAC-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-individual-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-individual-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-protocol-id-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-protocol-id-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-ISO8601-date-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-ISO8601-date-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGA-ISO8601-duration-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-ISO8601-duration-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group filename-filetype-pattern-check

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cel-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cel-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group tsv-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/tsv-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group adf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/adf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fastq-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fastq-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fasta-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fasta-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sdrf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sdrf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group idf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/idf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group vcf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/vcf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sra-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sra-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group srf-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/srf-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sff-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sff-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bam-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bam-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cram-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cram-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group xlsx-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/xlsx-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group csv-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/csv-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bed-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bed-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group idat-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/idat-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group map-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/map-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group ped-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ped-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bim-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bim-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fam-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fam-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group txt-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/txt-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group exp-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/exp-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group gpr-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gpr-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group py-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/py-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sh-file-filename-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sh-file-filename-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group object\_external\_accession

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession"}
```

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                        |
| :------------------------------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [external\_accession\_curie](#external_accession_curie) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession_curie") |
| [accession\_reference](#accession_reference)            | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_reference")  |
| [accession\_label](#accession_label)                    | Multiple | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")          |

### external\_accession\_curie

Unique identifier of an external, to EGA, object. It shall follow CURIE format (`prefix`:`accession`): prefix assigned to the archive (e.g. biosample - search for yours at identifiers.org) and the unique accession of the object (e.g. SAMEA7616999).

`external_accession_curie`

*   is optional

*   Type: `string` ([CURIE of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/external_accession_curie")

#### external\_accession\_curie Type

`string` ([CURIE of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-object-of-external-accession-of-the-object-properties-curie-of-the-external-accession-allof-compact-uri-curie-pattern.md "check type definition")

#### external\_accession\_curie Examples

```json
"biosample:SAMEA7616999"
```

```json
"arrayexpress:E-MEXP-1712"
```

```json
"biostudies:S-EPMC3314381"
```

```json
"pubmed:30962759"
```

### accession\_reference

Full or partial URL/URI of the external accession, for systems to resolve it.

`accession_reference`

*   is optional

*   Type: `string` ([Reference of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_reference")

#### accession\_reference Type

`string` ([Reference of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession.md))

all of

*   [URL/URI pattern](ega-12-definitions-object-of-external-accession-of-the-object-properties-reference-of-the-external-accession-allof-urluri-pattern.md "check type definition")

#### accession\_reference Examples

```json
"https://www.ebi.ac.uk/biosamples/samples/SAMN11716999"
```

```json
"https://pubmed.ncbi.nlm.nih.gov/19491253"
```

```json
"https://identifiers.org/arrayexpress:E-MEXP-1712"
```

```json
"https://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-1712/"
```

### accession\_label

Label (e.g. 'taken from biosample temporarily') of the external accession, used to add extra information to the identifier.

`accession_label`

*   is optional

*   Type: any of the folllowing: `string` or `number` ([Label of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/object_external_accession/properties/accession_label")

#### accession\_label Type

any of the folllowing: `string` or `number` ([Label of the external accession](ega-12-definitions-object-of-external-accession-of-the-object-properties-label-of-the-external-accession.md))

#### accession\_label Examples

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

```json
"Recurrent Erythema Nodosum in a Child with a SHOC2 Gene Mutation"
```

## Definitions group sample-label-association

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association"}
```

| Property                 | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                            |
| :----------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [label](#label)          | `object` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/label")                                   |
| [object\_id](#object_id) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id") |

### label

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node corresponds to the basic description of one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described. Its basic structure is a label ID and its optional CURIE.

`label`

*   is required

*   Type: `object` ([Repeatable array\_label node](ega-12-definitions-repeatable-array_label-node.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-array_label-node.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/label")

#### label Type

`object` ([Repeatable array\_label node](ega-12-definitions-repeatable-array_label-node.md))

### object\_id



`object_id`

*   is required

*   Type: `object` ([Object's IDs block](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sample-label-association/properties/object_id")

#### object\_id Type

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
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end"}
```

| Property                     | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                         |
| :--------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id-1)   | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")    |
| [object\_type](#object_type) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type") |

### object\_id

Node containing the main identifiers of the relationship's object (e.g. alias, center\_name...), inherited from the common definitions (#/definitions/object\_core\_id).

`object_id`

*   is required

*   Type: `object` ([Relationship's object's IDs block](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")

#### object\_id Type

`object` ([Relationship's object's IDs block](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

### object\_type

Type of the relationship's object, chosen from a list of CV (e.g. experiment, dataset, external\_URL...). Both the source or target types can be: (1) the object tag of one of EGA's object (e.g. file, sample...); (2) an 'external\_accession'; (3) or an 'external\_URL'. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`object_type`

*   is required

*   Type: `string` ([Type of the relationship's object](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type")

#### object\_type Type

`string` ([Type of the relationship's object](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

#### object\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation                                                                                                                                                         |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"experiment"`         | Contains information about the experimental design of the sequencing                                                                                                |
| `"study"`              | Information about the study                                                                                                                                         |
| `"sample"`             | Information about the used samples                                                                                                                                  |
| `"individual"`         | Information about the participants (i.e. humans) of the study                                                                                                       |
| `"submission"`         | Information about the submission actions                                                                                                                            |
| `"assay"`              | Contains information about the specific assays (either sequencing or array assays) from the experiment                                                              |
| `"dataset"`            | Contains the collection of assay/analysis data files to be subject to controlled access                                                                             |
| `"analysis"`           | Contains the analysis metadata and data files                                                                                                                       |
| `"policy"`             | Contains information related to the Data Access Agreement (DAA) the dataset is subject to                                                                           |
| `"DAC"`                | Contains information about the Data Access Committee (DAC)                                                                                                          |
| `"protocol"`           | Contains information about a planned process.                                                                                                                       |
| `"external_accession"` | An external accession among the ones Entrez (NCBI's text search) contemplates (search for the terms here: https\://www\.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?) |
| `"external_URL"`       | An external URL resource, of any type                                                                                                                               |

#### object\_type Examples

```json
"sample"
```

## Definitions group subject\_id

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/subject_id"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group biological\_sex

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/biological_sex"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group experimental\_condition\_descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor"}
```

| Property                                                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                         |
| :-------------------------------------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [experimental\_condition\_term](#experimental_condition_term)               | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")               |
| [experimental\_condition\_curie](#experimental_condition_curie)             | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")             |
| [experimental\_condition\_description](#experimental_condition_description) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description") |

### experimental\_condition\_term

Term that specifies the experimental condition (e.g. 'fibroadenoma').

`experimental_condition_term`

*   is required

*   Type: `string` ([Experimental condition term](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_term")

#### experimental\_condition\_term Type

`string` ([Experimental condition term](ega-12-definitions-experimental-condition-properties-experimental-condition-term.md))

#### experimental\_condition\_term Examples

```json
"control"
```

```json
"fibroadenoma"
```

```json
"osteonecrosis"
```

### experimental\_condition\_curie

Curie (i.e. ontologised term - e.g. 'EFO:0001461') of the experimental condition. Search for the ontologized term at the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/index).

`experimental_condition_curie`

*   is optional

*   Type: `string` ([Experimental condition curie](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_curie")

#### experimental\_condition\_curie Type

`string` ([Experimental condition curie](ega-12-definitions-experimental-condition-properties-experimental-condition-curie.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-experimental-condition-properties-experimental-condition-curie-allof-compact-uri-curie-pattern.md "check type definition")

#### experimental\_condition\_curie Examples

```json
"EFO:0001461"
```

```json
"EFO:1000254"
```

```json
"EFO:0004259"
```

### experimental\_condition\_description

Broad description of the experimental condition, providing further details and context over the ontologised term.

`experimental_condition_description`

*   is optional

*   Type: `string` ([Experimental condition description](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/experimental_condition_descriptor/properties/experimental_condition_description")

#### experimental\_condition\_description Type

`string` ([Experimental condition description](ega-12-definitions-experimental-condition-properties-experimental-condition-description.md))

#### experimental\_condition\_description Examples

```json
"A control role is borne by a material in a process in which results obtained from an experimental sample and a control sample are compared."
```

```json
"A benign tumor of the breast characterized by the presence of stromal and epithelial elements."
```

```json
"A none disease characterized by death of bone tissue due to a lack of blood supply."
```

## Definitions group organism\_descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor"}
```

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                  |
| :----------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [taxon\_id\_curie](#taxon_id_curie)  | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id_curie")                           |
| [scientific\_name](#scientific_name) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name") |
| [common\_name](#common_name)         | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")         |

### taxon\_id\_curie

Taxonomy Identifier (e.g. 'NCBITaxon:9606' for humans) curated by the NCBI Taxonomy (search for organisms here: <https://www.ncbi.nlm.nih.gov/taxonomy>; or use the OLS: <https://www.ebi.ac.uk/ols/ontologies/ncbitaxon>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

`taxon_id_curie`

*   is required

*   Type: `string` ([NCBI Taxon identifier](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/taxon_id_curie")

#### taxon\_id\_curie Type

`string` ([NCBI Taxon identifier](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-identifier-allof-compact-uri-curie-pattern.md "check type definition")

#### taxon\_id\_curie Examples

```json
"NCBITaxon:9606"
```

```json
"NCBITaxon:155900"
```

```json
"NCBITaxon:408170"
```

```json
"NCBITaxon:447426"
```

### scientific\_name

The name applied to a plant, animal, or other organism, according to the Codes of Nomenclature, consisting of a Genus and species (e.g. 'homo sapiens').

`scientific_name`

*   is optional

*   Type: `string` ([Biologic entity classification scientific name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name")

#### scientific\_name Type

`string` ([Biologic entity classification scientific name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md))

#### scientific\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### scientific\_name Examples

```json
"homo sapiens"
```

```json
"uncultured organism"
```

```json
"human gut metagenome"
```

```json
"human oral metagenome"
```

### common\_name

Common name (e.g. 'human') used to designate a plant, animal or other organism, as opposed to the scientific name.

`common_name`

*   is optional

*   Type: `string` ([Biologic entity classification common name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/common_name")

#### common\_name Type

`string` ([Biologic entity classification common name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

#### common\_name Examples

```json
"human"
```

## Definitions group schema\_descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor"}
```

| Property                                               | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                             |
| :----------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_type](#object_type-1)                         | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-type-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_type")                                 |
| [described\_by\_schema\_uri](#described_by_schema_uri) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/described_by_schema_uri")                      |
| [object\_schema\_version](#object_schema_version)      | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_schema_version")            |
| [common\_schema\_version](#common_schema_version)      | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/common_schema_version") |

### object\_type

Type of the object (e.g. 'sample') the JSON document describes.

`object_type`

*   is required

*   Type: `string` ([Type of the object](ega-12-definitions-schema-descriptor-properties-type-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-type-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_type")

#### object\_type Type

`string` ([Type of the object](ega-12-definitions-schema-descriptor-properties-type-of-the-object.md))

#### object\_type Constraints

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
| `"protocol"`   |             |
| `"object-set"` |             |

### described\_by\_schema\_uri

URI of the schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json>') that describes the JSON document (e.g. 'my\_sample.json')

`described_by_schema_uri`

*   is required

*   Type: `string` ([URI of the schema](ega-12-definitions-schema-descriptor-properties-uri-of-the-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/described_by_schema_uri")

#### described\_by\_schema\_uri Type

`string` ([URI of the schema](ega-12-definitions-schema-descriptor-properties-uri-of-the-schema.md))

#### described\_by\_schema\_uri Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^https://github\.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA\..+\.json$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3A%2F%2Fgithub%5C.com%2FEbiEga%2Fega-metadata-schema%2Ftree%2Fmain%2Fschemas%2FEGA%5C..%2B%5C.json%24 "try regular expression with regexr.com")

#### described\_by\_schema\_uri Examples

```json
"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json"
```

### object\_schema\_version

The version of the object's schema, the one specific for the object the JSON document corresponds to (e.g. 'EGA.sample.json'), not the common definitions schema's version (i.e. 'EGA.common-definitions.json').

`object_schema_version`

*   is required

*   Type: `string` ([Version of the object's schema](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_schema_version")

#### object\_schema\_version Type

`string` ([Version of the object's schema](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

all of

*   [Semantic versioning pattern](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema-allof-semantic-versioning-pattern.md "check type definition")

### common\_schema\_version

The version of the common definition's schema, the one containing all shared definitions (i.e. 'EGA.common-definitions.json'), not the one specific to the object described by the JSON document (e.g. 'EGA.sample.json').

`common_schema_version`

*   is required

*   Type: `string` ([Version of the common definition's schema](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/common_schema_version")

#### common\_schema\_version Type

`string` ([Version of the common definition's schema](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

all of

*   [Semantic versioning pattern](ega-12-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema-allof-semantic-versioning-pattern.md "check type definition")

## Definitions group semantic-versioning-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/semantic-versioning-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group contact\_details

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contact_details"}
```

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                          |
| :---------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [individual\_full\_name](#individual_full_name) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/individual_full_name") |
| [institution\_name](#institution_name)          | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-institution-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/institution_name")               |
| [email\_address](#email_address)                | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-email-address.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/email_address")                     |
| [phone\_number](#phone_number)                  | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-contact-details-properties-phone-number.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/phone_number")                       |

### individual\_full\_name

A full set of all personal names by which an individual is known and that can be recited as a word-group, with the understanding that, taken together, they all relate to that one individual. In case there are several, separate them with semicolons (;).

`individual_full_name`

*   is optional

*   Type: `string` ([Full name of an individual](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/individual_full_name")

#### individual\_full\_name Type

`string` ([Full name of an individual](ega-12-definitions-contact-details-properties-full-name-of-an-individual.md))

#### individual\_full\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### individual\_full\_name Examples

```json
"Wayne Jr., Bruce"
```

### institution\_name

The full name of an institution the contact belongs to. In case there are several, separate them with semicolons (;).

`institution_name`

*   is optional

*   Type: `string` ([Institution name](ega-12-definitions-contact-details-properties-institution-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-institution-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/institution_name")

#### institution\_name Type

`string` ([Institution name](ega-12-definitions-contact-details-properties-institution-name.md))

#### institution\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### institution\_name Examples

```json
"European Genome-phenome Archive (EGA)"
```

### email\_address

Current email address that would be used in case the contact needs to be reached. Its expected format is of a local-part (e.g. 'myname'), followed by an 'at' sign (i.e. '@') and the domain of the address (e.g. 'gmail.com' or 'ebi.ac.uk').

`email_address`

*   is required

*   Type: `string` ([Email address](ega-12-definitions-contact-details-properties-email-address.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-email-address.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/email_address")

#### email\_address Type

`string` ([Email address](ega-12-definitions-contact-details-properties-email-address.md))

#### email\_address Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%40\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%5C.\(%5Ba-zA-Z%5D%7B2%2C5%7D\)%24 "try regular expression with regexr.com")

#### email\_address Examples

```json
"myname@ebi.ac.uk"
```

### phone\_number

Current phone number that would be used in case the contact needs to be reached. Theoretically would only be used in case the email address was not provided, does not exist or is unresponsive.

`phone_number`

*   is optional

*   Type: `string` ([Phone number](ega-12-definitions-contact-details-properties-phone-number.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-contact-details-properties-phone-number.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/phone_number")

#### phone\_number Type

`string` ([Phone number](ega-12-definitions-contact-details-properties-phone-number.md))

#### phone\_number Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\+?\(?[0-9]{1,4}\)?[-\s\./0-9]+$
```

[try pattern](https://regexr.com/?expression=%5E%5C%2B%3F%5C\(%3F%5B0-9%5D%7B1%2C4%7D%5C\)%3F%5B-%5Cs%5C.%2F0-9%5D%2B%24 "try regular expression with regexr.com")

#### phone\_number Examples

```json
"+44 7427512529"
```

## Definitions group study-design-keywords

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/study-design-keywords"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group locus\_identifier

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier"}
```

| Property                                     | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [organism\_descriptor](#organism_descriptor) | `object` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/organism_descriptor")       |
| [loci\_descriptor](#loci_descriptor)         | `array`  | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-locus-identifier-properties-loci-context-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor") |

### organism\_descriptor

This property describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance by default.

`organism_descriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/organism_descriptor")

#### organism\_descriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-12-definitions-organism-obi0100026-descriptor-block.md))

### loci\_descriptor

Array of locus context items. Multiple loci can be described in the array if the organism remains the same.

`loci_descriptor`

*   is required

*   Type: `object[]` ([Locus context item](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-locus-identifier-properties-loci-context-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locus_identifier/properties/loci_descriptor")

#### loci\_descriptor Type

`object[]` ([Locus context item](ega-12-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

#### loci\_descriptor Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## Definitions group gene\_descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor"}
```

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                   |
| :------------------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [gene\_symbol](#gene_symbol)                            | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-symbol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_symbol")                                  |
| [gene\_id\_curie](#gene_id_curie)                       | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_id_curie")                              |
| [gene\_description](#gene_description)                  | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_description")                 |
| [alternate\_gene\_ids](#alternate_gene_ids)             | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_ids")                    |
| [alternate\_gene\_symbols](#alternate_gene_symbols)     | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_symbols")            |
| [gene\_external\_references](#gene_external_references) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_external_references") |

### gene\_symbol

The official gene symbol. It is typically derived from the gene name. This optional field exists to provide the common identifier of the gene. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: (1) in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature; (2) while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

`gene_symbol`

*   is optional

*   Type: `string` ([Gene Symbol](ega-12-definitions-gene-descriptor-properties-gene-symbol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-symbol.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_symbol")

#### gene\_symbol Type

`string` ([Gene Symbol](ega-12-definitions-gene-descriptor-properties-gene-symbol.md))

#### gene\_symbol Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### gene\_symbol Examples

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

### gene\_id\_curie

A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol (e.g. HGNC:11535 for gene TAF1). The identifier has to follow CURIE format. Additionally, there are 2 types of allowed databases to reference: NCBIGene and HGNC. Other archives' accessions (e.g. ensembl:ENSDARG00000035330) can be cross referenced with NCBIGene to obtain its gene ID (e.g. ncbigene:555452).

`gene_id_curie`

*   is required

*   Type: `string` ([Gene CURIE ID](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_id_curie")

#### gene\_id\_curie Type

`string` ([Gene CURIE ID](ega-12-definitions-gene-descriptor-properties-gene-curie-id.md))

one (and only one) of

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-ncbi-gene-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-hgnc-identifier-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

#### gene\_id\_curie Examples

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

### gene\_description

Free-text description of the gene, only to be used to provide additional context that would otherwise be impossible to add encoded in the schema. In other words, kindly refrain from providing alternative gene symbols in the description if they are not added likewise in the 'alternate\_gene\_symbols' property.

`gene_description`

*   is optional

*   Type: `string` ([Description of the gene](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_description")

#### gene\_description Type

`string` ([Description of the gene](ega-12-definitions-gene-descriptor-properties-description-of-the-gene.md))

#### gene\_description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### gene\_description Examples

```json
"In the used cells, locus of gene ... was modified at positions +23, where thymine was transitioned to cytosine (T-C)..."
```

### alternate\_gene\_ids

Array of alternate identifiers for this gene. For example, Ensemble identifiers for genes and its transcripts.

`alternate_gene_ids`

*   is optional

*   Type: `string[]` ([Alternate gene ID](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids-alternate-gene-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_ids")

#### alternate\_gene\_ids Type

`string[]` ([Alternate gene ID](ega-12-definitions-gene-descriptor-properties-alternate-gene-ids-alternate-gene-id.md))

#### alternate\_gene\_ids Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### alternate\_gene\_symbols

Array of alternate gene sumbols. This field can be used to provide any other alternate gene symbol to refer to the gene, including previously approved gene symbols. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: (1) in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature; (2) while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

`alternate_gene_symbols`

*   is optional

*   Type: `string[]` ([Alternate gene symbol](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols-alternate-gene-symbol.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/alternate_gene_symbols")

#### alternate\_gene\_symbols Type

`string[]` ([Alternate gene symbol](ega-12-definitions-gene-descriptor-properties-alternate-gene-symbols-alternate-gene-symbol.md))

#### alternate\_gene\_symbols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### gene\_external\_references

Array of related identifiers. This field can be used to provide identifiers to alternative resources representing related, but not equivalent concepts, for example gene paralog, analog or ortholog IDs.

`gene_external_references`

*   is optional

*   Type: `string[]` ([Related gene ID](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids-related-gene-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gene_descriptor/properties/gene_external_references")

#### gene\_external\_references Type

`string[]` ([Related gene ID](ega-12-definitions-gene-descriptor-properties-related-not-equivalent-gene-ids-related-gene-id.md))

#### gene\_external\_references Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## Definitions group ncbi\_assembly\_descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor"}
```

| Property                                                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                       |
| :--------------------------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assembly\_name](#assembly_name)                                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_name")                        |
| [ncbi\_assembly\_accession](#ncbi_assembly_accession)            | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_accession")           |
| [assembly\_unit\_name](#assembly_unit_name)                      | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_unit_name")              |
| [ncbi\_assembly\_unit\_accession](#ncbi_assembly_unit_accession) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_unit_accession") |

### assembly\_name

A free-text common name (e.g. 'GRCh38') that is used to denote the sequence assembly.

`assembly_name`

*   is optional

*   Type: `string` ([Assembly common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_name")

#### assembly\_name Type

`string` ([Assembly common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-common-name.md))

#### assembly\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### assembly\_name Examples

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

### ncbi\_assembly\_accession

Assembly's identifier (e.g. GCF\_000001405.26) of the assembly. For example, the assembly accession for the GenBank version of the public human reference assembly (GRCh38.p14) is GCA\_000001405.29. See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbi_assembly_accession`

*   is optional

*   Type: `string` ([NCBI Assembly accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_accession")

#### ncbi\_assembly\_accession Type

`string` ([NCBI Assembly accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md))

all of

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-ncbi-assembly-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

#### ncbi\_assembly\_accession Examples

```json
"assembly:GCF_000001405.26"
```

```json
"assembly:GCA_000001405.1"
```

```json
"assembly:GCF_000005845.2"
```

### assembly\_unit\_name

A free-text common name (e.g. 'chr17') that is used to denote the sequence assembly unit.

`assembly_unit_name`

*   is optional

*   Type: `string` ([Assembly unit common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/assembly_unit_name")

#### assembly\_unit\_name Type

`string` ([Assembly unit common name](ega-12-definitions-ncbis-assembly-descriptor-properties-assembly-unit-common-name.md))

#### assembly\_unit\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### assembly\_unit\_name Examples

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

### ncbi\_assembly\_unit\_accession

NCBI's identifier (e.g. ) of the assembly unit. An assembly unit is defined as the collection of sequences used to define discrete parts of an assembly. Commonly assembly units are entire chromosomes (e.g. Chromosome 1 of human genome), scaffolds or different types of sequences (e.g. Mitochondrial DNA). For example, GenBank's accession: (1) for the assembly unit of the human chromosome 1 is [NC\_000001.11](https://www.ncbi.nlm.nih.gov/nuccore/NC_000001.11) (for the human reference assembly GRCh38.p14); (2) and for the complete mitochondrion genome of a human it is [NC\_012920.1](https://www.ncbi.nlm.nih.gov/nuccore/NC_012920.1). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbi_assembly_unit_accession`

*   is optional

*   Type: `string` ([NCBI Assembly unit accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_unit_accession")

#### ncbi\_assembly\_unit\_accession Type

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

#### ncbi\_assembly\_unit\_accession Examples

```json
"refseq:NC_000001.11"
```

```json
"refseq:NC_012920.1"
```

## Definitions group genomic\_sequence\_descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor"}
```

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                              |
| :------------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [assembly\_descriptor](#assembly_descriptor)      | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/assembly_descriptor")                                      |
| [sequence\_coordinates](#sequence_coordinates)    | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-sequence-coordinates.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/sequence_coordinates")                                          |
| [dna\_sequence\_strand](#dna_sequence_strand)     | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-dna-sequence-strand.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/dna_sequence_strand")                                            |
| [nucleic\_acid\_sequence](#nucleic_acid_sequence) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/nucleic_acid_sequence") |

### assembly\_descriptor

Node describing a sequence assembly referenced in [NCBI's Assembly database](https://www.ncbi.nlm.nih.gov/assembly). Assembly is a database providing information on the structure of assembled genomes, assembly names and other meta-data, statistical reports, and links to genomic sequence data. An assembly is defined as the set of chromosomes, unlocalized and unplaced (sometimes called 'random') and alternate sequences used to represent an organism's genome. Assemblies are constructed from 1 or more assembly units.

`assembly_descriptor`

*   is optional

*   Type: `object` ([NCBI's Assembly descriptor](ega-12-definitions-ncbis-assembly-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ncbis-assembly-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/assembly_descriptor")

#### assembly\_descriptor Type

`object` ([NCBI's Assembly descriptor](ega-12-definitions-ncbis-assembly-descriptor.md))

any of

*   [Or the Assembly accession is required](ega-12-definitions-ncbis-assembly-descriptor-anyof-or-the-assembly-accession-is-required.md "check type definition")

*   [Or the Assembly unit accession is required](ega-12-definitions-ncbis-assembly-descriptor-anyof-or-the-assembly-unit-accession-is-required.md "check type definition")

### sequence\_coordinates

A position in a map (for example a genetic map), either a single position (e.g. 71366222) or a region interval (e.g. 71366222-71532374). Used to define coordinates within an assembly unit.

`sequence_coordinates`

*   is optional

*   Type: `object` ([Sequence coordinates](ega-12-definitions-sequence-coordinates.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-sequence-coordinates.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/sequence_coordinates")

#### sequence\_coordinates Type

`object` ([Sequence coordinates](ega-12-definitions-sequence-coordinates.md))

any of

*   [Either a single position is given](ega-12-definitions-sequence-coordinates-anyof-either-a-single-position-is-given.md "check type definition")

*   [Or the whole sequence interval](ega-12-definitions-sequence-coordinates-anyof-or-the-whole-sequence-interval.md "check type definition")

### dna\_sequence\_strand

DNA sequence is double-stranded. By convention, for a reference chromosome, one whole strand is designated the 'forward strand' and the other the 'reverse strand'. This designation is arbitrary and sometimes the terms 'plus strand' and 'minus strand', respectively, are used instead. A genomic feature can live on a DNA strand in one of two orientations. For instance, a gene is said to have a coding strand (also known as its 'sense strand'), and a template strand (also known as its 'antisense strand'), which can be forward or reverse strands depending on which contain the nucleotide sequence the RNA polymerase reads to create its RNA product. Annotations such as Ensembl and UCSC are concerned with the coding sequences of genes, so when they say a gene is on the forward strand, it means the gene's coding sequence is on the forward strand. To follow through again, that means that during transcription of this forward-strand gene, the gene's template sequence is read from the reverse strand, producing an mRNA that matches the sequence on the forward strand. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`dna_sequence_strand`

*   is optional

*   Type: `string` ([DNA Sequence strand](ega-12-definitions-dna-sequence-strand.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-dna-sequence-strand.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/dna_sequence_strand")

#### dna\_sequence\_strand Type

`string` ([DNA Sequence strand](ega-12-definitions-dna-sequence-strand.md))

#### dna\_sequence\_strand Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation                                                                                                                                                                                                                                                                                              |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"forward"` | Forward strand \[ENSGLOSSARY:0000369]: DNA strand arbitrary defined as the strand with its 5' end at the tip of the short chromosome arm (p). If a gene is forward-stranded, its sense (sequence matching cDNA) is on the forward strand. Forward strand is reverse complementary to the reverse strand. |
| `"reverse"` | Reverse strand \[ENSGLOSSARY:0000370]: DNA strand arbitrary defined as the strand with its 5' end at the tip of the long chromosome arm (q). If a gene is reverse-stranded, its sense (sequence matching cDNA) is on the reverse strand. Reverse strand is reverse complementary to the forward strand.  |

### nucleic\_acid\_sequence

Sequence of characters representing a specific nucleic (i.e. molecular species - e.g. Adenine) or groupings of these (through ambiguity codes), using [one-letter IUPAC abbreviations](https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry#Amino_acid_and_nucleotide_base_codes).

`nucleic_acid_sequence`

*   is optional

*   Type: `string` ([Nucleic acid sequence](ega-12-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/nucleic_acid_sequence")

#### nucleic\_acid\_sequence Type

`string` ([Nucleic acid sequence](ega-12-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md))

#### nucleic\_acid\_sequence Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([\.-]*[ACGTURYKMSWBDHVNX]+[\.-]*)+$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B%5C.-%5D*%5BACGTURYKMSWBDHVNX%5D%2B%5B%5C.-%5D*\)%2B%24 "try regular expression with regexr.com")

#### nucleic\_acid\_sequence Examples

```json
"ACTGCCG"
```

```json
"CTGCGCGCGCT"
```

```json
"KM-AGT-X-N"
```

## Definitions group sequence\_coordinates

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates"}
```

| Property                                 | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :--------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [single\_position](#single_position)     | `number` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-single-sequence-position.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/single_position") |
| [sequence\_interval](#sequence_interval) | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval")      |

### single\_position

A single 1-based (first base of the assembly unit is 1, not 0) sequence coordinate, inclusive. It can be used to describe the start or end coordinates of a sequence interval, or directly a single coordinate within a sequence.

`single_position`

*   is optional

*   Type: `number` ([Single sequence position](ega-12-definitions-sequence-coordinates-properties-single-sequence-position.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-single-sequence-position.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/single_position")

#### single\_position Type

`number` ([Single sequence position](ega-12-definitions-sequence-coordinates-properties-single-sequence-position.md))

#### single\_position Examples

```json
71366222
```

```json
36592394
```

```json
1
```

### sequence\_interval

The location of a sequence feature in a genome, defined by its start (e.g. 71366222) and end (e.g. 71532374) position on some reference genomic coordinate system. Positions are always represented by contiguous spans using interbase coordinates or coordinate ranges. Both coordinates are inclusive: the sequence bounds are included in the described genomic feature. In other words, if the sequence interval is 71366222-71532374, both 71366222 and 71532374 coordinates are included in the feature.

`sequence_interval`

*   is optional

*   Type: `object` ([Sequence interval](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval")

#### sequence\_interval Type

`object` ([Sequence interval](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md))

## Definitions group dna\_sequence\_strand

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/dna_sequence_strand"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group nucleic\_acid\_sequence

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/nucleic_acid_sequence"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group single\_sequence\_position

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/single_sequence_position"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie\_general\_pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curie_general_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie\_refseq\_pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curie_refseq_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie\_hgnc\_symbol\_pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curie_hgnc_symbol_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie\_hgnc\_identifier\_pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curie_hgnc_identifier_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie\_ncbi\_gene\_identifier\_pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curie_ncbi_gene_identifier_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curie\_ncbi\_assembly\_pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curie_ncbi_assembly_pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group assay\_technology\_descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor"}
```

| Property                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                        |
| :-------------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [assay\_instrument](#assay_instrument)                    | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assays-instrument-category.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument")      |
| [assay\_instrument\_platform](#assay_instrument_platform) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assay-instrument-label.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument_platform") |

### assay\_instrument

The general categories (e.g. sequencers) in which assay instruments are categorized. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assay_instrument`

*   is required

*   Type: `string` ([Assay's instrument category](ega-12-definitions-assay-technology-properties-assays-instrument-category.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assays-instrument-category.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument")

#### assay\_instrument Type

`string` ([Assay's instrument category](ega-12-definitions-assay-technology-properties-assays-instrument-category.md))

#### assay\_instrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation                                                                                                                                                         |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"array"`     | \[EFO:0002698]\[Array instrument]\(http\://www\.ebi.ac.uk/efo/EFO\_0002698), an instrument which consists of nucleic acid or protein molecules bound to a substrate |
| `"sequencer"` | \[EFO:0003739]\[Sequencer instrument]\(http\://www\.ebi.ac.uk/efo/EFO\_0003739), an instrument that determines the order of nucleic acids in their sequences.       |

### assay\_instrument\_platform

Label (e.g. 'Illumina HiSeq 2500'), chosen from a list of controlled vocabulary (CV), of the technology used at the experiment. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assay_instrument_platform`

*   is required

*   Type: `string` ([Assay instrument label](ega-12-definitions-assay-technology-properties-assay-instrument-label.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-assay-technology-properties-assay-instrument-label.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assay_technology_descriptor/properties/assay_instrument_platform")

#### assay\_instrument\_platform Type

`string` ([Assay instrument label](ega-12-definitions-assay-technology-properties-assay-instrument-label.md))

#### assay\_instrument\_platform Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### assay\_instrument\_platform Examples

```json
"Illumina HiSeq 2500"
```

```json
"[HuGene-1_1-st] Affymetrix Human Gene 1.1 ST Array [probe set (exon) version]"
```

```json
"DNBSEQ-G400 FAST"
```

## Definitions group library\_layout

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/library_layout"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group spot\_descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group type\_of\_data

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/type_of_data"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group reference\_alignment\_details

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/reference_alignment_details"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group organism-part-entity

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism-part-entity"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group r-type-referenced\_by

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-referenced_by"}
```

| Property             | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                             |
| :------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type-1) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-referenced_by-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-referenced_by/properties/r_type") |

### r\_type



`r_type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-referenced_by-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-referenced_by/properties/r_type")

#### r\_type Type

unknown

#### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"referenced_by"
```

## Definitions group r-type-grouped\_with

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-grouped_with"}
```

| Property             | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                           |
| :------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type-2) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-grouped_with-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-grouped_with/properties/r_type") |

### r\_type



`r_type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-grouped_with-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-grouped_with/properties/r_type")

#### r\_type Type

unknown

#### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"grouped_with"
```

## Definitions group r-type-member\_of

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-member_of"}
```

| Property             | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                     |
| :------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type-3) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-member_of-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-member_of/properties/r_type") |

### r\_type



`r_type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-member_of-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-member_of/properties/r_type")

#### r\_type Type

unknown

#### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"member_of"
```

## Definitions group r-type-is\_after

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-is_after"}
```

| Property             | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                   |
| :------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type-4) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-is_after-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-is_after/properties/r_type") |

### r\_type



`r_type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-is_after-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-is_after/properties/r_type")

#### r\_type Type

unknown

#### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"is_after"
```

## Definitions group r-type-child\_of

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-child_of"}
```

| Property             | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                   |
| :------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type-5) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-child_of-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-child_of/properties/r_type") |

### r\_type



`r_type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-child_of-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-child_of/properties/r_type")

#### r\_type Type

unknown

#### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"child_of"
```

## Definitions group r-type-develops\_from

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-develops_from"}
```

| Property             | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                             |
| :------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type-6) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-develops_from-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-develops_from/properties/r_type") |

### r\_type



`r_type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-develops_from-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-develops_from/properties/r_type")

#### r\_type Type

unknown

#### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"develops_from"
```

## Definitions group r-type-family\_relationship\_with

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-family_relationship_with"}
```

| Property             | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                   |
| :------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type-7) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-family_relationship_with-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-family_relationship_with/properties/r_type") |

### r\_type



`r_type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-family_relationship_with-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-family_relationship_with/properties/r_type")

#### r\_type Type

unknown

#### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"family_relationship_with"
```

## Definitions group r-type-same\_as

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-same_as"}
```

| Property             | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                 |
| :------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_type](#r_type-8) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-type-same_as-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-same_as/properties/r_type") |

### r\_type



`r_type`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-type-same_as-properties-r_type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-type-same_as/properties/r_type")

#### r\_type Type

unknown

#### r\_type Constraints

**constant**: the value of this property must be equal to:

```json
"same_as"
```

## Definitions group r-target-policy

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-policy"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                       |
| :----------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-1) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-policy-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-policy/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-policy-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-policy/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-policy

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-policy"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                       |
| :----------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-1) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-policy-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-policy/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-policy-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-policy/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-DAC

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-DAC"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                 |
| :----------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-2) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-dac-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-DAC/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-dac-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-DAC/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-DAC

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-DAC"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                 |
| :----------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-2) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-dac-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-DAC/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-dac-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-DAC/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-dataset

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-dataset"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                         |
| :----------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-3) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-dataset-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-dataset/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-dataset-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-dataset/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-dataset

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-dataset"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                         |
| :----------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-3) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-dataset-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-dataset/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-dataset-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-dataset/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-analysis

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-analysis"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                           |
| :----------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-4) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-analysis-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-analysis/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-analysis-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-analysis/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-analysis

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-analysis"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                           |
| :----------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-4) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-analysis-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-analysis/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-analysis-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-analysis/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-sample

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-sample"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                       |
| :----------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-5) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-sample-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-sample/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-sample-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-sample/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-sample

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-sample"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                       |
| :----------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-5) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-sample-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-sample/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-sample-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-sample/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-experiment

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-experiment"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :----------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-6) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-experiment-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-experiment/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-experiment-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-experiment/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-experiment

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-experiment"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :----------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-6) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-experiment-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-experiment/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-experiment-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-experiment/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-source-individual

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-individual"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :----------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-7) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-individual-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-individual/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-individual-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-individual/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-individual

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-individual"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :----------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-7) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-individual-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-individual/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-individual-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-individual/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-protocol

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-protocol"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                           |
| :----------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-8) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-protocol-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-protocol/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-protocol-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-protocol/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-protocol

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-protocol"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                           |
| :----------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-8) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-protocol-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-protocol/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-protocol-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-protocol/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-submission

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-submission"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :----------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-9) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-submission-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-submission/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-submission-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-submission/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-submission

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-submission"}
```

| Property                 | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :----------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-9) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-submission-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-submission/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-submission-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-submission/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-external\_accession

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-external_accession"}
```

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                               |
| :------------------------ | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-10) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-external_accession-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-external_accession/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-external_accession-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-external_accession/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-external\_accession

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-external_accession"}
```

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                               |
| :------------------------ | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-10) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-external_accession-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-external_accession/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-external_accession-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-external_accession/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-external\_URL

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-external_URL"}
```

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                   |
| :------------------------ | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-11) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-external_url-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-external_URL/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-external_url-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-external_URL/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-external\_URL

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-external_URL"}
```

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                   |
| :------------------------ | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-11) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-external_url-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-external_URL/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-external_url-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-external_URL/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-study

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-study"}
```

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                     |
| :------------------------ | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-12) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-study-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-study/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-study-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-study/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-target-study

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-study"}
```

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                     |
| :------------------------ | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-12) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-study-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-study/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-study-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-study/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-target-assay

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-assay"}
```

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                     |
| :------------------------ | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_target](#r_target-13) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-target-assay-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-assay/properties/r_target") |

### r\_target



`r_target`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-target-assay-properties-r_target.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-target-assay/properties/r_target")

#### r\_target Type

unknown

## Definitions group r-source-assay

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-assay"}
```

| Property                  | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                     |
| :------------------------ | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r\_source](#r_source-13) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationship-source-assay-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-assay/properties/r_source") |

### r\_source



`r_source`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationship-source-assay-properties-r_source.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-source-assay/properties/r_source")

#### r\_source Type

unknown

## Definitions group r-constraint-one-sourced-submission

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/r-constraint-one-sourced-submission"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group url-uri-pattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/url-uri-pattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group individual-age

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/individual-age"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cell-type-descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor"}
```

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                            |
| :------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [cell\_type\_curie](#cell_type_curie) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor/properties/cell_type_curie") |
| [cell\_type\_label](#cell_type_label) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor/properties/cell_type_label")             |

### cell\_type\_curie



`cell_type_curie`

*   is optional

*   Type: `string` ([Compact URI (CURIE) of the cell type](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor/properties/cell_type_curie")

#### cell\_type\_curie Type

`string` ([Compact URI (CURIE) of the cell type](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-cell-type-properties-compact-uri-curie-of-the-cell-type-allof-compact-uri-curie-pattern.md "check type definition")

### cell\_type\_label



`cell_type_label`

*   is optional

*   Type: `string` ([Label of the cell type](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cell-type-descriptor/properties/cell_type_label")

#### cell\_type\_label Type

`string` ([Label of the cell type](ega-12-definitions-cell-type-properties-label-of-the-cell-type.md))

#### cell\_type\_label Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### cell\_type\_label Examples

```json
"musculo-skeletal system cell"
```

```json
"neoplastic cell"
```

```json
"nervous system cell"
```

## Definitions group phenotypic-abnormality-descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypic-abnormality-descriptor"}
```

| Property                                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                |
| :-------------------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [phenotypic\_abnormality\_curie](#phenotypic_abnormality_curie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypic-abnormality-descriptor/properties/phenotypic_abnormality_curie") |
| [phenotypic\_abnormality\_label](#phenotypic_abnormality_label) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-phenotypic-abnormality-properties-label-of-the-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypic-abnormality-descriptor/properties/phenotypic_abnormality_label")             |

### phenotypic\_abnormality\_curie



`phenotypic_abnormality_curie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypic-abnormality-descriptor/properties/phenotypic_abnormality_curie")

#### phenotypic\_abnormality\_curie Type

`string` ([Compact URI (CURIE) of the phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality.md))

any of

*   [Ontology validation of phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality-anyof-ontology-validation-of-phenotypic-abnormality.md "check type definition")

*   [In case the phenotypic abnormality is unknown or there is none](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality-anyof-in-case-the-phenotypic-abnormality-is-unknown-or-there-is-none.md "check type definition")

#### phenotypic\_abnormality\_curie Examples

```json
"HP:0003003"
```

```json
"HP:0010442"
```

```json
"HP:0002515"
```

```json
"NCIT:C17998"
```

```json
"NCIT:C94232"
```

### phenotypic\_abnormality\_label



`phenotypic_abnormality_label`

*   is optional

*   Type: `string` ([Label of the phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-label-of-the-phenotypic-abnormality.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-phenotypic-abnormality-properties-label-of-the-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypic-abnormality-descriptor/properties/phenotypic_abnormality_label")

#### phenotypic\_abnormality\_label Type

`string` ([Label of the phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-label-of-the-phenotypic-abnormality.md))

#### phenotypic\_abnormality\_label Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### phenotypic\_abnormality\_label Examples

```json
"Colon cancer"
```

```json
"Polydactyly"
```

```json
"Waddling gait"
```

```json
"Unknown"
```

```json
"Unaffected"
```

## Definitions group disease-descriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/disease-descriptor"}
```

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                    |
| :------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [disease\_curie](#disease_curie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/disease-descriptor/properties/disease_curie") |
| [disease\_label](#disease_label) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-disease-properties-label-of-the-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/disease-descriptor/properties/disease_label")             |

### disease\_curie



`disease_curie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the disease](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/disease-descriptor/properties/disease_curie")

#### disease\_curie Type

`string` ([Compact URI (CURIE) of the disease](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease.md))

one (and only one) of

*   [Ontology validation of dieases](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease-oneof-ontology-validation-of-dieases.md "check type definition")

*   [In case whether the individual has a disease is unknown or there is none](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease-oneof-in-case-whether-the-individual-has-a-disease-is-unknown-or-there-is-none.md "check type definition")

#### disease\_curie Examples

```json
"MONDO:0100096"
```

```json
"EFO:0003101"
```

```json
"NCIT:C17998"
```

```json
"NCIT:C94232"
```

### disease\_label



`disease_label`

*   is optional

*   Type: `string` ([Label of the disease](ega-12-definitions-disease-properties-label-of-the-disease.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-disease-properties-label-of-the-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/disease-descriptor/properties/disease_label")

#### disease\_label Type

`string` ([Label of the disease](ega-12-definitions-disease-properties-label-of-the-disease.md))

#### disease\_label Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### disease\_label Examples

```json
"COVID-19"
```

```json
"testicular seminoma"
```

```json
"Unknown"
```

```json
"Unaffected"
```
