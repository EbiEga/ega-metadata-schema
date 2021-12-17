# Check that ArrayExperiment EGA ID (EGAE) is correct Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## 1 Type

unknown ([Check that ArrayExperiment EGA ID (EGAE) is correct](ega-1-properties-objects-ids-block-allof-check-that-arrayexperiment-ega-id-egae-is-correct.md))

# 1 Properties

| Property                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                          |
| :------------------------------ | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-objects-ids-block-allof-check-that-arrayexperiment-ega-id-egae-is-correct-properties-pattern-of-an-ega-arrayexperiments-id-egae.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_id/allOf/1/properties/ega_accession") |

## ega_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA ArrayExperiment's ID (EGAE...)](ega-1-properties-objects-ids-block-allof-check-that-arrayexperiment-ega-id-egae-is-correct-properties-pattern-of-an-ega-arrayexperiments-id-egae.md))

*   cannot be null

*   defined in: [EGA ArrayExperiment metadata schema v0.0.1](ega-1-properties-objects-ids-block-allof-check-that-arrayexperiment-ega-id-egae-is-correct-properties-pattern-of-an-ega-arrayexperiments-id-egae.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/object_id/allOf/1/properties/ega_accession")

### ega_accession Type

`string` ([Pattern of an EGA ArrayExperiment's ID (EGAE...)](ega-1-properties-objects-ids-block-allof-check-that-arrayexperiment-ega-id-egae-is-correct-properties-pattern-of-an-ega-arrayexperiments-id-egae.md))

### ega_accession Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^EGAE[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAE%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega_accession Examples

```json
"EGAE00001004508"
```
