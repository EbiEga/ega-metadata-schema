# DAC contacts' details Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts
```

Object containing the main contact's and optional additional contact's details.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.DAC.json\*](../../../schemas/EGA.DAC.json "open original schema") |

## dacContacts Type

`object` ([DAC contacts' details](ega-properties-dac-contacts-details.md))

# dacContacts Properties

| Property                                  | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                  |
| :---------------------------------------- | :------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [mainContact](#maincontact)               | Merged  | Required | cannot be null | [EGA DAC metadata schema](ega-4-definitions-contact-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts/properties/mainContact")                                                     |
| [additionalContacts](#additionalcontacts) | `array` | Optional | cannot be null | [EGA DAC metadata schema](ega-properties-dac-contacts-details-properties-additional-dac-contacts-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts/properties/additionalContacts") |

## mainContact

An object to contain the required metadata to identify and reach an individual or institution. Used, for instance, to list who needs to be informed (1) in case of a erroneous submission (2) or in case access to a dataset is requested by a user.

`mainContact`

*   is required

*   Type: `object` ([Contact details](ega-4-definitions-contact-details.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-4-definitions-contact-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts/properties/mainContact")

### mainContact Type

`object` ([Contact details](ega-4-definitions-contact-details.md))

any of

*   [Either the individual's name is required.](ega-4-definitions-contact-details-anyof-either-the-individuals-name-is-required.md "check type definition")

*   [Or the institution's name is required.](ega-4-definitions-contact-details-anyof-or-the-institutions-name-is-required.md "check type definition")

## additionalContacts

An array compromising additional contact details to use when in need to reach the DAC yet the main contact is unresponsive or does not exist.

`additionalContacts`

*   is optional

*   Type: `object[]` ([Contact details](ega-4-definitions-contact-details.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-properties-dac-contacts-details-properties-additional-dac-contacts-details.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.DAC.json#/properties/dacContacts/properties/additionalContacts")

### additionalContacts Type

`object[]` ([Contact details](ega-4-definitions-contact-details.md))

### additionalContacts Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
