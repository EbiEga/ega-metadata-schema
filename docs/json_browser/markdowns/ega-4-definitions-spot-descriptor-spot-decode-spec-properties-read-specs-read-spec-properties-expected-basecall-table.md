# Expected basecall table Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable
```

A set of choices of expected basecalls for a current read. Read will be zero-length if none is found.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## expectedBasecallTable Type

`object` ([Expected basecall table](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md))

# expectedBasecallTable Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                           |
| :------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [defaultLength](#defaultlength) | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-default-length.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/defaultLength") |
| [baseCoord](#basecoord)         | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-base-coord.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/baseCoord")         |
| [basecalls](#basecalls)         | `array`   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls")    |

## defaultLength

Specify whether the spot should have a default length for this tag if the expected base cannot be matched.

`defaultLength`

*   is optional

*   Type: `integer` ([Default length](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-default-length.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-default-length.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/defaultLength")

### defaultLength Type

`integer` ([Default length](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-default-length.md))

## baseCoord

Specify an optional starting point for tag (base offset from 1).

`baseCoord`

*   is optional

*   Type: `integer` ([Base coord](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-base-coord.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-base-coord.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/baseCoord")

### baseCoord Type

`integer` ([Base coord](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-base-coord.md))

## basecalls

Element's body contains a basecall, attribute provide description of this read meaning as well as matching rules.

`basecalls`

*   is required

*   Type: `object[]` ([Basecall](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable/properties/basecalls")

### basecalls Type

`object[]` ([Basecall](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall.md))

### basecalls Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
