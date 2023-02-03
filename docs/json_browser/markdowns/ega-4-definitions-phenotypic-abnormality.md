# Phenotypic abnormality Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities/items/properties/phenotypicAbnormality
```

Property to describe any abnormal (i.e. deviation from normal or average) phenotype (i.e. detectable outward manifestations of a specific genotype).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## phenotypicAbnormality Type

`object` ([Phenotypic abnormality](ega-4-definitions-phenotypic-abnormality.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# phenotypicAbnormality Properties

| Property          | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                           |
| :---------------- | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Merged | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormality/properties/termId") |

## termId



`termId`

*   is optional

*   Type: merged type ([Ontology constraints for this specific termId](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormality/properties/termId")

### termId Type

merged type ([Ontology constraints for this specific termId](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid.md))

any of

*   [Ontology validation of phenotypic abnormality](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-phenotypic-abnormality.md "check type definition")

*   [In case the phenotypic abnormality is unknown or there is none](ega-4-definitions-phenotypic-abnormality-properties-ontology-constraints-for-this-specific-termid-anyof-in-case-the-phenotypic-abnormality-is-unknown-or-there-is-none.md "check type definition")

### termId Examples

```json
"HP:0003003"
```

```json
"HP:0010442"
```

```json
"HP:0002515"
```

```json
"NCIT:C17998"
```

```json
"NCIT:C94232"
```
