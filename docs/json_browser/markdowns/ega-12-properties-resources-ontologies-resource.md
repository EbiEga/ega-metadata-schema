# Resource Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items
```

Object defining one item of the array: an individual resource (i.e. ontology).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## items Type

`object` ([Resource](ega-12-properties-resources-ontologies-resource.md))

# items Properties

| Property                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                  |
| :---------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [name](#name)                                   | `string`  | Required | cannot be null | [EGA submission metadata schema](ega-12-properties-resources-ontologies-resource-properties-resource-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/name")                                   |
| [namespacePrefix](#namespaceprefix)             | `string`  | Required | cannot be null | [EGA submission metadata schema](ega-12-properties-resources-ontologies-resource-properties-resource-namespace-prefix.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/namespacePrefix")            |
| [version](#version)                             | `string`  | Required | cannot be null | [EGA submission metadata schema](ega-12-properties-resources-ontologies-resource-properties-resource-version.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/version")                             |
| [automaticallyAssigned](#automaticallyassigned) | `boolean` | Optional | cannot be null | [EGA submission metadata schema](ega-12-properties-resources-ontologies-resource-properties-automatically-assigned-boolean.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/automaticallyAssigned") |

## name

Formal (common) name of the resource.

`name`

*   is required

*   Type: `string` ([Resource name](ega-12-properties-resources-ontologies-resource-properties-resource-name.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-resources-ontologies-resource-properties-resource-name.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/name")

### name Type

`string` ([Resource name](ega-12-properties-resources-ontologies-resource-properties-resource-name.md))

### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### name Examples

```json
"Human Phenotype Ontology"
```

```json
"Experimental Factor Ontology"
```

```json
"PubMed"
```

## namespacePrefix

Prefixes of namespaces are used to uniquely resolve the ambiguity between identically named elements or attributes. They can easily be checked at [**identifiers.org**](https://identifiers.org/) or [**OLS' list of ontologies**](https://www.ebi.ac.uk/ols/ontologies). For example, in our example of diabetes melitus, EFO:0000400, we need both parts of the CURIE: EFO (prefix) and 0000400 (local identifier). Without knowing the prefix, the local identifier alone is difficult to resolve.

`namespacePrefix`

*   is required

*   Type: `string` ([Resource namespace prefix](ega-12-properties-resources-ontologies-resource-properties-resource-namespace-prefix.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-resources-ontologies-resource-properties-resource-namespace-prefix.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/namespacePrefix")

### namespacePrefix Type

`string` ([Resource namespace prefix](ega-12-properties-resources-ontologies-resource-properties-resource-namespace-prefix.md))

### namespacePrefix Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### namespacePrefix Examples

```json
"hp"
```

```json
"efo"
```

```json
"pubmed"
```

## version

The version of the used resource. This is the main item of the object, since it's not included within the CURIEs and allows for traceability in the future. The version of an ontology varies in format and can be checked in multiple ways, the easiest being: (1) going straight to the source of the ontology, commonly a GitHub repository (e.g. [EFO's GH repo](https://github.com/EBISPOT/efo/releases)) and checking the latest release; (2) checking the latest version that the OLS service uses (e.g. 'version' field at [EFO's record](https://www.ebi.ac.uk/ols/ontologies/efo)).

`version`

*   is required

*   Type: `string` ([Resource version](ega-12-properties-resources-ontologies-resource-properties-resource-version.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-resources-ontologies-resource-properties-resource-version.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/version")

### version Type

`string` ([Resource version](ega-12-properties-resources-ontologies-resource-properties-resource-version.md))

### version Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### version Examples

```json
"2022-06-11"
```

```json
"3.45.0"
```

## automaticallyAssigned

Boolean switch to know if this specific resource was automatically assigned by EGA during the curation process ('true') or if it was manually given by the submitter ('false'). If this attribute is non-existent, it will also be considered to be 'false'.

`automaticallyAssigned`

*   is optional

*   Type: `boolean` ([Automatically assigned boolean](ega-12-properties-resources-ontologies-resource-properties-automatically-assigned-boolean.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-properties-resources-ontologies-resource-properties-automatically-assigned-boolean.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/automaticallyAssigned")

### automaticallyAssigned Type

`boolean` ([Automatically assigned boolean](ega-12-properties-resources-ontologies-resource-properties-automatically-assigned-boolean.md))
