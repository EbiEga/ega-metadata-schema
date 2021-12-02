# Protocols related to an ArrayExperiment Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/array_experiment_protocols
```

Comprises metadata (e.g. Type of protocol) of a plan specification related to an ArrayExperiment, with sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents. #! Using an empty item list but defining the protocols as possible additionalItems we create the correct constraint: anything but a protocol is rejected, but EGA can add as many as required.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## array_experiment_protocols Type

`object[]` ([EGA Protocols object](ega-2-definitions-ega-protocols-object.md))

## array_experiment_protocols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
