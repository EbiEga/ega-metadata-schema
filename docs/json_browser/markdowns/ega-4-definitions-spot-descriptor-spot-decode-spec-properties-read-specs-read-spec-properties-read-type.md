# Read type Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/readType
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## readType Type

`string` ([Read type](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md))

## readType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"Forward"` |             |
| `"Reverse"` |             |
| `"Adapter"` |             |
| `"Primer"`  |             |
| `"Linker"`  |             |
| `"BarCode"` |             |
| `"Other"`   |             |
