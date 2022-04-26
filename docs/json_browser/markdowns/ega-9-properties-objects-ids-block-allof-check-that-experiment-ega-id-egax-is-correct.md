# Check that experiment EGA ID (EGAX) is correct Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/object_id/allOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## 1 Type

unknown ([Check that experiment EGA ID (EGAX) is correct](ega-9-properties-objects-ids-block-allof-check-that-experiment-ega-id-egax-is-correct.md))

# 1 Properties

| Property                         | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                 |
| :------------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ega\_accession](#ega_accession) | `string` | Optional | cannot be null | [EGA Experiment metadata schema](ega-12-definitions-pattern-of-an-ega-experiments-id-egax.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/object_id/allOf/1/properties/ega_accession") |

## ega\_accession



`ega_accession`

*   is optional

*   Type: `string` ([Pattern of an EGA experiment's ID (EGAX...)](ega-12-definitions-pattern-of-an-ega-experiments-id-egax.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-12-definitions-pattern-of-an-ega-experiments-id-egax.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/object_id/allOf/1/properties/ega_accession")

### ega\_accession Type

`string` ([Pattern of an EGA experiment's ID (EGAX...)](ega-12-definitions-pattern-of-an-ega-experiments-id-egax.md))

### ega\_accession Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^EGAX[0-9]{11}$
```

[try pattern](https://regexr.com/?expression=%5EEGAX%5B0-9%5D%7B11%7D%24 "try regular expression with regexr.com")

### ega\_accession Examples

```json
"EGAX00002189113"
```
