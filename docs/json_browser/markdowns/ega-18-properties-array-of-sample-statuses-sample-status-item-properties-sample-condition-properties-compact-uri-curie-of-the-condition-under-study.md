# Compact URI (CURIE) of the condition under study Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_status/items/properties/condition_under_study/properties/cus_curie
```

The term needs to exist within the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/search?q=\&groupField=iri\&start=0\&ontology=hp\&ontology=efo\&ontology=ordo\&ontology=mondo) (OLS). We highly recommend the usage of the following ontologies: Experimental Factor Ontology (EFO), Human Phenotype Ontology (HP), Mondo Disease Ontology (MONDO) and Orphanet Rare Disease Ontology (ORDO).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## cus\_curie Type

`string` ([Compact URI (CURIE) of the condition under study](ega-18-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-compact-uri-curie-of-the-condition-under-study.md))

## cus\_curie Examples

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
