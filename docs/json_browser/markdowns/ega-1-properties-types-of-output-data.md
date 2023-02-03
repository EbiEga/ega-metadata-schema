# Types of output data Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/typesOfOutputData
```

Types of data the experiment produces.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## typesOfOutputData Type

`string[]` ([Type of data](ega-4-definitions-type-of-data.md))

## typesOfOutputData Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.
