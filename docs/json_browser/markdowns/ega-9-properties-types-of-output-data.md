# Types of output data Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/types_of_output_data
```

Types of data the experiment produces.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## types_of_output_data Type

`string[]` ([Type of data](ega-12-definitions-type-of-data.md))

## types_of_output_data Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.
