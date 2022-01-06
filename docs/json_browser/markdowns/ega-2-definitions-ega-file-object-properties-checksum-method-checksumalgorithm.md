# Checksum method \[ChecksumAlgorithm] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method
```

Node containing both the ID (MD5 or SHA-256) and the CURIE (NCIT:C171276 or NCIT:C80226), describing the method which yields the checksum from a data input for the purpose of detecting errors.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## checksum_method Type

`object` ([Checksum method \[ChecksumAlgorithm\]](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm.md))

# checksum_method Properties

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                               |
| :---------------------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [checksum_method_id](#checksum_method_id)       | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method/properties/checksum_method_id")       |
| [checksum_method_curie](#checksum_method_curie) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method/properties/checksum_method_curie") |

## checksum_method_id

The ID or name (MD5 or SHA-256) associated with the used checksum method.

`checksum_method_id`

*   is optional

*   Type: `string` ([Checksum method ID](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method/properties/checksum_method_id")

### checksum_method_id Type

`string` ([Checksum method ID](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-id.md))

### checksum_method_id Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"MD5"`     |             |
| `"SHA-256"` |             |

### checksum_method_id Examples

```json
"MD5"
```

## checksum_method_curie

The CURIE (i.e. ontologized term - NCIT:C171276 or NCIT:C80226) associated with the used checksum method.

`checksum_method_curie`

*   is optional

*   Type: `string` ([Checksum method CURIE](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/checksum_method/properties/checksum_method_curie")

### checksum_method_curie Type

`string` ([Checksum method CURIE](ega-2-definitions-ega-file-object-properties-checksum-method-checksumalgorithm-properties-checksum-method-curie.md))

### checksum_method_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value            | Explanation |
| :--------------- | :---------- |
| `"NCIT:C171276"` |             |
| `"NCIT:C80226"`  |             |

### checksum_method_curie Examples

```json
"NCIT:C171276"
```
