# Data Use Ontology (DUO) codes Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.policy.json#/properties/duoCodes
```

Collection of Data Use Ontology (DUO) codes. These allow to semantically tag datasets (bound by policies) with restriction about their usage, improving their discoverability based on the authorization level of users, or intended usage. See more info at <https://obofoundry.org/ontology/duo.html> and search for DUO codes at <https://www.ebi.ac.uk/ols/ontologies/duo>

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.policy.json\*](../../../schemas/EGA.policy.json "open original schema") |

## duoCodes Type

`object[]` ([Data Use Ontology (DUO)](ega-8-properties-data-use-ontology-duo-codes-data-use-ontology-duo.md))

## duoCodes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
