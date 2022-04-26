# Protocol step index Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_step_index
```

Lexically ordered value (greater than 0) that allows for the protocol section to be sequentially ordered. The float primitive data type is used to allow for pipe sections to be inserted later on. In other words, adding a new intermediate step 1.1 between steps 1 and 2 afterwards. For example, in an experiment where we treated samples before its DNA extraction, the sample treatment protocol would have a lower 'protocol\_step\_index' than the DNA extraction.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## protocol\_step\_index Type

`number` ([Protocol step index](ega-12-definitions-ega-protocols-object-properties-protocol-step-index.md))

## protocol\_step\_index Examples

```json
0.5
```

```json
1
```

```json
2.5
```

```json
2
```

```json
30
```
