# Biologic entity classification scientific name Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/organism_descriptor/properties/scientific_name
```

The name applied to a plant, animal, or other organism, according to the Codes of Nomenclature, consisting of a Genus and species (e.g. 'homo sapiens').

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## scientific\_name Type

`string` ([Biologic entity classification scientific name](ega-12-definitions-organism-obi0100026-descriptor-block-properties-biologic-entity-classification-scientific-name.md))

## scientific\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## scientific\_name Examples

```json
"homo sapiens"
```

```json
"uncultured organism"
```

```json
"human gut metagenome"
```

```json
"human oral metagenome"
```
