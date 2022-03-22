# Relative order Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/relative_order
```

The read is located beginning at the offset or cycle relative to another read. This choice is appropriate for example when specifying a read that follows a variable length expected sequence(s).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## relative_order Type

`object` ([Relative order](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md))

# relative_order Properties

| Property                                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [follows_read_index](#follows_read_index)   | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-follows-read-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/relative_order/properties/follows_read_index")   |
| [precedes_read_index](#precedes_read_index) | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-precedes_read_index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/relative_order/properties/precedes_read_index") |

## follows_read_index

Specify the read index that precedes this read.

`follows_read_index`

*   is optional

*   Type: `integer` ([Follows read index](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-follows-read-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-follows-read-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/relative_order/properties/follows_read_index")

### follows_read_index Type

`integer` ([Follows read index](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-follows-read-index.md))

## precedes_read_index

Specify the read index that follows this read.

`precedes_read_index`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order-properties-precedes_read_index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/relative_order/properties/precedes_read_index")

### precedes_read_index Type

`integer`
