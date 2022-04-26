# Checksum pattern obtained by SHA-256 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/encrypted_checksum/oneOf/1
```

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm SHA-256, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 1 Type

`string` ([Checksum pattern obtained by SHA-256](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-encrypted-file-oneof-checksum-pattern-obtained-by-sha-256.md))

## 1 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Fa-f0-9]{64}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Fa-f0-9%5D%7B64%7D%24 "try regular expression with regexr.com")

## 1 Examples

```json
"c01b39c7a35ccc3b081a3e83d2c71fa9a767ebfeb45c69f08e17dfe3ef375a7b"
```
