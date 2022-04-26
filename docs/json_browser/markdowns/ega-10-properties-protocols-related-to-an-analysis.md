# Protocols related to an analysis Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_protocols
```

Comprises metadata (e.g. Type of protocol) of a plan specification executed during an analysis. It shall have a sufficient level of detail and quantitative information to communicate it (and thus reproduce it) between investigation agents.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## analysis\_protocols Type

`object[]` ([EGA Protocols object](ega-12-definitions-ega-protocols-object.md))

## analysis\_protocols Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
