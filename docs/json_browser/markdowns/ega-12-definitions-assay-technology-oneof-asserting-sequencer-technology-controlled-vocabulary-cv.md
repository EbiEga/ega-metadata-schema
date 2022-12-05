# Asserting sequencer technology controlled vocabulary (CV) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor/oneOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 1 Type

unknown ([Asserting sequencer technology controlled vocabulary (CV)](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv.md))

# 1 Properties

| Property                                            | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                           |
| :-------------------------------------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assayInstrument](#assayinstrument)                 | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv-properties-assayinstrument.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor/oneOf/1/properties/assayInstrument") |
| [assayInstrumentPlatform](#assayinstrumentplatform) | `string`      | Optional | cannot be null | [EGA common metadata definitions](ega-7.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/controlled_vocabulary_schemas/EGA.cv.instrument_platforms_sequencing.json#/definitions/assayTechnologyDescriptor/oneOf/1/properties/assayInstrumentPlatform")                                                                  |

## assayInstrument



`assayInstrument`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-assay-technology-oneof-asserting-sequencer-technology-controlled-vocabulary-cv-properties-assayinstrument.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/assayTechnologyDescriptor/oneOf/1/properties/assayInstrument")

### assayInstrument Type

unknown

### assayInstrument Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value         | Explanation |
| :------------ | :---------- |
| `"sequencer"` |             |

## assayInstrumentPlatform

Controlled Vocabulary (CV) list for the sequencing instrument platforms. Commonly consisting in the manufacturers name (e.g. Illumina) and the instrument model (e.g. HiSeq 2000). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`assayInstrumentPlatform`

*   is optional

*   Type: `string` ([EGA Controlled Vocabulary (CV) for sequencing instrument platforms](ega-7.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-7.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/controlled_vocabulary_schemas/EGA.cv.instrument_platforms_sequencing.json#/definitions/assayTechnologyDescriptor/oneOf/1/properties/assayInstrumentPlatform")

### assayInstrumentPlatform Type

`string` ([EGA Controlled Vocabulary (CV) for sequencing instrument platforms](ega-7.md))

### assayInstrumentPlatform Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                                   | Explanation          |
| :-------------------------------------- | :------------------- |
| `"HiSeq X Five"`                        | GENEPIO:0100112      |
| `"HiSeq X Ten"`                         | GENEPIO:0100113      |
| `"Illumina Genome Analyzer"`            | EFO:0004200          |
| `"Illumina Genome Analyzer II"`         | EFO:0004201          |
| `"Illumina Genome Analyzer IIx"`        | EFO:0004202          |
| `"Illumina HiScanSQ"`                   | GENEPIO:0100109      |
| `"Illumina HiSeq 1000"`                 | EFO:0004204          |
| `"Illumina HiSeq 1500"`                 | EFO:0011027          |
| `"Illumina HiSeq 2000"`                 | EFO:0004203          |
| `"Illumina HiSeq 2500"`                 | EFO:0008565          |
| `"Illumina HiSeq 3000"`                 | EFO:0008564          |
| `"Illumina HiSeq 4000"`                 | EFO:0008563          |
| `"Illumina HiSeq X"`                    | EFO:0008567          |
| `"Illumina iSeq 100"`                   | EFO:0008635          |
| `"Illumina MiSeq"`                      | EFO:0004205          |
| `"Illumina MiniSeq"`                    | EFO:0008636          |
| `"Illumina NovaSeq 6000"`               | EFO:0008637          |
| `"NextSeq 500"`                         | OBI:0002021          |
| `"NextSeq 550"`                         | EFO:0008566          |
| `"NextSeq 1000"`                        | EFO:0010962          |
| `"NextSeq 2000"`                        | EFO:0010963          |
| `"Helicos HeliScope"`                   | OBI:0000717          |
| `"AB SOLiD System"`                     | EFO:0004435          |
| `"AB SOLiD System 2.0"`                 | EFO:0004442          |
| `"AB SOLiD System 3.0"`                 | EFO:0004439          |
| `"AB SOLiD 3 Plus System"`              | OBI:0002007          |
| `"AB SOLiD 4 System"`                   | EFO:0004438          |
| `"AB SOLiD 4hq System"`                 | EFO:0004441          |
| `"AB SOLiD PI System"`                  | EFO:0004437          |
| `"AB 5500 Genetic Analyzer"`            | EFO:0004440          |
| `"AB 5500xl Genetic Analyzer"`          | EFO:000443           |
| `"AB 5500xl-W Genetic Analysis System"` | EFO:0004436          |
| `"Complete Genomics"`                   | NCIT:C146815         |
| `"BGISEQ-50"`                           |                      |
| `"BGISEQ-500"`                          | NCIT:C146812         |
| `"MGISEQ-2000RS"`                       |                      |
| `"PacBio RS"`                           | GENEPIO:0100131      |
| `"PacBio RS II"`                        | EFO:0008631          |
| `"Sequel"`                              | OBI:0002632          |
| `"Sequel II"`                           | OBI:0002633          |
| `"Ion Torrent PGM"`                     | GENEPIO:0100136      |
| `"Ion Torrent Proton"`                  | GENEPIO:0100137      |
| `"Ion Torrent S5"`                      | GENEPIO:0100139      |
| `"Ion Torrent S5 XL"`                   | GENEPIO:0100138      |
| `"Ion Torrent Genexus"`                 |                      |
| `"Ion GeneStudio S5"`                   | GENEPIO:0100139      |
| `"Ion GeneStudio S5 Prime"`             | thermofisher:A38196  |
| `"Ion GeneStudio S5 Plus"`              | thermofisher:A38195  |
| `"AB 3730xL Genetic Analyzer"`          | thermofisher:3730XL  |
| `"AB 3730 Genetic Analyzer"`            |                      |
| `"AB 3500xL Genetic Analyzer"`          | thermofisher:4405633 |
| `"AB 3500 Genetic Analyzer"`            | thermofisher:4405673 |
| `"AB 3130xL Genetic Analyzer"`          | thermofisher:3130XLR |
| `"AB 3130 Genetic Analyzer"`            |                      |
| `"AB 310 Genetic Analyzer"`             |                      |
| `"DNBSEQ-T7"`                           | GENEPIO:0100147      |
| `"DNBSEQ-G400"`                         | GENEPIO:0100148      |
| `"DNBSEQ-G50"`                          | GENEPIO:0100150      |
| `"DNBSEQ-G400 FAST"`                    | GENEPIO:0100149      |
| `"MinION"`                              | EFO:0008632          |
| `"GridION"`                             | OBI:0002751          |
| `"PromethION"`                          | EFO:0008634          |
