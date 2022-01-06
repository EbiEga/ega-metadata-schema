# Filetype \[NCIT:C172272] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype
```

The nature of the content stored in an electronic file. Contains up to two properties, the name (e.g. CEL or TSV) and the CURIE (e.g. EFO:0005630 or NCIT:C164049), chosen from a list of CVs.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## filetype Type

`object` ([Filetype \[NCIT:C172272\]](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272.md))

# filetype Properties

| Property                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                             |
| :-------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype_id](#filetype_id)       | `string` | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype/properties/filetype_id")       |
| [filetype_curie](#filetype_curie) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype/properties/filetype_curie") |

## filetype_id

The ID or name (e.g. FASTA or TSV) associated with the given filetype.

`filetype_id`

*   is required

*   Type: `string` ([Filetype ID](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype/properties/filetype_id")

### filetype_id Type

`string` ([Filetype ID](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-id.md))

### filetype_id Constraints

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

### filetype_id Examples

```json
"TSV"
```

## filetype_curie

The CURIE (i.e. ontologized term - e.g. NCIT:C47845 or NCIT:C164049) associated with the given filetype.

`filetype_curie`

*   is optional

*   Type: `string` ([Filetype CURIE](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype/properties/filetype_curie")

### filetype_curie Type

`string` ([Filetype CURIE](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-curie.md))

### filetype_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"EFO:0005630"`  |             |
| `"NCIT:C164049"` |             |
| `"NCIT:C172213"` |             |
| `"EFO:0004155"`  |             |
| `"NCIT:C47845"`  |             |
| `"NCIT:C172211"` |             |
| `"NCIT:C172212"` |             |
| `"NCIT:C172216"` |             |
| `"format:3698"`  |             |
| `"EFO:0004154"`  |             |
| `"EFO:0004156"`  |             |
| `"EFO:0004157"`  |             |
| `"format:3462"`  |             |
| `"format:3620"`  |             |
| `"format:3752"`  |             |
| `"format:3003"`  |             |
| `"format:3578"`  |             |
| `"format:3285"`  |             |
| `"format:3286"`  |             |

### filetype_curie Examples

```json
"NCIT:C164049"
```
