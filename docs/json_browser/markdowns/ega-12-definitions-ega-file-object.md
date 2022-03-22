# EGA File object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment/properties/adf_files/items
```

Object containing the base metadata attributes of a file object in the EGA. These can inherited elsewhere with or without extending them.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## items Type

`object` ([EGA File object](ega-12-definitions-ega-file-object.md))

all of

*   any of

    *   [Checksum pattern check - MD5](ega-12-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5.md "check type definition")

    *   [Checksum pattern check - SHA-256](ega-12-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256.md "check type definition")

*   any of

    *   [CEL Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-cel-filename-pattern-check.md "check type definition")

    *   [TSV Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-tsv-filename-pattern-check.md "check type definition")

    *   [ADF Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-adf-filename-pattern-check.md "check type definition")

    *   [FASTQ Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-fastq-filename-pattern-check.md "check type definition")

    *   [FASTA Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-fasta-filename-pattern-check.md "check type definition")

    *   [SDRF Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-sdrf-filename-pattern-check.md "check type definition")

    *   [IDF Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-idf-filename-pattern-check.md "check type definition")

    *   [VCF Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-vcf-filename-pattern-check.md "check type definition")

    *   [SRA Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-sra-filename-pattern-check.md "check type definition")

    *   [SRF Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-srf-filename-pattern-check.md "check type definition")

    *   [SFF Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-sff-filename-pattern-check.md "check type definition")

    *   [BAM Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-bam-filename-pattern-check.md "check type definition")

    *   [CRAM Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-cram-filename-pattern-check.md "check type definition")

    *   [XLSX Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-xlsx-filename-pattern-check.md "check type definition")

    *   [CSV Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-csv-filename-pattern-check.md "check type definition")

    *   [BED Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-bed-filename-pattern-check.md "check type definition")

    *   [IDAT Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-idat-filename-pattern-check.md "check type definition")

    *   [MAP Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-map-filename-pattern-check.md "check type definition")

    *   [PED Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-ped-filename-pattern-check.md "check type definition")

    *   [BIM Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-bim-filename-pattern-check.md "check type definition")

    *   [FAM Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-fam-filename-pattern-check.md "check type definition")

    *   [TXT Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-txt-filename-pattern-check.md "check type definition")

    *   [EXP Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-exp-filename-pattern-check.md "check type definition")

    *   [GPR Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-gpr-filename-pattern-check.md "check type definition")

    *   [PY Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-py-filename-pattern-check.md "check type definition")

    *   [SH Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-sh-filename-pattern-check.md "check type definition")

# items Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :-------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filename](#filename)                         | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filename.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")                                                |
| [filetype](#filetype)                         | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")                                                |
| [checksum_method](#checksum_method)           | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-method-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")                               |
| [unencrypted_checksum](#unencrypted_checksum) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum") |
| [encrypted_checksum](#encrypted_checksum)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")     |

## filename

The full name of a file, including all of their file extensions (e.g. .gpg, .md5...), that identifies the file (e.g. 'my-bam-file.bam.gpg').

`filename`

*   is required

*   Type: `string` ([Filename](ega-12-definitions-ega-file-object-properties-filename.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filename.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")

### filename Type

`string` ([Filename](ega-12-definitions-ega-file-object-properties-filename.md))

### filename Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[^<>:;,?"*|]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22\*%7C%5D%2B%24 "try regular expression with regexr.com")

### filename Examples

```json
"my-bam-file.bam.gpg"
```

## filetype

The nature of the content stored in an electronic file. The string corresponds to the ID or name (e.g. FASTA or TSV), chosen from a list of controlled vocabulary (CV), associated with the given filetype. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`filetype`

*   is required

*   Type: `string` ([Filetype](ega-12-definitions-ega-file-object-properties-filetype.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")

### filetype Type

`string` ([Filetype](ega-12-definitions-ega-file-object-properties-filetype.md))

### filetype Constraints

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

## checksum_method

Node containing both the ID (MD5 or SHA-256), describing the method which yields the checksum from a data input for the purpose of detecting errors. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`checksum_method`

*   is required

*   Type: `string` ([Checksum method ID](ega-12-definitions-ega-file-object-properties-checksum-method-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-method-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")

### checksum_method Type

`string` ([Checksum method ID](ega-12-definitions-ega-file-object-properties-checksum-method-id.md))

### checksum_method Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"MD5"`     |             |
| `"SHA-256"` |             |

## unencrypted_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the unencrypted files.

`unencrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum")

### unencrypted_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-12-definitions-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md "check type definition")

### unencrypted_checksum Examples

```json
"46798b5cfca45c46a84b7419f8b74735"
```

## encrypted_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the encrypted files.

`encrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")

### encrypted_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-12-definitions-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md "check type definition")

### encrypted_checksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```
