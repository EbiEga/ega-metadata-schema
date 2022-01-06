# EGA File object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object
```

Object containing the base metadata attributes of a file object in the EGA. These can inherited elsewhere with or without extending them.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## file_object Type

`object` ([EGA File object](ega-2-definitions-ega-file-object.md))

all of

*   any of

    *   [Checksum pattern check - MD5](ega-2-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5.md "check type definition")

    *   [Checksum pattern check - SHA-256](ega-2-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256.md "check type definition")

*   any of

    *   [CEL Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-cel-filename-pattern-check.md "check type definition")

    *   [TSV Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-tsv-filename-pattern-check.md "check type definition")

    *   [ADF Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-adf-filename-pattern-check.md "check type definition")

    *   [FASTQ Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-fastq-filename-pattern-check.md "check type definition")

    *   [FASTA Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-fasta-filename-pattern-check.md "check type definition")

    *   [SDRF Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-sdrf-filename-pattern-check.md "check type definition")

    *   [IDF Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-idf-filename-pattern-check.md "check type definition")

    *   [VCF Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-vcf-filename-pattern-check.md "check type definition")

    *   [SRA Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-sra-filename-pattern-check.md "check type definition")

    *   [SRF Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-srf-filename-pattern-check.md "check type definition")

    *   [SFF Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-sff-filename-pattern-check.md "check type definition")

    *   [BAM Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-bam-filename-pattern-check.md "check type definition")

    *   [CRAM Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-cram-filename-pattern-check.md "check type definition")

    *   [XLSX Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-xlsx-filename-pattern-check.md "check type definition")

    *   [CSV Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-csv-filename-pattern-check.md "check type definition")

    *   [BED Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-bed-filename-pattern-check.md "check type definition")

    *   [IDAT Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-idat-filename-pattern-check.md "check type definition")

    *   [MAP Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-map-filename-pattern-check.md "check type definition")

    *   [PED Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-ped-filename-pattern-check.md "check type definition")

    *   [BIM Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-bim-filename-pattern-check.md "check type definition")

    *   [FAM Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-fam-filename-pattern-check.md "check type definition")

# file_object Properties

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                            |
| :-------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [filename](#filename)                         | `string` | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-filename-data1050.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")                                       |
| [filetype](#filetype)                         | `object` | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")                                    |
| [checksum_method](#checksum_method)           | `object` | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")                |
| [unencrypted_checksum](#unencrypted_checksum) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum") |
| [encrypted_checksum](#encrypted_checksum)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")     |

## filename

The full name of a file, including all of their file extensions (e.g. .gpg, .md5...), that identifies the file (e.g. 'my-bam-file.bam.gpg').

`filename`

*   is required

*   Type: `string` ([Filename \[data:1050\]](ega-2-definitions-ega-file-object-properties-filename-data1050.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-filename-data1050.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")

### filename Type

`string` ([Filename \[data:1050\]](ega-2-definitions-ega-file-object-properties-filename-data1050.md))

### filename Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[^<>:;,?"*|/]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22\*%7C%2F%5D%2B%24 "try regular expression with regexr.com")

### filename Examples

```json
"my-bam-file.bam.gpg"
```

## filetype

The nature of the content stored in an electronic file. Contains up to two properties, the name (e.g. CEL or TSV) and the CURIE (e.g. EFO:0005630 or NCIT:C164049), chosen from a list of CVs.

`filetype`

*   is required

*   Type: `object` ([Filetype \[NCIT:C172272\]](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")

### filetype Type

`object` ([Filetype \[NCIT:C172272\]](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272.md))

## checksum_method

Node containing both the ID (MD5 or SHA-256) and the CURIE (NCIT:C171276 or NCIT:C80226), describing the method which yields the checksum from a data input for the purpose of detecting errors.

`checksum_method`

*   is required

*   Type: `object` ([Checksum method \[ChecksumAlgorithm\]](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")

### checksum_method Type

`object` ([Checksum method \[ChecksumAlgorithm\]](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md))

## unencrypted_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the unencrypted files.

`unencrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum")

### unencrypted_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

### unencrypted_checksum Examples

```json
"46798b5cfca45c46a84b7419f8b74735"
```

## encrypted_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the encrypted files.

`encrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")

### encrypted_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-2-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

### encrypted_checksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```
