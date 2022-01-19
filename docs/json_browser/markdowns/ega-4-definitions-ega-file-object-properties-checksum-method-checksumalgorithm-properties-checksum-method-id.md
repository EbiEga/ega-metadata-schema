# Checksum method ID Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method/properties/checksum_method_id
```

The ID or name (MD5 or SHA-256) associated with the used checksum method.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## checksum_method_id Type

`string` ([Checksum method ID](ega-4-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-id.md))

## checksum_method_id Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"MD5"`     |             |
| `"SHA-256"` |             |

## checksum_method_id Examples

```json
"MD5"
```
