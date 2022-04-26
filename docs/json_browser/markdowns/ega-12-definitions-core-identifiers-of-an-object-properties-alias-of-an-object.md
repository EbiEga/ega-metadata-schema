# Alias of an object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object_core_id/properties/alias
```

Submitter designated name (e.g. 'my\_sample\_J13') for the object (e.g. Sample). The name must be unique within the submission account (e.g. 'ega-box-79'), since the aliases and submission accounts are concatenated within our database to obtain the unique alias (e.g. 'ega-box-79::my\_sample\_J13').

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## alias Type

`string` ([Alias of an object](ega-12-definitions-core-identifiers-of-an-object-properties-alias-of-an-object.md))

## alias Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## alias Examples

```json
"my_sample_J13"
```
