# Individual's age range at sample collection Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/ageRange
```

Age range of the individual when the sample was collected. Composed of two (start and end) age points.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## ageRange Type

`object` ([Individual's age range at sample collection](ega-10-properties-sample-collection-descriptor-properties-individuals-age-at-sample-collection-properties-individuals-age-range-at-sample-collection.md))

# ageRange Properties

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                           |
| :-------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [start](#start) | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-4-defs-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/ageRange/properties/start") |
| [end](#end)     | `string` | Optional | cannot be null | [EGA sample metadata schema](ega-4-defs-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/ageRange/properties/end")   |

## start

Precise age in ISO8601 format of the individual. For example, 'P3Y6M4D' represents a duration of three years, six months and four days.

`start`

*   is optional

*   Type: `string` ([Individual's age](ega-4-defs-individuals-age.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-4-defs-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/ageRange/properties/start")

### start Type

`string` ([Individual's age](ega-4-defs-individuals-age.md))

### start Constraints

**duration**: the string must be a duration string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

### start Examples

```json
"P3Y6M4D"
```

```json
"P4Y"
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

## end

Precise age in ISO8601 format of the individual. For example, 'P3Y6M4D' represents a duration of three years, six months and four days.

`end`

*   is optional

*   Type: `string` ([Individual's age](ega-4-defs-individuals-age.md))

*   cannot be null

*   defined in: [EGA sample metadata schema](ega-4-defs-individuals-age.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleCollection/properties/ageAtCollection/properties/ageRange/properties/end")

### end Type

`string` ([Individual's age](ega-4-defs-individuals-age.md))

### end Constraints

**duration**: the string must be a duration string, according to [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339 "check the specification")

### end Examples

```json
"P3Y6M4D"
```

```json
"P4Y"
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
