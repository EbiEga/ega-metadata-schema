# Read spec Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Read spec](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec.md))

# items Properties

| Property                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [readIndex](#readindex)                         | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-index.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/readIndex")                          |
| [readLabel](#readlabel)                         | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-label.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/readLabel")                          |
| [readClass](#readclass)                         | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-class.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/readClass")                          |
| [readType](#readtype)                           | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/readType")                            |
| [relativeOrder](#relativeorder)                 | `object`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/relativeOrder")                  |
| [baseCoord](#basecoord)                         | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-base-coord.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/baseCoord")                          |
| [expectedBasecallTable](#expectedbasecalltable) | `object`  | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable") |

## readIndex

READ\_INDEX starts at 0 and is incrementally increased for each sequential READ\_SPEC within a SPOT\_DECODE\_SPEC.

`readIndex`

*   is optional

*   Type: `string` ([Read index](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-index.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/readIndex")

### readIndex Type

`string` ([Read index](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-index.md))

### readIndex Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## readLabel

READ\_LABEL is a name for this tag, and can be used to on output to determine read name, for example F or R.

`readLabel`

*   is optional

*   Type: `string` ([Read label](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-label.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-label.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/readLabel")

### readLabel Type

`string` ([Read label](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-label.md))

### readLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## readClass



`readClass`

*   is optional

*   Type: `string` ([Read class](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-class.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-class.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/readClass")

### readClass Type

`string` ([Read class](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-class.md))

### readClass Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                | Explanation |
| :------------------- | :---------- |
| `"Application Read"` |             |
| `"Technical Read"`   |             |

## readType



`readType`

*   is optional

*   Type: `string` ([Read type](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/readType")

### readType Type

`string` ([Read type](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md))

### readType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"Forward"` |             |
| `"Reverse"` |             |
| `"Adapter"` |             |
| `"Primer"`  |             |
| `"Linker"`  |             |
| `"BarCode"` |             |
| `"Other"`   |             |

## relativeOrder

The read is located beginning at the offset or cycle relative to another read. This choice is appropriate for example when specifying a read that follows a variable length expected sequence(s).

`relativeOrder`

*   is optional

*   Type: `object` ([Relative order](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/relativeOrder")

### relativeOrder Type

`object` ([Relative order](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md))

## baseCoord

The location of the read start in terms of base count (1 is beginning of spot)

`baseCoord`

*   is optional

*   Type: `integer` ([Base coord](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-base-coord.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-base-coord.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/baseCoord")

### baseCoord Type

`integer` ([Base coord](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-base-coord.md))

## expectedBasecallTable

A set of choices of expected basecalls for a current read. Read will be zero-length if none is found.

`expectedBasecallTable`

*   is optional

*   Type: `object` ([Expected basecall table](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/expectedBasecallTable")

### expectedBasecallTable Type

`object` ([Expected basecall table](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md))
