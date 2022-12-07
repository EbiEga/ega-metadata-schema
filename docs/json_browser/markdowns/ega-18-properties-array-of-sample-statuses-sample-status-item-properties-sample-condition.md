# Sample condition Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy
```

One of the primary conditions under study (CUS). Notice that the sample may or may not be affected by this condition under study, belonging to the case or control groups respectively.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## conditionUnderStudy Type

`object` ([Sample condition](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md))

# conditionUnderStudy Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cusCurie](#cuscurie) | `string` | Required | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-compact-uri-curie-of-the-condition-under-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy/properties/cusCurie") |
| [cusLabel](#cuslabel) | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-label-of-the-condition-under-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy/properties/cusLabel")             |

## cusCurie

The term should exist within the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/search?q=\&groupField=iri\&start=0\&ontology=hp\&ontology=efo\&ontology=ordo\&ontology=mondo) (OLS). We highly recommend the usage of the following ontologies: Experimental Factor Ontology (EFO), Human Phenotype Ontology (HP), Mondo Disease Ontology (MONDO) and Orphanet Rare Disease Ontology (ORDO).

`cusCurie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the condition under study](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-compact-uri-curie-of-the-condition-under-study.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-compact-uri-curie-of-the-condition-under-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy/properties/cusCurie")

### cusCurie Type

`string` ([Compact URI (CURIE) of the condition under study](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-compact-uri-curie-of-the-condition-under-study.md))

### cusCurie Examples

```json
"MONDO:0021354"
```

```json
"EFO:1002024"
```

```json
"MAXO:0000647"
```

```json
"MONDO:0005081"
```

```json
"MONDO:0100096"
```

## cusLabel



`cusLabel`

*   is optional

*   Type: `string` ([Label of the condition under study](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-label-of-the-condition-under-study.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-label-of-the-condition-under-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy/properties/cusLabel")

### cusLabel Type

`string` ([Label of the condition under study](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-label-of-the-condition-under-study.md))

### cusLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### cusLabel Examples

```json
"tumor of adipose tissue"
```

```json
"streptococcal pharyngitis"
```

```json
"chemotherapy"
```

```json
"preeclampsia"
```

```json
"COVID-19"
```
