# Pattern of an EGA ArrayExperiment's ID (EGAE...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_id/allOf/1/properties/ega_accession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## ega_accession Type

`string` ([Pattern of an EGA ArrayExperiment's ID (EGAE...)](ega-1-properties-objects-ids-block-allof-check-that-arrayexperiment-ega-id-egae-is-correct-properties-pattern-of-an-ega-arrayexperiments-id-egae.md))

## ega_accession Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^EGAE[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAE%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## ega_accession Examples

```json
"EGAE00001004508"
```