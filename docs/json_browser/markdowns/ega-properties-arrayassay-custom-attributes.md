# ArrayAssay custom attributes Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/array_assay_attributes
```

Custom attributes of an ArrayAssay: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema. #! Using an empty item list but defining the custom attributes as possible additionalItems we create the correct constraint: anything but a custom attribute is rejected, but EGA can add as many as required.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.ArrayAssay.json*](../out/EGA.ArrayAssay.json "open original schema") |

## array_assay_attributes Type

`object[]` ([Custom attribute of an object](ega-2-definitions-custom-attribute-of-an-object.md))

## array_assay_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
