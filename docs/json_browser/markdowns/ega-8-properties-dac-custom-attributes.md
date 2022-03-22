# DAC custom attributes Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/dac_attributes
```

Custom attributes of a DAC: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.DAC.json*](../out/EGA.DAC.json "open original schema") |

## dac_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

## dac_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
