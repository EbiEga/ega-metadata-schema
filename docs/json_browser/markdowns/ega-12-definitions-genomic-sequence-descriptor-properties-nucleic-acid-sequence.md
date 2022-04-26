# Nucleic acid sequence Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/genomic_sequence_descriptor/properties/nucleic_acid_sequence
```

Sequence of characters representing a specific nucleic (i.e. molecular species - e.g. Adenine) or groupings of these (through ambiguity codes), using [one-letter IUPAC abbreviations](https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry#Amino_acid_and_nucleotide_base_codes).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## nucleic\_acid\_sequence Type

`string` ([Nucleic acid sequence](ega-12-definitions-genomic-sequence-descriptor-properties-nucleic-acid-sequence.md))

## nucleic\_acid\_sequence Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([\.-]*[ACGTURYKMSWBDHVNX]+[\.-]*)+$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B%5C.-%5D*%5BACGTURYKMSWBDHVNX%5D%2B%5B%5C.-%5D*\)%2B%24 "try regular expression with regexr.com")

## nucleic\_acid\_sequence Examples

```json
"ACTGCCG"
```

```json
"CTGCGCGCGCT"
```

```json
"KM-AGT-X-N"
```
