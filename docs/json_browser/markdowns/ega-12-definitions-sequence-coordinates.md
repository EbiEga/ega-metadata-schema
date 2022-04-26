# Sequence coordinates Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/sequence_coordinates
```

A position in a map (for example a genetic map), either a single position (e.g. 71366222) or a region interval (e.g. 71366222-71532374). Used to define coordinates within an assembly unit.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## sequence\_coordinates Type

`object` ([Sequence coordinates](ega-12-definitions-sequence-coordinates.md))

any of

*   [Either a single position is given](ega-12-definitions-sequence-coordinates-anyof-either-a-single-position-is-given.md "check type definition")

*   [Or the whole sequence interval](ega-12-definitions-sequence-coordinates-anyof-or-the-whole-sequence-interval.md "check type definition")

# sequence\_coordinates Properties

| Property                                 | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                              |
| :--------------------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [single\_position](#single_position)     | `number` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-single-sequence-position.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/single_position")                            |
| [sequence\_interval](#sequence_interval) | `object` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval") |

## single\_position

A single 1-based (first base of the assembly unit is 1, not 0) sequence coordinate, inclusive. It can be used to describe the start or end coordinates of a sequence interval, or directly a single coordinate within a sequence.

`single_position`

*   is optional

*   Type: `number` ([Single sequence position](ega-12-definitions-single-sequence-position.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-single-sequence-position.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/single_position")

### single\_position Type

`number` ([Single sequence position](ega-12-definitions-single-sequence-position.md))

### single\_position Examples

```json
71366222
```

```json
36592394
```

```json
1
```

## sequence\_interval

The location of a sequence feature in a genome, defined by its start (e.g. 71366222) and end (e.g. 71532374) position on some reference genomic coordinate system. Positions are always represented by contiguous spans using interbase coordinates or coordinate ranges. Both coordinates are inclusive: the sequence bounds are included in the described genomic feature. In other words, if the sequence interval is 71366222-71532374, both 71366222 and 71532374 coordinates are included in the feature.

`sequence_interval`

*   is optional

*   Type: `object` ([Sequence interval](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval")

### sequence\_interval Type

`object` ([Sequence interval](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md))
