# JPG Filename patternCheck Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/filenameFiletypePatternCheck/anyOf/41
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 41 Type

unknown ([JPG Filename patternCheck](ega-4-defs-check-filetype-checks-based-on-its-filename-anyof-jpg-filename-patterncheck.md))

# 41 Properties

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                      |
| :-------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype](#filetype) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-defs-check-filetype-checks-based-on-its-filename-anyof-jpg-filename-patterncheck-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/filenameFiletypePatternCheck/anyOf/41/properties/filetype")                       |
| [filename](#filename) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-4-defs-check-filetype-checks-based-on-its-filename-anyof-jpg-filename-patterncheck-properties-filename-pattern-of-a-jpg-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/filenameFiletypePatternCheck/anyOf/41/properties/filename") |

## filetype



`filetype`

* is optional

* Type: unknown

* cannot be null

* defined in: [EGA common metadata definitions](ega-4-defs-check-filetype-checks-based-on-its-filename-anyof-jpg-filename-patterncheck-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/filenameFiletypePatternCheck/anyOf/41/properties/filetype")

### filetype Type

unknown

### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"JPG"` |             |

## filename

This object exists to hold the filename pattern that a 'JPG' filetypeId would have, for it to be referenced elsewhere within this (or other) JSON schema.

`filename`

* is optional

* Type: `string` ([Filename pattern of a JPG file](ega-4-defs-check-filetype-checks-based-on-its-filename-anyof-jpg-filename-patterncheck-properties-filename-pattern-of-a-jpg-file.md))

* cannot be null

* defined in: [EGA common metadata definitions](ega-4-defs-check-filetype-checks-based-on-its-filename-anyof-jpg-filename-patterncheck-properties-filename-pattern-of-a-jpg-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/filenameFiletypePatternCheck/anyOf/41/properties/filename")

### filename Type

`string` ([Filename pattern of a JPG file](ega-4-defs-check-filetype-checks-based-on-its-filename-anyof-jpg-filename-patterncheck-properties-filename-pattern-of-a-jpg-file.md))

### filename Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>:;,?"*|/]+\.jpg(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22*%7C%2F%5D%2B%5C.jpg\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

### filename Examples

```json
"my_file1.jpg.gpg"
```
