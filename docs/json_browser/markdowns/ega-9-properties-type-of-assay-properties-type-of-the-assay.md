# Type of the assay Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assay_type_descriptor/properties/assay_type
```

Overall type of the assay. Term chosen from a controlled vocabulary (CV) list. Search for yours either at (1) our GitHub repository ([array types](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_array.json) and [sequencing types](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assay_type_by_sequencer.json)) or (2) in the OLS service ([sequencing types](http://www.ebi.ac.uk/efo/EFO_0003740) and [array types](http://www.ebi.ac.uk/efo/EFO_0002696)).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## assay\_type Type

`string` ([Type of the assay](ega-9-properties-type-of-assay-properties-type-of-the-assay.md))

any of

*   [EGA Controlled Vocabulary (CV) for assay types by sequencer \[EFO:0003740\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-sequencer-efo0003740.md "check type definition")

*   [EGA Controlled Vocabulary (CV) for assay types by array \[EFO:0002696\]](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-ega-controlled-vocabulary-cv-for-assay-types-by-array-efo0002696.md "check type definition")

## assay\_type Examples

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
