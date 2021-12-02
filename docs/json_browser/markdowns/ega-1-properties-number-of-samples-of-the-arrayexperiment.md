# Number of samples of the ArrayExperiment Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/sample_number
```

Number of samples included in the experiment. One sample corresponds to one biological replicate \[EFO:0002091] (it could be the genetic content from a single cell, a tissue… from a single individual or from several individuals). Shall not be mistaken for technical replicates \[CHEBI:24432] being used several times (see <https://www.ebi.ac.uk/seqdb/confluence/pages/viewpage.action?spaceKey=EGA&title=Sample+Representation>).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## sample_number Type

`integer` ([Number of samples of the ArrayExperiment](ega-1-properties-number-of-samples-of-the-arrayexperiment.md))

## sample_number Examples

```json
30
```
