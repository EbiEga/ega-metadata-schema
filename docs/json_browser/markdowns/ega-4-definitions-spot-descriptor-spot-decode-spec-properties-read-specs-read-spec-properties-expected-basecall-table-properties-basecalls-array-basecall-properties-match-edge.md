# Match edge Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items/properties/matchEdge
```

Where the match should occur. Changes the rules on how minMatch and maxMismatch are counted.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## matchEdge Type

`string` ([Match edge](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md))

## matchEdge Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation                                                                                                                                |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| `"full"`  | Only @maxMismatch influences matching process                                                                                              |
| `"start"` | Both matches and mismatches are counted. When @maxMismatch is exceeded - it is not a match. When @minMatch is reached - match is declared. |
| `"end"`   | Both matches and mismatches are counted. When @maxMismatch is exceeded - it is not a match. When @minMatch is reached - match is declared. |
