# Relative order Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/relativeOrder
```

The read is located beginning at the offset or cycle relative to another read. This choice is appropriate for example when specifying a read that follows a variable length expected sequence(s).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## relativeOrder Type

`object` ([Relative order](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md))

# relativeOrder Properties

| Property                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                   |
| :-------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [followsReadIndex](#followsreadindex)   | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-follows-read-index.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/relativeOrder/properties/followsReadIndex")   |
| [precedesReadIndex](#precedesreadindex) | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-precedes-read-index.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/relativeOrder/properties/precedesReadIndex") |

## followsReadIndex

Specify the read index that precedes this read.

`followsReadIndex`

*   is optional

*   Type: `integer` ([Follows read index](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-follows-read-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-follows-read-index.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/relativeOrder/properties/followsReadIndex")

### followsReadIndex Type

`integer` ([Follows read index](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-follows-read-index.md))

## precedesReadIndex

Specify the read index that follows this read.

`precedesReadIndex`

*   is optional

*   Type: `integer` ([Precedes read index](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-precedes-read-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-precedes-read-index.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs/items/properties/relativeOrder/properties/precedesReadIndex")

### precedesReadIndex Type

`integer` ([Precedes read index](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-precedes-read-index.md))
