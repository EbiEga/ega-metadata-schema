# ASCII offset Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/ascii_offset
```

Character used in representing the minimum quality value.  Helps specify how to decode text rendering of quality data.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## ascii\_offset Type

`string` ([ASCII offset](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md))

## ascii\_offset Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation                                      |
| :---- | :----------------------------------------------- |
| `"!"` | ASCII value 33.  Typically used for range 0..63. |
| `"@"` | ASCII value 64.  Typically used for range 0..60. |
