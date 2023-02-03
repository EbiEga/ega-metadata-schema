# Pattern of an EGA DAC's ID (EGAC...) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/objectId/allOf/1/properties/egaAccession
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.DAC.json\*](../../../schemas/EGA.DAC.json "open original schema") |

## egaAccession Type

`string` ([Pattern of an EGA DAC's ID (EGAC...)](ega-properties-objects-ids-block-allof-check-that-dac-ega-id-egac-is-correct-properties-pattern-of-an-ega-dacs-id-egac.md))

## egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAC[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAC%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## egaAccession Examples

```json
"EGAC00001000908"
```
