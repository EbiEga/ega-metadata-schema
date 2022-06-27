# Quality encoding format Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/file_object/properties/sequence_quality_details/properties/quality_encoding
```

Encoding system used to represent the quality score.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## quality\_encoding Type

`string` ([Quality encoding format](ega-12-definitions-ega-file-object-properties-sequence-quality-details-properties-quality-encoding-format.md))

## quality\_encoding Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation                                 |
| :-------------- | :------------------------------------------ |
| `"ascii"`       | ASCII character based encoding.             |
| `"decimal"`     | Single decimal value per quality score.     |
| `"hexadecimal"` | Single hexadecimal value per quality score. |
