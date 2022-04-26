# Read spec Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Read spec](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec.md))

# items Properties

| Property                                              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read\_index](#read_index)                            | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/read_index")                           |
| [read\_label](#read_label)                            | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-label.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/read_label")                           |
| [read\_class](#read_class)                            | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-class.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/read_class")                           |
| [read\_type](#read_type)                              | `string`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/read_type")                             |
| [relative\_order](#relative_order)                    | `object`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/relative_order")                   |
| [base\_coord](#base_coord)                            | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-base-coord.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/base_coord")                           |
| [expected\_basecall\_table](#expected_basecall_table) | `object`  | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table") |

## read\_index

READ\_INDEX starts at 0 and is incrementally increased for each sequential READ\_SPEC within a SPOT\_DECODE\_SPEC.

`read_index`

*   is optional

*   Type: `string` ([Read index](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-index.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-index.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/read_index")

### read\_index Type

`string` ([Read index](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-index.md))

## read\_label

READ\_LABEL is a name for this tag, and can be used to on output to determine read name, for example F or R.

`read_label`

*   is optional

*   Type: `string` ([Read label](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-label.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-label.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/read_label")

### read\_label Type

`string` ([Read label](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-label.md))

## read\_class



`read_class`

*   is optional

*   Type: `string` ([Read class](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-class.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-class.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/read_class")

### read\_class Type

`string` ([Read class](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-class.md))

### read\_class Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                | Explanation |
| :------------------- | :---------- |
| `"Application Read"` |             |
| `"Technical Read"`   |             |

## read\_type



`read_type`

*   is optional

*   Type: `string` ([Read type](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/read_type")

### read\_type Type

`string` ([Read type](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-read-type.md))

### read\_type Constraints

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

## relative\_order

The read is located beginning at the offset or cycle relative to another read. This choice is appropriate for example when specifying a read that follows a variable length expected sequence(s).

`relative_order`

*   is optional

*   Type: `object` ([Relative order](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/relative_order")

### relative\_order Type

`object` ([Relative order](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-relative-order.md))

## base\_coord

The location of the read start in terms of base count (1 is beginning of spot)

`base_coord`

*   is optional

*   Type: `integer` ([Base coord](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-base-coord.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-base-coord.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/base_coord")

### base\_coord Type

`integer` ([Base coord](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-base-coord.md))

## expected\_basecall\_table

A set of choices of expected basecalls for a current read. Read will be zero-length if none is found.

`expected_basecall_table`

*   is optional

*   Type: `object` ([Expected basecall table](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table")

### expected\_basecall\_table Type

`object` ([Expected basecall table](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md))
