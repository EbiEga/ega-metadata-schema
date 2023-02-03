# Ontology term Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolTypeDescriptor/properties/protocolSubtype/allOf/0
```

This property represents an ontology term (a.k.a. class). It consists on two properties: the term identifier (termId) and its label (termLabel). This property and its structure is inherited across many other elements in the schemas. It is there, when inherited, where the real ontology constraint is put in place (e.g. using 'graphRestriction' keywords). Based on phenopacket's [OntologyClass](https://phenopacket-schema.readthedocs.io/en/latest/ontologyclass.html)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## 0 Type

`object` ([Ontology term](ega-4-definitions-ontology-term.md))

# 0 Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :---------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid)       | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ontology-term-properties-id-of-the-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termId")       |
| [termLabel](#termlabel) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ontology-term-properties-label-of-the-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termLabel") |

## termId

The identifier of an ontology term must be in CURIE format (check property 'curieGeneralPattern'). Whether a specific term is valid or not according to an ontology hierarchy is checked at each specific termId using ontology validation keywords (e.g. 'graphRestriction').

`termId`

*   is required

*   Type: `string` ([ID of the term](ega-4-definitions-ontology-term-properties-id-of-the-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ontology-term-properties-id-of-the-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termId")

### termId Type

`string` ([ID of the term](ega-4-definitions-ontology-term-properties-id-of-the-term.md))

all of

*   [Compact URI (CURIE) pattern](ega-4-definitions-compact-uri-curie-pattern.md "check type definition")

### termId Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### termId Examples

```json
"MONDO:0100096"
```

```json
"EFO:0003101"
```

```json
"EFO:0005518"
```

```json
"EFO:0002944"
```

```json
"EFO:0003813"
```

## termLabel

The label of a term is the human-readable string associated with the identifier. It is not required that it matches the label of the termId within the referenced ontology, although it should. This is due to the fact that the source of truth will always be the termId, and not the label, which adds more context.

`termLabel`

*   is required

*   Type: `string` ([Label of the term](ega-4-definitions-ontology-term-properties-label-of-the-term.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ontology-term-properties-label-of-the-term.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termLabel")

### termLabel Type

`string` ([Label of the term](ega-4-definitions-ontology-term-properties-label-of-the-term.md))

### termLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### termLabel Examples

```json
"COVID-19"
```

```json
"Axila skin"
```

```json
"bone marrow cell"
```

```json
"astrocyte"
```

```json
"oligodendrocyte"
```

```json
"Unknown"
```

```json
"Unaffected"
```

```json
"homo sapiens"
```
