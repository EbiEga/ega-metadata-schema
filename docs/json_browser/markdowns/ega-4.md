# EGA common metadata definitions Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json
```

Metadata schema used by the European Genome-phenome Archive (EGA) to store common definitions for other metadata objects. Basically, we are defining here common properties (e.g. instances' aliases) that other metadata objects (e.g. sample) may use. The way we refer to them is by using this object's '$id' field, referencing it in other files (with '$ref' and the relative path of the property - e.g. '$ref': '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId>'). See structuring documentation (<https://json-schema.org/understanding-json-schema/structuring.html>). Further details can be found in the EGA-metadata-schema GitHub repository (<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas>) and EGA-archive website (<https://ega-archive.org/>)

| Abstract               | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                         |
| :--------------------- | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------- |
| Cannot be instantiated | Yes        | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json](../../../schemas/EGA.common-definitions.json "open original schema") |

## EGA common metadata definitions Type

`object` ([EGA common metadata definitions](ega-4.md))

# EGA common metadata definitions Definitions

## Definitions group objectCoreId

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId"}
```

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                 |
| :---------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [alias](#alias)                           | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/alias")                     |
| [centerName](#centername)                 | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/centerName")      |
| [egaAccession](#egaaccession)             | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/egaAccession")    |
| [externalAccessions](#externalaccessions) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/externalAccessions") |

### alias

Submitter designated name (e.g. 'my\_sample\_J13') for the object (e.g. Sample). The name must be unique within the submission account (e.g. 'ega-box-79'), since the aliases and submission accounts are concatenated within our database to obtain the unique alias (e.g. 'ega-box-79::my\_sample\_J13').

`alias`

*   is optional

*   Type: `string` ([Alias of an object](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/alias")

#### alias Type

`string` ([Alias of an object](ega-4-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

#### alias Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### alias Examples

```json
"my_sample_J13"
```

### centerName

Center name (e.g. 'EBI-TEST') associated to the submitter. In other words, it is the acronym of the submitter's account (provided by the HelpDesk team).

`centerName`

*   is optional

*   Type: `string` ([Center name of the submitter](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/centerName")

#### centerName Type

`string` ([Center name of the submitter](ega-4-definitions-core-identifiers-of-an-object-properties-center-name-of-the-submitter.md))

#### centerName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### centerName Examples

```json
"EBI-TEST"
```

### egaAccession

The object accession (i.e. unique identifier) assigned by the archive (EGA). Object accessions can be found in the 'Identifiers' section of the EGA-archive website (<https://ega-archive.org/metadata/how-to-use-the-api>) and commonly start with EGA, followed by the distinctive letter of the object and finally the numeric ID of the instance.

`egaAccession`

*   is optional

*   Type: `string` ([EGA's accession of the object](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/egaAccession")

#### egaAccession Type

`string` ([EGA's accession of the object](ega-4-definitions-core-identifiers-of-an-object-properties-egas-accession-of-the-object.md))

#### egaAccession Examples

```json
"EGAN00003245489"
```

### externalAccessions

External accession node to reference objects in other archives (e.g. an already existing sample at BioSamples).

`externalAccessions`

*   is optional

*   Type: `object[]` ([Object External accession](ega-4-definitions-object-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-core-identifiers-of-an-object-properties-external-accessions-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectCoreId/properties/externalAccessions")

#### externalAccessions Type

`object[]` ([Object External accession](ega-4-definitions-object-external-accession.md))

#### externalAccessions Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## Definitions group customAttribute

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/customAttribute"}
```

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                           |
| :-------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tag](#tag)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/customAttribute/properties/tag")     |
| [value](#value) | Multiple | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/customAttribute/properties/value") |
| [units](#units) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/customAttribute/properties/units") |

### tag

The name of the attribute (e.g. 'Age').

`tag`

*   is required

*   Type: `string` ([Tag of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/customAttribute/properties/tag")

#### tag Type

`string` ([Tag of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md))

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

*   Type: any of the following: `string` or `number` ([Value of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/customAttribute/properties/value")

#### value Type

any of the following: `string` or `number` ([Value of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md))

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

*   Type: `string` ([Units of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/customAttribute/properties/units")

#### units Type

`string` ([Units of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md))

#### units Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### units Examples

```json
"years"
```

## Definitions group fileObject

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject"}
```

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                    |
| :------------------------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filename](#filename)                             | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-filename.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/filename")                                               |
| [fileContent](#filecontent)                       | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-file-content-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent")                                  |
| [filetype](#filetype)                             | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/filetype")                                               |
| [checksumMethod](#checksummethod)                 | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-method-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/checksumMethod")                               |
| [unencryptedChecksum](#unencryptedchecksum)       | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/unencryptedChecksum") |
| [encryptedChecksum](#encryptedchecksum)           | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/encryptedChecksum")     |
| [sequenceQualityDetails](#sequencequalitydetails) | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-sequence-quality-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails")                 |

### filename

The full name of a file, including all of their file extensions (e.g. .gpg, .md5...), that identifies the file (e.g. 'my-bam-file.bam.gpg').

`filename`

*   is required

*   Type: `string` ([Filename](ega-4-definitions-ega-file-object-properties-filename.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-filename.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/filename")

#### filename Type

`string` ([Filename](ega-4-definitions-ega-file-object-properties-filename.md))

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

### fileContent

Array of file content items. This array exists to clarify what the purpose of a file, regardless of its format, may be. For example, a TXT formatted file could contain multiple types of data, from gene annotations to READMEs. Therefore, select the items from the used ontology that best describe the content of your file.

`fileContent`

*   is optional

*   Type: `object[]` ([File content item](ega-4-definitions-ega-file-object-properties-file-content-array-file-content-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-file-content-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/fileContent")

#### fileContent Type

`object[]` ([File content item](ega-4-definitions-ega-file-object-properties-file-content-array-file-content-item.md))

#### fileContent Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### filetype

The main format in which data is structured and represented in an electronic file. It is normally defined by the file extension of the file (e.g. FASTQ for a '.fastq' file). The string corresponds to the ID or name (e.g. FASTA, TSV...), chosen from a list of controlled vocabulary (CV), associated with the given filetype. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`filetype`

*   is required

*   Type: `string` ([Filetype](ega-4-definitions-ega-file-object-properties-filetype.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/filetype")

#### filetype Type

`string` ([Filetype](ega-4-definitions-ega-file-object-properties-filetype.md))

#### filetype Constraints

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

### checksumMethod

Node containing both the ID (MD5 or SHA-256), describing the method which yields the checksum from a data input for the purpose of detecting errors. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`checksumMethod`

*   is required

*   Type: `string` ([Checksum method ID](ega-4-definitions-ega-file-object-properties-checksum-method-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-method-id.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/checksumMethod")

#### checksumMethod Type

`string` ([Checksum method ID](ega-4-definitions-ega-file-object-properties-checksum-method-id.md))

#### checksumMethod Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation     |
| :---------- | :-------------- |
| `"MD5"`     | \[NCIT:C171276] |
| `"SHA-256"` | \[NCIT:C80226]  |

### unencryptedChecksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the unencrypted files.

`unencryptedChecksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/unencryptedChecksum")

#### unencryptedChecksum Type

`string` ([Checksum \[NCIT:C43522\] of the unencrypted file](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

#### unencryptedChecksum Examples

```json
"46798b5cfca45c46a84b7419f8b74735"
```

### encryptedChecksum

A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data, computed from the encrypted files.

`encryptedChecksum`

*   is required

*   Type: `string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/encryptedChecksum")

#### encryptedChecksum Type

`string` ([Checksum \[NCIT:C43522\] of the encrypted file](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file.md))

one (and only one) of

*   [Checksum pattern obtained by MD5](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-md5.md "check type definition")

*   [Checksum pattern obtained by SHA-256](ega-4-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md "check type definition")

#### encryptedChecksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```

### sequenceQualityDetails

Sequencing quality scores measure the probability that a base is called (i.e. sequenced) incorrectly. New sequencing technologies assign a quality score to each of the bases in the sequence.

`sequenceQualityDetails`

*   is optional

*   Type: `object` ([Sequence quality details](ega-4-definitions-ega-file-object-properties-sequence-quality-details.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-file-object-properties-sequence-quality-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails")

#### sequenceQualityDetails Type

`object` ([Sequence quality details](ega-4-definitions-ega-file-object-properties-sequence-quality-details.md))

## Definitions group relationshipObject

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject"}
```

| Property            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-relationship-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rType")                 |
| [rSource](#rsource) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rSource")      |
| [rTarget](#rtarget) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rTarget")      |
| [rLabel](#rlabel)   | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rLabel") |

### rType

ID (e.g. sameAs) of the type of the relationship. To be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`rType`

*   is required

*   Type: `string` ([Relationship type](ega-4-definitions-ega-relationships-object-properties-relationship-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-relationship-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rType")

#### rType Type

`string` ([Relationship type](ega-4-definitions-ega-relationships-object-properties-relationship-type.md))

#### rType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                      | Explanation    |
| :------------------------- | :------------- |
| `"referencedBy"`           | \[SIO:000252]  |
| `"developsFrom"`           | \[RO:0002202]  |
| `"sameAs"`                 | \[NCIT:C64637] |
| `"memberOf"`               | \[RO:0002350]  |
| `"groupedWith"`            |                |
| `"familyRelationshipWith"` | \[EFO:0004424] |
| `"childOf"`                | \[GSSO:000728] |
| `"isAfter"`                | \[SIO:000211]  |
| `"publishedIn"`            | \[EFO:0001796] |
| `"submittedBy"`            | \[NCIT:C25695] |
| `"contactOf"`              | \[NCIT:C25461] |
| `"mainContactOf"`          |                |

#### rType Examples

```json
"referencedBy"
```

### rSource

Object reference of the relationship's source. In other words, the starting point of the relationship: in 'sample\_A developsFrom sample\_B' the source is 'sample\_A'.

`rSource`

*   is optional

*   Type: `object` ([Source of the relationship](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rSource")

#### rSource Type

`object` ([Source of the relationship](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-alias-and-centername-objectid-and-objecttype-check.md "check type definition")

        *   [External accession: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-external-accession-objectid-and-objecttype-check.md "check type definition")

        *   [Experiment: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-experiment-objectid-and-objecttype-check.md "check type definition")

        *   [Study: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-study-objectid-and-objecttype-check.md "check type definition")

        *   [Sample: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-sample-objectid-and-objecttype-check.md "check type definition")

        *   [Submission: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-submission-objectid-and-objecttype-check.md "check type definition")

        *   [Assay: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-assay-objectid-and-objecttype-check.md "check type definition")

        *   [Dataset: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dataset-objectid-and-objecttype-check.md "check type definition")

        *   [Analysis: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-analysis-objectid-and-objecttype-check.md "check type definition")

        *   [Policy: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-policy-objectid-and-objecttype-check.md "check type definition")

        *   [DAC: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dac-objectid-and-objecttype-check.md "check type definition")

        *   [Individual: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-individual-objectid-and-objecttype-check.md "check type definition")

        *   [Protocol: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-protocol-objectid-and-objecttype-check.md "check type definition")

### rTarget

Object reference of the relationship's target. In other words, the ending point of the relationship: in 'sample\_A developsFrom sample\_B' the target is 'sample\_B'.

`rTarget`

*   is optional

*   Type: `object` ([Target of the relationship](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rTarget")

#### rTarget Type

`object` ([Target of the relationship](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-alias-and-centername-objectid-and-objecttype-check.md "check type definition")

        *   [External accession: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-external-accession-objectid-and-objecttype-check.md "check type definition")

        *   [Experiment: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-experiment-objectid-and-objecttype-check.md "check type definition")

        *   [Study: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-study-objectid-and-objecttype-check.md "check type definition")

        *   [Sample: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-sample-objectid-and-objecttype-check.md "check type definition")

        *   [Submission: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-submission-objectid-and-objecttype-check.md "check type definition")

        *   [Assay: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-assay-objectid-and-objecttype-check.md "check type definition")

        *   [Dataset: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dataset-objectid-and-objecttype-check.md "check type definition")

        *   [Analysis: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-analysis-objectid-and-objecttype-check.md "check type definition")

        *   [Policy: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-policy-objectid-and-objecttype-check.md "check type definition")

        *   [DAC: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dac-objectid-and-objecttype-check.md "check type definition")

        *   [Individual: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-individual-objectid-and-objecttype-check.md "check type definition")

        *   [Protocol: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-protocol-objectid-and-objecttype-check.md "check type definition")

### rLabel

Custom free-form label of the relationship, used to add extra details of the relationship if needed.

`rLabel`

*   is optional

*   Type: `string` ([Custom label of the relationship](ega-4-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rLabel")

#### rLabel Type

`string` ([Custom label of the relationship](ega-4-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md))

#### rLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### rLabel Examples

```json
"Source individual is the third child of the target individual"
```

```json
"Grouped samples by colour of the medium"
```

```json
"Both samples are the same because of an error in the submission at..."
```

## Definitions group arrayLabel

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel"}
```

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :---------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [arrayLabelIdentifier](#arraylabelidentifier)   | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelIdentifier")   |
| [arrayLabelDescription](#arraylabeldescription) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelDescription") |

### arrayLabelIdentifier

The chosen term (e.g. 'Cy3 dye' \[CHEBI:37987]) needs to be a Chemical Entity from the CHEBI ontology, look for yours at: <https://www.ebi.ac.uk/ols/search?q=&ontology=chebi>

`arrayLabelIdentifier`

*   is optional

*   Type: `object` ([Array label identifier](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelIdentifier")

#### arrayLabelIdentifier Type

`object` ([Array label identifier](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-identifier.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

### arrayLabelDescription

Additional description of the used array label, indicating further details: context, purpose of the label, description of the label in the absence of an ontologized term, etcetera.

`arrayLabelDescription`

*   is optional

*   Type: `string` ([Array label description](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-description.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-description.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/arrayLabel/properties/arrayLabelDescription")

#### arrayLabelDescription Type

`string` ([Array label description](ega-4-definitions-repeatable-arraylabel-node-properties-array-label-description.md))

#### arrayLabelDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### arrayLabelDescription Examples

```json
"This label was used to dye the control samples"
```

```json
"This newly discovered label (yet to be added to an ontology) consists of a compound of type X..."
```

```json
"The label ID is unknown because we were given an already dyed kit..."
```

## Definitions group objectIdAndObjectTypeCheck

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectIdAndObjectTypeCheck"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group checksumPatternCheck

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group md5ChecksumPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/md5ChecksumPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group SHA256ChecksumPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/SHA256ChecksumPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGAExperimentIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGAExperimentIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGAStudyIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGAStudyIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGASampleIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGASampleIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGASubmissionIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGASubmissionIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGAAssayIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGAAssayIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGADatasetIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGADatasetIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGAAnalysisIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGAAnalysisIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGAPolicyIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGAPolicyIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGADACIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGADACIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGAIndividualIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGAIndividualIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGAProtocolIdPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGAProtocolIdPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGAISO8601DatePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGAISO8601DatePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group EGAISO8601DurationPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGAISO8601DurationPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group filenameFiletypePatternCheck

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filenameFiletypePatternCheck"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group assayFiletypes

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayFiletypes"}
```

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :---------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype](#filetype-1) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-allowed-filetypes-for-an-assay-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayFiletypes/properties/filetype") |

### filetype



`filetype`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-allowed-filetypes-for-an-assay-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayFiletypes/properties/filetype")

#### filetype Type

`string`

#### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value              | Explanation |
| :----------------- | :---------- |
| `"BAM"`            |             |
| `"CRAM"`           |             |
| `"SAM"`            |             |
| `"FASTA"`          |             |
| `"BAI"`            |             |
| `"CRAI"`           |             |
| `"CSI"`            |             |
| `"MD"`             |             |
| `"TXT"`            |             |
| `"XML"`            |             |
| `"MD5"`            |             |
| `"FASTQ"`          |             |
| `"FASTQ-helicos"`  |             |
| `"FASTQ-illumina"` |             |
| `"BAS.H5"`         |             |
| `"BAX.H5"`         |             |
| `"HDF5"`           |             |
| `"FASTQ-sanger"`   |             |
| `"FASTQ-solexa"`   |             |
| `"IDAT"`           |             |
| `"CEL"`            |             |
| `"qualsolid"`      |             |
| `"qual454"`        |             |
| `"SRA"`            |             |
| `"SRF"`            |             |
| `"SFF"`            |             |
| `"CSFASTA"`        |             |
| `"GPR"`            |             |
| `"ADF"`            |             |
| `"FAST5"`          |             |

## Definitions group celFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/celFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group tsvFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/tsvFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fastqFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fastqFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fastaFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fastaFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sdrfFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sdrfFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group idfFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/idfFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group vcfFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/vcfFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sraFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sraFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group srfFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/srfFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sffFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sffFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bamFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bamFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cramFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cramFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group xlsxFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/xlsxFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group csvFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/csvFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bedFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bedFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group idatFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/idatFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group mapFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/mapFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group pedFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/pedFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bimFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bimFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group famFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/famFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group txtFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/txtFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group expFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/expFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group gprFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gprFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group pyFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/pyFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group shFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/shFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group adfFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/adfFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group md5FileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/md5FileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group hapFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/hapFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group csfastaFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/csfastaFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group locFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group tgzFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/tgzFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group zipFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/zipFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group htmlFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/htmlFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group hicFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/hicFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group tifFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/tifFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group mdFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/mdFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group matlabFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/matlabFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group perlFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/perlFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group rFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group tarFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/tarFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group snpFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/snpFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group xmlFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/xmlFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group svgFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/svgFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group pngFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/pngFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group jpgFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/jpgFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group gtcFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gtcFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group hdf5FileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/hdf5FileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fast5FileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fast5FileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group pairFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/pairFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bgiFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bgiFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bgenFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bgenFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group genFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group pxfFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/pxfFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group loomFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/loomFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bax.h5FileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bax.h5FileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bas.h5FileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bas.h5FileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group asmFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/asmFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group csiFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/csiFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group tbiFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/tbiFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bcfFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/bcfFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group qual454FileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/qual454FileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group qualsolidFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/qualsolidFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fastqIlluminaFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fastqIlluminaFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fastqHelicosFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fastqHelicosFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fastqSangerFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fastqSangerFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fastqSolexaFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fastqSolexaFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group samFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/samFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group craiFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/craiFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group baiFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/baiFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group mtxFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/mtxFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group mexFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/mexFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group gmxFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gmxFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group gmtFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/gmtFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group grpFileFilenamePattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/grpFileFilenamePattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group objectExternalAccession

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession"}
```

| Property                                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                    |
| :------------------------------------------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectExternalAccessionIdentifier](#objectexternalaccessionidentifier)   | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionIdentifier")   |
| [objectExternalAccessionURI](#objectexternalaccessionuri)                 | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionURI")                 |
| [objectExternalAccessionDescription](#objectexternalaccessiondescription) | Multiple | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-description-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionDescription") |

### objectExternalAccessionIdentifier

Unique identifier of an external record. Its 'termId' (e.g. 'biosample:SAMEA7616999', 'pubmed:30962759', 'biostudies:S-EPMC3314381', etc.) shall follow CURIE format of `prefix`:`accession`, where: (1) the prefix (e.g. 'biosample') is unique and assigned to the external resource at identifiers.org; (2) and the unique accession of the object (e.g. SAMEA7616999) should resolve to an existing record within the resource. If in doubt, use identifiers.org to resolve your external accession: '<https://identifiers.org/>' + 'termId', e.g. '<https://identifiers.org/biosample:SAMEA7616999>'

`objectExternalAccessionIdentifier`

*   is optional

*   Type: `object` ([Identifier of the external accession](ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionIdentifier")

#### objectExternalAccessionIdentifier Type

`object` ([Identifier of the external accession](ega-4-definitions-object-external-accession-properties-identifier-of-the-external-accession.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

### objectExternalAccessionURI

Full or partial URL/URI of the external accession, for systems to resolve it. Should only be used in case identifiers.org does not contain a namespace for the required resource or the mapping to the URI from its identifier is faulty.

`objectExternalAccessionURI`

*   is optional

*   Type: `string` ([URI of the external accession](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionURI")

#### objectExternalAccessionURI Type

`string` ([URI of the external accession](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession.md))

all of

*   [URL/URI pattern](ega-4-definitions-object-external-accession-properties-uri-of-the-external-accession-allof-urluri-pattern.md "check type definition")

#### objectExternalAccessionURI Examples

```json
"https://www.ebi.ac.uk/biosamples/samples/SAMN11716999"
```

```json
"https://pubmed.ncbi.nlm.nih.gov/19491253"
```

```json
"https://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-1712/"
```

### objectExternalAccessionDescription

Optional description of the external accession, used to add context to the identifier if applicable.

`objectExternalAccessionDescription`

*   is optional

*   Type: any of the following: `string` or `number` ([Description of the external accession](ega-4-definitions-object-external-accession-properties-description-of-the-external-accession.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-object-external-accession-properties-description-of-the-external-accession.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/objectExternalAccession/properties/objectExternalAccessionDescription")

#### objectExternalAccessionDescription Type

any of the following: `string` or `number` ([Description of the external accession](ega-4-definitions-object-external-accession-properties-description-of-the-external-accession.md))

#### objectExternalAccessionDescription Examples

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

## Definitions group sampleLabelAssociation

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation"}
```

| Property                  | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                        |
| :------------------------ | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [arrayLabel](#arraylabel) | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/arrayLabel")                              |
| [objectId](#objectid)     | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/objectId") |

### arrayLabel

Chemical conjugated to nucleic acid/proteins to label them before microarray hybridisation. This node defines one single label, and thus should be repeated as an array where inherited if multiple labels are intended to be described.

`arrayLabel`

*   is required

*   Type: `object` ([Repeatable arrayLabel node](ega-4-definitions-repeatable-arraylabel-node.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/arrayLabel")

#### arrayLabel Type

`object` ([Repeatable arrayLabel node](ega-4-definitions-repeatable-arraylabel-node.md))

any of

*   [Untitled undefined type in EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-anyof-0.md "check type definition")

*   [Untitled undefined type in EGA common metadata definitions](ega-4-definitions-repeatable-arraylabel-node-anyof-1.md "check type definition")

### objectId



`objectId`

*   is required

*   Type: `object` ([Object's IDs block](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sampleLabelAssociation/properties/objectId")

#### objectId Type

`object` ([Object's IDs block](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

*   [Check that sample EGA ID (EGAN) pattern is correct](ega-4-definitions-repeatable-sample-label-node-properties-objects-ids-block-allof-check-that-sample-ega-id-egan-pattern-is-correct.md "check type definition")

## Definitions group oneRelationshipEnd

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd"}
```

| Property                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                     |
| :------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid-1)   | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd/properties/objectId")    |
| [objectType](#objecttype) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd/properties/objectType") |

### objectId

Node containing the main identifiers of the relationship's object (e.g. alias, centerName...), inherited from the common definitions (#/definitions/objectCoreId).

`objectId`

*   is required

*   Type: `object` ([Relationship's object's IDs block](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd/properties/objectId")

#### objectId Type

`object` ([Relationship's object's IDs block](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

### objectType

Type of the relationship's object, chosen from a list of CV (e.g. experiment, dataset, externalURL...). Both the source or target types can be: (1) the object tag of one of EGA's object (e.g. file, sample...); (2) an 'externalAccession'; (3) or an 'externalURL'. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`objectType`

*   is required

*   Type: `string` ([Type of the relationship's object](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd/properties/objectType")

#### objectType Type

`string` ([Type of the relationship's object](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

#### objectType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation                                                                                                                                                         |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"experiment"`        | Contains information about the experimental design of the sequencing                                                                                                |
| `"study"`             | Information about the study                                                                                                                                         |
| `"sample"`            | Information about the used samples                                                                                                                                  |
| `"individual"`        | Information about the participants (i.e. humans) of the study                                                                                                       |
| `"submission"`        | Information about the submission actions                                                                                                                            |
| `"assay"`             | Contains information about the specific assays (either sequencing or array assays) from the experiment                                                              |
| `"dataset"`           | Contains the collection of assay/analysis data files to be subject to controlled access                                                                             |
| `"analysis"`          | Contains the analysis metadata and data files                                                                                                                       |
| `"policy"`            | Contains information related to the Data Access Agreement (DAA) the dataset is subject to                                                                           |
| `"DAC"`               | Contains information about the Data Access Committee (DAC)                                                                                                          |
| `"protocol"`          | Contains information about a planned process.                                                                                                                       |
| `"externalAccession"` | An external accession among the ones Entrez (NCBI's text search) contemplates (search for the terms here: https\://www\.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?) |
| `"externalURL"`       | An external URL resource, of any type                                                                                                                               |

#### objectType Examples

```json
"sample"
```

## Definitions group subjectId

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/subjectId"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group biologicalSex

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/biologicalSex"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group organismDescriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor"}
```

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                       |
| :------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [organismTaxon](#organismtaxon) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/organismTaxon")              |
| [commonName](#commonname)       | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/commonName") |

### organismTaxon

Taxonomic classification of the organism (e.g. 'NCBITaxon:9606' and 'homo sapiens' for humans) curated by the NCBI Taxonomy (search for organisms here: <https://www.ncbi.nlm.nih.gov/taxonomy>; or use the OLS: <https://www.ebi.ac.uk/ols/ontologies/ncbitaxon>). You can find further details at '<https://www.uniprot.org/help/taxonomic_identifier>'. This is appropriate for individual organisms and some environmental samples.

`organismTaxon`

*   is required

*   Type: `object` ([NCBI Taxon of the organism](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/organismTaxon")

#### organismTaxon Type

`object` ([NCBI Taxon of the organism](ega-4-definitions-organism-obi0100026-descriptor-block-properties-ncbi-taxon-of-the-organism.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

### commonName

Common name (e.g. 'human') used to designate a plant, animal or other organism, as opposed to the scientific name.

`commonName`

*   is optional

*   Type: `string` ([Biologic entity classification common name](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/commonName")

#### commonName Type

`string` ([Biologic entity classification common name](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

#### commonName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### commonName Examples

```json
"human"
```

```json
"goat"
```

```json
"horse"
```

## Definitions group schemaDescriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor"}
```

| Property                                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                         |
| :-------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectType](#objecttype-1)                   | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/objectType")                                |
| [describedBySchemaUri](#describedbyschemauri) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/describedBySchemaUri")                       |
| [objectSchemaVersion](#objectschemaversion)   | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/objectSchemaVersion")            |
| [commonSchemaVersion](#commonschemaversion)   | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/commonSchemaVersion") |

### objectType

Type of the object (e.g. 'sample') the JSON document describes.

`objectType`

*   is required

*   Type: `string` ([Type of the object](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/objectType")

#### objectType Type

`string` ([Type of the object](ega-4-definitions-schema-descriptor-properties-type-of-the-object.md))

#### objectType Constraints

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

### describedBySchemaUri

URI of the schema (e.g. '<https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json>') that describes the JSON document (e.g. 'my\_sample.json')

`describedBySchemaUri`

*   is required

*   Type: `string` ([URI of the schema](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/describedBySchemaUri")

#### describedBySchemaUri Type

`string` ([URI of the schema](ega-4-definitions-schema-descriptor-properties-uri-of-the-schema.md))

#### describedBySchemaUri Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^https://github\.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA\..+\.json$
```

[try pattern](https://regexr.com/?expression=%5Ehttps%3A%2F%2Fgithub%5C.com%2FEbiEga%2Fega-metadata-schema%2Ftree%2Fmain%2Fschemas%2FEGA%5C..%2B%5C.json%24 "try regular expression with regexr.com")

#### describedBySchemaUri Examples

```json
"https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json"
```

### objectSchemaVersion

The version of the object's schema, the one specific for the object the JSON document corresponds to (e.g. 'EGA.sample.json'), not the common definitions schema's version (i.e. 'EGA.common-definitions.json').

`objectSchemaVersion`

*   is required

*   Type: `string` ([Version of the object's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/objectSchemaVersion")

#### objectSchemaVersion Type

`string` ([Version of the object's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema.md))

all of

*   [Semantic versioning pattern](ega-4-definitions-schema-descriptor-properties-version-of-the-objects-schema-allof-semantic-versioning-pattern.md "check type definition")

### commonSchemaVersion

The version of the common definition's schema, the one containing all shared definitions (i.e. 'EGA.common-definitions.json'), not the one specific to the object described by the JSON document (e.g. 'EGA.sample.json').

`commonSchemaVersion`

*   is required

*   Type: `string` ([Version of the common definition's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/schemaDescriptor/properties/commonSchemaVersion")

#### commonSchemaVersion Type

`string` ([Version of the common definition's schema](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema.md))

all of

*   [Semantic versioning pattern](ega-4-definitions-schema-descriptor-properties-version-of-the-common-definitions-schema-allof-semantic-versioning-pattern.md "check type definition")

## Definitions group semanticVersioningPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/semanticVersioningPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group contactDetails

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails"}
```

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                      |
| :---------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [individualFullName](#individualfullname) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-contact-details-properties-full-name-of-an-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/individualFullName") |
| [institutionName](#institutionname)       | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-contact-details-properties-institution-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/institutionName")              |
| [emailAddress](#emailaddress)             | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-contact-details-properties-email-address.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/emailAddress")                    |
| [phoneNumber](#phonenumber)               | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-contact-details-properties-phone-number.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/phoneNumber")                      |

### individualFullName

A full set of all personal names by which an individual is known and that can be recited as a word-group, with the understanding that, taken together, they all relate to that one individual. In case there are several, separate them with semicolons (;).

`individualFullName`

*   is optional

*   Type: `string` ([Full name of an individual](ega-4-definitions-contact-details-properties-full-name-of-an-individual.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-contact-details-properties-full-name-of-an-individual.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/individualFullName")

#### individualFullName Type

`string` ([Full name of an individual](ega-4-definitions-contact-details-properties-full-name-of-an-individual.md))

#### individualFullName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### individualFullName Examples

```json
"Wayne Jr., Bruce"
```

### institutionName

The full name of an institution the contact belongs to. In case there are several, separate them with semicolons (;).

`institutionName`

*   is optional

*   Type: `string` ([Institution name](ega-4-definitions-contact-details-properties-institution-name.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-contact-details-properties-institution-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/institutionName")

#### institutionName Type

`string` ([Institution name](ega-4-definitions-contact-details-properties-institution-name.md))

#### institutionName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### institutionName Examples

```json
"European Genome-phenome Archive (EGA)"
```

### emailAddress

Current email address that would be used in case the contact needs to be reached. Its expected format is of a local-part (e.g. 'myname'), followed by an 'at' sign (i.e. '@') and the domain of the address (e.g. 'gmail.com' or 'ebi.ac.uk').

`emailAddress`

*   is required

*   Type: `string` ([Email address](ega-4-definitions-contact-details-properties-email-address.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-contact-details-properties-email-address.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/emailAddress")

#### emailAddress Type

`string` ([Email address](ega-4-definitions-contact-details-properties-email-address.md))

#### emailAddress Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%40\(%5Ba-zA-Z0-9_%5C-%5C.%5D%2B\)%5C.\(%5Ba-zA-Z%5D%7B2%2C5%7D\)%24 "try regular expression with regexr.com")

#### emailAddress Examples

```json
"myname@ebi.ac.uk"
```

### phoneNumber

Current phone number that would be used in case the contact needs to be reached. Theoretically would only be used in case the email address was not provided, does not exist or is unresponsive.

`phoneNumber`

*   is optional

*   Type: `string` ([Phone number](ega-4-definitions-contact-details-properties-phone-number.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-contact-details-properties-phone-number.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/phoneNumber")

#### phoneNumber Type

`string` ([Phone number](ega-4-definitions-contact-details-properties-phone-number.md))

#### phoneNumber Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\+?\(?[0-9]{1,4}\)?[-\s\./0-9]+$
```

[try pattern](https://regexr.com/?expression=%5E%5C%2B%3F%5C\(%3F%5B0-9%5D%7B1%2C4%7D%5C\)%3F%5B-%5Cs%5C.%2F0-9%5D%2B%24 "try regular expression with regexr.com")

#### phoneNumber Examples

```json
"+44 7427512529"
```

## Definitions group studyDesignKeywords

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/studyDesignKeywords"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group locusIdentifier

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier"}
```

| Property                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                            |
| :---------------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [organismDescriptor](#organismdescriptor) | `object` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/organismDescriptor")       |
| [lociDescriptor](#locidescriptor)         | `array`  | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-locus-identifier-properties-loci-context-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor") |

### organismDescriptor

This property describes the material entity the sample consists in. That is, an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or, like humans, made up of many billions of cells divided into specialized tissues and organs. This node is of special interest in case the provenance of the sample is not human (e.g. microbiota taken from a donor). Unless stated otherwise, given the nature of the EGA, it is expected to be of human provenance.

`organismDescriptor`

*   is required

*   Type: `object` ([Organism \[OBI:0100026\] descriptor block](ega-4-definitions-organism-obi0100026-descriptor-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-organism-obi0100026-descriptor-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/organismDescriptor")

#### organismDescriptor Type

`object` ([Organism \[OBI:0100026\] descriptor block](ega-4-definitions-organism-obi0100026-descriptor-block.md))

### lociDescriptor

Array of locus context items. Multiple loci can be described in the array if the organism remains the same.

`lociDescriptor`

*   is required

*   Type: `object[]` ([Locus context item](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-locus-identifier-properties-loci-context-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/locusIdentifier/properties/lociDescriptor")

#### lociDescriptor Type

`object[]` ([Locus context item](ega-4-definitions-locus-identifier-properties-loci-context-array-locus-context-item.md))

#### lociDescriptor Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## Definitions group geneDescriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor"}
```

| Property                                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                       |
| :---------------------------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [geneIdentifier](#geneidentifier)                     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-gene-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdentifier")                                 |
| [geneDescription](#genedescription)                   | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneDescription")                        |
| [alternateGeneIdentifiers](#alternategeneidentifiers) | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIdentifiers")            |
| [relatedGeneIdentifiers](#relatedgeneidentifiers)     | `array`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/relatedGeneIdentifiers") |

### geneIdentifier

Property uniquely identifying a gene. It consists of a 'termId' and 'termLabel', which correspond to: (1)  'termId': A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol (e.g. HGNC:11535 for gene TAF1). There are 2 types of allowed databases to reference: NCBIGene and HGNC. Other archives' accessions (e.g. ensembl:ENSDARG00000035330) can be cross referenced with NCBIGene to obtain its gene ID (e.g. ncbigene:555452). (2) 'termLabel': the official gene symbol (e.g. 'TAF1'). It is typically derived from the gene name. There are several resources to search for a gene of interest, although we recommend [NCBI's service](https://www.ncbi.nlm.nih.gov/gene). For example: in the case of human genes, the symbol follows [HGNC](https://www.genenames.org/)'s nomenclature, while in the case of mice genes they are provided by [MGI](http://www.informatics.jax.org/).

`geneIdentifier`

*   is required

*   Type: `object` ([Gene identifier](ega-4-definitions-gene-descriptor-properties-gene-identifier.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-gene-identifier.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneIdentifier")

#### geneIdentifier Type

`object` ([Gene identifier](ega-4-definitions-gene-descriptor-properties-gene-identifier.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

### geneDescription

Free-text description of the gene, only to be used to provide additional context that would otherwise be impossible to add encoded in the schema. In other words, kindly refrain from providing alternative gene identifiers in the description, when they could be added at 'alternateGeneIdentifiers'.

`geneDescription`

*   is optional

*   Type: `string` ([Description of the gene](ega-4-definitions-gene-descriptor-properties-description-of-the-gene.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-description-of-the-gene.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/geneDescription")

#### geneDescription Type

`string` ([Description of the gene](ega-4-definitions-gene-descriptor-properties-description-of-the-gene.md))

#### geneDescription Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### geneDescription Examples

```json
"In the mutated cells, the only difference with the reference gene is that at locus ... position +23 was modified: thymine was transitioned to cytosine (T-C)..."
```

### alternateGeneIdentifiers

Array of alternate identifiers for this gene. This array can be used to provide any other alternate gene identifiers that refer to a gene, including previously approved gene symbols, Ensembl identifiers, gene transcripts (e.g. 'ensembl:ENST00000423759'), etcetera.

`alternateGeneIdentifiers`

*   is optional

*   Type: `object[]` ([Alternate gene identifier item](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers-alternate-gene-identifier-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/alternateGeneIdentifiers")

#### alternateGeneIdentifiers Type

`object[]` ([Alternate gene identifier item](ega-4-definitions-gene-descriptor-properties-alternate-gene-identifiers-alternate-gene-identifier-item.md))

#### alternateGeneIdentifiers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### relatedGeneIdentifiers

Array of related identifiers (e.g. termIds 'VGNC:97422', 'MGI:2385071', 'RGD:1305712' for gene ETF1). This field can be used to provide identifiers to resources representing related, but not equivalent gene identifiers. For example: paralog, analog or ortholog identifiers.

`relatedGeneIdentifiers`

*   is optional

*   Type: `object[]` ([Related gene identifier item](ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers-related-gene-identifier-item.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/geneDescriptor/properties/relatedGeneIdentifiers")

#### relatedGeneIdentifiers Type

`object[]` ([Related gene identifier item](ega-4-definitions-gene-descriptor-properties-related-not-equivalent-gene-identifiers-related-gene-identifier-item.md))

#### relatedGeneIdentifiers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## Definitions group ncbiAssemblyDescriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor"}
```

| Property                              | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                              |
| :------------------------------------ | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ncbiAssembly](#ncbiassembly)         | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssembly")          |
| [ncbiAssemblyUnit](#ncbiassemblyunit) | Merged | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssemblyUnit") |

### ncbiAssembly

Node defining an Assembly (e.g. 'GCF\_000001405.26'). For example, the assembly accession for the GenBank version of the public human reference assembly ('termLabel' being 'GRCh38.p14') is 'GCA\_000001405.29' ('termId'). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbiAssembly`

*   is required

*   Type: `object` ([NCBI Assembly](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssembly")

#### ncbiAssembly Type

`object` ([NCBI Assembly](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

### ncbiAssemblyUnit

NCBI's identifier of the assembly unit. An assembly unit is defined as the collection of sequences used to define discrete parts of an assembly. Commonly, assembly units are entire chromosomes (e.g. Chromosome 1 of human genome), scaffolds or different types of sequences (e.g. Mitochondrial DNA). Again, it follows an 'ontologyTerm' structure, having a 'termId' (e.g. 'refseq:NC\_000001.11') and 'termLabel' (e.g. 'chromosome 1'). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbiAssemblyUnit`

*   is optional

*   Type: `object` ([NCBI assembly unit](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssemblyUnit")

#### ncbiAssemblyUnit Type

`object` ([NCBI assembly unit](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

## Definitions group genomicSequenceDescriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor"}
```

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                         |
| :------------------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assemblyDescriptor](#assemblydescriptor)   | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/assemblyDescriptor")                                     |
| [sequenceCoordinates](#sequencecoordinates) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-sequence-coordinates.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/sequenceCoordinates")                                         |
| [dnaSequenceStrand](#dnasequencestrand)     | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-dna-sequence-strand.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/dnaSequenceStrand")                                            |
| [nucleicAcidSequence](#nucleicacidsequence) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/nucleicAcidSequence") |

### assemblyDescriptor

Node describing a sequence assembly referenced in [NCBI's Assembly database](https://www.ncbi.nlm.nih.gov/assembly). Assembly is a database providing information on the structure of assembled genomes, assembly names and other meta-data, statistical reports, and links to genomic sequence data. An assembly is defined as the set of chromosomes, unlocalized and unplaced (sometimes called 'random') and alternate sequences used to represent an organism's genome. Assemblies are constructed from 1 or more assembly units.

`assemblyDescriptor`

*   is optional

*   Type: `object` ([NCBI's Assembly descriptor](ega-4-definitions-ncbis-assembly-descriptor.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/assemblyDescriptor")

#### assemblyDescriptor Type

`object` ([NCBI's Assembly descriptor](ega-4-definitions-ncbis-assembly-descriptor.md))

### sequenceCoordinates

A position in a map (for example a genetic map), either a single position (e.g. 71366222) or a region interval (e.g. 71366222-71532374). Used to define coordinates within an assembly unit.

`sequenceCoordinates`

*   is optional

*   Type: `object` ([Sequence coordinates](ega-4-definitions-sequence-coordinates.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-sequence-coordinates.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/sequenceCoordinates")

#### sequenceCoordinates Type

`object` ([Sequence coordinates](ega-4-definitions-sequence-coordinates.md))

any of

*   [Either a single position is given](ega-4-definitions-sequence-coordinates-anyof-either-a-single-position-is-given.md "check type definition")

*   [Or the whole sequence interval](ega-4-definitions-sequence-coordinates-anyof-or-the-whole-sequence-interval.md "check type definition")

### dnaSequenceStrand

DNA sequence is double-stranded. By convention, for a reference chromosome, one whole strand is designated the 'forward strand' and the other the 'reverse strand'. This designation is arbitrary and sometimes the terms 'plus strand' and 'minus strand', respectively, are used instead. A genomic feature can live on a DNA strand in one of two orientations. For instance, a gene is said to have a coding strand (also known as its 'sense strand'), and a template strand (also known as its 'antisense strand'), which can be forward or reverse strands depending on which contain the nucleotide sequence the RNA polymerase reads to create its RNA product. Annotations such as Ensembl and UCSC are concerned with the coding sequences of genes, so when they say a gene is on the forward strand, it means the gene's coding sequence is on the forward strand. To follow through again, that means that during transcription of this forward-strand gene, the gene's template sequence is read from the reverse strand, producing an mRNA that matches the sequence on the forward strand. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`dnaSequenceStrand`

*   is optional

*   Type: `string` ([DNA Sequence strand](ega-4-definitions-dna-sequence-strand.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-dna-sequence-strand.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/dnaSequenceStrand")

#### dnaSequenceStrand Type

`string` ([DNA Sequence strand](ega-4-definitions-dna-sequence-strand.md))

#### dnaSequenceStrand Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation                                                                                                                                                                                                                                                                                              |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"forward"` | Forward strand \[ENSGLOSSARY:0000369]: DNA strand arbitrary defined as the strand with its 5' end at the tip of the short chromosome arm (p). If a gene is forward-stranded, its sense (sequence matching cDNA) is on the forward strand. Forward strand is reverse complementary to the reverse strand. |
| `"reverse"` | Reverse strand \[ENSGLOSSARY:0000370]: DNA strand arbitrary defined as the strand with its 5' end at the tip of the long chromosome arm (q). If a gene is reverse-stranded, its sense (sequence matching cDNA) is on the reverse strand. Reverse strand is reverse complementary to the forward strand.  |

### nucleicAcidSequence

Sequence of characters representing a specific nucleic (i.e. molecular species - e.g. Adenine) or groupings of these (through ambiguity codes), using [one-letter IUPAC abbreviations](https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry#Amino_acid_and_nucleotide_base_codes).

`nucleicAcidSequence`

*   is optional

*   Type: `string` ([Nucleic acid sequence](ega-4-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/genomicSequenceDescriptor/properties/nucleicAcidSequence")

#### nucleicAcidSequence Type

`string` ([Nucleic acid sequence](ega-4-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md))

#### nucleicAcidSequence Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([\.-]*[ACGTURYKMSWBDHVNX]+[\.-]*)+$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B%5C.-%5D*%5BACGTURYKMSWBDHVNX%5D%2B%5B%5C.-%5D*\)%2B%24 "try regular expression with regexr.com")

#### nucleicAcidSequence Examples

```json
"ACTGCCG"
```

```json
"CTGCGCGCGCT"
```

```json
"KM-AGT-X-N"
```

## Definitions group sequenceCoordinates

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates"}
```

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                          |
| :------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [singlePosition](#singleposition)     | `number` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-sequence-coordinates-properties-single-sequence-position.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/singlePosition") |
| [sequenceInterval](#sequenceinterval) | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-sequence-coordinates-properties-sequence-interval.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/sequenceInterval")      |

### singlePosition

A single 1-based (first base of the assembly unit is 1, not 0) sequence coordinate, inclusive. It can be used to describe the start or end coordinates of a sequence interval, or directly a single coordinate within a sequence.

`singlePosition`

*   is optional

*   Type: `number` ([Single sequence position](ega-4-definitions-sequence-coordinates-properties-single-sequence-position.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-sequence-coordinates-properties-single-sequence-position.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/singlePosition")

#### singlePosition Type

`number` ([Single sequence position](ega-4-definitions-sequence-coordinates-properties-single-sequence-position.md))

#### singlePosition Examples

```json
71366222
```

```json
36592394
```

```json
1
```

### sequenceInterval

The location of a sequence feature in a genome, defined by its start (e.g. 71366222) and end (e.g. 71532374) position on some reference genomic coordinate system. Positions are always represented by contiguous spans using interbase coordinates or coordinate ranges. Both coordinates are inclusive: the sequence bounds are included in the described genomic feature. In other words, if the sequence interval is 71366222-71532374, both 71366222 and 71532374 coordinates are included in the feature.

`sequenceInterval`

*   is optional

*   Type: `object` ([Sequence interval](ega-4-definitions-sequence-coordinates-properties-sequence-interval.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-sequence-coordinates-properties-sequence-interval.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/sequenceInterval")

#### sequenceInterval Type

`object` ([Sequence interval](ega-4-definitions-sequence-coordinates-properties-sequence-interval.md))

## Definitions group dnaSequenceStrand

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/dnaSequenceStrand"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group nucleicAcidSequence

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/nucleicAcidSequence"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group singleSequencePosition

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/singleSequencePosition"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curieGeneralPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieGeneralPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curieRefseqPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieRefseqPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curieHgncSymbolPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieHgncSymbolPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curieHgncIdentifierPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieHgncIdentifierPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curieNcbiGeneIdentifierPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieNcbiGeneIdentifierPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group curieNcbiAssemblyPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieNcbiAssemblyPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group assayTechnologyDescriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor"}
```

| Property                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                      |
| :-------------------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assayInstrument](#assayinstrument)                 | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-assay-technology-properties-assays-instrument-category.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor/properties/assayInstrument")        |
| [assayInstrumentPlatform](#assayinstrumentplatform) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-assay-technology-properties-assay-instrument-platform.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor/properties/assayInstrumentPlatform") |

### assayInstrument

The general categories (e.g. sequencer) in which assay instruments are categorized. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assayInstrument`

*   is required

*   Type: `string` ([Assay's instrument category](ega-4-definitions-assay-technology-properties-assays-instrument-category.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-assay-technology-properties-assays-instrument-category.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor/properties/assayInstrument")

#### assayInstrument Type

`string` ([Assay's instrument category](ega-4-definitions-assay-technology-properties-assays-instrument-category.md))

#### assayInstrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation                                                                                                                                                         |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"array"`     | \[EFO:0002698]\[Array instrument]\(http\://www\.ebi.ac.uk/efo/EFO\_0002698), an instrument which consists of nucleic acid or protein molecules bound to a substrate |
| `"sequencer"` | \[EFO:0003739]\[Sequencer instrument]\(http\://www\.ebi.ac.uk/efo/EFO\_0003739), an instrument that determines the order of nucleic acids in their sequences.       |

### assayInstrumentPlatform

Platform of the used instrument (e.g. 'Illumina HiSeq 2500'). Given the heterogenity in sequencing and array platforms (power of thousands), this property is not restricted by a CV list (i.e. it is free text).

`assayInstrumentPlatform`

*   is required

*   Type: `string` ([Assay instrument platform](ega-4-definitions-assay-technology-properties-assay-instrument-platform.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-assay-technology-properties-assay-instrument-platform.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor/properties/assayInstrumentPlatform")

#### assayInstrumentPlatform Type

`string` ([Assay instrument platform](ega-4-definitions-assay-technology-properties-assay-instrument-platform.md))

#### assayInstrumentPlatform Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### assayInstrumentPlatform Examples

```json
"Illumina HiSeq 2500"
```

```json
"[HuGene-1_1-st] Affymetrix Human Gene 1.1 ST Array [probe set (exon) version]"
```

```json
"DNBSEQ-G400 FAST"
```

## Definitions group libraryLayout

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/libraryLayout"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group spotDescriptor

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group typeOfData

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/typeOfData"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group referenceAlignmentDetails

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/referenceAlignmentDetails"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group materialAnatomicalEntity

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/materialAnatomicalEntity"}
```

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                  |
| :---------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-material-anatomical-entity-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/materialAnatomicalEntity/properties/termId") |

### termId



`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-4-definitions-material-anatomical-entity-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-material-anatomical-entity-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/materialAnatomicalEntity/properties/termId")

#### termId Type

unknown ([Ontology constraints for this specific termId](ega-4-definitions-material-anatomical-entity-properties-ontology-constraints-for-this-specific-termid.md))

#### termId Examples

```json
"UBERON:0000956"
```

```json
"UBERON:0006530"
```

## Definitions group rTypeReferencedBy

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeReferencedBy"}
```

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :---------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype-1) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-type-referencedby-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeReferencedBy/properties/rType") |

### rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-type-referencedby-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeReferencedBy/properties/rType")

#### rType Type

unknown

#### rType Constraints

**constant**: the value of this property must be equal to:

```json
"referencedBy"
```

## Definitions group rTypeGroupedWith

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeGroupedWith"}
```

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                    |
| :---------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rType](#rtype-2) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-type-groupedwith-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeGroupedWith/properties/rType") |

### rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-type-groupedwith-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeGroupedWith/properties/rType")

#### rType Type

unknown

#### rType Constraints

**constant**: the value of this property must be equal to:

```json
"groupedWith"
```

## Definitions group rTypeMemberOf

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeMemberOf"}
```

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                              |
| :---------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rType](#rtype-3) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-type-memberof-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeMemberOf/properties/rType") |

### rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-type-memberof-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeMemberOf/properties/rType")

#### rType Type

unknown

#### rType Constraints

**constant**: the value of this property must be equal to:

```json
"memberOf"
```

## Definitions group rTypeIsAfter

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeIsAfter"}
```

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                            |
| :---------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype-4) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-type-isafter-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeIsAfter/properties/rType") |

### rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-type-isafter-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeIsAfter/properties/rType")

#### rType Type

unknown

#### rType Constraints

**constant**: the value of this property must be equal to:

```json
"isAfter"
```

## Definitions group rTypeChildOf

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeChildOf"}
```

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                            |
| :---------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype-5) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-type-childof-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeChildOf/properties/rType") |

### rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-type-childof-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeChildOf/properties/rType")

#### rType Type

unknown

#### rType Constraints

**constant**: the value of this property must be equal to:

```json
"childOf"
```

## Definitions group rTypeDevelopsFrom

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeDevelopsFrom"}
```

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :---------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype-6) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-type-developsfrom-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeDevelopsFrom/properties/rType") |

### rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-type-developsfrom-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeDevelopsFrom/properties/rType")

#### rType Type

unknown

#### rType Constraints

**constant**: the value of this property must be equal to:

```json
"developsFrom"
```

## Definitions group rTypeFamilyRelationshipWith

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeFamilyRelationshipWith"}
```

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                          |
| :---------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype-7) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-type-familyrelationshipwith-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeFamilyRelationshipWith/properties/rType") |

### rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-type-familyrelationshipwith-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeFamilyRelationshipWith/properties/rType")

#### rType Type

unknown

#### rType Constraints

**constant**: the value of this property must be equal to:

```json
"familyRelationshipWith"
```

## Definitions group rTypeSameAs

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeSameAs"}
```

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                          |
| :---------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype-8) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-type-sameas-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeSameAs/properties/rType") |

### rType



`rType`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-type-sameas-properties-rtype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTypeSameAs/properties/rType")

#### rType Type

unknown

#### rType Constraints

**constant**: the value of this property must be equal to:

```json
"sameAs"
```

## Definitions group rTargetPolicy

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetPolicy"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                  |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rTarget](#rtarget-1) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-policy-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetPolicy/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-policy-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetPolicy/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourcePolicy

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourcePolicy"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                  |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rSource](#rsource-1) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-policy-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourcePolicy/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-policy-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourcePolicy/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetDAC

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetDAC"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                            |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rTarget](#rtarget-2) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-dac-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetDAC/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-dac-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetDAC/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceDAC

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceDAC"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                            |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rSource](#rsource-2) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-dac-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceDAC/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-dac-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceDAC/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetDataset

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetDataset"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                    |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rTarget](#rtarget-3) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-dataset-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetDataset/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-dataset-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetDataset/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceDataset

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceDataset"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                    |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rSource](#rsource-3) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-dataset-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceDataset/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-dataset-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceDataset/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetAnalysis

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetAnalysis"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :-------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rTarget](#rtarget-4) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-analysis-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetAnalysis/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-analysis-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetAnalysis/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceAnalysis

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceAnalysis"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :-------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rSource](#rsource-4) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-analysis-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceAnalysis/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-analysis-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceAnalysis/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetSample

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetSample"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                  |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rTarget](#rtarget-5) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-sample-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetSample/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-sample-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetSample/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceSample

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceSample"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                  |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rSource](#rsource-5) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-sample-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceSample/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-sample-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceSample/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetExperiment

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExperiment"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                          |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rTarget](#rtarget-6) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-experiment-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExperiment/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-experiment-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExperiment/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceExperiment

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExperiment"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                          |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rSource](#rsource-6) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-experiment-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExperiment/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-experiment-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExperiment/properties/rSource")

#### rSource Type

unknown

## Definitions group rSourceIndividual

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceIndividual"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                          |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rSource](#rsource-7) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-individual-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceIndividual/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-individual-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceIndividual/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetIndividual

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetIndividual"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                          |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rTarget](#rtarget-7) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-individual-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetIndividual/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-individual-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetIndividual/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceProtocol

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceProtocol"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :-------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rSource](#rsource-8) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-protocol-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceProtocol/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-protocol-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceProtocol/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetProtocol

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetProtocol"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :-------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rTarget](#rtarget-8) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-protocol-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetProtocol/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-protocol-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetProtocol/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceSubmission

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceSubmission"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                          |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rSource](#rsource-9) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-submission-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceSubmission/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-submission-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceSubmission/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetSubmission

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetSubmission"}
```

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                          |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rTarget](#rtarget-9) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-submission-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetSubmission/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-submission-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetSubmission/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceExternalAccession

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExternalAccession"}
```

| Property               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                        |
| :--------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rSource](#rsource-10) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-externalaccession-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExternalAccession/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-externalaccession-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExternalAccession/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetExternalAccession

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExternalAccession"}
```

| Property               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                        |
| :--------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rTarget](#rtarget-10) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-externalaccession-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExternalAccession/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-externalaccession-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExternalAccession/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceExternalURL

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExternalURL"}
```

| Property               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                            |
| :--------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rSource](#rsource-11) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-externalurl-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExternalURL/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-externalurl-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceExternalURL/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetExternalURL

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExternalURL"}
```

| Property               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                            |
| :--------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rTarget](#rtarget-11) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-externalurl-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExternalURL/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-externalurl-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetExternalURL/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceStudy

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceStudy"}
```

| Property               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :--------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rSource](#rsource-12) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-study-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceStudy/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-study-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceStudy/properties/rSource")

#### rSource Type

unknown

## Definitions group rTargetStudy

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetStudy"}
```

| Property               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :--------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rTarget](#rtarget-12) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-study-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetStudy/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-study-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetStudy/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rTargetAssay

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetAssay"}
```

| Property               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :--------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rTarget](#rtarget-13) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-target-assay-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetAssay/properties/rTarget") |

### rTarget



`rTarget`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-target-assay-properties-rtarget.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rTargetAssay/properties/rTarget")

#### rTarget Type

unknown

## Definitions group rSourceAssay

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceAssay"}
```

| Property               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :--------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rSource](#rsource-13) | Not specified | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationship-source-assay-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceAssay/properties/rSource") |

### rSource



`rSource`

*   is required

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationship-source-assay-properties-rsource.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rSourceAssay/properties/rSource")

#### rSource Type

unknown

## Definitions group rConstraintOneSourcedSubmission

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/rConstraintOneSourcedSubmission"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group urlUriPattern

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/urlUriPattern"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group individualAge

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/individualAge"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cellType

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellType"}
```

| Property            | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :------------------ | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid-1) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-cell-type-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellType/properties/termId") |

### termId



`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-4-definitions-cell-type-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-cell-type-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/cellType/properties/termId")

#### termId Type

unknown ([Ontology constraints for this specific termId](ega-4-definitions-cell-type-properties-ontology-constraints-for-this-specific-termid.md))

#### termId Examples

```json
"CL:0002092"
```

```json
"CL:0000127"
```

```json
"CL:0000128"
```

## Definitions group phenotypicAbnormality

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormality"}
```

| Property            | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                           |
| :------------------ | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid-2) | Merged | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormality/properties/termId") |

### termId



`termId`

*   is optional

*   Type: merged type ([Ontology constraints for this specific termId](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormality/properties/termId")

#### termId Type

merged type ([Ontology constraints for this specific termId](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid.md))

any of

*   [Ontology validation of phenotypic abnormality](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-phenotypic-abnormality.md "check type definition")

*   [In case the phenotypic abnormality is unknown or there is none](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid-anyof-in-case-the-phenotypic-abnormality-is-unknown-or-there-is-none.md "check type definition")

#### termId Examples

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

## Definitions group disease

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/disease"}
```

| Property            | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                              |
| :------------------ | :----- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid-3) | Merged | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-disease-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/disease/properties/termId") |

### termId



`termId`

*   is optional

*   Type: merged type ([Ontology constraints for this specific termId](ega-4-definitions-disease-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-disease-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/disease/properties/termId")

#### termId Type

merged type ([Ontology constraints for this specific termId](ega-4-definitions-disease-properties-ontology-constraints-for-this-specific-termid.md))

any of

*   [Ontology validation of 'disease' - EFO](ega-4-definitions-disease-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-disease---efo.md "check type definition")

*   [Ontology validation of 'disease' - ORDO](ega-4-definitions-disease-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-disease---ordo.md "check type definition")

*   [Ontology validation of 'human disease or disorder' - MONDO](ega-4-definitions-disease-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-human-disease-or-disorder---mondo.md "check type definition")

*   [In case the phenotypic abnormality is unknown or there is none](ega-4-definitions-disease-properties-ontology-constraints-for-this-specific-termid-anyof-in-case-the-phenotypic-abnormality-is-unknown-or-there-is-none.md "check type definition")

#### termId Examples

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

## Definitions group ontologyTerm

Reference this group by using

```json
{"$ref":"https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm"}
```

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :---------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid-4)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ontology-term-properties-id-of-the-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termId")       |
| [termLabel](#termlabel) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ontology-term-properties-label-of-the-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termLabel") |

### termId

The identifier of an ontology term must be in CURIE format (check property 'curieGeneralPattern'). Whether a specific term is valid or not according to an ontology hierarchy is checked at each specific termId using ontology validation keywords (e.g. 'graphRestriction').

`termId`

*   is required

*   Type: `string` ([ID of the term](ega-4-definitions-ontology-term-properties-id-of-the-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ontology-term-properties-id-of-the-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termId")

#### termId Type

`string` ([ID of the term](ega-4-definitions-ontology-term-properties-id-of-the-term.md))

all of

*   [Compact URI (CURIE) pattern](ega-4-definitions-ontology-term-properties-id-of-the-term-allof-compact-uri-curie-pattern.md "check type definition")

#### termId Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### termId Examples

```json
"MONDO:0100096"
```

```json
"EFO:0003101"
```

```json
"EFO:0005518"
```

```json
"EFO:0002944"
```

```json
"EFO:0003813"
```

### termLabel

The label of a term is the human-readable string associated with the identifier. It is not required that it matches the label of the termId within the referenced ontology, although it should. This is due to the fact that the source of truth will always be the termId, and not the label, which adds more context.

`termLabel`

*   is required

*   Type: `string` ([Label of the term](ega-4-definitions-ontology-term-properties-label-of-the-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ontology-term-properties-label-of-the-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termLabel")

#### termLabel Type

`string` ([Label of the term](ega-4-definitions-ontology-term-properties-label-of-the-term.md))

#### termLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

#### termLabel Examples

```json
"COVID-19"
```

```json
"Axila skin"
```

```json
"bone marrow cell"
```

```json
"astrocyte"
```

```json
"oligodendrocyte"
```

```json
"Unknown"
```

```json
"Unaffected"
```

```json
"homo sapiens"
```
