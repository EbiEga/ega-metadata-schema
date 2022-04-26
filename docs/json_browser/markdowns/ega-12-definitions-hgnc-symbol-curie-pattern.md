# HGNC symbol CURIE pattern Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/curie_hgnc_symbol_pattern
```

The HGNC (HUGO Gene Nomenclature Committee) provides an approved gene name and symbol (short-form abbreviation) for each known human gene. All approved symbols are stored in the HGNC database, and each symbol is unique. This collection refers to records using the HGNC symbol. See further details here: <https://registry.identifiers.org/registry/hgnc.symbol>

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## curie\_hgnc\_symbol\_pattern Type

`string` ([HGNC symbol CURIE pattern](ega-12-definitions-hgnc-symbol-curie-pattern.md))

all of

*   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

## curie\_hgnc\_symbol\_pattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
hgnc.symbol:[A-Za-z-0-9_]+(\@)?$
```

[try pattern](https://regexr.com/?expression=hgnc.symbol%3A%5BA-Za-z-0-9_%5D%2B\(%5C%40\)%3F%24 "try regular expression with regexr.com")

## curie\_hgnc\_symbol\_pattern Examples

```json
"hgnc.symbol:DAPK1"
```

```json
"hgnc.symbol:TAF1"
```
