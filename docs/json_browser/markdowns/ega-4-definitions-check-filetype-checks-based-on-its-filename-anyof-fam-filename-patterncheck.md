# FAM Filename patternCheck Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filenameFiletypePatternCheck/anyOf/20
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 20 Type

unknown ([FAM Filename patternCheck](ega-4-definitions-check-filetype-checks-based-on-its-filename-anyof-fam-filename-patterncheck.md))

# 20 Properties

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                   |
| :-------------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [filetype](#filetype) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-filetype-checks-based-on-its-filename-anyof-fam-filename-patterncheck-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filenameFiletypePatternCheck/anyOf/20/properties/filetype")                       |
| [filename](#filename) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-filetype-checks-based-on-its-filename-anyof-fam-filename-patterncheck-properties-filename-pattern-of-a-fam-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filenameFiletypePatternCheck/anyOf/20/properties/filename") |

## filetype



`filetype`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-filetype-checks-based-on-its-filename-anyof-fam-filename-patterncheck-properties-filetype.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filenameFiletypePatternCheck/anyOf/20/properties/filetype")

### filetype Type

unknown

### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"FAM"` |             |

## filename

This object exists to hold the filename pattern that a 'FAM' filetypeId would have, for it to be referenced elsewhere within this (or other) JSON schema.

`filename`

*   is optional

*   Type: `string` ([Filename pattern of a FAM file](ega-4-definitions-check-filetype-checks-based-on-its-filename-anyof-fam-filename-patterncheck-properties-filename-pattern-of-a-fam-file.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-filetype-checks-based-on-its-filename-anyof-fam-filename-patterncheck-properties-filename-pattern-of-a-fam-file.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/filenameFiletypePatternCheck/anyOf/20/properties/filename")

### filename Type

`string` ([Filename pattern of a FAM file](ega-4-definitions-check-filetype-checks-based-on-its-filename-anyof-fam-filename-patterncheck-properties-filename-pattern-of-a-fam-file.md))

### filename Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^.+\.(fam|tfam)(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E.%2B%5C.\(fam%7Ctfam\)\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

### filename Examples

```json
"my_file1.fam.gz.gpg"
```
