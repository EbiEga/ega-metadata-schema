# Previous protocol step index Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/previous_protocol_step_index
```

The 'protocol_step_index' of the previous protocol, if hierarchically ordered. Set to '0' if this protocol is the first step. In case several protocols are not sequential, both can share the same 'previous_protocol_step_index'.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## previous_protocol_step_index Type

`number` ([Previous protocol step index](ega-12-definitions-ega-protocols-object-properties-previous-protocol-step-index.md))

## previous_protocol_step_index Examples

```json
0
```

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
