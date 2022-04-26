# Policy custom attributes Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.policy.json#/properties/policy_attributes
```

Custom attributes of a policy: reusable attributes to encode tag-value pairs (e.g. Tag being 'Targeted loci' and its Value '5:63256183-63258334') with optional units (e.g. 'base pairs'). Its properties are inherited from the common-definitions.json schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## policy\_attributes Type

`object[]` ([Custom attribute of an object](ega-12-definitions-custom-attribute-of-an-object.md))

## policy\_attributes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
