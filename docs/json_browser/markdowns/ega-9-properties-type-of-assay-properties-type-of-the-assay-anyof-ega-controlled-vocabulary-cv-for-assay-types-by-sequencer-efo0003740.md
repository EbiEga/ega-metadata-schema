# EGA Controlled Vocabulary (CV) for assay types by sequencer \[EFO:0003740] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_sequencer.json#/properties/assay_type_descriptor/properties/assay_type/anyOf/0
```

Controlled Vocabulary (CV) list for assay types by sequencer \[EFO:0003740]: an assay that exploits a sequencer as the instrument to find results.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## 0 Type

`string` ([EGA Controlled Vocabulary (CV) for assay types by sequencer \[EFO:0003740\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-sequencer-efo0003740.md))

## 0 Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                  | Explanation |
| :------------------------------------- | :---------- |
| `"454 Sequencing"`                     |             |
| `"5C"`                                 |             |
| `"Bisulfite-seq"`                      |             |
| `"CTS (Concatenated Tag Sequencing)"`  |             |
| `"Capture-C"`                          |             |
| `"DNase-hypersensitivity seq"`         |             |
| `"EST sequencing"`                     |             |
| `"FAIRE-seq"`                          |             |
| `"FL-cDNA"`                            |             |
| `"GRO-seq"`                            |             |
| `"Helicos sequencing"`                 |             |
| `"Hi-C"`                               |             |
| `"MNase-seq"`                          |             |
| `"MRE-seq"`                            |             |
| `"Ribo-seq"`                           |             |
| `"Solexa sequencing assay"`            |             |
| `"amplicon sequencing"`                |             |
| `"assay by high throughput sequencer"` |             |
| `"assay by long read sequencer"`       |             |
| `"clone by clone sequencing"`          |             |
| `"clone end sequencing"`               |             |
| `"finishing sequencing assay"`         |             |
| `"immune sequencing"`                  |             |
| `"random chromosome sequencing"`       |             |
| `"random exon sequencing"`             |             |
| `"whole genome shotgun sequencing"`    |             |
