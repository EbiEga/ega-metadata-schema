# Filename pattern of a BIM file Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/bimFileFilenamePattern
```

This object exists to hold the filename pattern that a 'BIM' filetypeId would have, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## bimFileFilenamePattern Type

`string` ([Filename pattern of a BIM file](ega-4-defs-filename-pattern-of-a-bim-file.md))

## bimFileFilenamePattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^.+\.bim(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E.%2B%5C.bim\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

## bimFileFilenamePattern Examples

```json
"my_file1.bim.gz.gpg"
```