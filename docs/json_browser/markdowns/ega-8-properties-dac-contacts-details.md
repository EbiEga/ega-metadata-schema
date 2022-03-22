# DAC contacts' details Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/dac_contacts
```

Object containing the main contact's and optional additional contact's details.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.DAC.json*](../out/EGA.DAC.json "open original schema") |

## dac_contacts Type

`object` ([DAC contacts' details](ega-8-properties-dac-contacts-details.md))

# dac_contacts Properties

| Property                                    | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                            |
| :------------------------------------------ | :------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [main_contact](#main_contact)               | Merged  | Required | cannot be null | [EGA DAC metadata schema](ega-12-definitions-contact-details.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/dac_contacts/properties/main_contact")                                                      |
| [additional_contacts](#additional_contacts) | `array` | Optional | cannot be null | [EGA DAC metadata schema](ega-8-properties-dac-contacts-details-properties-additional-dac-contacts-details.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/dac_contacts/properties/additional_contacts") |

## main_contact

An object to contain the required metadata to identify and reach an individual or institution. Used, for instance, to list who needs to be informed (1) in case of a erroneous submission (2) or in case access to a dataset is requested by a user.

`main_contact`

*   is required

*   Type: `object` ([Contact details](ega-12-definitions-contact-details.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-12-definitions-contact-details.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/dac_contacts/properties/main_contact")

### main_contact Type

`object` ([Contact details](ega-12-definitions-contact-details.md))

any of

*   [Either the individual's name is required.](ega-12-definitions-contact-details-anyof-either-the-individuals-name-is-required.md "check type definition")

*   [Or the institution's name is required.](ega-12-definitions-contact-details-anyof-or-the-institutions-name-is-required.md "check type definition")

## additional_contacts

An array compromising additional contact details to use when in need to reach the DAC yet the main contact is unresponsive or does not exist.

`additional_contacts`

*   is optional

*   Type: `object[]` ([Contact details](ega-12-definitions-contact-details.md))

*   cannot be null

*   defined in: [EGA DAC metadata schema](ega-8-properties-dac-contacts-details-properties-additional-dac-contacts-details.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.DAC.json#/properties/dac_contacts/properties/additional_contacts")

### additional_contacts Type

`object[]` ([Contact details](ega-12-definitions-contact-details.md))

### additional_contacts Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
