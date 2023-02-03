# HGNC identifier CURIE pattern Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieHgncIdentifierPattern
```

The HGNC (HUGO Gene Nomenclature Committee) provides an approved gene name and symbol (short-form abbreviation) for each known human gene. All approved symbols are stored in the HGNC database, and each symbol is unique. HGNC identifiers refer to records in the HGNC symbol database. See further details here: <https://registry.identifiers.org/registry/hgnc>

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## curieHgncIdentifierPattern Type

`string` ([HGNC identifier CURIE pattern](ega-4-definitions-hgnc-identifier-curie-pattern.md))

all of

*   [Compact URI (CURIE) pattern](ega-4-definitions-compact-uri-curie-pattern.md "check type definition")

## curieHgncIdentifierPattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^((HGNC|hgnc):)?\d{1,5}$
```

[try pattern](https://regexr.com/?expression=%5E\(\(HGNC%7Chgnc\)%3A\)%3F%5Cd%7B1%2C5%7D%24 "try regular expression with regexr.com")

## curieHgncIdentifierPattern Examples

```json
"hgnc:2674"
```

```json
"HGNC:11535"
```
