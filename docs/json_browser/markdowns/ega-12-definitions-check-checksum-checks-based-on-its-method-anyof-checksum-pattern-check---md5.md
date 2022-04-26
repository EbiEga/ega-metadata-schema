# Checksum pattern check - MD5 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/0
```

A check that ensures that, if MD5 is given as a checksum\_method\_id, the checksums per se (e.g. unencrypted\_checksum) follow MD5 patterns (md5-checksum-pattern).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 0 Type

unknown ([Checksum pattern check - MD5](ega-12-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5.md))

# 0 Properties

| Property                                       | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                            |
| :--------------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [checksum\_method](#checksum_method)           | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum_method.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/0/properties/checksum_method") |
| [unencrypted\_checksum](#unencrypted_checksum) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-checksum-pattern-obtained-by-md5.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/0/properties/unencrypted_checksum")                                                                   |
| [encrypted\_checksum](#encrypted_checksum)     | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-checksum-pattern-obtained-by-md5.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/0/properties/encrypted_checksum")                                                                     |

## checksum\_method



`checksum_method`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum_method.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/0/properties/checksum_method")

### checksum\_method Type

unknown

### checksum\_method Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"MD5"` |             |

## unencrypted\_checksum

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm MD5, for it to be referenced elsewhere within this (or other) JSON schema.

`unencrypted_checksum`

*   is optional

*   Type: `string` ([Checksum pattern obtained by MD5](ega-12-definitions-checksum-pattern-obtained-by-md5.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-checksum-pattern-obtained-by-md5.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/0/properties/unencrypted_checksum")

### unencrypted\_checksum Type

`string` ([Checksum pattern obtained by MD5](ega-12-definitions-checksum-pattern-obtained-by-md5.md))

### unencrypted\_checksum Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-z](?:-?[0-9a-z]){31}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-z%5D\(%3F%3A-%3F%5B0-9a-z%5D\)%7B31%7D%24 "try regular expression with regexr.com")

### unencrypted\_checksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```

## encrypted\_checksum

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm MD5, for it to be referenced elsewhere within this (or other) JSON schema.

`encrypted_checksum`

*   is optional

*   Type: `string` ([Checksum pattern obtained by MD5](ega-12-definitions-checksum-pattern-obtained-by-md5.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-checksum-pattern-obtained-by-md5.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/0/properties/encrypted_checksum")

### encrypted\_checksum Type

`string` ([Checksum pattern obtained by MD5](ega-12-definitions-checksum-pattern-obtained-by-md5.md))

### encrypted\_checksum Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-z](?:-?[0-9a-z]){31}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-z%5D\(%3F%3A-%3F%5B0-9a-z%5D\)%7B31%7D%24 "try regular expression with regexr.com")

### encrypted\_checksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```
