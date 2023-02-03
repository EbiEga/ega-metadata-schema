# Ontology constraints for this specific termId Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy/properties/termId
```

The term should exist within the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/search?q=\&groupField=iri\&start=0\&ontology=hp\&ontology=efo\&ontology=ordo\&ontology=mondo) (OLS). We highly recommend the usage of the following ontologies: Experimental Factor Ontology (EFO), Human Phenotype Ontology (HP), Mondo Disease Ontology (MONDO) and Orphanet Rare Disease Ontology (ORDO).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## termId Type

unknown ([Ontology constraints for this specific termId](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-ontology-constraints-for-this-specific-termid.md))

## termId Examples

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
