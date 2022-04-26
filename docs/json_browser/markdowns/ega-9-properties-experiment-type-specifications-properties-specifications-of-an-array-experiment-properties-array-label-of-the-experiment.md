# Array label of the experiment Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment/properties/array_labels
```

Chemicals conjugated to nucleic acid/proteins to label them before microarray hybridisation. Can be repeated so that dual labelled arrays can be taken into account.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## array\_labels Type

`object[]` ([Repeatable array\_label node](ega-12-definitions-repeatable-array_label-node.md))

## array\_labels Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
