# EGA Controlled Vocabulary (CV) for assay subtypes by DNA \[EFO:0001456] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_dna.json#/properties/assay_type_descriptor/anyOf/0/properties/assay_subtype/anyOf/0
```

Controlled Vocabulary (CV) list for assay subtypes by the assayed molecule being DNA: any ontologized term for a subtype (i.e. child ontology) of a DNA assay \[EFO:0001456]. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## 0 Type

`string` ([EGA Controlled Vocabulary (CV) for assay subtypes by DNA \[EFO:0001456\]](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays-properties-assay_subtype-anyof-ega-controlled-vocabulary-cv-for-assay-subtypes-by-dna-efo0001456.md))

## 0 Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                                       | Explanation    |
| :---------------------------------------------------------- | :------------- |
| `"2b-RAD"`                                                  | \[EFO:0008638] |
| `"454 Sequencing"`                                          | \[EFO:0005016] |
| `"AHT-ChIP-Seq"`                                            | \[EFO:0008652] |
| `"ARS-Seq"`                                                 | \[EFO:0008653] |
| `"Aba-seq"`                                                 | \[EFO:0008649] |
| `"Advanved Chia-PET"`                                       | \[EFO:0008650] |
| `"BLESS"`                                                   | \[EFO:0008657] |
| `"BS-Seq"`                                                  | \[EFO:0008665] |
| `"BSAS"`                                                    | \[EFO:0008666] |
| `"BSPP"`                                                    | \[EFO:0008667] |
| `"Bar-Seq"`                                                 | \[EFO:0008654] |
| `"Barcode-Seq"`                                             | \[EFO:0008655] |
| `"BisChIP-Seq"`                                             | \[EFO:0008656] |
| `"Bisulfite-seq"`                                           | \[EFO:0003753] |
| `"Break-seq"`                                               | \[EFO:0008659] |
| `"Bubble-Seq"`                                              | \[EFO:0009992] |
| `"CAB-Seq"`                                                 | \[EFO:0008668] |
| `"CAP-seq"`                                                 | \[EFO:0008671] |
| `"CAST-ChIP"`                                               | \[EFO:0008676] |
| `"CATCH-IT"`                                                | \[EFO:0008677] |
| `"CATCH-seq"`                                               | \[EFO:0008678] |
| `"CNV-Seq"`                                                 | \[EFO:0008695] |
| `"COPRO-seq"`                                               | \[EFO:0008696] |
| `"CPT-seq"`                                                 | \[EFO:0008698] |
| `"CRE-Seq"`                                                 | \[EFO:0008699] |
| `"CREST-seq"`                                               | \[EFO:0008700] |
| `"CRISPR-UMI"`                                              | \[EFO:0010030] |
| `"CROP-Seq"`                                                | \[EFO:0008701] |
| `"CUT&RUN"`                                                 | \[EFO:0009973] |
| `"Capp-Seq"`                                                | \[EFO:0008672] |
| `"ChAP-seq"`                                                | \[EFO:0008680] |
| `"ChEC-seq"`                                                | \[EFO:0008682] |
| `"ChIP-BMS"`                                                | \[EFO:0009993] |
| `"ChIP-BS-seq"`                                             | \[EFO:0008685] |
| `"ChIP-Chip"`                                               | \[EFO:0000748] |
| `"ChIP-chip by SNP array"`                                  | \[EFO:0002764] |
| `"ChIP-chip by array"`                                      | \[EFO:0002760] |
| `"ChIP-chip by tiling array"`                               | \[EFO:0002762] |
| `"ChIP-exo"`                                                | \[EFO:0005302] |
| `"ChIP-seq"`                                                | \[EFO:0002692] |
| `"ChIPmentation"`                                           | \[EFO:0008686] |
| `"Chem-Seq"`                                                | \[EFO:0008683] |
| `"Circle-Seq"`                                              | \[EFO:0008689] |
| `"CrY2H-seq"`                                               | \[EFO:0008702] |
| `"DAP-seq"`                                                 | \[EFO:0008705] |
| `"DArTSeq"`                                                 | \[EFO:0008706] |
| `"DIP-seq"`                                                 | \[EFO:0008711] |
| `"DNA-seq"`                                                 | \[EFO:0002693] |
| `"ATAC-seq"`                                                | \[EFO:0007045] |
| `"Fast-ATAC"`                                               | \[EFO:0008736] |
| `"scATAC-seq"`                                              | \[EFO:0010891] |
| `"10x multiome"`                                            | \[EFO:0030059] |
| `"10x scATAC-seq"`                                          | \[EFO:0030007] |
| `"scATAC-seq (Microfluidics)"`                              | \[EFO:0008904] |
| `"scATAC-seq (cell index)"`                                 | \[EFO:0008925] |
| `"massively parallel signature sequencing"`                 | \[EFO:0010805] |
| `"DNase-hypersensitivity seq"`                              | \[EFO:0003752] |
| `"scDNase-seq"`                                             | \[EFO:0008907] |
| `"DR-Seq"`                                                  | \[EFO:0010005] |
| `"DSB-seq"`                                                 | \[EFO:0008724] |
| `"DSBCapture"`                                              | \[EFO:0008725] |
| `"DamID"`                                                   | \[EFO:0008704] |
| `"Digenome-seq"`                                            | \[EFO:0008709] |
| `"Dnase I SIM"`                                             | \[EFO:0008715] |
| `"Drop-ChIP"`                                               | \[EFO:0008721] |
| `"Droplet-CirSeq"`                                          | \[EFO:0008723] |
| `"Duplex-Seq"`                                              | \[EFO:0008727] |
| `"EC-seq"`                                                  | \[EFO:0008728] |
| `"END-seq"`                                                 | \[EFO:0008729] |
| `"EnIGMA"`                                                  | \[EFO:0008730] |
| `"EpiRADSeq"`                                               | \[EFO:0009997] |
| `"FAIRE-seq"`                                               | \[EFO:0004428] |
| `"FAST-SeqS"`                                               | \[EFO:0008738] |
| `"FiT-Seq"`                                                 | \[EFO:0008743] |
| `"FlowSeq"`                                                 | \[EFO:0008744] |
| `"G&T-Seq"`                                                 | \[EFO:0009999] |
| `"G4 ChIP-seq"`                                             | \[EFO:0008750] |
| `"G4-seq"`                                                  | \[EFO:0008751] |
| `"GRIP"`                                                    | \[EFO:0008755] |
| `"GT-seq"`                                                  | \[EFO:0008758] |
| `"GUIDE-seq"`                                               | \[EFO:0008760] |
| `"HELP-Seq"`                                                | \[EFO:0008761] |
| `"HT-ChIP"`                                                 | \[EFO:0008768] |
| `"HTGTS"`                                                   | \[EFO:0008770] |
| `"Helicos sequencing"`                                      | \[OBI:0000697] |
| `"HiChIP"`                                                  | \[EFO:0010011] |
| `"HiTS-Flip"`                                               | \[EFO:0008765] |
| `"Histone meth."`                                           | \[EFO:0008764] |
| `"HydEn-seq"`                                               | \[EFO:0008771] |
| `"IMS-MDA"`                                                 | \[EFO:0008778] |
| `"INSeq"`                                                   | \[EFO:0008782] |
| `"Ig-Seq"`                                                  | \[EFO:0008777] |
| `"JBP1-seq"`                                                | \[EFO:0010000] |
| `"LAM-HTGTS"`                                               | \[EFO:0008784] |
| `"LIANTI"`                                                  | \[EFO:0008785] |
| `"Look-Seq"`                                                | \[EFO:0008787] |
| `"MAB-seq"`                                                 | \[EFO:0010001] |
| `"MAF"`                                                     | \[EFO:0008791] |
| `"MAINE-Seq"`                                               | \[EFO:0008792] |
| `"MALBAC"`                                                  | \[EFO:0008793] |
| `"MARDI"`                                                   | \[EFO:0008794] |
| `"MARGI"`                                                   | \[EFO:0009988] |
| `"MBD-seq"`                                                 | \[EFO:0003750] |
| `"MBDCap-Seq"`                                              | \[EFO:0008798] |
| `"MCC-Seq"`                                                 | \[EFO:0008799] |
| `"MDA"`                                                     | \[EFO:0008800] |
| `"PMA"`                                                     | \[EFO:0008864] |
| `"MDS"`                                                     | \[EFO:0008801] |
| `"ME-Scan-SVA"`                                             | \[EFO:0008802] |
| `"MIDAS"`                                                   | \[EFO:0008809] |
| `"MINCE-seq"`                                               | \[EFO:0008812] |
| `"MIPSTR"`                                                  | \[EFO:0008814] |
| `"MIRA"`                                                    | \[EFO:0008816] |
| `"MNase-seq"`                                               | \[EFO:0003751] |
| `"MPE-seq"`                                                 | \[EFO:0008821] |
| `"MPRA"`                                                    | \[EFO:0008822] |
| `"MRE-seq"`                                                 | \[EFO:0003748] |
| `"MeDIP-seq"`                                               | \[EFO:0003749] |
| `"Methyl-seq"`                                              | \[EFO:0008804] |
| `"MethylCap-Seq"`                                           | \[EFO:0008805] |
| `"MiGS"`                                                    | \[EFO:0008811] |
| `"Mint-ChIP"`                                               | \[EFO:0008813] |
| `"MitoRCA-seq"`                                             | \[EFO:0008817] |
| `"Mosaic-Seq"`                                              | \[EFO:0008820] |
| `"Mseek"`                                                   | \[EFO:0008823] |
| `"Mu-Seq"`                                                  | \[EFO:0010038] |
| `"NAD-seq"`                                                 | \[EFO:0009972] |
| `"NG Capture-C"`                                            | \[EFO:0008827] |
| `"NOIR"`                                                    | \[EFO:0008829] |
| `"NOME-Seq"`                                                | \[EFO:0008830] |
| `"NS-seq"`                                                  | \[EFO:0008831] |
| `"NSCR"`                                                    | \[EFO:0008832] |
| `"Nano-hmC-Seal"`                                           | \[EFO:0010040] |
| `"Nucleo-Seq"`                                              | \[EFO:0008836] |
| `"OK-Seq"`                                                  | \[EFO:0008837] |
| `"ORGANIC"`                                                 | \[EFO:0008838] |
| `"OS-Seq"`                                                  | \[EFO:0008839] |
| `"Omni-ATAC"`                                               | \[EFO:0010014] |
| `"PAT-ChIP"`                                                | \[EFO:0008852] |
| `"PB-seq"`                                                  | \[EFO:0008854] |
| `"PBAT"`                                                    | \[EFO:0008855] |
| `"PD-Seq"`                                                  | \[EFO:0008856] |
| `"PDZ-Seq"`                                                 | \[EFO:0008857] |
| `"PE RAD-Seq"`                                              | \[EFO:0008858] |
| `"PELE-Seq"`                                                | \[EFO:0010023] |
| `"PhIP-seq"`                                                | \[EFO:0008861] |
| `"Pool-Seq"`                                                | \[EFO:0008867] |
| `"ProP-PD"`                                                 | \[EFO:0008871] |
| `"Profiler"`                                                | \[EFO:0008870] |
| `"Pu-seq"`                                                  | \[EFO:0008875] |
| `"Pvu-Seal-seq"`                                            | \[EFO:0008876] |
| `"RAD-tag"`                                                 | \[EFO:0008879] |
| `"RBBS"`                                                    | \[EFO:0008883] |
| `"RC-Seq"`                                                  | \[EFO:0008885] |
| `"RICC-seq"`                                                | \[EFO:0008894] |
| `"RRBS"`                                                    | \[EFO:0008900] |
| `"RRMAB-seq"`                                               | \[EFO:0010002] |
| `"Rapture"`                                                 | \[EFO:0008881] |
| `"RedBS-Seq"`                                               | \[EFO:0008886] |
| `"Ren-Seq"`                                                 | \[EFO:0010042] |
| `"Rep-Seq"`                                                 | \[EFO:0008887] |
| `"RepeatSeq"`                                               | \[EFO:0008888] |
| `"Repli-Seq"`                                               | \[EFO:0008889] |
| `"2-stage Repli-seq"`                                       | \[EFO:0009969] |
| `"multi-stage Repli-seq"`                                   | \[EFO:0009970] |
| `"Ribose-seq"`                                              | \[EFO:0008893] |
| `"SCI-seq"`                                                 | \[EFO:0008908] |
| `"SCL-exo"`                                                 | \[EFO:0008909] |
| `"SCMDA"`                                                   | \[EFO:0008910] |
| `"SCTG"`                                                    | \[EFO:0010015] |
| `"SELEX-seq"`                                               | \[EFO:0008918] |
| `"HT-SELEX"`                                                | \[EFO:0008769] |
| `"gSELEX-Seq"`                                              | \[EFO:0008757] |
| `"SITE-Seq"`                                                | \[EFO:0008926] |
| `"SLAF-Seq"`                                                | \[EFO:0008927] |
| `"SLBS"`                                                    | \[EFO:0008928] |
| `"SMDB"`                                                    | \[EFO:0008932] |
| `"SMiLE-seq"`                                               | \[EFO:0008933] |
| `"SNES"`                                                    | \[EFO:0008938] |
| `"SPLAT"`                                                   | \[EFO:0008946] |
| `"SSB-Seq"`                                                 | \[EFO:0008949] |
| `"STAP-seq"`                                                | \[EFO:0010028] |
| `"STARR-Seq"`                                               | \[EFO:0010044] |
| `"STATseq"`                                                 | \[EFO:0008951] |
| `"Safe-SeqS"`                                               | \[EFO:0008901] |
| `"SiMSen-Seq"`                                              | \[EFO:0008923] |
| `"Simul-seq"`                                               | \[EFO:0008924] |
| `"Solexa sequencing assay"`                                 | \[OBI:0000724] |
| `"Sono-Seq"`                                                | \[EFO:0008942] |
| `"SpDamID"`                                                 | \[EFO:0008944] |
| `"Stable-Seq"`                                              | \[EFO:0010043] |
| `"Strand-seq"`                                              | \[EFO:0008952] |
| `"T-WGBS"`                                                  | \[EFO:0008957] |
| `"TAB-Seq"`                                                 | \[EFO:0008958] |
| `"TAm-Seq"`                                                 | \[EFO:0010046] |
| `"TAmC-Seq"`                                                | \[EFO:0008961] |
| `"TC-Seq"`                                                  | \[EFO:0008964] |
| `"THS-seq"`                                                 | \[EFO:0008969] |
| `"TN-Seq"`                                                  | \[EFO:0008973] |
| `"TSA-seq"`                                                 | \[EFO:0009971] |
| `"TaDa"`                                                    | \[EFO:0008959] |
| `"TraDIS sequencing"`                                       | \[EFO:0005219] |
| `"TruePrime"`                                               | \[EFO:0008977] |
| `"Tuba-seq"`                                                | \[EFO:0008979] |
| `"VDJ-Seq"`                                                 | \[EFO:0008981] |
| `"VirScan"`                                                 | \[EFO:0008983] |
| `"WGA-X"`                                                   | \[EFO:0008984] |
| `"WGBS"`                                                    | \[EFO:0008985] |
| `"X-ChIP-seq"`                                              | \[EFO:0008986] |
| `"caMAB-seq"`                                               | \[EFO:0008670] |
| `"chromosome conformation capture assay"`                   | \[EFO:0007688] |
| `"3C"`                                                      | \[EFO:0007689] |
| `"Capture-C"`                                               | \[EFO:0007691] |
| `"TCC"`                                                     | \[EFO:0008965] |
| `"ligation-free chromosome conformation capture assay"`     | \[EFO:0009968] |
| `"GAM"`                                                     | \[EFO:0009987] |
| `"Hi-C"`                                                    | \[EFO:0007693] |
| `"Capture-HiC"`                                             | \[EFO:0008674] |
| `"DNase Hi-C"`                                              | \[EFO:0009976] |
| `"MC-Hi-C"`                                                 | \[EFO:0009980] |
| `"Micro-C XL"`                                              | \[EFO:0008808] |
| `"dilution HiC"`                                            | \[EFO:0009975] |
| `"in situ HiC"`                                             | \[EFO:0009974] |
| `"sci-Hi-C"`                                                | \[EFO:0009977] |
| `"single cell Hi-C"`                                        | \[EFO:0009979] |
| `"sn-Hi-C"`                                                 | \[EFO:0009978] |
| `"SPRITE"`                                                  | \[EFO:0009984] |
| `"DNA SPRITE"`                                              | \[EFO:0009985] |
| `"RNA-DNA SPRITE"`                                          | \[EFO:0009986] |
| `"Trac-Loop"`                                               | \[EFO:0009982] |
| `"ligation-mediated chromosome conformation capture assay"` | \[EFO:0009967] |
| `"4C"`                                                      | \[EFO:0007690] |
| `"MC-4C"`                                                   | \[EFO:0009983] |
| `"UMI-4C"`                                                  | \[EFO:0009995] |
| `"5C"`                                                      | \[EFO:0007692] |
| `"Chia-PET"`                                                | \[EFO:0008684] |
| `"PLAC-seq"`                                                | \[EFO:0009981] |
| `"clone by clone sequencing"`                               | \[EFO:0003742] |
| `"clone end sequencing"`                                    | \[EFO:0003743] |
| `"comparative genomic hybridization (CGH)"`                 | \[EFO:0010937] |
| `"comparative genomic hybridization by array"`              | \[EFO:0000749] |
| `"ddMDA"`                                                   | \[EFO:0009996] |
| `"ddRADseq"`                                                | \[EFO:0008707] |
| `"eWGA"`                                                    | \[EFO:0008733] |
| `"epiGBS"`                                                  | \[EFO:0008732] |
| `"exome sequencing"`                                        | \[EFO:0005396] |
| `"ezRAD"`                                                   | \[EFO:0008734] |
| `"fC-CET"`                                                  | \[EFO:0008739] |
| `"fC-Seal"`                                                 | \[EFO:0008740] |
| `"fCAB-Seq"`                                                | \[EFO:0008741] |
| `"gRNA-seq"`                                                | \[EFO:0030033] |
| `"genotyping by array"`                                     | \[EFO:0002767] |
| `"genotyping by high throughput sequencing"`                | \[EFO:0002771] |
| `"hMeDIP-seq"`                                              | \[EFO:0008767] |
| `"hyRAD"`                                                   | \[EFO:0008772] |
| `"iDES"`                                                    | \[EFO:0008776] |
| `"ini-seq"`                                                 | \[EFO:0008781] |
| `"mCT-seq"`                                                 | \[EFO:0030060] |
| `"methylation profiling"`                                   | \[EFO:0000751] |
| `"methylation profiling by array"`                          | \[EFO:0002759] |
| `"methylation profiling by high throughput sequencing"`     | \[EFO:0002761] |
| `"snmC-Seq2"`                                               | \[EFO:0030027] |
| `"middRAD"`                                                 | \[EFO:0008810] |
| `"miniARS-seq"`                                             | \[EFO:0010021] |
| `"mutARS-Seq"`                                              | \[EFO:0010039] |
| `"nuc-ChIP-seq"`                                            | \[EFO:0008833] |
| `"nuc-seq"`                                                 | \[EFO:0008835] |
| `"nucleosome sequencing"`                                   | \[EFO:0008834] |
| `"oxBS-Seq"`                                                | \[EFO:0008840] |
| `"pooled clone sequencing"`                                 | \[EFO:0003741] |
| `"random chromosome sequencing"`                            | \[EFO:0003745] |
| `"random exon sequencing"`                                  | \[EFO:0003746] |
| `"restriction-site associated DNA sequencing"`              | \[EFO:0008878] |
| `"scABA-seq"`                                               | \[EFO:0009994] |
| `"scBS-seq"`                                                | \[EFO:0008905] |
| `"scChIP-seq"`                                              | \[EFO:0008906] |
| `"scM&T-seq"`                                               | \[EFO:0010006] |
| `"scMT-Seq"`                                                | \[EFO:0008911] |
| `"scRC-Seq"`                                                | \[EFO:0008912] |
| `"scRRBS"`                                                  | \[EFO:0008914] |
| `"scTHS-seq"`                                               | \[EFO:0008915] |
| `"scTrio-seq"`                                              | \[EFO:0010007] |
| `"scWGBS"`                                                  | \[EFO:0008916] |
| `"shRNA-seq"`                                               | \[EFO:0030034] |
| `"smMIP"`                                                   | \[EFO:0008935] |
| `"snDrop-seq"`                                              | \[EFO:0008937] |
| `"snmC-seq"`                                                | \[EFO:0008939] |
| `"tiling path by array"`                                    | \[EFO:0001031] |
| `"whole chromosome random sequencing"`                      | \[EFO:0004160] |
| `"whole genome shotgun sequencing"`                         | \[EFO:0003744] |
