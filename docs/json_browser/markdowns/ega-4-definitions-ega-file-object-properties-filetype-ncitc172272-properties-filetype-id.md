# Filetype ID Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype/properties/filetype_id
```

The ID or name (e.g. FASTA or TSV) associated with the given filetype.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## filetype_id Type

`string` ([Filetype ID](ega-4-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-id.md))

## filetype_id Constraints

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

## filetype_id Examples

```json
"TSV"
```
