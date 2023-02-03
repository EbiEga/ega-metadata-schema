# Sample condition Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy
```

One of the primary conditions under study (CUS). For example: treated with cisplatin, sample taken from a fibroadenoma, osteonecrosis, differences in sequencing workflows, etcetera. Notice that the sample may or may not be affected by this condition under study, belonging to the case or control groups respectively (defined by 'caseVsControl' for each CUS).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## conditionUnderStudy Type

`object` ([Sample condition](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# conditionUnderStudy Properties

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                      |
| :---------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Not specified | Optional | cannot be null | [EGA sample metadata schema](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy/properties/termId") |

## termId

The term should exist within the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/search?q=\&groupField=iri\&start=0\&ontology=hp\&ontology=efo\&ontology=ordo\&ontology=mondo) (OLS). We highly recommend the usage of the following ontologies: Experimental Factor Ontology (EFO), Human Phenotype Ontology (HP), Mondo Disease Ontology (MONDO) and Orphanet Rare Disease Ontology (ORDO).

`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus/items/properties/conditionUnderStudy/properties/termId")

### termId Type

unknown ([Ontology constraints for this specific termId](ega-10-properties-array-of-sample-statuses-sample-status-item-properties-sample-condition-properties-ontology-constraints-for-this-specific-termid.md))

### termId Examples

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
