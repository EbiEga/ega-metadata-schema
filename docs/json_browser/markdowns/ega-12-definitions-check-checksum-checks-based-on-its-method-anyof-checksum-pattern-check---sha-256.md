# Checksum pattern check - SHA-256 Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/1
```

A check that ensures that, if SHA-256 is given as a checksum_method_id, the checksums per se (e.g. unencrypted_checksum) follow SHA-256 patterns (sha-256-checksum-pattern).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## 1 Type

unknown ([Checksum pattern check - SHA-256](ega-12-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256.md))

# 1 Properties

| Property                                      | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                |
| :-------------------------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [checksum_method](#checksum_method)           | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum_method.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/1/properties/checksum_method") |
| [unencrypted_checksum](#unencrypted_checksum) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/1/properties/unencrypted_checksum")                                                                   |
| [encrypted_checksum](#encrypted_checksum)     | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/1/properties/encrypted_checksum")                                                                     |

## checksum_method



`checksum_method`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum_method.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/1/properties/checksum_method")

### checksum_method Type

unknown

### checksum_method Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"SHA-256"` |             |

## unencrypted_checksum

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm SHA-256, for it to be referenced elsewhere within this (or other) JSON schema.

`unencrypted_checksum`

*   is optional

*   Type: `string` ([Checksum pattern obtained by SHA-256](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/1/properties/unencrypted_checksum")

### unencrypted_checksum Type

`string` ([Checksum pattern obtained by SHA-256](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md))

### unencrypted_checksum Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Fa-f0-9]{64}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Fa-f0-9%5D%7B64%7D%24 "try regular expression with regexr.com")

### unencrypted_checksum Examples

```json
"c01b39c7a35ccc3b081a3e83d2c71fa9a767ebfeb45c69f08e17dfe3ef375a7b"
```

## encrypted_checksum

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm SHA-256, for it to be referenced elsewhere within this (or other) JSON schema.

`encrypted_checksum`

*   is optional

*   Type: `string` ([Checksum pattern obtained by SHA-256](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/checksum-pattern-check/anyOf/1/properties/encrypted_checksum")

### encrypted_checksum Type

`string` ([Checksum pattern obtained by SHA-256](ega-12-definitions-checksum-pattern-obtained-by-sha-256.md))

### encrypted_checksum Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Fa-f0-9]{64}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Fa-f0-9%5D%7B64%7D%24 "try regular expression with regexr.com")

### encrypted_checksum Examples

```json
"c01b39c7a35ccc3b081a3e83d2c71fa9a767ebfeb45c69f08e17dfe3ef375a7b"
```
