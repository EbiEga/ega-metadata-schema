# Name of the protocol Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_name
```

Name of the protocol (e.g. 'myProtocol-13'). To be defined by the user.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## protocol\_name Type

`string` ([Name of the protocol](ega-12-definitions-ega-protocols-object-properties-name-of-the-protocol.md))

## protocol\_name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## protocol\_name Examples

```json
"myProtocol-13"
```

```json
"Treatment for leukemia patients C30"
```

```json
"Sample collection from infected patients"
```
