# EGA File object Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment/properties/adf_files/items
```

Object containing the base metadata attributes of a file object in the EGA. These can inherited elsewhere with or without extending them.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

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

    *   [MD5 Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-md5-filename-pattern-check.md "check type definition")

    *   [HAP Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-hap-filename-pattern-check.md "check type definition")

    *   [CSFASTA Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-csfasta-filename-pattern-check.md "check type definition")

    *   [LOC Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-loc-filename-pattern-check.md "check type definition")

    *   [HTML Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-html-filename-pattern-check.md "check type definition")

    *   [HIC Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-hic-filename-pattern-check.md "check type definition")

    *   [MD Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-md-filename-pattern-check.md "check type definition")

    *   [MATLAB Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-matlab-filename-pattern-check.md "check type definition")

    *   [PERL Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-perl-filename-pattern-check.md "check type definition")

    *   [TIF Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-tif-filename-pattern-check.md "check type definition")

    *   [R Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-r-filename-pattern-check.md "check type definition")

    *   [SNP Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-snp-filename-pattern-check.md "check type definition")

    *   [XML Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-xml-filename-pattern-check.md "check type definition")

    *   [SVG Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-svg-filename-pattern-check.md "check type definition")

    *   [PNG Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-png-filename-pattern-check.md "check type definition")

    *   [JPG Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-jpg-filename-pattern-check.md "check type definition")

    *   [GTC Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-gtc-filename-pattern-check.md "check type definition")

    *   [HDF5 Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-hdf5-filename-pattern-check.md "check type definition")

    *   [FAST5 Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-fast5-filename-pattern-check.md "check type definition")

    *   [PAIR Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-pair-filename-pattern-check.md "check type definition")

    *   [TXT Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-txt-filename-pattern-check-1.md "check type definition")

    *   [BGI Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-bgi-filename-pattern-check.md "check type definition")

    *   [BGEN Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-bgen-filename-pattern-check.md "check type definition")

    *   [GEN Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-gen-filename-pattern-check.md "check type definition")

    *   [PXF Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-pxf-filename-pattern-check.md "check type definition")

    *   [LOOM Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-loom-filename-pattern-check.md "check type definition")

    *   [BAX.H5 Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-baxh5-filename-pattern-check.md "check type definition")

    *   [BAS.H5 Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-bash5-filename-pattern-check.md "check type definition")

    *   [ASM Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-asm-filename-pattern-check.md "check type definition")

    *   [CSI Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-csi-filename-pattern-check.md "check type definition")

    *   [TBI Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-tbi-filename-pattern-check.md "check type definition")

    *   [BCF Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-bcf-filename-pattern-check.md "check type definition")

    *   [qual454 Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-qual454-filename-pattern-check.md "check type definition")

    *   [qualsolid Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-qualsolid-filename-pattern-check.md "check type definition")

    *   [FASTQ-illumina Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-fastq-illumina-filename-pattern-check.md "check type definition")

    *   [FASTQ-helicos Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-fastq-helicos-filename-pattern-check.md "check type definition")

    *   [FASTQ-sanger Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-fastq-sanger-filename-pattern-check.md "check type definition")

    *   [FASTQ-solexa Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-fastq-solexa-filename-pattern-check.md "check type definition")

    *   [SAM Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-sam-filename-pattern-check.md "check type definition")

    *   [CRAI Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-crai-filename-pattern-check.md "check type definition")

    *   [BAI Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-bai-filename-pattern-check.md "check type definition")

    *   [MTX Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-mtx-filename-pattern-check.md "check type definition")

    *   [MEX Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-mex-filename-pattern-check.md "check type definition")

    *   [GMX Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-gmx-filename-pattern-check.md "check type definition")

    *   [GMT Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-gmt-filename-pattern-check.md "check type definition")

    *   [GRP Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-grp-filename-pattern-check.md "check type definition")

# items Properties

| Property                                                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                       |
| :------------------------------------------------------ | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filename](#filename)                                   | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filename.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")                                                |
| [file\_content](#file_content)                          | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/file_content")                                  |
| [filetype](#filetype)                                   | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")                                                |
| [checksum\_method](#checksum_method)                    | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-method-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")                               |
| [unencrypted\_checksum](#unencrypted_checksum)          | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum") |
| [encrypted\_checksum](#encrypted_checksum)              | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")     |
| [sequence\_quality\_details](#sequence_quality_details) | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details")                |

## filename

The full name of a file, including all of their file extensions (e.g. .gpg, .md5...), that identifies the file (e.g. 'my-bam-file.bam.gpg').

`filename`

*   is required

*   Type: `string` ([Filename](ega-12-definitions-ega-file-object-properties-filename.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filename.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filename")

### filename Type

`string` ([Filename](ega-12-definitions-ega-file-object-properties-filename.md))

### filename Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>:;,?"*|]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22*%7C%5D%2B%24 "try regular expression with regexr.com")

### filename Examples

```json
"my-bam-file.bam.gpg"
```

## file\_content

Array of file content items. This array exists to clarify what the purpose of a file, regardless of its format, may be. For example, a TXT formatted file could contain multiple types of data, from gene annotations to READMEs. Therefore, select the items from the used ontology that best describe the content of your file.

`file_content`

*   is optional

*   Type: `object[]` ([File content item](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-file-content-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/file_content")

### file\_content Type

`object[]` ([File content item](ega-12-definitions-ega-file-object-properties-file-content-array-file-content-item.md))

### file\_content Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## filetype

The main format in which data is structured and represented in an electronic file. It is normally defined by the file extension of the file (e.g. FASTQ for a '.fastq' file). The string corresponds to the ID or name (e.g. FASTA, TSV...), chosen from a list of controlled vocabulary (CV), associated with the given filetype. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`filetype`

*   is required

*   Type: `string` ([Filetype](ega-12-definitions-ega-file-object-properties-filetype.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype")

### filetype Type

`string` ([Filetype](ega-12-definitions-ega-file-object-properties-filetype.md))

### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation                                                                                                                                                                                                                         |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"CEL"`            | \[format:1638]                                                                                                                                                                                                                      |
| `"TSV"`            | \[format:3475]                                                                                                                                                                                                                      |
| `"FASTQ"`          | \[format:1930]                                                                                                                                                                                                                      |
| `"FASTA"`          | \[format:1929]                                                                                                                                                                                                                      |
| `"VCF"`            | \[format:3016]                                                                                                                                                                                                                      |
| `"SRA"`            | \[format:3698]                                                                                                                                                                                                                      |
| `"SRF"`            | \[format:3698]                                                                                                                                                                                                                      |
| `"SFF"`            | \[format:3284]                                                                                                                                                                                                                      |
| `"BAM"`            | \[format:2572]                                                                                                                                                                                                                      |
| `"CRAM"`           | \[format:3462]                                                                                                                                                                                                                      |
| `"XLSX"`           | \[format:3620]                                                                                                                                                                                                                      |
| `"CSV"`            | \[format:3752]                                                                                                                                                                                                                      |
| `"BED"`            | \[format:3003]                                                                                                                                                                                                                      |
| `"IDAT"`           | \[format:3578]                                                                                                                                                                                                                      |
| `"MAP"`            | \[format:3285]                                                                                                                                                                                                                      |
| `"PED"`            | \[format:3286]                                                                                                                                                                                                                      |
| `"BIM"`            | \[]                                                                                                                                                                                                                                 |
| `"FAM"`            | \[]                                                                                                                                                                                                                                 |
| `"TXT"`            | \[format:2330]                                                                                                                                                                                                                      |
| `"EXP"`            | \[format:1631]                                                                                                                                                                                                                      |
| `"GPR"`            | \[format:3829]                                                                                                                                                                                                                      |
| `"PY"`             | \[format:3996]                                                                                                                                                                                                                      |
| `"SH"`             | \[]                                                                                                                                                                                                                                 |
| `"ADF"`            | \[NCIT:C172213]                                                                                                                                                                                                                     |
| `"SDRF"`           | \[NCIT:C172211]                                                                                                                                                                                                                     |
| `"IDF"`            | \[NCIT:C172212]                                                                                                                                                                                                                     |
| `"MD5"`            | \[data:2190]                                                                                                                                                                                                                        |
| `"HAP"`            | \[]                                                                                                                                                                                                                                 |
| `"CSFASTA"`        | \[]                                                                                                                                                                                                                                 |
| `"LOC"`            | \[]                                                                                                                                                                                                                                 |
| `"HTML"`           | \[format:2331]                                                                                                                                                                                                                      |
| `"HIC"`            | \[]                                                                                                                                                                                                                                 |
| `"MD"`             | \[]                                                                                                                                                                                                                                 |
| `"MATLAB"`         | \[format:4007]                                                                                                                                                                                                                      |
| `"PERL"`           | \[format:3998]                                                                                                                                                                                                                      |
| `"TIF"`            | \[]                                                                                                                                                                                                                                 |
| `"R"`              | \[format:3999]                                                                                                                                                                                                                      |
| `"SNP"`            | \[]                                                                                                                                                                                                                                 |
| `"XML"`            | \[format:2332]                                                                                                                                                                                                                      |
| `"SVG"`            | \[format:3604]                                                                                                                                                                                                                      |
| `"PNG"`            | \[format:3603]                                                                                                                                                                                                                      |
| `"JPG"`            | \[format:3579]                                                                                                                                                                                                                      |
| `"GTC"`            | \[]: An Illumina-specific file containing called genotypes in AA/AB/BB format                                                                                                                                                       |
| `"HDF5"`           | \[format:3590]                                                                                                                                                                                                                      |
| `"FAST5"`          | \[]                                                                                                                                                                                                                                 |
| `"PAIR"`           | \[]                                                                                                                                                                                                                                 |
| `"TXT"`            | \[format:2330]                                                                                                                                                                                                                      |
| `"BGI"`            | \[]: Index file of a BGEN file                                                                                                                                                                                                      |
| `"BGEN"`           | \[]: Binary version of a GEN file                                                                                                                                                                                                   |
| `"GEN"`            | \[format:3812]                                                                                                                                                                                                                      |
| `"PXF"`            | \[]: A phenopacket. An open standard for sharing disease and phenotype information represented as PXF (Phenotype Exchange Format) files, which may be encoded in JSON or YAML.                                                      |
| `"LOOM"`           | \[format:3913]                                                                                                                                                                                                                      |
| `"BAX.H5"`         | \[]                                                                                                                                                                                                                                 |
| `"BAS.H5"`         | \[]                                                                                                                                                                                                                                 |
| `"ASM"`            | \[]: The files in the ASM directory describe and annotate the genome assembly with respect to the reference genome.                                                                                                                 |
| `"CSI"`            | \[]                                                                                                                                                                                                                                 |
| `"TBI"`            | \[format:3700]                                                                                                                                                                                                                      |
| `"BCF"`            | \[format:3020]                                                                                                                                                                                                                      |
| `"qual454"`        | \[format:3611]                                                                                                                                                                                                                      |
| `"qualsolid"`      | \[format:3610]                                                                                                                                                                                                                      |
| `"FASTQ-illumina"` | \[format:1931]                                                                                                                                                                                                                      |
| `"FASTQ-helicos"`  | \[]                                                                                                                                                                                                                                 |
| `"FASTQ-sanger"`   | \[format:1932]                                                                                                                                                                                                                      |
| `"FASTQ-solexa"`   | \[format:1933]                                                                                                                                                                                                                      |
| `"SAM"`            | \[format:2573]                                                                                                                                                                                                                      |
| `"CRAI"`           | \[]: CRAM indexing format                                                                                                                                                                                                           |
| `"BAI"`            | \[format:3327]                                                                                                                                                                                                                      |
| `"MTX"`            | \[format:3916]                                                                                                                                                                                                                      |
| `"MEX "`           | \[]: Market Exchange Format (MEX) for sparse matrices. It  contains a matrix (MTX) file, and also gzipped TSV files with feature and barcode sequences corresponding to row and column indices respectively. Feature-barcode matrix |
| `"GMX"`            | \[]                                                                                                                                                                                                                                 |
| `"GMT"`            | \[]                                                                                                                                                                                                                                 |
| `"GRP"`            | \[]                                                                                                                                                                                                                                 |

## checksum\_method

Node containing both the ID (MD5 or SHA-256), describing the method which yields the checksum from a data input for the purpose of detecting errors. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`checksum_method`

*   is required

*   Type: `string` ([Checksum method ID](ega-12-definitions-ega-file-object-properties-checksum-method-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-method-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method")

### checksum\_method Type

`string` ([Checksum method ID](ega-12-definitions-ega-file-object-properties-checksum-method-id.md))

### checksum\_method Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation     |
| :---------- | :-------------- |
| `"MD5"`     | \[NCIT:C171276] |
| `"SHA-256"` | \[NCIT:C80226]  |

## unencrypted\_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the unencrypted files.

`unencrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum")

### unencrypted\_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-12-definitions-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md "check type definition")

### unencrypted\_checksum Examples

```json
"46798b5cfca45c46a84b7419f8b74735"
```

## encrypted\_checksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the encrypted files.

`encrypted_checksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum")

### encrypted\_checksum Type

`string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-12-definitions-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md "check type definition")

### encrypted\_checksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```

## sequence\_quality\_details

Sequencing quality scores measure the probability that a base is called (i.e. sequenced) incorrectly. New sequencing technologies assign a quality score to each of the bases in the sequence.

`sequence_quality_details`

*   is optional

*   Type: `object` ([Sequence quality details](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details")

### sequence\_quality\_details Type

`object` ([Sequence quality details](ega-12-definitions-ega-file-object-properties-sequence-quality-details.md))
