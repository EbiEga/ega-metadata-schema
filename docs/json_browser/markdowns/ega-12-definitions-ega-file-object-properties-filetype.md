# Filetype Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype
```

The nature of the content stored in an electronic file. The string corresponds to the ID or name (e.g. FASTA or TSV), chosen from a list of controlled vocabulary (CV), associated with the given filetype. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## filetype Type

`string` ([Filetype](ega-12-definitions-ega-file-object-properties-filetype.md))

## filetype Constraints

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
