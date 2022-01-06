# CRAM Filename pattern-check Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/12
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## 12 Type

unknown ([CRAM Filename pattern-check](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-cram-filename-pattern-check.md))

# 12 Properties

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                               |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype](#filetype) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-cram-filename-pattern-check-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/12/properties/filetype")                        |
| [filename](#filename) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-cram-filename-pattern-check-properties-filename-pattern-of-a-cram-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/12/properties/filename") |

## filetype



`filetype`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-cram-filename-pattern-check-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/12/properties/filetype")

### filetype Type

unknown

## filename

This object exists to hold the filename pattern that a 'CRAM' filetype_id would have, for it to be referenced elsewhere within this (or other) JSON schema.

`filename`

*   is optional

*   Type: `string` ([Filename pattern of a CRAM file](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-cram-filename-pattern-check-properties-filename-pattern-of-a-cram-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-cram-filename-pattern-check-properties-filename-pattern-of-a-cram-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/12/properties/filename")

### filename Type

`string` ([Filename pattern of a CRAM file](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-cram-filename-pattern-check-properties-filename-pattern-of-a-cram-file.md))

### filename Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[^<>:;,?"*|/]+\.cram(.gz|.zip|.rar|.arj|.tar|.7z)?(.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22\*%7C%2F%5D%2B%5C.cram\(.gz%7C.zip%7C.rar%7C.arj%7C.tar%7C.7z\)%3F\(.gpg\)%3F%24 "try regular expression with regexr.com")

### filename Examples

```json
"my_file1.cram.gz.gpg"
```
