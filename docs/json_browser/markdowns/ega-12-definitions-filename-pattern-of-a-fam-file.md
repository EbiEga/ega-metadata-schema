# Filename pattern of a FAM file Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fam-file-filename-pattern
```

This object exists to hold the filename pattern that a 'FAM' filetype\_id would have, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## fam-file-filename-pattern Type

`string` ([Filename pattern of a FAM file](ega-12-definitions-filename-pattern-of-a-fam-file.md))

## fam-file-filename-pattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^.+\.(fam|tfam)(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E.%2B%5C.\(fam%7Ctfam\)\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

## fam-file-filename-pattern Examples

```json
"my_file1.fam.gz.gpg"
```
