# ID of the term Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termId
```

The identifier of an ontology term must be in CURIE format (check property 'curieGeneralPattern'). Whether a specific term is valid or not according to an ontology hierarchy is checked at each specific termId using ontology validation keywords (e.g. 'graphRestriction').

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## termId Type

`string` ([ID of the term](ega-4-definitions-ontology-term-properties-id-of-the-term.md))

all of

*   [Compact URI (CURIE) pattern](ega-4-definitions-ontology-term-properties-id-of-the-term-allof-compact-uri-curie-pattern.md "check type definition")

## termId Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## termId Examples

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
