# Filename pattern of a ZIP file Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/zipFileFilenamePattern
```

This object exists to hold the filename pattern that a 'ZIP' filetypeId would have, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## zipFileFilenamePattern Type

`string` ([Filename pattern of a ZIP file](ega-4-definitions-filename-pattern-of-a-zip-file.md))

## zipFileFilenamePattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>:;,?"*|/]+\.zip(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22*%7C%2F%5D%2B%5C.zip\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

## zipFileFilenamePattern Examples

```json
"my_file1.zip.gpg"
```
