# ASCII offset Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails/properties/asciiOffset
```

Character used in representing the minimum quality value.  Helps specify how to decode text rendering of quality data.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## asciiOffset Type

`string` ([ASCII offset](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-ascii-offset.md))

## asciiOffset Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation                                      |
| :---- | :----------------------------------------------- |
| `"!"` | ASCII value 33.  Typically used for range 0..63. |
| `"@"` | ASCII value 64.  Typically used for range 0..60. |
