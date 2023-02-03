# Individual's age Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/ageRange/properties/end
```

Precise age in ISO8601 format of the individual. For example, 'P3Y6M4D' represents a duration of three years, six months and four days.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## end Type

`string` ([Individual's age](ega-4-definitions-individuals-age.md))

all of

*   [Pattern of a partial EGA ISO 8601 duration](ega-4-definitions-pattern-of-a-partial-ega-iso-8601-duration.md "check type definition")

## end Examples

```json
"P3Y6M4D"
```

```json
"P23DT23H"
```

```json
"P4Y"
```
