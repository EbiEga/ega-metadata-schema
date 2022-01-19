# Custom attribute of an object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_attributes/items
```

Reusable attributes to encode tag-value pairs (e.g. Tag being 'Age' and its Value '40') with optional units (e.g. 'years').

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json*](../out/EGA.sample.json "open original schema") |

## items Type

`object` ([Custom attribute of an object](ega-4-definitions-custom-attribute-of-an-object.md))

# items Properties

| Property        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                  |
| :-------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [tag](#tag)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/tag")     |
| [value](#value) | Multiple | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/value") |
| [units](#units) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/units") |

## tag

The name of the attribute (e.g. 'Age').

`tag`

*   is required

*   Type: `string` ([Tag of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/tag")

### tag Type

`string` ([Tag of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-tag-of-the-custom-attribute.md))

### tag Examples

```json
"age"
```

## value

The value of the attribute (e.g. '40').

`value`

*   is required

*   Type: any of the folllowing: `string` or `number` ([Value of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/value")

### value Type

any of the folllowing: `string` or `number` ([Value of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-value-of-the-custom-attribute.md))

### value Examples

```json
"40"
```

## units

The optional units of the attribute (e.g. 'years').

`units`

*   is optional

*   Type: `string` ([Units of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/custom_attribute/properties/units")

### units Type

`string` ([Units of the custom attribute](ega-4-definitions-custom-attribute-of-an-object-properties-units-of-the-custom-attribute.md))

### units Examples

```json
"years"
```
