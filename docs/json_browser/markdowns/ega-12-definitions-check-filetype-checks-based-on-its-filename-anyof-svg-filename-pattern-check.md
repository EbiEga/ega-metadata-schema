# SVG Filename pattern-check Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/39
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 39 Type

unknown ([SVG Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-svg-filename-pattern-check.md))

# 39 Properties

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype](#filetype) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-svg-filename-pattern-check-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/39/properties/filetype")                       |
| [filename](#filename) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-svg-filename-pattern-check-properties-filename-pattern-of-a-svg-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/39/properties/filename") |

## filetype



`filetype`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-svg-filename-pattern-check-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/39/properties/filetype")

### filetype Type

unknown

### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"SVG"` |             |

## filename

This object exists to hold the filename pattern that a 'SVG' filetype\_id would have, for it to be referenced elsewhere within this (or other) JSON schema.

`filename`

*   is optional

*   Type: `string` ([Filename pattern of a SVG file](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-svg-filename-pattern-check-properties-filename-pattern-of-a-svg-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-svg-filename-pattern-check-properties-filename-pattern-of-a-svg-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/39/properties/filename")

### filename Type

`string` ([Filename pattern of a SVG file](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-svg-filename-pattern-check-properties-filename-pattern-of-a-svg-file.md))

### filename Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>:;,?"*|/]+\.svg(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22*%7C%2F%5D%2B%5C.svg\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

### filename Examples

```json
"my_file1.svg.gpg"
```