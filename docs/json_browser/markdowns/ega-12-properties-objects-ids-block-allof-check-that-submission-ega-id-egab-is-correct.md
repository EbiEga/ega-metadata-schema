# Check that Submission EGA ID (EGAB) is correct Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectId/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## 1 Type

unknown ([Check that Submission EGA ID (EGAB) is correct](ega-12-properties-objects-ids-block-allof-check-that-submission-ega-id-egab-is-correct.md))

# 1 Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                        |
| :---------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [egaAccession](#egaaccession) | `string` | Optional | cannot be null | [EGA submission metadata schema](ega-4-definitions-pattern-of-an-ega-submissions-id-egab.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectId/allOf/1/properties/egaAccession") |

## egaAccession



`egaAccession`

*   is optional

*   Type: `string` ([Pattern of an EGA submission's ID (EGAB...)](ega-4-definitions-pattern-of-an-ega-submissions-id-egab.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-4-definitions-pattern-of-an-ega-submissions-id-egab.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/objectId/allOf/1/properties/egaAccession")

### egaAccession Type

`string` ([Pattern of an EGA submission's ID (EGAB...)](ega-4-definitions-pattern-of-an-ega-submissions-id-egab.md))

### egaAccession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAB[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAB%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### egaAccession Examples

```json
"EGAB00001001831"
```
