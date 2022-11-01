# TXT Filename pattern-check Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/21
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 21 Type

unknown ([TXT Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-txt-filename-pattern-check.md))

# 21 Properties

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype](#filetype) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-txt-filename-pattern-check-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/21/properties/filetype")                       |
| [filename](#filename) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-txt-filename-pattern-check-properties-filename-pattern-of-a-txt-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/21/properties/filename") |

## filetype



`filetype`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-txt-filename-pattern-check-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/21/properties/filetype")

### filetype Type

unknown

### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"TXT"` |             |

## filename

This object exists to hold the filename pattern that a 'TXT' filetype\_id would have, for it to be referenced elsewhere within this (or other) JSON schema.

`filename`

*   is optional

*   Type: `string` ([Filename pattern of a TXT file](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-txt-filename-pattern-check-properties-filename-pattern-of-a-txt-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-txt-filename-pattern-check-properties-filename-pattern-of-a-txt-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/21/properties/filename")

### filename Type

`string` ([Filename pattern of a TXT file](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-txt-filename-pattern-check-properties-filename-pattern-of-a-txt-file.md))

### filename Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>:;,?"*|/]+\.(txt|TXT)(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22*%7C%2F%5D%2B%5C.\(txt%7CTXT\)\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

### filename Examples

```json
"my_file1.txt.gz.gpg"
```
