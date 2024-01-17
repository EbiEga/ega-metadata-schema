# Pattern of an EGA experiment's ID (EGAX...) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/objectId/allOf/1/properties/egaAccession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## egaAccession Type

`string` ([Pattern of an EGA experiment's ID (EGAX...)](ega-4-defs-pattern-of-an-ega-experiments-id-egax.md))

## egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAX[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAX%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## egaAccession Examples

```json
"EGAX00002189113"
```