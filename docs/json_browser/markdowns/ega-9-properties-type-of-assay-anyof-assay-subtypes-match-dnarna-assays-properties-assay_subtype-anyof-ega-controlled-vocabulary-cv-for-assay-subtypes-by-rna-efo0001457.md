# EGA Controlled Vocabulary (CV) for assay subtypes by RNA \[EFO:0001457] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_rna.json#/properties/assay_type_descriptor/anyOf/0/properties/assay_subtype/anyOf/1
```

Controlled Vocabulary (CV) list for assay subtypes by the assayed molecule being RNA: any ontologized term for a subtype (i.e. child ontology) of a RNA assay \[EFO:0001457]. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## 1 Type

`string` ([EGA Controlled Vocabulary (CV) for assay subtypes by RNA \[EFO:0001457\]](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assay_subtype-anyof-ega-controlled-vocabulary-cv-for-assay-subtypes-by-rna-efo0001457.md))

## 1 Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                                     | Explanation    |
| :-------------------------------------------------------- | :------------- |
| `"10x immune profiling"`                                  | \[EFO:0010713] |
| `"10x Ig enrichment"`                                     | \[EFO:0010715] |
| `"10x TCR enrichment"`                                    | \[EFO:0010714] |
| `"10x scATAC-seq"`                                        | \[EFO:0030007] |
| `"2P-Seq"`                                                | \[EFO:0008639] |
| `"3'T-fill"`                                              | \[EFO:0008640] |
| `"3-Seq"`                                                 | \[EFO:0008645] |
| `"3P-Seq"`                                                | \[EFO:0008644] |
| `"3’-end-seq"`                                            | \[EFO:0008641] |
| `"3’NT method"`                                           | \[EFO:0008642] |
| `"3′-Seq"`                                                | \[EFO:0008643] |
| `"4sUDRB-seq"`                                            | \[EFO:0008646] |
| `"5PSeq"`                                                 | \[EFO:0008648] |
| `"5’-GRO-seq"`                                            | \[EFO:0008647] |
| `"AGO HITS-CLIP"`                                         | \[EFO:0010020] |
| `"AGO-CLIP"`                                              | \[EFO:0008651] |
| `"AGO-PAR-CLIP"`                                          | \[EFO:0010024] |
| `"BRB-seq"`                                               | \[EFO:0011028] |
| `"BRIC-seq"`                                              | \[EFO:0008660] |
| `"BrdU-CLIP"`                                             | \[EFO:0008658] |
| `"Bru-Seq"`                                               | \[EFO:0008661] |
| `"BruChase-Seq"`                                          | \[EFO:0008662] |
| `"BruDRB-seq"`                                            | \[EFO:0008663] |
| `"BruUV-Seq"`                                             | \[EFO:0008664] |
| `"Bubble-Seq"`                                            | \[EFO:0009992] |
| `"CAGEscan"`                                              | \[EFO:0008669] |
| `"CEL-seq"`                                               | \[EFO:0008679] |
| `"CEL-seq2"`                                              | \[EFO:0010010] |
| `"CHART"`                                                 | \[EFO:0008681] |
| `"CIP-TAP"`                                               | \[EFO:0008688] |
| `"CIRS-seq"`                                              | \[EFO:0008690] |
| `"CITE-seq"`                                              | \[EFO:0009294] |
| `"CITE-seq (cell surface protein profiling)"`             | \[EFO:0030008] |
| `"CITE-seq (sample multiplexing)"`                        | \[EFO:0030009] |
| `"CLASH"`                                                 | \[EFO:0008693] |
| `"CLIP-seq"`                                              | \[EFO:0003143] |
| `"CLaP"`                                                  | \[EFO:0008692] |
| `"CapSeq"`                                                | \[EFO:0008673] |
| `"Cappable-Seq"`                                          | \[EFO:0010034] |
| `"CaptureSeq"`                                            | \[EFO:0008675] |
| `"ChIRP"`                                                 | \[EFO:0008687] |
| `"CirSeq"`                                                | \[EFO:0008691] |
| `"ClickSeq"`                                              | \[EFO:0008694] |
| `"CytoSeq"`                                               | \[EFO:0008703] |
| `"DLAF"`                                                  | \[EFO:0008712] |
| `"DMS-MapSeq"`                                            | \[EFO:0008713] |
| `"DMS-Seq"`                                               | \[EFO:0008714] |
| `"DP-Seq"`                                                | \[EFO:0008718] |
| `"DR-Seq"`                                                | \[EFO:0010005] |
| `"DeepCAGE"`                                              | \[EFO:0008708] |
| `"Digital RNA"`                                           | \[EFO:0008710] |
| `"Div-Seq"`                                               | \[EFO:0009309] |
| `"DroNc-seq"`                                             | \[EFO:0008720] |
| `"Drop-seq"`                                              | \[EFO:0008722] |
| `"EPIG-Seq"`                                              | \[EFO:0008731] |
| `"EST sequencing"`                                        | \[EFO:0003754] |
| `"FACS-seq"`                                              | \[EFO:0008735] |
| `"FAST-iCLIP"`                                            | \[EFO:0008737] |
| `"FISSEQ"`                                                | \[EFO:0008990] |
| `"FL-cDNA"`                                               | \[EFO:0003755] |
| `"FREQ-Seq"`                                              | \[EFO:0008746] |
| `"FRISCR"`                                                | \[EFO:0008747] |
| `"FRT-Seq"`                                               | \[EFO:0008748] |
| `"Frac-Seq"`                                              | \[EFO:0010035] |
| `"Frag-seq"`                                              | \[EFO:0008745] |
| `"Fusion-seq"`                                            | \[EFO:0008749] |
| `"G&T-Seq"`                                               | \[EFO:0009999] |
| `"GMUCT 1.0"`                                             | \[EFO:0008752] |
| `"GMUCT 2.0"`                                             | \[EFO:0008753] |
| `"GRIL-seq"`                                              | \[EFO:0008754] |
| `"GRO-CAP"`                                               | \[EFO:0008756] |
| `"GRO-seq"`                                               | \[EFO:0005227] |
| `"GTI-Seq"`                                               | \[EFO:0008759] |
| `"HITS-KIN"`                                              | \[EFO:0010036] |
| `"HITS-RAP"`                                              | \[EFO:0008766] |
| `"Hi-SCL"`                                                | \[EFO:0008763] |
| `"HiRes-Seq"`                                             | \[EFO:0010016] |
| `"ICE"`                                                   | \[EFO:0008773] |
| `"INTACT"`                                                | \[EFO:0010037] |
| `"ISS"`                                                   | \[EFO:0008989] |
| `"IVT-SAPAS"`                                             | \[EFO:0008783] |
| `"LM-Seq"`                                                | \[EFO:0008786] |
| `"M6A-RIP"`                                               | \[EFO:0008789] |
| `"MARGI"`                                                 | \[EFO:0009988] |
| `"MARIO"`                                                 | \[EFO:0008795] |
| `"MARS-seq"`                                              | \[EFO:0008796] |
| `"MATQ-seq"`                                              | \[EFO:0008797] |
| `"MeRIP-Seq"`                                             | \[EFO:0008803] |
| `"MiR‐CLIP"`                                              | \[EFO:0008815] |
| `"NET-Seq"`                                               | \[EFO:0008826] |
| `"NanoCAGE"`                                              | \[EFO:0008824] |
| `"Nanogrid RNA-Seq"`                                      | \[EFO:0008825] |
| `"Nascent-Seq"`                                           | \[EFO:0010041] |
| `"Nm-seq"`                                                | \[EFO:0008828] |
| `"Nuc-Seq"`                                               | \[EFO:0009991] |
| `"PAIR"`                                                  | \[EFO:0008841] |
| `"PAL-seq"`                                               | \[EFO:0008843] |
| `"PAPERCLIP"`                                             | \[EFO:0008844] |
| `"PAR-CLIP"`                                              | \[EFO:0008845] |
| `"PARE-Seq"`                                              | \[EFO:0008846] |
| `"PARIS"`                                                 | \[EFO:0008847] |
| `"PARS"`                                                  | \[EFO:0008848] |
| `"PARTE"`                                                 | \[EFO:0008849] |
| `"PAS-Seq"`                                               | \[EFO:0008850] |
| `"PASP"`                                                  | \[EFO:0010025] |
| `"PAT-Seq"`                                               | \[EFO:0008851] |
| `"PEAT"`                                                  | \[EFO:0008859] |
| `"PIP-Seq"`                                               | \[EFO:0008862] |
| `"PLATE-Seq"`                                             | \[EFO:0008863] |
| `"PRO-cap"`                                               | \[EFO:0008868] |
| `"PRO-seq"`                                               | \[EFO:0008869] |
| `"PSI-seq"`                                               | \[EFO:0008873] |
| `"PTB-Seq"`                                               | \[EFO:0008874] |
| `"Paired VH:VL Antibody Repertoire Analysis"`             | \[EFO:0008842] |
| `"Patch-seq"`                                             | \[EFO:0008853] |
| `"Perturb-Seq"`                                           | \[EFO:0008860] |
| `"Pol II CLIP"`                                           | \[EFO:0008865] |
| `"Poly(A)-ClickSeq"`                                      | \[EFO:0008866] |
| `"Pseudo-seq"`                                            | \[EFO:0008872] |
| `"Quartz-seq"`                                            | \[EFO:0008877] |
| `"RAP"`                                                   | \[EFO:0008880] |
| `"RARseq"`                                                | \[EFO:0008882] |
| `"RASL-seq"`                                              | \[EFO:0010003] |
| `"RBNS"`                                                  | \[EFO:0008884] |
| `"RESA"`                                                  | \[EFO:0010027] |
| `"RESA-CLIP"`                                             | \[EFO:0010026] |
| `"RIL-seq"`                                               | \[EFO:0008895] |
| `"RIP-Chip by array"`                                     | \[EFO:0005517] |
| `"RNA-DNA SPRITE"`                                        | \[EFO:0009986] |
| `"RNA-Seq"`                                               | \[EFO:0008896] |
| `"RNAi profiling by array"`                               | \[EFO:0001030] |
| `"RNAtag-Seq"`                                            | \[EFO:0008897] |
| `"RNET-seq"`                                              | \[EFO:0008898] |
| `"RPL"`                                                   | \[EFO:0008899] |
| `"Ribo-seq"`                                              | \[EFO:0008891] |
| `"RiboMeth-seq"`                                          | \[EFO:0008892] |
| `"SAPAS"`                                                 | \[EFO:0008902] |
| `"SC3-seq"`                                               | \[EFO:0008903] |
| `"SCRB-seq"`                                              | \[EFO:0010004] |
| `"mcSCRB-seq"`                                            | \[EFO:0030061] |
| `"SCTG"`                                                  | \[EFO:0010015] |
| `"SHAPE-MaP"`                                             | \[EFO:0008921] |
| `"SHAPE-Seq"`                                             | \[EFO:0008922] |
| `"SMA"`                                                   | \[EFO:0008929] |
| `"SMIT"`                                                  | \[EFO:0008934] |
| `"SMORE-Seq"`                                             | \[EFO:0008936] |
| `"SPARE"`                                                 | \[EFO:0008943] |
| `"SPET-seq"`                                              | \[EFO:0008945] |
| `"SPLASH"`                                                | \[EFO:0010029] |
| `"SPLiT-seq"`                                             | \[EFO:0009919] |
| `"SS3-Seq"`                                               | \[EFO:0008948] |
| `"STARmap"`                                               | \[EFO:0030000] |
| `"STRT-seq"`                                              | \[EFO:0008953] |
| `"STRT-seq-2i"`                                           | \[EFO:0008954] |
| `"SUPeR-seq"`                                             | \[EFO:0008956] |
| `"Seq-Well"`                                              | \[EFO:0008919] |
| `"Seq-Well S3"`                                           | \[EFO:0030019] |
| `"SeqZip"`                                                | \[EFO:0008920] |
| `"Smart-3Seq"`                                            | \[EFO:0010022] |
| `"Smart-seq"`                                             | \[EFO:0008930] |
| `"Smart-seq2"`                                            | \[EFO:0008931] |
| `"Start-seq"`                                             | \[EFO:0010045] |
| `"Structure-Seq"`                                         | \[EFO:0008955] |
| `"TAIL-seq"`                                              | \[EFO:0008960] |
| `"TARDIS"`                                                | \[EFO:0008962] |
| `"TATL-seq"`                                              | \[EFO:0008963] |
| `"TCR Chain Paring"`                                      | \[EFO:0008966] |
| `"TCR-LA-MC PCR"`                                         | \[EFO:0008967] |
| `"TIF-Seq"`                                               | \[EFO:0008970] |
| `"TIVA"`                                                  | \[EFO:0008971] |
| `"TL-seq"`                                                | \[EFO:0008972] |
| `"TRAP-Seq"`                                              | \[EFO:0008975] |
| `"TRIBE"`                                                 | \[EFO:0008976] |
| `"TSS Sequencing"`                                        | \[EFO:0008978] |
| `"Term-Seq"`                                              | \[EFO:0008968] |
| `"Tomo-Seq"`                                              | \[EFO:0008974] |
| `"UMI Method"`                                            | \[EFO:0008980] |
| `"VirCapSeq-VERT"`                                        | \[EFO:0008982] |
| `"YAMAT-Seq"`                                             | \[EFO:0008987] |
| `"cP-RNA-Seq"`                                            | \[EFO:0008697] |
| `"dRNA-Seq"`                                              | \[EFO:0008719] |
| `"dsRNA-Seq"`                                             | \[EFO:0008726] |
| `"eCLIP"`                                                 | \[EFO:0009998] |
| `"gSELEX-Seq"`                                            | \[EFO:0008757] |
| `"hi-CLIP"`                                               | \[EFO:0008762] |
| `"iCLIP"`                                                 | \[EFO:0008774] |
| `"icSHAPE"`                                               | \[EFO:0008775] |
| `"in-cell SHAPE-Seq"`                                     | \[EFO:0008779] |
| `"inDrop"`                                                | \[EFO:0008780] |
| `"irCLIP"`                                                | \[EFO:0010008] |
| `"m1A mapping"`                                           | \[EFO:0008788] |
| `"m6A-LAIC-seq"`                                          | \[EFO:0010019] |
| `"m6A-seq"`                                               | \[EFO:0008790] |
| `"mNET-seq"`                                              | \[EFO:0008819] |
| `"miCLIP-m5A"`                                            | \[EFO:0008806] |
| `"miCLIP-m6A"`                                            | \[EFO:0008807] |
| `"miTRAP"`                                                | \[EFO:0008818] |
| `"microRNA profiling by RT-PCR"`                          | \[EFO:0007687] |
| `"microRNA profiling by array"`                           | \[EFO:0000753] |
| `"rG4-seq"`                                               | \[EFO:0008890] |
| `"sNuc-Seq"`                                              | \[EFO:0008941] |
| `"sRNA-Seq"`                                              | \[EFO:0008947] |
| `"scM&T-seq"`                                             | \[EFO:0010006] |
| `"scRNA-seq"`                                             | \[EFO:0008913] |
| `"10x multiome"`                                          | \[EFO:0030059] |
| `"mCT-seq"`                                               | \[EFO:0030060] |
| `"scTrio-seq"`                                            | \[EFO:0010007] |
| `"smFISH"`                                                | \[EFO:0009918] |
| `"Ex-FISH"`                                               | \[EFO:0008993] |
| `"MERFISH"`                                               | \[EFO:0008992] |
| `"RNAscope"`                                              | \[EFO:0010965] |
| `"seqFISH"`                                               | \[EFO:0008991] |
| `"spatial transcriptomics"`                               | \[EFO:0008994] |
| `"spatial transcriptomics by high-throughput sequencing"` | \[EFO:0030005] |
| `"NanoString digital spatial profiling"`                  | \[EFO:0030029] |
| `"Slide-seq"`                                             | \[EFO:0009920] |
| `"Slide-seqV2"`                                           | \[EFO:0030062] |
| `"Visium Spatial Gene Expression"`                        | \[EFO:0010961] |
| `"ssRNA-seq"`                                             | \[EFO:0008950] |
| `"transcription profiling by array"`                      | \[EFO:0002768] |
| `"transcription profiling by high throughput sequencing"` | \[EFO:0002770] |
| `"Quant-seq"`                                             | \[EFO:0030030] |
| `"RNA-seq of coding RNA"`                                 | \[EFO:0003738] |
| `"RNA-seq of non coding RNA"`                             | \[EFO:0003737] |
| `"microRNA profiling by high throughput sequencing"`      | \[EFO:0002896] |
| `"RNA-seq of total RNA"`                                  | \[EFO:0009653] |
| `"random RNA-Seq across whole transcriptome"`             | \[EFO:0004158] |
| `"single cell sequencing"`                                | \[EFO:0007832] |
| `"RNA-seq of coding RNA from single cells"`               | \[EFO:0005684] |
| `"RNA-seq of non coding RNA from single cells"`           | \[EFO:0005685] |
| `"full length single cell RNA sequencing"`                | \[EFO:0008441] |
| `"tag based single cell RNA sequencing"`                  | \[EFO:0008440] |
| `"single nucleus RNA sequencing"`                         | \[EFO:0009809] |
| `"full length single nucleus RNA sequencing"`             | \[EFO:0009810] |
| `"tag based single nucleus RNA sequencing"`               | \[EFO:0009811] |
| `"transcription profiling by tiling array"`               | \[EFO:0002769] |
| `"translation profiling"`                                 | \[EFO:0001033] |
| `"Ψ-seq"`                                                 | \[EFO:0008988] |