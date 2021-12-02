# Type of the relationship Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type
```

The Type of the relationship, containing both its ID (e.g. same_as and the CURIE (e.g. NCIT:C64637), that summarises its purpose. #! The list of CV shall be agreed on, improved and enlarged.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## r_type Type

`object` ([Type of the relationship](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship.md))

any of

*   [Check that r_type is present](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-anyof-check-that-r_type-is-present.md "check type definition")

*   [Check that r_type_curie is present](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-anyof-check-that-r_type_curie-is-present.md "check type definition")

# r_type Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                       |
| :---------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r_type_id](#r_type_id)       | `string` | Optional | cannot be null | [EGA common metadata definitions v0.0.1](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type/properties/r_type_id")       |
| [r_type_curie](#r_type_curie) | `string` | Optional | cannot be null | [EGA common metadata definitions v0.0.1](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type/properties/r_type_curie") |

## r_type_id

The human readable ID (e.g. same_as), chosen from a list of CVs, of the type of the relationship.

`r_type_id`

*   is optional

*   Type: `string` ([Type of the relationship - ID](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---id.md))

*   cannot be null

*   defined in: [EGA common metadata definitions v0.0.1](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type/properties/r_type_id")

### r_type_id Type

`string` ([Type of the relationship - ID](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---id.md))

### r_type_id Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                        | Explanation |
| :--------------------------- | :---------- |
| `"referenced_by"`            |             |
| `"develops_from"`            |             |
| `"same_as"`                  |             |
| `"member_of"`                |             |
| `"grouped_with"`             |             |
| `"family_relationship_with"` |             |
| `"child_of"`                 |             |
| `"parent_of"`                |             |
| `"is_after"`                 |             |
| `"published_in"`             |             |
| `"submitted_by"`             |             |
| `"contact_of"`               |             |
| `"main_contact_of"`          |             |

### r_type_id Examples

```json
"referenced_by"
```

## r_type_curie

The CURIE (i.e. ontologized term - e.g. NCIT:C64637), chosen from a list of CVs, of the type of the relationship.

`r_type_curie`

*   is optional

*   Type: `string` ([Type of the relationship - CURIE](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---curie.md))

*   cannot be null

*   defined in: [EGA common metadata definitions v0.0.1](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---curie.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type/properties/r_type_curie")

### r_type_curie Type

`string` ([Type of the relationship - CURIE](ega-2-definitions-ega-relationships-object-properties-type-of-the-relationship-properties-type-of-the-relationship---curie.md))

### r_type_curie Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"SIO:000252"`  |             |
| `"RO:0002202"`  |             |
| `"NCIT:C64637"` |             |
| `"RO:0002350"`  |             |
| `"EFO:0004424"` |             |
| `"GSSO:000728"` |             |
| `"GSSO:001986"` |             |
| `"SIO:000211"`  |             |
| `"EFO:0001796"` |             |
| `"NCIT:C25695"` |             |
| `"NCIT:C25461"` |             |

### r_type_curie Examples

```json
"RO:0002202"
```
