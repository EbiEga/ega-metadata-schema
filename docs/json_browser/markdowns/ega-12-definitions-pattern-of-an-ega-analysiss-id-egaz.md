# Pattern of an EGA analysis's ID (EGAZ...) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/EGA-analysis-id-pattern
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## EGA-analysis-id-pattern Type

`string` ([Pattern of an EGA analysis's ID (EGAZ...)](ega-12-definitions-pattern-of-an-ega-analysiss-id-egaz.md))

## EGA-analysis-id-pattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAZ[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAZ%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

## EGA-analysis-id-pattern Examples

```json
"EGAZ00001004170"
```
