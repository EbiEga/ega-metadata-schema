# Disease Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases/items
```

Property to describe a disease (i.e. a disposition to undergo pathological processes because of one or more disorders).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## items Type

`object` ([Disease](ega-12-definitions-disease.md))

# items Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                  |
| :---------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [diseaseCurie](#diseasecurie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/diseaseDescriptor/properties/diseaseCurie") |
| [diseaseLabel](#diseaselabel) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-disease-properties-label-of-the-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/diseaseDescriptor/properties/diseaseLabel")             |

## diseaseCurie



`diseaseCurie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the disease](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/diseaseDescriptor/properties/diseaseCurie")

### diseaseCurie Type

`string` ([Compact URI (CURIE) of the disease](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease.md))

one (and only one) of

*   [Ontology validation of dieases](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease-oneof-ontology-validation-of-dieases.md "check type definition")

*   [In case whether the individual has a disease is unknown or there is none](ega-12-definitions-disease-properties-compact-uri-curie-of-the-disease-oneof-in-case-whether-the-individual-has-a-disease-is-unknown-or-there-is-none.md "check type definition")

### diseaseCurie Examples

```json
"MONDO:0100096"
```

```json
"EFO:0003101"
```

```json
"NCIT:C17998"
```

```json
"NCIT:C94232"
```

## diseaseLabel



`diseaseLabel`

*   is optional

*   Type: `string` ([Label of the disease](ega-12-definitions-disease-properties-label-of-the-disease.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-disease-properties-label-of-the-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/diseaseDescriptor/properties/diseaseLabel")

### diseaseLabel Type

`string` ([Label of the disease](ega-12-definitions-disease-properties-label-of-the-disease.md))

### diseaseLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### diseaseLabel Examples

```json
"COVID-19"
```

```json
"testicular seminoma"
```

```json
"Unknown"
```

```json
"Unaffected"
```
