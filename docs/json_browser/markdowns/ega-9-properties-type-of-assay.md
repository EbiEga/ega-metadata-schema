# Type of assay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor
```

Node defining the type of assay applicable to the experiment. Consists in an overall category (based on the purpose and technology of the instrument \[EFO:0002773]) and its possible subtype. Both types and subtypes are taken from controlled vocabulary (CV) lists, stored in the controlled_vocabulary_schemas folder. For example, in a single cell RNA-seq assay the assay type would be 'assay by high throughput sequencer' \[EFO:0002697] and its subtype 'RNA-seq of coding RNA from single cells' \[EFO:0005684].

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## assay_type_descriptor Type

`object` ([Type of assay](ega-9-properties-type-of-assay.md))

any of

*   [Assay subtypes match DNA/RNA assays](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-dnarna-assays.md "check type definition")

*   one (and only one) of

    *   [Assay type and subtype terms are from the array CV list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-array-cv-list.md "check type definition")

    *   [Assay type and subtype terms are from the sequencer CV list](ega-9-properties-type-of-assay-anyof-assay-subtypes-match-arraysequencer-assays-oneof-assay-type-and-subtype-terms-are-from-the-sequencer-cv-list.md "check type definition")

# assay_type_descriptor Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                           |
| :------------------------------ | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [assay_type](#assay_type)       | Merged   | Required | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-type-of-the-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/properties/assay_type")       |
| [assay_subtype](#assay_subtype) | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-subtype-of-the-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/properties/assay_subtype") |

## assay_type

Overall type of the assay. Term chosen from a controlled vocabulary (CV) list. Search for yours either at (1) our GitHub repository ([array types](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_array.json) and [sequencing types](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_sequencer.json)) or (2) in the OLS service ([sequencing types](http://www.ebi.ac.uk/efo/EFO\_0003740) and [array types](http://www.ebi.ac.uk/efo/EFO\_0002696)).

`assay_type`

*   is required

*   Type: `string` ([Type of the assay](ega-9-properties-type-of-assay-properties-type-of-the-assay.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-type-of-the-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/properties/assay_type")

### assay_type Type

`string` ([Type of the assay](ega-9-properties-type-of-assay-properties-type-of-the-assay.md))

any of

*   [EGA Controlled Vocabulary (CV) for assay types by sequencer \[EFO:0003740\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-sequencer-efo0003740.md "check type definition")

*   [EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-array-efo0002696.md "check type definition")

### assay_type Examples

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

## assay_subtype

Subtype of the assay: any ontologized term hierarchically below the assay type. Term chosen from a controlled vocabulary (CV) list. Search for yours at our GitHub repository: [array subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_array.json), [sequencing subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_sequencer.json), [RNA assay subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_rna.json) and [DNA assay subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_dna.json))

`assay_subtype`

*   is optional

*   Type: `string` ([Subtype of the assay](ega-9-properties-type-of-assay-properties-subtype-of-the-assay.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-9-properties-type-of-assay-properties-subtype-of-the-assay.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/properties/assay_subtype")

### assay_subtype Type

`string` ([Subtype of the assay](ega-9-properties-type-of-assay-properties-subtype-of-the-assay.md))

### assay_subtype Examples

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
