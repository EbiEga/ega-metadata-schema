# Sample custom attributes Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_attributes
```

Custom attributes of a sample: reusable attributes to encode tag-value pairs (e.g. Tag being 'age' and its Value '30') with optional units (e.g. 'years'). Its properties are inherited from the common-definitions.json schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.sample.json*](../out/EGA.sample.json "open original schema") |

## sample_attributes Type

`object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

## sample_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
