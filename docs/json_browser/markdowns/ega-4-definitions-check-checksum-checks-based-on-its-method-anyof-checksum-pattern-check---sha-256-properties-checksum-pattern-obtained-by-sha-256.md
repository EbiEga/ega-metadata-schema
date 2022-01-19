# Checksum pattern obtained by SHA-256 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/1/properties/unencrypted_checksum
```

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm SHA-256, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## unencrypted_checksum Type

`string` ([Checksum pattern obtained by SHA-256](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum-pattern-obtained-by-sha-256.md))

## unencrypted_checksum Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Fa-f0-9]{64}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Fa-f0-9%5D%7B64%7D%24 "try regular expression with regexr.com")

## unencrypted_checksum Examples

```json
"c01b39c7a35ccc3b081a3e83d2c71fa9a767ebfeb45c69f08e17dfe3ef375a7b"
```
