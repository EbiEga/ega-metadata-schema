# Spot decode spec Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([Spot decode spec](ega-4-definitions-spot-descriptor-spot-decode-spec.md))

# items Properties

| Property                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                      |
| :------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [spotLength](#spotlength) | `integer` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-spot-length.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/spotLength") |
| [readSpecs](#readspecs)   | `array`   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs")   |

## spotLength

Number of base/color calls, cycles, or flows per spot (raw sequence length or flow length including all application and technical tags and mate pairs, but not including gap lengths). This value will be platform dependent, library dependent, and possibly run dependent. Variable length platforms will still have a constant flow/cycle length.

`spotLength`

*   is optional

*   Type: `integer` ([Spot length](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-spot-length.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-spot-length.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/spotLength")

### spotLength Type

`integer` ([Spot length](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-spot-length.md))

## readSpecs



`readSpecs`

*   is required

*   Type: `object[]` ([Read spec](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/readSpecs")

### readSpecs Type

`object[]` ([Read spec](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-read-specs-read-spec.md))

### readSpecs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
