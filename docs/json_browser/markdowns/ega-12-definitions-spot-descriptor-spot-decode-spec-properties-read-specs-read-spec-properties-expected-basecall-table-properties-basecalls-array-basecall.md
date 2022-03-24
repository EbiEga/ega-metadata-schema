# Basecall Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Basecall](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall.md))

# items Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :-------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [read_group_tag](#read_group_tag) | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-read-group-tag.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items/properties/read_group_tag") |
| [min_match](#min_match)           | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-min-match.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items/properties/min_match")           |
| [max_mismatch](#max_mismatch)     | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-max-mismatch.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items/properties/max_mismatch")     |
| [match_edge](#match_edge)         | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items/properties/match_edge")         |

## read_group_tag

When match occurs, the read will be tagged with this group membership.

`read_group_tag`

*   is optional

*   Type: `string` ([Read group tag](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-read-group-tag.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-read-group-tag.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items/properties/read_group_tag")

### read_group_tag Type

`string` ([Read group tag](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-read-group-tag.md))

## min_match

Minimum number of matches to trigger identification.

`min_match`

*   is optional

*   Type: `integer` ([Min match](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-min-match.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-min-match.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items/properties/min_match")

### min_match Type

`integer` ([Min match](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-min-match.md))

## max_mismatch

Maximum number of mismatches

`max_mismatch`

*   is optional

*   Type: `integer` ([Max mismatch](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-max-mismatch.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-max-mismatch.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items/properties/max_mismatch")

### max_mismatch Type

`integer` ([Max mismatch](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-max-mismatch.md))

## match_edge

Where the match should occur. Changes the rules on how min_match and max_mismatch are counted.

`match_edge`

*   is optional

*   Type: `string` ([Match edge](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items/properties/match_edge")

### match_edge Type

`string` ([Match edge](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md))

### match_edge Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"full"`  |             |
| `"start"` |             |
| `"end"`   |             |
