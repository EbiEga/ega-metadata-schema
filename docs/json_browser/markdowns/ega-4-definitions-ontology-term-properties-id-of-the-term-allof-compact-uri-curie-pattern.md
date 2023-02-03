# Compact URI (CURIE) pattern Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ontologyTerm/properties/termId/allOf/0
```

A [W3C Compact URI](https://www.w3.org/TR/curie/) formatted string. A CURIE string has the structure `prefix`:`reference`, as defined by the W3C syntax. Even though we do not restrict prefixes, we recommend that the term used as `prefix` is uniformely resolved. In other words, it is better to use prefixes (e.g. 'ensembl') from identifiers.org.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 0 Type

`string` ([Compact URI (CURIE) pattern](ega-4-definitions-ontology-term-properties-id-of-the-term-allof-compact-uri-curie-pattern.md))

## 0 Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\w[^:]*:.+$
```

[try pattern](https://regexr.com/?expression=%5E%5Cw%5B%5E%3A%5D*%3A.%2B%24 "try regular expression with regexr.com")

## 0 Examples

```json
"ensembl:ENSG00000139618"
```

```json
"HGNC:11535"
```

```json
"data:1026"
```

```json
"EFO:0003815"
```
