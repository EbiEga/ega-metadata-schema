# Full name of an individual Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/contactDetails/properties/individualFullName
```

A full set of all personal names by which an individual is known and that can be recited as a word-group, with the understanding that, taken together, they all relate to that one individual. In case there are several, separate them with semicolons (;).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## individualFullName Type

`string` ([Full name of an individual](ega-4-definitions-contact-details-properties-full-name-of-an-individual.md))

## individualFullName Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## individualFullName Examples

```json
"Wayne Jr., Bruce"
```
