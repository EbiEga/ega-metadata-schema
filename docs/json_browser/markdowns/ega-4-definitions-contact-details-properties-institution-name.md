# Institution name Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/institutionName
```

The full name of an institution the contact belongs to. In case there are several, separate them with semicolons (;).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## institutionName Type

`string` ([Institution name](ega-4-definitions-contact-details-properties-institution-name.md))

## institutionName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## institutionName Examples

```json
"European Genome-phenome Archive (EGA)"
```
