# EGA Controlled Vocabulary (CV) for assay subtypes by sequencer \[EFO:0003740] Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_sequencer.json
```

Controlled Vocabulary (CV) list for assay subtypes by sequencer: any ontologized term for a subtype (i.e. child ontology) of an sequencing assay \[EFO:0003740]. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.cv.assay\_subtype\_by\_sequencer.json](../../../schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_sequencer.json "open original schema") |

## EGA Controlled Vocabulary (CV) for assay subtypes by sequencer \[EFO:0003740] Type

`string` ([EGA Controlled Vocabulary (CV) for assay subtypes by sequencer \[EFO:0003740\]](ega-4.md))

## EGA Controlled Vocabulary (CV) for assay subtypes by sequencer \[EFO:0003740] Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                                     | Explanation    |
| :-------------------------------------------------------- | :------------- |
| `"bulk immune repertoire sequencing"`                     | \[EFO:0030014] |
| `"HTGTS-Rep-seq"`                                         | \[EFO:0010017] |
| `"Ig-Seq"`                                                | \[EFO:0008777] |
| `"Paired VH:VL Antibody Repertoire Analysis"`             | \[EFO:0008842] |
| `"Rep-Seq"`                                               | \[EFO:0008887] |
| `"single cell immune repertoire sequencing"`              | \[EFO:0030015] |
| `"10x immune profiling"`                                  | \[EFO:0010713] |
| `"10x Ig enrichment"`                                     | \[EFO:0010715] |
| `"10x TCR enrichment"`                                    | \[EFO:0010714] |
| `"TCR Chain Paring"`                                      | \[EFO:0008966] |
| `"MC-Hi-C"`                                               | \[EFO:0009980] |
| `"CUT&RUN"`                                               | \[EFO:0009973] |
| `"DNA-seq"`                                               | \[EFO:0002693] |
| `"ATAC-seq"`                                              | \[EFO:0007045] |
| `"Fast-ATAC"`                                             | \[EFO:0008736] |
| `"scATAC-seq"`                                            | \[EFO:0010891] |
| `"10x multiome"`                                          | \[EFO:0030059] |
| `"10x scATAC-seq"`                                        | \[EFO:0030007] |
| `"scATAC-seq (Microfluidics)"`                            | \[EFO:0008904] |
| `"scATAC-seq (cell index)"`                               | \[EFO:0008925] |
| `"massively parallel signature sequencing"`               | \[EFO:0010805] |
| `"DNase Hi-C"`                                            | \[EFO:0009976] |
| `"GAM"`                                                   | \[EFO:0009987] |
| `"IP-seq"`                                                | \[EFO:0005032] |
| `"Bru-Seq"`                                               | \[EFO:0008661] |
| `"CLIP-seq"`                                              | \[EFO:0003143] |
| `"ChIP-exo"`                                              | \[EFO:0005302] |
| `"ChIP-seq"`                                              | \[EFO:0002692] |
| `"Chia-PET"`                                              | \[EFO:0008684] |
| `"PLAC-seq"`                                              | \[EFO:0009981] |
| `"RIP-seq"`                                               | \[EFO:0005310] |
| `"Repli-Seq"`                                             | \[EFO:0008889] |
| `"2-stage Repli-seq"`                                     | \[EFO:0009969] |
| `"multi-stage Repli-seq"`                                 | \[EFO:0009970] |
| `"eCLIP"`                                                 | \[EFO:0009998] |
| `"irCLIP"`                                                | \[EFO:0010008] |
| `"MARGI"`                                                 | \[EFO:0009988] |
| `"MBD-seq"`                                               | \[EFO:0003750] |
| `"MeDIP-seq"`                                             | \[EFO:0003749] |
| `"Micro-C XL"`                                            | \[EFO:0008808] |
| `"NAD-seq"`                                               | \[EFO:0009972] |
| `"RNA-Seq"`                                               | \[EFO:0008896] |
| `"SPRITE"`                                                | \[EFO:0009984] |
| `"DNA SPRITE"`                                            | \[EFO:0009985] |
| `"RNA-DNA SPRITE"`                                        | \[EFO:0009986] |
| `"TSA-seq"`                                               | \[EFO:0009971] |
| `"TraDIS sequencing"`                                     | \[EFO:0005219] |
| `"Trac-Loop"`                                             | \[EFO:0009982] |
| `"dilution HiC"`                                          | \[EFO:0009975] |
| `"exome sequencing"`                                      | \[EFO:0005396] |
| `"genotyping by high throughput sequencing"`              | \[EFO:0002771] |
| `"in situ HiC"`                                           | \[EFO:0009974] |
| `"methylation profiling by high throughput sequencing"`   | \[EFO:0002761] |
| `"snmC-Seq2"`                                             | \[EFO:0030027] |
| `"pooled clone sequencing"`                               | \[EFO:0003741] |
| `"sci-Hi-C"`                                              | \[EFO:0009977] |
| `"single cell Hi-C"`                                      | \[EFO:0009979] |
| `"sn-Hi-C"`                                               | \[EFO:0009978] |
| `"spatial transcriptomics by high-throughput sequencing"` | \[EFO:0030005] |
| `"NanoString digital spatial profiling"`                  | \[EFO:0030029] |
| `"Slide-seq"`                                             | \[EFO:0009920] |
| `"Slide-seqV2"`                                           | \[EFO:0030062] |
| `"Visium Spatial Gene Expression"`                        | \[EFO:0010961] |
| `"transcription profiling by high throughput sequencing"` | \[EFO:0002770] |
| `"Quant-seq"`                                             | \[EFO:0030030] |
| `"RNA-seq of coding RNA"`                                 | \[EFO:0003738] |
| `"RNA-seq of coding RNA from single cells"`               | \[EFO:0005684] |
| `"RNA-seq of non coding RNA"`                             | \[EFO:0003737] |
| `"RNA-seq of non coding RNA from single cells"`           | \[EFO:0005685] |
| `"microRNA profiling by high throughput sequencing"`      | \[EFO:0002896] |
| `"RNA-seq of total RNA"`                                  | \[EFO:0009653] |
| `"random RNA-Seq across whole transcriptome"`             | \[EFO:0004158] |
| `"single cell sequencing"`                                | \[EFO:0007832] |
| `"full length single cell RNA sequencing"`                | \[EFO:0008441] |
| `"tag based single cell RNA sequencing"`                  | \[EFO:0008440] |
| `"single nucleus RNA sequencing"`                         | \[EFO:0009809] |
| `"full length single nucleus RNA sequencing"`             | \[EFO:0009810] |
| `"tag based single nucleus RNA sequencing"`               | \[EFO:0009811] |
| `"whole chromosome random sequencing"`                    | \[EFO:0004160] |
| `"16S metagenomic sequencing"`                            | \[EFO:0030055] |
| `"gRNA-seq"`                                              | \[EFO:0030033] |
| `"shRNA-seq"`                                             | \[EFO:0030034] |
| `"Capture-HiC"`                                           | \[EFO:0008674] |
| `"scDNase-seq"`                                           | \[EFO:0008907] |
