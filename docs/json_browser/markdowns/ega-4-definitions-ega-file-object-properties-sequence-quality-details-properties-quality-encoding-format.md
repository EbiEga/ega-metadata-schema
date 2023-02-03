# Quality encoding format Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fileObject/properties/sequenceQualityDetails/properties/qualityEncoding
```

Encoding system used to represent the quality score.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## qualityEncoding Type

`string` ([Quality encoding format](ega-4-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md))

## qualityEncoding Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation                                 |
| :-------------- | :------------------------------------------ |
| `"ascii"`       | ASCII character based encoding.             |
| `"decimal"`     | Single decimal value per quality score.     |
| `"hexadecimal"` | Single hexadecimal value per quality score. |
