# Data Use Ontology (DUO) codes' curies Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/duoCodesCuries
```

Collection of Data Use Ontology (DUO) codes in Shorter Compact URI (CURIE) format. These allow to semantically tag datasets (bound by policies) with restriction about their usage, making them discoverable automatically based on the authorization level of users, or intended usage. See more info at <https://obofoundry.org/ontology/duo.html> and search for DUO codes at <https://www.ebi.ac.uk/ols/ontologies/duo>

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## duoCodesCuries Type

`string[]` ([Data Use Ontology (DUO) code](ega-16-properties-data-use-ontology-duo-codes-curies-data-use-ontology-duo-code.md))

## duoCodesCuries Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.