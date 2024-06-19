# Sample custom attributes Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleAttributes
```

Custom attributes of a sample: reusable attributes to encode tag-value pairs (e.g. Tag being 'age' and its Value '30') with optional units (e.g. 'years'). Its properties are inherited from the common-definitions.json schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sampleAttributes Type

`object[]` ([Custom attribute of an object](ega-4-defs-custom-attribute-of-an-object.md))

## sampleAttributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
