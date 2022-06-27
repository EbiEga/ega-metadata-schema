# Match edge Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls/items/properties/match_edge
```

Where the match should occur. Changes the rules on how min\_match and max\_mismatch are counted.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## match\_edge Type

`string` ([Match edge](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md))

## match\_edge Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation                                                                                                                                    |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| `"full"`  | Only @max\_mismatch influences matching process                                                                                                |
| `"start"` | Both matches and mismatches are counted. When @max\_mismatch is exceeded - it is not a match. When @min\_match is reached - match is declared. |
| `"end"`   | Both matches and mismatches are counted. When @max\_mismatch is exceeded - it is not a match. When @min\_match is reached - match is declared. |
