# Label of the term Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termLabel
```

The label of a term is the human-readable string associated with the identifier. It is not required that it matches the label of the termId within the referenced ontology, although it should. This is due to the fact that the source of truth will always be the termId, and not the label, which adds more context.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## termLabel Type

`string` ([Label of the term](ega-4-definitions-ontology-term-properties-label-of-the-term.md))

## termLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## termLabel Examples

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
