# Check: allowed filetypes for an assay Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayFiletypes
```

This object exists with the only purpose of being a reference list of the allowed filetypes of an assay (e.g. if the filetype is 'PY', it should not be accepted as raw data). It imitates the 'filetype' property with a subset of the allowed filetypes.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## assayFiletypes Type

`object` ([Check: allowed filetypes for an assay](ega-4-definitions-check-allowed-filetypes-for-an-assay.md))

# assayFiletypes Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :-------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype](#filetype) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-allowed-filetypes-for-an-assay-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayFiletypes/properties/filetype") |

## filetype



`filetype`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-allowed-filetypes-for-an-assay-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayFiletypes/properties/filetype")

### filetype Type

`string`

### filetype Constraints

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
