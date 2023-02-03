# Additional DAC contacts' details Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts/properties/additionalContacts
```

An array compromising additional contact details to use when in need to reach the DAC yet the main contact is unresponsive or does not exist.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.DAC.json\*](../../../schemas/EGA.DAC.json "open original schema") |

## additionalContacts Type

`object[]` ([Contact details](ega-4-definitions-contact-details.md))

## additionalContacts Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
