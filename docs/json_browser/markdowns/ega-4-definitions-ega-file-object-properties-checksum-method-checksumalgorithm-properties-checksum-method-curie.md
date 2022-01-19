# Checksum method CURIE Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method/properties/checksum_method_curie
```

The CURIE (i.e. ontologized term - NCIT:C171276 or NCIT:C80226) associated with the used checksum method.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## checksum_method_curie Type

`string` ([Checksum method CURIE](ega-4-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-curie.md))

## checksum_method_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"NCIT:C171276"` |             |
| `"NCIT:C80226"`  |             |

## checksum_method_curie Examples

```json
"NCIT:C171276"
```
