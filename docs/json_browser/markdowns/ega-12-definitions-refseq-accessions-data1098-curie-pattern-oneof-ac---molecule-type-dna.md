# AC - Molecule type: DNA Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/curieRefseqPattern/oneOf/1
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 1 Type

unknown ([AC - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-ac---molecule-type-dna.md))

## 1 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^:]+:AC_\d+(\.\d+)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3A%5D%2B%3AAC_%5Cd%2B\(%5C.%5Cd%2B\)%3F%24 "try regular expression with regexr.com")
