# Checksum pattern check - MD5 Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/0
```

A check that ensures that, if MD5 is given as a checksumMethodId, the checksums per se (e.g. unencryptedChecksum) follow MD5 patterns (md5ChecksumPattern).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 0 Type

unknown ([Checksum pattern check - MD5](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5.md))

# 0 Properties

| Property                                    | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                        |
| :------------------------------------------ | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [checksumMethod](#checksummethod)           | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksummethod.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/0/properties/checksumMethod")                        |
| [unencryptedChecksum](#unencryptedchecksum) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum-pattern-obtained-by-md5.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/0/properties/unencryptedChecksum") |
| [encryptedChecksum](#encryptedchecksum)     | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum-pattern-obtained-by-md5-1.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/0/properties/encryptedChecksum") |

## checksumMethod



`checksumMethod`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksummethod.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/0/properties/checksumMethod")

### checksumMethod Type

unknown

### checksumMethod Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"MD5"` |             |

## unencryptedChecksum

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm MD5, for it to be referenced elsewhere within this (or other) JSON schema.

`unencryptedChecksum`

*   is optional

*   Type: `string` ([Checksum pattern obtained by MD5](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum-pattern-obtained-by-md5.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum-pattern-obtained-by-md5.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/0/properties/unencryptedChecksum")

### unencryptedChecksum Type

`string` ([Checksum pattern obtained by MD5](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum-pattern-obtained-by-md5.md))

### unencryptedChecksum Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-z](?:-?[0-9a-z]){31}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-z%5D\(%3F%3A-%3F%5B0-9a-z%5D\)%7B31%7D%24 "try regular expression with regexr.com")

### unencryptedChecksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```

## encryptedChecksum

This object exists to hold the pattern that a checksum would have if it was obtained using the algorithm MD5, for it to be referenced elsewhere within this (or other) JSON schema.

`encryptedChecksum`

*   is optional

*   Type: `string` ([Checksum pattern obtained by MD5](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum-pattern-obtained-by-md5-1.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum-pattern-obtained-by-md5-1.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/checksumPatternCheck/anyOf/0/properties/encryptedChecksum")

### encryptedChecksum Type

`string` ([Checksum pattern obtained by MD5](ega-4-definitions-check-checksum-checks-based-on-its-method-anyof-checksum-pattern-check---md5-properties-checksum-pattern-obtained-by-md5-1.md))

### encryptedChecksum Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-z](?:-?[0-9a-z]){31}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-z%5D\(%3F%3A-%3F%5B0-9a-z%5D\)%7B31%7D%24 "try regular expression with regexr.com")

### encryptedChecksum Examples

```json
"bc527343c7ffc103111f3a694b004e2f"
```
