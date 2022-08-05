# Sample condition Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/condition_under_study
```

One of the primary conditions under study (CUS). Notice that the sample may or may not be affected by this condition under study, belonging to the case or control groups respectively.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## condition\_under\_study Type

`object` ([Sample condition](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md))

# condition\_under\_study Properties

| Property                 | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                             |
| :----------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cus\_curie](#cus_curie) | `string` | Required | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-compact-uri-curie-of-the-condition-under-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/condition_under_study/properties/cus_curie") |
| [cus\_label](#cus_label) | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-label-of-the-condition-under-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/condition_under_study/properties/cus_label")             |

## cus\_curie

The term needs to exist within the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/search?q=\&groupField=iri\&start=0\&ontology=hp\&ontology=efo\&ontology=ordo\&ontology=mondo) (OLS). We highly recommend the usage of the following ontologies: Experimental Factor Ontology (EFO), Human Phenotype Ontology (HP), Mondo Disease Ontology (MONDO) and Orphanet Rare Disease Ontology (ORDO).

`cus_curie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the condition under study](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-compact-uri-curie-of-the-condition-under-study.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-compact-uri-curie-of-the-condition-under-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/condition_under_study/properties/cus_curie")

### cus\_curie Type

`string` ([Compact URI (CURIE) of the condition under study](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-compact-uri-curie-of-the-condition-under-study.md))

### cus\_curie Examples

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

## cus\_label



`cus_label`

*   is optional

*   Type: `string` ([Label of the condition under study](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-label-of-the-condition-under-study.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-label-of-the-condition-under-study.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/condition_under_study/properties/cus_label")

### cus\_label Type

`string` ([Label of the condition under study](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-label-of-the-condition-under-study.md))

### cus\_label Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### cus\_label Examples

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
