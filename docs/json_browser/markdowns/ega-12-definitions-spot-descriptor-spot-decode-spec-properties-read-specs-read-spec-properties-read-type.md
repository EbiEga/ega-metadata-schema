# Read type Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/read_type
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## read\_type Type

`string` ([Read type](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md))

## read\_type Constraints

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
