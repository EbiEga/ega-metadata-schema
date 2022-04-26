# Protocols related to an experiment Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_protocols
```

Comprises metadata (e.g. Type of protocol) of a plan specification executed during an experiment. It shall have a sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## experiment\_protocols Type

`object[]` ([EGA Protocols object](ega-12-definitions-ega-protocols-object.md))

## experiment\_protocols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
