# Filename pattern of a FAM file Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/fam-file-filename-pattern
```

This object exists to hold the filename pattern that a 'FAM' filetype_id would have, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## fam-file-filename-pattern Type

`string` ([Filename pattern of a FAM file](ega-2-definitions-filename-pattern-of-a-fam-file.md))

## fam-file-filename-pattern Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[^<>:;,?"*|/]+\.fam(.gz|.zip|.rar|.arj|.tar|.7z)?(.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22\*%7C%2F%5D%2B%5C.fam\(.gz%7C.zip%7C.rar%7C.arj%7C.tar%7C.7z\)%3F\(.gpg\)%3F%24 "try regular expression with regexr.com")

## fam-file-filename-pattern Examples

```json
"my_file1.fam.gz.gpg"
```
