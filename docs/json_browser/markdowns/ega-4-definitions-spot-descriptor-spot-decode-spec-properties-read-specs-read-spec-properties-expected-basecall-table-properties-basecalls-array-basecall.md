# Basecall Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Basecall](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall.md))

# items Properties

| Property                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :---------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [readGroupTag](#readgrouptag) | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-read-group-tag.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items/properties/readGroupTag") |
| [minMatch](#minmatch)         | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-min-match.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items/properties/minMatch")          |
| [maxMismatch](#maxmismatch)   | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-max-mismatch.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items/properties/maxMismatch")    |
| [matchEdge](#matchedge)       | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items/properties/matchEdge")        |

## readGroupTag

When match occurs, the read will be tagged with this group membership.

`readGroupTag`

*   is optional

*   Type: `string` ([Read group tag](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-read-group-tag.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-read-group-tag.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items/properties/readGroupTag")

### readGroupTag Type

`string` ([Read group tag](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-read-group-tag.md))

### readGroupTag Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## minMatch

Minimum number of matches to trigger identification.

`minMatch`

*   is optional

*   Type: `integer` ([Min match](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-min-match.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-min-match.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items/properties/minMatch")

### minMatch Type

`integer` ([Min match](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-min-match.md))

## maxMismatch

Maximum number of mismatches

`maxMismatch`

*   is optional

*   Type: `integer` ([Max mismatch](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-max-mismatch.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-max-mismatch.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items/properties/maxMismatch")

### maxMismatch Type

`integer` ([Max mismatch](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-max-mismatch.md))

## matchEdge

Where the match should occur. Changes the rules on how minMatch and maxMismatch are counted.

`matchEdge`

*   is optional

*   Type: `string` ([Match edge](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls/items/properties/matchEdge")

### matchEdge Type

`string` ([Match edge](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall-properties-match-edge.md))

### matchEdge Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation                                                                                                                                |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| `"full"`  | Only @maxMismatch influences matching process                                                                                              |
| `"start"` | Both matches and mismatches are counted. When @maxMismatch is exceeded - it is not a match. When @minMatch is reached - match is declared. |
| `"end"`   | Both matches and mismatches are counted. When @maxMismatch is exceeded - it is not a match. When @minMatch is reached - match is declared. |
