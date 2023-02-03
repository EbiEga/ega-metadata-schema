# Filename pattern of a PED file Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/pedFileFilenamePattern
```

This object exists to hold the filename pattern that a 'PED' filetypeId would have, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## pedFileFilenamePattern Type

`string` ([Filename pattern of a PED file](ega-4-definitions-filename-pattern-of-a-ped-file.md))

## pedFileFilenamePattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^.+\.(ped|tped)(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E.%2B%5C.\(ped%7Ctped\)\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

## pedFileFilenamePattern Examples

```json
"my_file1.ped.gz.gpg"
```
