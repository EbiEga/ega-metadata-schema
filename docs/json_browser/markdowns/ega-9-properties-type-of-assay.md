# Type of assay Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTypeDescriptor
```

Node defining the type of assay applicable to the experiment. Consists in an overall category (based on the purpose and technology of the instrument \[EFO:0002773]) and its possible subtype. Both types and subtypes are taken from controlled vocabulary (CV) lists, stored in the controlled\_vocabulary\_schemas folder. For example, in a single cell RNA-seq assay the assay type would be 'assay by high throughput sequencer' \[EFO:0002697] and its subtype 'RNA-seq of coding RNA from single cells' \[EFO:0005684].

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## assayTypeDescriptor Type

`object` ([Type of assay](ega-9-properties-type-of-assay.md))

any of

*   [Assay subtypes match DNA/RNA assays](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays.md "check type definition")

*   one (and only one) of

    *   [Assay type and subtype terms are from the array CV list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list.md "check type definition")

    *   [Assay type and subtype terms are from the sequencer CV list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-sequencer-cv-list.md "check type definition")

# assayTypeDescriptor Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                  |
| :---------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assayType](#assaytype)       | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-type-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTypeDescriptor/properties/assayType")       |
| [assaySubtype](#assaysubtype) | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-subtype-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTypeDescriptor/properties/assaySubtype") |

## assayType

Overall type of the assay. Term chosen from a controlled vocabulary (CV) list. Search for yours either at (1) our GitHub repository ([array types](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assayType_by_array.json) and [sequencing types](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assayType_by_sequencer.json)) or (2) in the OLS service ([sequencing types](http://www.ebi.ac.uk/efo/EFO_0003740) and [array types](http://www.ebi.ac.uk/efo/EFO_0002696)).

`assayType`

*   is required

*   Type: `string` ([Type of the assay](ega-9-properties-type-of-assay-properties-type-of-the-assay.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-type-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTypeDescriptor/properties/assayType")

### assayType Type

`string` ([Type of the assay](ega-9-properties-type-of-assay-properties-type-of-the-assay.md))

any of

*   [Array-assay type controlled vocabulary (CV) list](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-array-assay-type-controlled-vocabulary-cv-list.md "check type definition")

*   [Sequencer-assay type controlled vocabulary (CV) list](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-sequencer-assay-type-controlled-vocabulary-cv-list.md "check type definition")

### assayType Examples

```json
"Hi-C"
```

```json
"amplicon sequencing"
```

```json
"assay by high throughput sequencer"
```

```json
"immune sequencing"
```

```json
"ChIP-chip by array"
```

```json
"transcription profiling by array"
```

```json
"microRNA profiling by array"
```

```json
"genotyping by array"
```

```json
"comparative genomic hybridization by array"
```

## assaySubtype

Subtype of the assay: any ontologized term hierarchically below the assay type. Term chosen from a controlled vocabulary (CV) list. Search for yours at our GitHub repository: [array subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assaySubtype_by_array.json), [sequencing subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assaySubtype_by_sequencer.json), [RNA assay subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assaySubtype_by_rna.json) and [DNA assay subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assaySubtype_by_dna.json))

`assaySubtype`

*   is optional

*   Type: `string` ([Subtype of the assay](ega-9-properties-type-of-assay-properties-subtype-of-the-assay.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-subtype-of-the-assay.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTypeDescriptor/properties/assaySubtype")

### assaySubtype Type

`string` ([Subtype of the assay](ega-9-properties-type-of-assay-properties-subtype-of-the-assay.md))

### assaySubtype Examples

```json
"MC-4C"
```

```json
"UMI-4C"
```

```json
"single nucleus RNA sequencing"
```

```json
"RNA-seq of coding RNA from single cells"
```

```json
"Quant-seq"
```

```json
"DNA-seq"
```

```json
"ATAC-seq"
```

```json
"DNase Hi-C"
```

```json
"scDNase-seq"
```

```json
"in situ HiC"
```

```json
"exome sequencing"
```
