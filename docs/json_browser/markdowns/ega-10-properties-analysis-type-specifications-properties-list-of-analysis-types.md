# List of analysis types Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.analysis.json#/properties/analysis_type_specifications/properties/analysis_types
```

Array of all analysis types applicable to this analysis. Details on how the analysis was performed (instruments, software, procedure...) shall be included in the 'analysis\_protocols' field, not here. For example, if the analysis includes sequence variation files (e.g. VCF) that were obtained by a sequencing assay (i.e. from the sequenced reads), at least the analysis type 'sequence variation' would be expected. Furthermore, depending on the types of analysis, different details may be required (e.g. reference sequence details in a 'sequence alignment' type).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## analysis\_types Type

`string[]` ([Type of analysis](ega-10-properties-analysis-type-specifications-properties-list-of-analysis-types-type-of-analysis.md))

## analysis\_types Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
