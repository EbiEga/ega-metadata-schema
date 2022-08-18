# Resource namespace prefix Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/namespace_prefix
```

Prefixes of namespaces are used to uniquely resolve the ambiguity between identically named elements or attributes. They can easily be checked at [**identifiers.org**](https://identifiers.org/) or [**OLS' list of ontologies**](https://www.ebi.ac.uk/ols/ontologies). For example, in our example of diabetes melitus, EFO:0000400, we need both parts of the CURIE: EFO (prefix) and 0000400 (local identifier). Without knowing the prefix, the local identifier alone is difficult to resolve.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## namespace\_prefix Type

`string` ([Resource namespace prefix](ega-20-properties-resources-ontologies-resource-properties-resource-namespace-prefix.md))

## namespace\_prefix Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## namespace\_prefix Examples

```json
"hp"
```

```json
"efo"
```

```json
"pubmed"
```
