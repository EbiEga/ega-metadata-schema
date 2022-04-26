# Phone number Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/contact_details/properties/phone_number
```

Current phone number that would be used in case the contact needs to be reached. Theoretically would only be used in case the email address was not provided, does not exist or is unresponsive.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## phone\_number Type

`string` ([Phone number](ega-12-definitions-contact-details-properties-phone-number.md))

## phone\_number Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^\+?\(?[0-9]{1,4}\)?[-\s\./0-9]+$
```

[try pattern](https://regexr.com/?expression=%5E%5C%2B%3F%5C\(%3F%5B0-9%5D%7B1%2C4%7D%5C\)%3F%5B-%5Cs%5C.%2F0-9%5D%2B%24 "try regular expression with regexr.com")

## phone\_number Examples

```json
"+44 7427512529"
```
