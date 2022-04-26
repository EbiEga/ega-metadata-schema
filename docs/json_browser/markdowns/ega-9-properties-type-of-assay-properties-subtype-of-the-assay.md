# Subtype of the assay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/properties/assay_subtype
```

Subtype of the assay: any ontologized term hierarchically below the assay type. Term chosen from a controlled vocabulary (CV) list. Search for yours at our GitHub repository: [array subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_array.json), [sequencing subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_sequencer.json), [RNA assay subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_rna.json) and [DNA assay subtypes](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_subtype_by_dna.json))

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## assay\_subtype Type

`string` ([Subtype of the assay](ega-9-properties-type-of-assay-properties-subtype-of-the-assay.md))

## assay\_subtype Examples

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
