# NZ - Molecule type: DNA Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/curie_refseq_pattern/oneOf/2
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 2 Type

unknown ([NZ - Molecule type: DNA](ega-12-definitions-refseq-accessions-data1098-curie-pattern-oneof-nz---molecule-type-dna.md))

## 2 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^:]+:NZ_[A-Z]{2,4}\d+(\.\d+)?$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%3A%5D%2B%3ANZ_%5BA-Z%5D%7B2%2C4%7D%5Cd%2B\(%5C.%5Cd%2B\)%3F%24 "try regular expression with regexr.com")
