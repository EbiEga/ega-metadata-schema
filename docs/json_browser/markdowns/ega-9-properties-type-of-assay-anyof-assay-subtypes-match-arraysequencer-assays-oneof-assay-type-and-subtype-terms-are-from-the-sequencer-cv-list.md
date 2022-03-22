# Assay type and subtype terms are from the sequencer CV list Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/anyOf/1/oneOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## 1 Type

unknown ([Assay type and subtype terms are from the sequencer CV list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-sequencer-cv-list.md))

# 1 Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :------------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [assay_type](#assay_type)       | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-sequencer-efo0003740.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_sequencer.json#/properties/assay_type_descriptor/anyOf/1/oneOf/1/properties/assay_type")                                                                                                     |
| [assay_subtype](#assay_subtype) | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-sequencer-cv-list-properties-ega-controlled-vocabulary-cv-for-assay-subtypes-by-sequencer-efo0003740.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_sequencer.json#/properties/assay_type_descriptor/anyOf/1/oneOf/1/properties/assay_subtype") |

## assay_type

Controlled Vocabulary (CV) list for assay types by sequencer \[EFO:0003740]: an assay that exploits a sequencer as the instrument to find results.

`assay_type`

*   is optional

*   Type: `string` ([EGA Controlled Vocabulary (CV) for assay types by sequencer \[EFO:0003740\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-sequencer-efo0003740.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-sequencer-efo0003740.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_sequencer.json#/properties/assay_type_descriptor/anyOf/1/oneOf/1/properties/assay_type")

### assay_type Type

`string` ([EGA Controlled Vocabulary (CV) for assay types by sequencer \[EFO:0003740\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-sequencer-efo0003740.md))

### assay_type Constraints

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

## assay_subtype

Controlled Vocabulary (CV) list for assay subtypes by sequencer: any ontologized term for a subtype (i.e. child ontology) of an sequencing assay \[EFO:0003740].

`assay_subtype`

*   is optional

*   Type: `string` ([EGA Controlled Vocabulary (CV) for assay subtypes by sequencer \[EFO:0003740\]](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-sequencer-cv-list-properties-ega-controlled-vocabulary-cv-for-assay-subtypes-by-sequencer-efo0003740.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-sequencer-cv-list-properties-ega-controlled-vocabulary-cv-for-assay-subtypes-by-sequencer-efo0003740.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_sequencer.json#/properties/assay_type_descriptor/anyOf/1/oneOf/1/properties/assay_subtype")

### assay_subtype Type

`string` ([EGA Controlled Vocabulary (CV) for assay subtypes by sequencer \[EFO:0003740\]](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-sequencer-cv-list-properties-ega-controlled-vocabulary-cv-for-assay-subtypes-by-sequencer-efo0003740.md))

### assay_subtype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                                     | Explanation |
| :-------------------------------------------------------- | :---------- |
| `"bulk immune repertoire sequencing"`                     |             |
| `"HTGTS-Rep-seq"`                                         |             |
| `"Ig-Seq"`                                                |             |
| `"Paired VH:VL Antibody Repertoire Analysis"`             |             |
| `"Rep-Seq"`                                               |             |
| `"single cell immune repertoire sequencing"`              |             |
| `"10x immune profiling"`                                  |             |
| `"10x Ig enrichment"`                                     |             |
| `"10x TCR enrichment"`                                    |             |
| `"TCR Chain Paring"`                                      |             |
| `"MC-Hi-C"`                                               |             |
| `"CUT&RUN"`                                               |             |
| `"DNA-seq"`                                               |             |
| `"ATAC-seq"`                                              |             |
| `"Fast-ATAC"`                                             |             |
| `"scATAC-seq"`                                            |             |
| `"10x multiome"`                                          |             |
| `"10x scATAC-seq"`                                        |             |
| `"scATAC-seq (Microfluidics)"`                            |             |
| `"scATAC-seq (cell index)"`                               |             |
| `"massively parallel signature sequencing"`               |             |
| `"DNase Hi-C"`                                            |             |
| `"GAM"`                                                   |             |
| `"IP-seq"`                                                |             |
| `"Bru-Seq"`                                               |             |
| `"CLIP-seq"`                                              |             |
| `"ChIP-exo"`                                              |             |
| `"ChIP-seq"`                                              |             |
| `"Chia-PET"`                                              |             |
| `"PLAC-seq"`                                              |             |
| `"RIP-seq"`                                               |             |
| `"Repli-Seq"`                                             |             |
| `"2-stage Repli-seq"`                                     |             |
| `"multi-stage Repli-seq"`                                 |             |
| `"eCLIP"`                                                 |             |
| `"irCLIP"`                                                |             |
| `"MARGI"`                                                 |             |
| `"MBD-seq"`                                               |             |
| `"MeDIP-seq"`                                             |             |
| `"Micro-C XL"`                                            |             |
| `"NAD-seq"`                                               |             |
| `"RNA-Seq"`                                               |             |
| `"SPRITE"`                                                |             |
| `"DNA SPRITE"`                                            |             |
| `"RNA-DNA SPRITE"`                                        |             |
| `"TSA-seq"`                                               |             |
| `"TraDIS sequencing"`                                     |             |
| `"Trac-Loop"`                                             |             |
| `"dilution HiC"`                                          |             |
| `"exome sequencing"`                                      |             |
| `"genotyping by high throughput sequencing"`              |             |
| `"in situ HiC"`                                           |             |
| `"methylation profiling by high throughput sequencing"`   |             |
| `"snmC-Seq2"`                                             |             |
| `"pooled clone sequencing"`                               |             |
| `"sci-Hi-C"`                                              |             |
| `"single cell Hi-C"`                                      |             |
| `"sn-Hi-C"`                                               |             |
| `"spatial transcriptomics by high-throughput sequencing"` |             |
| `"NanoString digital spatial profiling"`                  |             |
| `"Slide-seq"`                                             |             |
| `"Slide-seqV2"`                                           |             |
| `"Visium Spatial Gene Expression"`                        |             |
| `"transcription profiling by high throughput sequencing"` |             |
| `"Quant-seq"`                                             |             |
| `"RNA-seq of coding RNA"`                                 |             |
| `"RNA-seq of coding RNA from single cells"`               |             |
| `"RNA-seq of non coding RNA"`                             |             |
| `"RNA-seq of non coding RNA from single cells"`           |             |
| `"microRNA profiling by high throughput sequencing"`      |             |
| `"RNA-seq of total RNA"`                                  |             |
| `"random RNA-Seq across whole transcriptome"`             |             |
| `"single cell sequencing"`                                |             |
| `"full length single cell RNA sequencing"`                |             |
| `"tag based single cell RNA sequencing"`                  |             |
| `"single nucleus RNA sequencing"`                         |             |
| `"full length single nucleus RNA sequencing"`             |             |
| `"tag based single nucleus RNA sequencing"`               |             |
| `"whole chromosome random sequencing"`                    |             |
| `"16S metagenomic sequencing"`                            |             |
| `"gRNA-seq"`                                              |             |
| `"shRNA-seq"`                                             |             |
| `"Capture-HiC"`                                           |             |
| `"scDNase-seq"`                                           |             |
