# Sequencing library layout Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/sequencing_experiment/properties/library_layout
```

Whether the sequenced reads are paired or single. In other words, if the sequencing assay is paired- (OBI:0001850) or single-end (OBI:0002485). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## library_layout Type

`string` ([Sequencing library layout](ega-12-definitions-sequencing-library-layout.md))

## library_layout Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"paired-end"` |             |
| `"single-end"` |             |
