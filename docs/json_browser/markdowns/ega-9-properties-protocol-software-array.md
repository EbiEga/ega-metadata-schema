# Protocol software array Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolSoftware
```

Array of software descriptions used in the protocol. It is not indispensable to provide each and every piece of software used, but a set of the ones you would highlight in your protocol for other researchers to know, since it will help them discover your data.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## protocolSoftware Type

`string[]` ([Software descriptions used in the protocol](ega-9-properties-protocol-software-array-software-descriptions-used-in-the-protocol.md))

## protocolSoftware Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
