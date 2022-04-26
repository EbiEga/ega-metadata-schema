# Sequence interval Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval
```

The location of a sequence feature in a genome, defined by its start (e.g. 71366222) and end (e.g. 71532374) position on some reference genomic coordinate system. Positions are always represented by contiguous spans using interbase coordinates or coordinate ranges. Both coordinates are inclusive: the sequence bounds are included in the described genomic feature. In other words, if the sequence interval is 71366222-71532374, both 71366222 and 71532374 coordinates are included in the feature.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## sequence\_interval Type

`object` ([Sequence interval](ega-12-definitions-sequence-coordinates-properties-sequence-interval.md))

# sequence\_interval Properties

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :-------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [start](#start) | `number` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-single-sequence-position.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval/properties/start") |
| [end](#end)     | `number` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-single-sequence-position.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval/properties/end")   |

## start

A single 1-based (first base of the assembly unit is 1, not 0) sequence coordinate, inclusive. It can be used to describe the start or end coordinates of a sequence interval, or directly a single coordinate within a sequence.

`start`

*   is required

*   Type: `number` ([Single sequence position](ega-12-definitions-single-sequence-position.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-single-sequence-position.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval/properties/start")

### start Type

`number` ([Single sequence position](ega-12-definitions-single-sequence-position.md))

### start Examples

```json
71366222
```

```json
36592394
```

```json
1
```

## end

A single 1-based (first base of the assembly unit is 1, not 0) sequence coordinate, inclusive. It can be used to describe the start or end coordinates of a sequence interval, or directly a single coordinate within a sequence.

`end`

*   is required

*   Type: `number` ([Single sequence position](ega-12-definitions-single-sequence-position.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-single-sequence-position.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/sequence_coordinates/properties/sequence_interval/properties/end")

### end Type

`number` ([Single sequence position](ega-12-definitions-single-sequence-position.md))

### end Examples

```json
71366222
```

```json
36592394
```

```json
1
```
