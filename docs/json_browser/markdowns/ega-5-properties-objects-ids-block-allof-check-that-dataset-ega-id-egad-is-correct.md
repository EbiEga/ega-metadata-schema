# Check that dataset EGA ID (EGAD) is correct Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectId/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.dataset.json\*](../../../schemas/EGA.dataset.json "open original schema") |

## 1 Type

unknown ([Check that dataset EGA ID (EGAD) is correct](ega-5-properties-objects-ids-block-allof-check-that-dataset-ega-id-egad-is-correct.md))

# 1 Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                               |
| :---------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [egaAccession](#egaaccession) | `string` | Optional | cannot be null | [EGA dataset metadata schema](ega-4-definitions-pattern-of-an-ega-datasets-id-egad.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectId/allOf/1/properties/egaAccession") |

## egaAccession



`egaAccession`

*   is optional

*   Type: `string` ([Pattern of an EGA dataset's ID (EGAD...)](ega-4-definitions-pattern-of-an-ega-datasets-id-egad.md))

*   cannot be null

*   defined in: [EGA dataset metadata schema](ega-4-definitions-pattern-of-an-ega-datasets-id-egad.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectId/allOf/1/properties/egaAccession")

### egaAccession Type

`string` ([Pattern of an EGA dataset's ID (EGAD...)](ega-4-definitions-pattern-of-an-ega-datasets-id-egad.md))

### egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAD[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAD%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### egaAccession Examples

```json
"EGAD00001004170"
```
