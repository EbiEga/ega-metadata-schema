# Pattern of an EGA DAC's ID (EGAC...) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/object_id/allOf/1/properties/ega_accession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.DAC.json\*](../../../schemas/EGA.DAC.json "open original schema") |

## ega\_accession Type

`string` ([Pattern of an EGA DAC's ID (EGAC...)](ega-8-properties-objects-ids-block-allof-check-that-dac-ega-id-egac-is-correct-properties-pattern-of-an-ega-dacs-id-egac.md))

## ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAC[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAC%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## ega\_accession Examples

```json
"EGAC00001000908"
```
