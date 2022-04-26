# EGA Controlled Vocabulary (CV) for assay types by sequencer \[EFO:0003740] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_sequencer.json#/properties/assay_type_descriptor/properties/assay_type/anyOf/0
```

Controlled Vocabulary (CV) list for assay types by sequencer \[EFO:0003740]: an assay that exploits a sequencer as the instrument to find results. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## 0 Type

`string` ([EGA Controlled Vocabulary (CV) for assay types by sequencer \[EFO:0003740\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-sequencer-efo0003740.md))

## 0 Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                  | Explanation    |
| :------------------------------------- | :------------- |
| `"454 Sequencing"`                     | \[EFO:0005016] |
| `"5C"`                                 | \[EFO:0007692] |
| `"Bisulfite-seq"`                      | \[EFO:0003753] |
| `"CTS (Concatenated Tag Sequencing)"`  | \[EFO:0004162] |
| `"Capture-C"`                          | \[EFO:0007691] |
| `"DNase-hypersensitivity seq"`         | \[EFO:0003752] |
| `"EST sequencing"`                     | \[EFO:0003754] |
| `"FAIRE-seq"`                          | \[EFO:0004428] |
| `"FL-cDNA"`                            | \[EFO:0003755] |
| `"GRO-seq"`                            | \[EFO:0005227] |
| `"Helicos sequencing"`                 | \[OBI:0000697] |
| `"Hi-C"`                               | \[EFO:0007693] |
| `"MNase-seq"`                          | \[EFO:0003751] |
| `"MRE-seq"`                            | \[EFO:0003748] |
| `"Ribo-seq"`                           | \[EFO:0008891] |
| `"Solexa sequencing assay"`            | \[OBI:0000724] |
| `"amplicon sequencing"`                | \[EFO:0003747] |
| `"assay by high throughput sequencer"` | \[EFO:0002697] |
| `"assay by long read sequencer"`       | \[EFO:0009966] |
| `"clone by clone sequencing"`          | \[EFO:0003742] |
| `"clone end sequencing"`               | \[EFO:0003743] |
| `"finishing sequencing assay"`         | \[EFO:0004161] |
| `"immune sequencing"`                  | \[EFO:0030006] |
| `"random chromosome sequencing"`       | \[EFO:0003745] |
| `"random exon sequencing"`             | \[EFO:0003746] |
| `"whole genome shotgun sequencing"`    | \[EFO:0003744] |
