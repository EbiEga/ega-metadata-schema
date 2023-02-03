# Checksum pattern check - SHA-256 Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/1
```

A check that ensures that, if SHA-256 is given as a checksumMethodId, the checksums per se (e.g. unencryptedChecksum) follow SHA-256 patterns (sha-256-checksum-pattern).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 1 Type

unknown ([Checksum pattern check - SHA-256](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256.md))

# 1 Properties

| Property                                    | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                |
| :------------------------------------------ | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [checksumMethod](#checksummethod)           | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksummethod.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/1/properties/checksumMethod")                            |
| [unencryptedChecksum](#unencryptedchecksum) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum-pattern-obtained-by-sha-256.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/1/properties/unencryptedChecksum") |
| [encryptedChecksum](#encryptedchecksum)     | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum-pattern-obtained-by-sha-256-1.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/1/properties/encryptedChecksum") |

## checksumMethod



`checksumMethod`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksummethod.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/1/properties/checksumMethod")

### checksumMethod Type

unknown

### checksumMethod Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"SHA-256"` |             |

## unencryptedChecksum

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm SHA-256, for it to be referenced elsewhere within this (or other) JSON schema.

`unencryptedChecksum`

*   is optional

*   Type: `string` ([Checksum pattern obtained by SHA-256](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum-pattern-obtained-by-sha-256.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum-pattern-obtained-by-sha-256.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/1/properties/unencryptedChecksum")

### unencryptedChecksum Type

`string` ([Checksum pattern obtained by SHA-256](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum-pattern-obtained-by-sha-256.md))

### unencryptedChecksum Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Fa-f0-9]{64}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Fa-f0-9%5D%7B64%7D%24 "try regular expression with regexr.com")

### unencryptedChecksum Examples

```json
"c01b39c7a35ccc3b081a3e83d2c71fa9a767ebfeb45c69f08e17dfe3ef375a7b"
```

## encryptedChecksum

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm SHA-256, for it to be referenced elsewhere within this (or other) JSON schema.

`encryptedChecksum`

*   is optional

*   Type: `string` ([Checksum pattern obtained by SHA-256](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum-pattern-obtained-by-sha-256-1.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum-pattern-obtained-by-sha-256-1.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/1/properties/encryptedChecksum")

### encryptedChecksum Type

`string` ([Checksum pattern obtained by SHA-256](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---sha-256-properties-checksum-pattern-obtained-by-sha-256-1.md))

### encryptedChecksum Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[A-Fa-f0-9]{64}$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Fa-f0-9%5D%7B64%7D%24 "try regular expression with regexr.com")

### encryptedChecksum Examples

```json
"c01b39c7a35ccc3b081a3e83d2c71fa9a767ebfeb45c69f08e17dfe3ef375a7b"
```
