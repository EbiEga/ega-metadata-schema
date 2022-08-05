# Sample relationships Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_relationships
```

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. a viral sample from BioSamples being linked to a blood sample within the EGA) and within (e.g. a sample being linked to a sequencing run) the EGA.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sample\_relationships Type

an array of merged types ([Details](ega-17-properties-sample-relationships-items.md))

## sample\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
