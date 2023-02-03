# Resource version Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources/items/properties/version
```

The version of the used resource. This is the main item of the object, since it's not included within the CURIEs and allows for traceability in the future. The version of an ontology varies in format and can be checked in multiple ways, the easiest being: (1) going straight to the source of the ontology, commonly a GitHub repository (e.g. [EFO's GH repo](https://github.com/EBISPOT/efo/releases)) and checking the latest release; (2) checking the latest version that the OLS service uses (e.g. 'version' field at [EFO's record](https://www.ebi.ac.uk/ols/ontologies/efo)).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## version Type

`string` ([Resource version](ega-12-properties-resources-ontologies-resource-properties-resource-version.md))

## version Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## version Examples

```json
"2022-06-11"
```

```json
"3.45.0"
```
