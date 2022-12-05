# Type of the assay Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayTypeDescriptor/properties/assayType
```

Overall type of the assay. Term chosen from a controlled vocabulary (CV) list. Search for yours either at (1) our GitHub repository ([array types](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assayType_by_array.json) and [sequencing types](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/controlled_vocabulary_schemas/EGA.cv.assayType_by_sequencer.json)) or (2) in the OLS service ([sequencing types](http://www.ebi.ac.uk/efo/EFO_0003740) and [array types](http://www.ebi.ac.uk/efo/EFO_0002696)).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## assayType Type

`string` ([Type of the assay](ega-9-properties-type-of-assay-properties-type-of-the-assay.md))

any of

*   [Array-assay type controlled vocabulary (CV) list](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-array-assay-type-controlled-vocabulary-cv-list.md "check type definition")

*   [Sequencer-assay type controlled vocabulary (CV) list](ega-9-properties-type-of-assay-properties-type-of-the-assay-anyof-sequencer-assay-type-controlled-vocabulary-cv-list.md "check type definition")

## assayType Examples

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
