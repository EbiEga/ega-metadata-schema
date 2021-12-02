# Filename pattern of a SRF file Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/filename-filetype-pattern-check/anyOf/9/properties/filename
```

This object exists to hold the filename pattern that a 'SRF' filetype_id would have, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## filename Type

`string` ([Filename pattern of a SRF file](ega-2-definitions-check-filetype-checks-based-on-its-filename-anyof-srf-filename-pattern-check-properties-filename-pattern-of-a-srf-file.md))

## filename Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[^<>:;,?"*|/]+\.srf(.gz|.zip|.rar|.arj|.tar|.7z)?(.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3C%3E%3A%3B%2C%3F%22\*%7C%2F%5D%2B%5C.srf\(.gz%7C.zip%7C.rar%7C.arj%7C.tar%7C.7z\)%3F\(.gpg\)%3F%24 "try regular expression with regexr.com")

## filename Examples

```json
"my_file1.srf.gz.gpg"
```
