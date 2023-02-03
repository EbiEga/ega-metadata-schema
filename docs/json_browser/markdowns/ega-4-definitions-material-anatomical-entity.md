# Material anatomical entity Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/samplingSite/allOf/0
```

The part of organism's anatomy or substance arising from an organism from which the biomaterial was derived, exlucing cell types. For example: tissues, organs, systems, fluids (e.g. semen, blood), body locations (e.g. arm skin, eye), etcetera. Search for yours at: <http://purl.obolibrary.org/obo/UBERON_0000465>. This property can be used to describe a sampling site or the morphological site of a disease, for example.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## 0 Type

`object` ([Material anatomical entity](ega-4-definitions-material-anatomical-entity.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# 0 Properties

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                  |
| :---------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-material-anatomical-entity-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/materialAnatomicalEntity/properties/termId") |

## termId



`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-4-definitions-material-anatomical-entity-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-material-anatomical-entity-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/materialAnatomicalEntity/properties/termId")

### termId Type

unknown ([Ontology constraints for this specific termId](ega-4-definitions-material-anatomical-entity-properties-ontology-constraints-for-this-specific-termid.md))

### termId Examples

```json
"UBERON:0000956"
```

```json
"UBERON:0006530"
```
