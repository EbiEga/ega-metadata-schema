# Individual's age range at sample collection Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/age_at_collection/properties/age_range
```

Age range of the individual when the sample was collected. Composed of two (start and end) age points.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## age\_range Type

`object` ([Individual's age range at sample collection](ega-18-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-properties-individuals-age-range-at-sample-collection.md))

# age\_range Properties

| Property        | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                       |
| :-------------- | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [start](#start) | Merged | Optional | cannot be null | [EGA sample metadata schema](ega-12-definitions-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/age_at_collection/properties/age_range/properties/start") |
| [end](#end)     | Merged | Optional | cannot be null | [EGA sample metadata schema](ega-12-definitions-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/age_at_collection/properties/age_range/properties/end")   |

## start

Precise age in ISO8601 format of the individual. For example, 'P3Y6M4D' represents a duration of three years, six months and four days.

`start`

*   is optional

*   Type: `string` ([Individual's age](ega-12-definitions-individuals-age.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-12-definitions-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/age_at_collection/properties/age_range/properties/start")

### start Type

`string` ([Individual's age](ega-12-definitions-individuals-age.md))

all of

*   [Pattern of a partial EGA ISO 8601 duration](ega-12-definitions-pattern-of-a-partial-ega-iso-8601-duration.md "check type definition")

### start Examples

```json
"P3Y6M4D"
```

```json
"P23DT23H"
```

```json
"P4Y"
```

## end

Precise age in ISO8601 format of the individual. For example, 'P3Y6M4D' represents a duration of three years, six months and four days.

`end`

*   is optional

*   Type: `string` ([Individual's age](ega-12-definitions-individuals-age.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-12-definitions-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sample_collection/properties/age_at_collection/properties/age_range/properties/end")

### end Type

`string` ([Individual's age](ega-12-definitions-individuals-age.md))

all of

*   [Pattern of a partial EGA ISO 8601 duration](ega-12-definitions-pattern-of-a-partial-ega-iso-8601-duration.md "check type definition")

### end Examples

```json
"P3Y6M4D"
```

```json
"P23DT23H"
```

```json
"P4Y"
```
