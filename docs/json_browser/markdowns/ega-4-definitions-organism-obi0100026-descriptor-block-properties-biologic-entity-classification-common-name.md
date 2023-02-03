# Biologic entity classification common name Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organismDescriptor/properties/commonName
```

Common name (e.g. 'human') used to designate a plant, animal or other organism, as opposed to the scientific name.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## commonName Type

`string` ([Biologic entity classification common name](ega-4-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-common-name.md))

## commonName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## commonName Examples

```json
"human"
```

```json
"goat"
```

```json
"horse"
```
