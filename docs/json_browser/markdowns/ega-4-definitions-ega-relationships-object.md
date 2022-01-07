# EGA Relationships object Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/sample_relationships/items
```

Object containing the base metadata attributes of a relationship object in the EGA. Comprises metadata (e.g. Source and Target) of a directional association between two entities. Ontologies of each type of connection are stored the meta:enum field, and details of each in its corresponding record within the ontologies.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.sample.json*](../out/EGA.sample.json "open original schema") |

## items Type

`object` ([EGA Relationships object](ega-4-definitions-ega-relationships-object.md))

# items Properties

| Property              | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                |
| :-------------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [r_type](#r_type)     | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")     |
| [r_source](#r_source) | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source") |
| [r_target](#r_target) | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target") |

## r_type

The Type of the relationship, containing both its ID (e.g. same_as and the CURIE (e.g. NCIT:C64637), that summarises its purpose. #! The list of CV shall be agreed on, improved and enlarged.

`r_type`

*   is required

*   Type: `object` ([Type of the relationship](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_type")

### r_type Type

`object` ([Type of the relationship](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship.md))

any of

*   [Check that r_type is present](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship-anyof-check-that-r_type-is-present.md "check type definition")

*   [Check that r_type_curie is present](ega-4-definitions-ega-relationships-object-properties-type-of-the-relationship-anyof-check-that-r_type_curie-is-present.md "check type definition")

## r_source

Object reference of the relationship’s source. In other words, the starting point of the relationship: in 'sample_A develops_from sample_B' the source is 'sample_A'.

`r_source`

*   is required

*   Type: `object` ([Source of the relationship](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_source")

### r_source Type

`object` ([Source of the relationship](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

        *   [External accession: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

        *   [Experiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

        *   [Study: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

        *   [Sample: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

        *   [Submission: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

        *   [Run: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-run-object_id-and-object_type-check.md "check type definition")

        *   [Dataset: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

        *   [Analysis: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

        *   [Policy: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

        *   [DAC: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

        *   [ArrayExperiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayexperiment-object_id-and-object_type-check.md "check type definition")

        *   [ArrayAssay: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayassay-object_id-and-object_type-check.md "check type definition")

        *   [Individual: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")

## r_target

Object reference of the relationship’s target. In other words, the ending point of the relationship: in 'sample_A develops_from sample_B' the target is 'sample_B'.

`r_target`

*   is required

*   Type: `object` ([Target of the relationship](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target")

### r_target Type

`object` ([Target of the relationship](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

all of

*   all of

    *   any of

        *   [Alias and Centername: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-alias-and-centername-object_id-and-object_type-check.md "check type definition")

        *   [External accession: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-external-accession-object_id-and-object_type-check.md "check type definition")

        *   [Experiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-experiment-object_id-and-object_type-check.md "check type definition")

        *   [Study: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-study-object_id-and-object_type-check.md "check type definition")

        *   [Sample: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-sample-object_id-and-object_type-check.md "check type definition")

        *   [Submission: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-submission-object_id-and-object_type-check.md "check type definition")

        *   [Run: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-run-object_id-and-object_type-check.md "check type definition")

        *   [Dataset: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dataset-object_id-and-object_type-check.md "check type definition")

        *   [Analysis: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-analysis-object_id-and-object_type-check.md "check type definition")

        *   [Policy: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-policy-object_id-and-object_type-check.md "check type definition")

        *   [DAC: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-dac-object_id-and-object_type-check.md "check type definition")

        *   [ArrayExperiment: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayexperiment-object_id-and-object_type-check.md "check type definition")

        *   [ArrayAssay: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-arrayassay-object_id-and-object_type-check.md "check type definition")

        *   [Individual: object_id and object_type check](ega-4-definitions-check-that-the-object_ids-accession-pattern-and-object_type-match-anyof-individual-object_id-and-object_type-check.md "check type definition")
