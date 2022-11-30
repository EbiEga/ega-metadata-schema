# Filename pattern of a ASM file Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/asm-file-filename-pattern
```

This object exists to hold the filename pattern that a 'ASM' filetype\_id would have, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## asm-file-filename-pattern Type

`string` ([Filename pattern of a ASM file](ega-12-definitions-filename-pattern-of-a-asm-file.md))

## asm-file-filename-pattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^<>:;,?"*|/]+\.asm(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22*%7C%2F%5D%2B%5C.asm\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

## asm-file-filename-pattern Examples

```json
"my_file1.asm.gpg"
```
