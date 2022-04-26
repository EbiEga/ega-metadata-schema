# Semantic versioning pattern Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/schema_descriptor/properties/object_schema_version/allOf/0
```

This object exists to hold the pattern that semantic versioning has, for it to be referenced elsewhere within this (or other) JSON schema. For further details about semantic versioning check '<https://semver.org/>'

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 0 Type

`string` ([Semantic versioning pattern](ega-12-definitions-schema-descriptor-properties-version-of-the-objects-schema-allof-semantic-versioning-pattern.md))

## 0 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9]+\.[0-9]+\.[0-9]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9%5D%2B%5C.%5B0-9%5D%2B%5C.%5B0-9%5D%2B%24 "try regular expression with regexr.com")

## 0 Examples

```json
"2.5.1"
```
