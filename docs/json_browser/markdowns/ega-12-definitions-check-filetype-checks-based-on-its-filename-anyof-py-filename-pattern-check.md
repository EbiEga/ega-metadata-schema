# PY Filename pattern-check Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/24
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 24 Type

unknown ([PY Filename pattern-check](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-py-filename-pattern-check.md))

# 24 Properties

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                       |
| :-------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype](#filetype) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-py-filename-pattern-check-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/24/properties/filetype") |
| [filename](#filename) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-filename-pattern-of-a-py-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/24/properties/filename")                                                                   |

## filetype



`filetype`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-filetype-checks-based-on-its-filename-anyof-py-filename-pattern-check-properties-filetype.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/24/properties/filetype")

### filetype Type

unknown

### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value  | Explanation |
| :----- | :---------- |
| `"PY"` |             |

## filename

This object exists to hold the filename pattern that a 'PY' filetype\_id would have, for it to be referenced elsewhere within this (or other) JSON schema.

`filename`

*   is optional

*   Type: `string` ([Filename pattern of a PY file](ega-12-definitions-filename-pattern-of-a-py-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-filename-pattern-of-a-py-file.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/24/properties/filename")

### filename Type

`string` ([Filename pattern of a PY file](ega-12-definitions-filename-pattern-of-a-py-file.md))

### filename Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>:;,?"*|/]+\.(py|PY)(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22*%7C%2F%5D%2B%5C.\(py%7CPY\)\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

### filename Examples

```json
"my_file1.py.gz.gpg"
```
