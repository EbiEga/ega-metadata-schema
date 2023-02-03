# Analysis custom attributes Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/analysisAttributes
```

Custom attributes of an analysis: reusable attributes to encode tag-value pairs (e.g. Tag being 'internal tag' and its Value 'this analysis is corresponds to internal tag XYZ') with optional units. Its properties are inherited from the common-definitions.json schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## analysisAttributes Type

`object[]` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

## analysisAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
