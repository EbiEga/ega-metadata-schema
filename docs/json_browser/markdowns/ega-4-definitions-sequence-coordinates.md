# Sequence coordinates Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates
```

A position in a map (for example a genetic map), either a single position (e.g. 71366222) or a region interval (e.g. 71366222-71532374). Used to define coordinates within an assembly unit.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## sequenceCoordinates Type

`object` ([Sequence coordinates](ega-4-definitions-sequence-coordinates.md))

any of

*   [Either a single position is given](ega-4-definitions-sequence-coordinates-anyof-either-a-single-position-is-given.md "check type definition")

*   [Or the whole sequence interval](ega-4-definitions-sequence-coordinates-anyof-or-the-whole-sequence-interval.md "check type definition")

# sequenceCoordinates Properties

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                          |
| :------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [singlePosition](#singleposition)     | `number` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-sequence-coordinates-properties-single-sequence-position.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/singlePosition") |
| [sequenceInterval](#sequenceinterval) | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-sequence-coordinates-properties-sequence-interval.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/sequenceInterval")      |

## singlePosition

A single 1-based (first base of the assembly unit is 1, not 0) sequence coordinate, inclusive. It can be used to describe the start or end coordinates of a sequence interval, or directly a single coordinate within a sequence.

`singlePosition`

*   is optional

*   Type: `number` ([Single sequence position](ega-4-definitions-sequence-coordinates-properties-single-sequence-position.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-sequence-coordinates-properties-single-sequence-position.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/singlePosition")

### singlePosition Type

`number` ([Single sequence position](ega-4-definitions-sequence-coordinates-properties-single-sequence-position.md))

### singlePosition Examples

```json
71366222
```

```json
36592394
```

```json
1
```

## sequenceInterval

The location of a sequence feature in a genome, defined by its start (e.g. 71366222) and end (e.g. 71532374) position on some reference genomic coordinate system. Positions are always represented by contiguous spans using interbase coordinates or coordinate ranges. Both coordinates are inclusive: the sequence bounds are included in the described genomic feature. In other words, if the sequence interval is 71366222-71532374, both 71366222 and 71532374 coordinates are included in the feature.

`sequenceInterval`

*   is optional

*   Type: `object` ([Sequence interval](ega-4-definitions-sequence-coordinates-properties-sequence-interval.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-sequence-coordinates-properties-sequence-interval.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/sequenceCoordinates/properties/sequenceInterval")

### sequenceInterval Type

`object` ([Sequence interval](ega-4-definitions-sequence-coordinates-properties-sequence-interval.md))
