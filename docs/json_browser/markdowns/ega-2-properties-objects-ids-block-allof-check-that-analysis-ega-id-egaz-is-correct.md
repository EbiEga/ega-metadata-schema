# Check that analysis EGA ID (EGAZ) is correct Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectId/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.analysis.json\*](../../../schemas/EGA.analysis.json "open original schema") |

## 1 Type

unknown ([Check that analysis EGA ID (EGAZ) is correct](ega-2-properties-objects-ids-block-allof-check-that-analysis-ega-id-egaz-is-correct.md))

# 1 Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                               |
| :---------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [egaAccession](#egaaccession) | `string` | Optional | cannot be null | [EGA analysis metadata schema](ega-2-properties-objects-ids-block-allof-check-that-analysis-ega-id-egaz-is-correct-properties-pattern-of-an-ega-analysiss-id-egaz.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectId/allOf/1/properties/egaAccession") |

## egaAccession



`egaAccession`

*   is optional

*   Type: `string` ([Pattern of an EGA analysis's ID (EGAZ...)](ega-2-properties-objects-ids-block-allof-check-that-analysis-ega-id-egaz-is-correct-properties-pattern-of-an-ega-analysiss-id-egaz.md))

*   cannot be null

*   defined in: [EGA analysis metadata schema](ega-2-properties-objects-ids-block-allof-check-that-analysis-ega-id-egaz-is-correct-properties-pattern-of-an-ega-analysiss-id-egaz.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.analysis.json#/properties/objectId/allOf/1/properties/egaAccession")

### egaAccession Type

`string` ([Pattern of an EGA analysis's ID (EGAZ...)](ega-2-properties-objects-ids-block-allof-check-that-analysis-ega-id-egaz-is-correct-properties-pattern-of-an-ega-analysiss-id-egaz.md))

### egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAZ[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAZ%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### egaAccession Examples

```json
"EGAZ00001004170"
```
