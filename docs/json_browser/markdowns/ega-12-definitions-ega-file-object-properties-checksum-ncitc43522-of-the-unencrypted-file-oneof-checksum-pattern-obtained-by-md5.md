# Checksum pattern obtained by MD5 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/unencrypted_checksum/oneOf/0
```

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm MD5, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 0 Type

`string` ([Checksum pattern obtained by MD5](ega-12-definitions-ega-file-object-properties-checksum-ncitc43522-of-the-unencrypted-file-oneof-checksum-pattern-obtained-by-md5.md))

## 0 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-z](?:-?[0-9a-z]){31}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-z%5D\(%3F%3A-%3F%5B0-9a-z%5D\)%7B31%7D%24 "try regular expression with regexr.com")

## 0 Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```
