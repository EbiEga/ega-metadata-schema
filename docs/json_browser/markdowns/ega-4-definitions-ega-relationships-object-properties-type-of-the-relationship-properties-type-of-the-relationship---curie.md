# Type of the relationship - CURIE Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type/properties/r_type_curie
```

The CURIE (i.e. ontologized term - e.g. NCIT:C64637), chosen from a list of CVs, of the type of the relationship.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## r_type_curie Type

`string` ([Type of the relationship - CURIE](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---curie.md))

## r_type_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"SIO:000252"`  |             |
| `"RO:0002202"`  |             |
| `"NCIT:C64637"` |             |
| `"RO:0002350"`  |             |
| `"EFO:0004424"` |             |
| `"GSSO:000728"` |             |
| `"GSSO:001986"` |             |
| `"SIO:000211"`  |             |
| `"EFO:0001796"` |             |
| `"NCIT:C25695"` |             |
| `"NCIT:C25461"` |             |

## r_type_curie Examples

```json
"RO:0002202"
```
