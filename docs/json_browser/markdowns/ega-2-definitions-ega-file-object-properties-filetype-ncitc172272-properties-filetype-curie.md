# Filetype CURIE Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/filetype/properties/filetype_curie
```

The CURIE (i.e. ontologized term - e.g. NCIT:C47845 or NCIT:C164049) associated with the given filetype.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## filetype_curie Type

`string` ([Filetype CURIE](ega-2-definitions-ega-file-object-properties-filetype-ncitc172272-properties-filetype-curie.md))

## filetype_curie Constraints

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

## filetype_curie Examples

```json
"NCIT:C164049"
```
