# Single sequence position Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/sequenceCoordinates/properties/singlePosition
```

A single 1-based (first base of the assembly unit is 1, not 0) sequence coordinate, inclusive. It can be used to describe the start or end coordinates of a sequence interval, or directly a single coordinate within a sequence.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## singlePosition Type

`number` ([Single sequence position](ega-4-defs-sequence-coordinates-properties-single-sequence-position.md))

## singlePosition Examples

```json
71366222
```

```json
36592394
```

```json
1
```