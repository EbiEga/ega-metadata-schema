# Pattern of a partial EGA ISO 8601 duration Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/individualAge/allOf/0
```

Pattern of ISO 8601 durations. It can be used to define time intervals (e.g. 'P3Y6M4DT12H30M5S' represents a duration of three years, six months, four days, twelve hours, thirty minutes, and five seconds). See more at <https://en.wikipedia.org/wiki/ISO_8601#Durations>.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 0 Type

`string` ([Pattern of a partial EGA ISO 8601 duration](ega-4-definitions-pattern-of-a-partial-ega-iso-8601-duration.md))

## 0 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[-+]?P(?!$)(([-+]?\d+Y)|([-+]?\d+\.\d+Y$))?(([-+]?\d+M)|([-+]?\d+\.\d+M$))?(([-+]?\d+W)|([-+]?\d+\.\d+W$))?(([-+]?\d+D)|([-+]?\d+\.\d+D$))?(T(?=[\d+-])(([-+]?\d+H)|([-+]?\d+\.\d+H$))?(([-+]?\d+M)|([-+]?\d+\.\d+M$))?([-+]?\d+(\.\d+)?S)?)??$
```

[try pattern](https://regexr.com/?expression=%5E%5B-%2B%5D%3FP\(%3F!%24\)\(\(%5B-%2B%5D%3F%5Cd%2BY\)%7C\(%5B-%2B%5D%3F%5Cd%2B%5C.%5Cd%2BY%24\)\)%3F\(\(%5B-%2B%5D%3F%5Cd%2BM\)%7C\(%5B-%2B%5D%3F%5Cd%2B%5C.%5Cd%2BM%24\)\)%3F\(\(%5B-%2B%5D%3F%5Cd%2BW\)%7C\(%5B-%2B%5D%3F%5Cd%2B%5C.%5Cd%2BW%24\)\)%3F\(\(%5B-%2B%5D%3F%5Cd%2BD\)%7C\(%5B-%2B%5D%3F%5Cd%2B%5C.%5Cd%2BD%24\)\)%3F\(T\(%3F%3D%5B%5Cd%2B-%5D\)\(\(%5B-%2B%5D%3F%5Cd%2BH\)%7C\(%5B-%2B%5D%3F%5Cd%2B%5C.%5Cd%2BH%24\)\)%3F\(\(%5B-%2B%5D%3F%5Cd%2BM\)%7C\(%5B-%2B%5D%3F%5Cd%2B%5C.%5Cd%2BM%24\)\)%3F\(%5B-%2B%5D%3F%5Cd%2B\(%5C.%5Cd%2B\)%3FS\)%3F\)%3F%3F%24 "try regular expression with regexr.com")

## 0 Examples

```json
"P3Y6M4DT12H30M5S"
```

```json
"P23DT23H"
```

```json
"PT0S"
```

```json
"P0D"
```

```json
"P0,5Y"
```

```json
"P0.5Y"
```
