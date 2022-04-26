# Relationship's object (either source or target) Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/relationship_object/properties/r_target/allOf/0
```

Node containing metadata (identifiers and the type of reference) of one of the ends of the relationship, whether it is the source or the target of the relationship.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## 0 Type

`object` ([Relationship's object (either source or target)](ega-12-definitions-relationships-object-either-source-or-target.md))

all of

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

# 0 Properties

| Property                     | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                               |
| :--------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [object\_id](#object_id)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")    |
| [object\_type](#object_type) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type") |

## object\_id

Node containing the main identifiers of the relationship's object (e.g. alias, center\_name...), inherited from the common definitions (#/definitions/object\_core\_id).

`object_id`

*   is required

*   Type: `object` ([Relationship's object's IDs block](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_id")

### object\_id Type

`object` ([Relationship's object's IDs block](ega-12-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-12-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

## object\_type

Type of the relationship's object, chosen from a list of CV (e.g. experiment, dataset, external\_URL...). Both the source or target types can be: (1) the object tag of one of EGA's object (e.g. file, sample...); (2) an 'external\_accession'; (3) or an 'external\_URL'. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`object_type`

*   is required

*   Type: `string` ([Type of the relationship's object](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type")

### object\_type Type

`string` ([Type of the relationship's object](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

### object\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation                                                                                                                                                         |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"experiment"`         | Contains information about the experimental design of the sequencing                                                                                                |
| `"study"`              | Information about the study                                                                                                                                         |
| `"sample"`             | Information about the used samples                                                                                                                                  |
| `"individual"`         | Information about the participants (i.e. humans) of the study                                                                                                       |
| `"submission"`         | Information about the submission actions                                                                                                                            |
| `"assay"`              | Contains information about the specific assays (either sequencing or array assays) from the experiment                                                              |
| `"dataset"`            | Contains the collection of assay/analysis data files to be subject to controlled access                                                                             |
| `"analysis"`           | Contains the analysis metadata and data files                                                                                                                       |
| `"policy"`             | Contains information related to the Data Access Agreement (DAA) the dataset is subject to                                                                           |
| `"DAC"`                | Contains information about the Data Access Committee (DAC)                                                                                                          |
| `"external_accession"` | An external accession among the ones Entrez (NCBI's text search) contemplates (search for the terms here: https\://www\.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?) |
| `"external_URL"`       | An external URL resource, of any type                                                                                                                               |

### object\_type Examples

```json
"sample"
```
