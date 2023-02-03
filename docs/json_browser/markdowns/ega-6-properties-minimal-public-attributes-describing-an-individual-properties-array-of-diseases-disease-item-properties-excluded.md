# Excluded Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases/items/properties/excluded
```

Property that specifies whether the disease was observed or not. Similar to phenopacket's 'excluded' property, by default it is 'false', which means that the disease was observed (i.e. not excluded). This flag is only required to indicate that the disease was looked for, but found to be absent. The terms 'not excluded' (i.e. false) and 'excluded' (i.e. true) correlate with the common notation of 'case' versus 'control', respectively.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## excluded Type

`boolean` ([Excluded](ega-6-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases-disease-item-properties-excluded.md))
