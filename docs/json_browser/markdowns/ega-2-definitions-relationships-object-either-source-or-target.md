# Relationship's object (either source or target) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target/allOf/0
```

Node containing metadata (identifiers and the type of reference) of one of the ends of the relationship, whether it is the source or the target of the relationship.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json*](../out/EGA.common-definitions.json "open original schema") |

## 0 Type

`object` ([Relationship's object (either source or target)](ega-2-definitions-relationships-object-either-source-or-target.md))

all of

*   any of

    *   [Alias and Centername: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

    *   [External accession: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

    *   [Experiment: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

    *   [Study: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

    *   [Sample: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

    *   [Submission: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

    *   [Run: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-run-object_id-and-object_type-check.md "check type definition")

    *   [Dataset: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

    *   [Analysis: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

    *   [Policy: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

    *   [DAC: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

    *   [ArrayExperiment: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayexperiment-object_id-and-object_type-check.md "check type definition")

    *   [ArrayAssay: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayassay-object_id-and-object_type-check.md "check type definition")

    *   [Individual: object_id and object_type check](ega-2-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")

# 0 Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                              |
| :-------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [object_id](#object_id)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")    |
| [object_type](#object_type) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-2-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type") |

## object_id

Node containing the main identifiers of the relationship's object (e.g. alias, center_name...), inherited from the common definitions (#/definitions/object_core_id).

`object_id`

*   is required

*   Type: `object` ([Relationship's object's IDs block](ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")

### object_id Type

`object` ([Relationship's object's IDs block](ega-2-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-2-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

## object_type

Type of the relationship's object, chosen from a list of CV (e.g. arrayExperiment, dataset, external_URL...). Both the source or target types can be: (1) the object tag of one of EGA’s object (e.g. file, sample…); (2) an 'external_accession'; (3) or an 'external_URL'.

`object_type`

*   is required

*   Type: `string` ([Type of the relationship's object](ega-2-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-2-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type")

### object_type Type

`string` ([Type of the relationship's object](ega-2-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

### object_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation |
| :--------------------- | :---------- |
| `"experiment"`         |             |
| `"study"`              |             |
| `"sample"`             |             |
| `"individual"`         |             |
| `"submission"`         |             |
| `"run"`                |             |
| `"dataset"`            |             |
| `"analysis"`           |             |
| `"policy"`             |             |
| `"DAC"`                |             |
| `"ArrayExperiment"`    |             |
| `"ArrayAssay"`         |             |
| `"external_accession"` |             |
| `"external_URL"`       |             |

### object_type Examples

```json
"sample"
```
