# NCBI Gene identifier CURIE pattern Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieNcbiGeneIdentifierPattern
```

Entrez Gene is the NCBI's database for gene-specific information, focusing on completely sequenced genomes, those with an active research community to contribute gene-specific information, or those that are scheduled for intense sequence analysis. See further details here: <https://registry.identifiers.org/registry/ncbigene>

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## curieNcbiGeneIdentifierPattern Type

`string` ([NCBI Gene identifier CURIE pattern](ega-4-definitions-ncbi-gene-identifier-curie-pattern.md))

all of

*   [Compact URI (CURIE) pattern](ega-4-definitions-compact-uri-curie-pattern.md "check type definition")

## curieNcbiGeneIdentifierPattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^ncbigene:\d+$
```

[try pattern](https://regexr.com/?expression=%5Encbigene%3A%5Cd%2B%24 "try regular expression with regexr.com")

## curieNcbiGeneIdentifierPattern Examples

```json
"ncbigene:100010"
```

```json
"ncbigene:270627"
```
