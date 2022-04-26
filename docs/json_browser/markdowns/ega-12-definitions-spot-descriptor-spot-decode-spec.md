# Spot decode spec Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Spot decode spec](ega-12-definitions-spot-descriptor-spot-decode-spec.md))

# items Properties

| Property                     | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                               |
| :--------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [spot\_length](#spot_length) | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-spot-length.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/spot_length") |
| [read\_specs](#read_specs)   | `array`   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs")   |

## spot\_length

Number of base/color calls, cycles, or flows per spot (raw sequence length or flow length including all application and technical tags and mate pairs, but not including gap lengths). This value will be platform dependent, library dependent, and possibly run dependent. Variable length platforms will still have a constant flow/cycle length.

`spot_length`

*   is optional

*   Type: `integer` ([Spot length](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-spot-length.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-spot-length.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/spot_length")

### spot\_length Type

`integer` ([Spot length](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-spot-length.md))

## read\_specs



`read_specs`

*   is required

*   Type: `object[]` ([Read spec](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/spot_descriptor/items/properties/read_specs")

### read\_specs Type

`object[]` ([Read spec](ega-12-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec.md))

### read\_specs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
