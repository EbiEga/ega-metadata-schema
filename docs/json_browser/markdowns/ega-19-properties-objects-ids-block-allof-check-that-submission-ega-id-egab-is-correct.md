# Check that Submission EGA ID (EGAB) is correct Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## 1 Type

unknown ([Check that Submission EGA ID (EGAB) is correct](ega-19-properties-objects-ids-block-allof-check-that-submission-ega-id-egab-is-correct.md))

# 1 Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                           |
| :------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega\_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA submission metadata schema](ega-12-definitions-pattern-of-an-ega-submissions-id-egab.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/object_id/allOf/1/properties/ega_accession") |

## ega\_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA submission's ID (EGAB...)](ega-12-definitions-pattern-of-an-ega-submissions-id-egab.md))

*   cannot be null

*   defined in: [EGA submission metadata schema](ega-12-definitions-pattern-of-an-ega-submissions-id-egab.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/object_id/allOf/1/properties/ega_accession")

### ega\_accession Type

`string` ([Pattern of an EGA submission's ID (EGAB...)](ega-12-definitions-pattern-of-an-ega-submissions-id-egab.md))

### ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAB[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAB%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega\_accession Examples

```json
"EGAB00001001831"
```
