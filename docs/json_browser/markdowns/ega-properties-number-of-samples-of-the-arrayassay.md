# Number of samples of the ArrayAssay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayAssay.json#/properties/sample_number
```

Number of samples included in the Assay (i.e. pooled into one single microarray, labelled differently). One sample corresponds to one biological replicate \[EFO:0002091] (e.g. genetic content from a single cell, a tissue, buccal swab, etc.) from a single individual or from several individuals. Shall not be mistaken for technical replicates \[EFO:0002090] being used several times (see <https://www.ebi.ac.uk/seqdb/confluence/pages/viewpage.action?spaceKey=EGA&title=Sample+Representation>).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayAssay.json*](../out/EGA.ArrayAssay.json "open original schema") |

## sample_number Type

`integer` ([Number of samples of the ArrayAssay](ega-properties-number-of-samples-of-the-arrayassay.md))

## sample_number Examples

```json
30
```
