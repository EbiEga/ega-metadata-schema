# Expected basecall table Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table
```

A set of choices of expected basecalls for a current read. Read will be zero-length if none is found.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## expected_basecall_table Type

`object` ([Expected basecall table](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table.md))

# expected_basecall_table Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                       |
| :-------------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [default_length](#default_length) | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-default-length.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/default_length") |
| [base_coord](#base_coord)         | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-base-coord.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/base_coord")         |
| [basecalls](#basecalls)           | `array`   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls")     |

## default_length

Specify whether the spot should have a default length for this tag if the expected base cannot be matched.

`default_length`

*   is optional

*   Type: `integer` ([Default length](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-default-length.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-default-length.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/default_length")

### default_length Type

`integer` ([Default length](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-default-length.md))

## base_coord

Specify an optional starting point for tag (base offset from 1).

`base_coord`

*   is optional

*   Type: `integer` ([Base coord](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-base-coord.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-base-coord.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/base_coord")

### base_coord Type

`integer` ([Base coord](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-base-coord.md))

## basecalls

Element's body contains a basecall, attribute provide description of this read meaning as well as matching rules.

`basecalls`

*   is required

*   Type: `object[]` ([Basecall](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs/items/properties/expected_basecall_table/properties/basecalls")

### basecalls Type

`object[]` ([Basecall](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec-properties-expected-basecall-table-properties-basecalls-array-basecall.md))

### basecalls Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
