# Spot length Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/spotDescriptor/items/properties/spotLength
```

Number of base/color calls, cycles, or flows per spot (raw sequence length or flow length including all application and technical tags and mate pairs, but not including gap lengths). This value will be platform dependent, library dependent, and possibly run dependent. Variable length platforms will still have a constant flow/cycle length.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## spotLength Type

`integer` ([Spot length](ega-4-definitions-spot-descriptor-spot-decode-spec-properties-spot-length.md))
