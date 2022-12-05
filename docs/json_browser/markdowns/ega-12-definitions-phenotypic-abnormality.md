# Phenotypic abnormality Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypes/items
```

Property to describe any abnormal (i.e. deviation from normal or average) phenotype (i.e. detectable outward manifestations of a specific genotype).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## items Type

`object` ([Phenotypic abnormality](ega-12-definitions-phenotypic-abnormality.md))

# items Properties

| Property                                                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [phenotypicAbnormalityCurie](#phenotypicabnormalitycurie) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormalityDescriptor/properties/phenotypicAbnormalityCurie") |
| [phenotypicAbnormalityLabel](#phenotypicabnormalitylabel) | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-phenotypic-abnormality-properties-label-of-the-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormalityDescriptor/properties/phenotypicAbnormalityLabel")             |

## phenotypicAbnormalityCurie



`phenotypicAbnormalityCurie`

*   is required

*   Type: `string` ([Compact URI (CURIE) of the phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormalityDescriptor/properties/phenotypicAbnormalityCurie")

### phenotypicAbnormalityCurie Type

`string` ([Compact URI (CURIE) of the phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality.md))

any of

*   [Ontology validation of phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality-anyof-ontology-validation-of-phenotypic-abnormality.md "check type definition")

*   [In case the phenotypic abnormality is unknown or there is none](ega-12-definitions-phenotypic-abnormality-properties-compact-uri-curie-of-the-phenotypic-abnormality-anyof-in-case-the-phenotypic-abnormality-is-unknown-or-there-is-none.md "check type definition")

### phenotypicAbnormalityCurie Examples

```json
"HP:0003003"
```

```json
"HP:0010442"
```

```json
"HP:0002515"
```

```json
"NCIT:C17998"
```

```json
"NCIT:C94232"
```

## phenotypicAbnormalityLabel



`phenotypicAbnormalityLabel`

*   is optional

*   Type: `string` ([Label of the phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-label-of-the-phenotypic-abnormality.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-phenotypic-abnormality-properties-label-of-the-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/phenotypicAbnormalityDescriptor/properties/phenotypicAbnormalityLabel")

### phenotypicAbnormalityLabel Type

`string` ([Label of the phenotypic abnormality](ega-12-definitions-phenotypic-abnormality-properties-label-of-the-phenotypic-abnormality.md))

### phenotypicAbnormalityLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### phenotypicAbnormalityLabel Examples

```json
"Colon cancer"
```

```json
"Polydactyly"
```

```json
"Waddling gait"
```

```json
"Unknown"
```

```json
"Unaffected"
```
