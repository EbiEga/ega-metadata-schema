# EGA Relationships object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.study.json#/properties/study_relationships/items
```

Object containing the base metadata attributes of a relationship object in the EGA. Comprises metadata (e.g. Source and Target) of a directional association between two entities. For example: (1) a sample being referenced in an experiment; (2) an study being the same as another study at a different archive (e.g. in BioStudies); (3) an individual being the parent of another individual; (4) hundreds of samples being grouped with each other for broad reasons.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.study.json*](../out/EGA.study.json "open original schema") |

## items Type

`object` ([EGA Relationships object](ega-12-definitions-ega-relationships-object.md))

# items Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [r_type](#r_type)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-relationship-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")            |
| [r_source](#r_source) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source") |
| [r_target](#r_target) | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target") |

## r_type

ID (e.g. same_as) of the type of the relationship. To be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`r_type`

*   is required

*   Type: `string` ([Relationship type](ega-12-definitions-ega-relationships-object-properties-relationship-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-relationship-type.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")

### r_type Type

`string` ([Relationship type](ega-12-definitions-ega-relationships-object-properties-relationship-type.md))

### r_type Constraints

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

### r_type Examples

```json
"referenced_by"
```

## r_source

Object reference of the relationship's source. In other words, the starting point of the relationship: in 'sample_A develops_from sample_B' the source is 'sample_A'.

`r_source`

*   is required

*   Type: `object` ([Source of the relationship](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source")

### r_source Type

`object` ([Source of the relationship](ega-12-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

        *   [External accession: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

        *   [Experiment: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

        *   [Study: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

        *   [Sample: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

        *   [Submission: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

        *   [Assay: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-assay-object_id-and-object_type-check.md "check type definition")

        *   [Dataset: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

        *   [Analysis: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

        *   [Policy: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

        *   [DAC: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

        *   [Individual: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")

## r_target

Object reference of the relationship's target. In other words, the ending point of the relationship: in 'sample_A develops_from sample_B' the target is 'sample_B'.

`r_target`

*   is required

*   Type: `object` ([Target of the relationship](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target")

### r_target Type

`object` ([Target of the relationship](ega-12-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

        *   [External accession: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

        *   [Experiment: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

        *   [Study: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

        *   [Sample: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

        *   [Submission: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

        *   [Assay: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-assay-object_id-and-object_type-check.md "check type definition")

        *   [Dataset: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

        *   [Analysis: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

        *   [Policy: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

        *   [DAC: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

        *   [Individual: object_id and object_type check](ega-12-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")
