# Disease Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases/items/properties/disease
```

Property to describe a disease (i.e. a disposition to undergo pathological processes because of one or more disorders).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## disease Type

`object` ([Disease](ega-4-defs-disease.md))

all of

*   [Ontology term](ega-4-defs-ontology-term.md "check type definition")

# disease Properties

| Property          | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                 |
| :---------------- | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Merged | Optional | cannot be null | [EGA common metadata definitions](ega-4-defs-disease-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/disease/properties/termId") |

## termId



`termId`

*   is optional

*   Type: merged type ([Ontology constraints for this specific termId](ega-4-defs-disease-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-defs-disease-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/$defs/disease/properties/termId")

### termId Type

merged type ([Ontology constraints for this specific termId](ega-4-defs-disease-properties-ontology-constraints-for-this-specific-termid.md))

any of

*   [Ontology validation of 'disease' - EFO](ega-4-defs-disease-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-disease---efo.md "check type definition")

*   [Ontology validation of 'disease' - ORDO](ega-4-defs-disease-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-disease---ordo.md "check type definition")

*   [Ontology validation of 'human disease or disorder' - MONDO](ega-4-defs-disease-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-human-disease-or-disorder---mondo.md "check type definition")

*   [In case the phenotypic abnormality is unknown or there is none](ega-4-defs-disease-properties-ontology-constraints-for-this-specific-termid-anyof-in-case-the-phenotypic-abnormality-is-unknown-or-there-is-none.md "check type definition")

### termId Examples

```json
"MONDO:0100096"
```

```json
"EFO:0003101"
```

```json
"NCIT:C17998"
```

```json
"NCIT:C94232"
```
