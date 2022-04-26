# DAC: object\_id and object\_type check Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/10
```

A check that ensures that, if 'DAC' is given as the object\_type and an EGA accession for it is given, it matches the corresponding EGA ID pattern.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 10 Type

unknown ([DAC: object\_id and object\_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md))

# 10 Properties

| Property                     | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                             |
| :--------------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id)     | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check-properties-object_id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/10/properties/object_id")     |
| [object\_type](#object_type) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check-properties-object_type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/10/properties/object_type") |

## object\_id



`object_id`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check-properties-object_id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/10/properties/object_id")

### object\_id Type

unknown

## object\_type



`object_type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check-properties-object_type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/object-id-and-object-type-check/anyOf/10/properties/object_type")

### object\_type Type

unknown

### object\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"DAC"` |             |
