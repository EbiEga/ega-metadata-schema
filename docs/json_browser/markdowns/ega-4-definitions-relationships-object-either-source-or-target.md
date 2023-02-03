# Relationship's object (either source or target) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd
```

Node containing metadata (identifiers and the type of reference) of one of the ends of the relationship, whether it is the source or the target of the relationship.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## oneRelationshipEnd Type

`object` ([Relationship's object (either source or target)](ega-4-definitions-relationships-object-either-source-or-target.md))

all of

*   any of

    *   [Alias and Centername: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-alias-and-centername-objectid-and-objecttype-check.md "check type definition")

    *   [External accession: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-external-accession-objectid-and-objecttype-check.md "check type definition")

    *   [Experiment: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-experiment-objectid-and-objecttype-check.md "check type definition")

    *   [Study: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-study-objectid-and-objecttype-check.md "check type definition")

    *   [Sample: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-sample-objectid-and-objecttype-check.md "check type definition")

    *   [Submission: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-submission-objectid-and-objecttype-check.md "check type definition")

    *   [Assay: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-assay-objectid-and-objecttype-check.md "check type definition")

    *   [Dataset: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dataset-objectid-and-objecttype-check.md "check type definition")

    *   [Analysis: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-analysis-objectid-and-objecttype-check.md "check type definition")

    *   [Policy: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-policy-objectid-and-objecttype-check.md "check type definition")

    *   [DAC: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-dac-objectid-and-objecttype-check.md "check type definition")

    *   [Individual: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-individual-objectid-and-objecttype-check.md "check type definition")

    *   [Protocol: objectId and objectType check](ega-4-definitions-check-that-the-objectids-accession-pattern-and-objecttype-match-anyof-protocol-objectid-and-objecttype-check.md "check type definition")

# oneRelationshipEnd Properties

| Property                  | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                     |
| :------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [objectId](#objectid)     | Merged   | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd/properties/objectId")    |
| [objectType](#objecttype) | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd/properties/objectType") |

## objectId

Node containing the main identifiers of the relationship's object (e.g. alias, centerName...), inherited from the common definitions (#/definitions/objectCoreId).

`objectId`

*   is required

*   Type: `object` ([Relationship's object's IDs block](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd/properties/objectId")

### objectId Type

`object` ([Relationship's object's IDs block](ega-4-definitions-relationships-object-either-source-or-target-properties-relationships-objects-ids-block.md))

all of

*   any of

    *   [Check core IDs: combination of Alias and Center name](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-combination-of-alias-and-center-name.md "check type definition")

    *   [Check core IDs: EGA accession ID](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-ega-accession-id.md "check type definition")

    *   [Check core IDs: external accessions](ega-4-definitions-core-identifiers-of-an-object-anyof-check-core-ids-external-accessions.md "check type definition")

## objectType

Type of the relationship's object, chosen from a list of CV (e.g. experiment, dataset, externalURL...). Both the source or target types can be: (1) the object tag of one of EGA's object (e.g. file, sample...); (2) an 'externalAccession'; (3) or an 'externalURL'. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`objectType`

*   is required

*   Type: `string` ([Type of the relationship's object](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/oneRelationshipEnd/properties/objectType")

### objectType Type

`string` ([Type of the relationship's object](ega-4-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

### objectType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation                                                                                                                                                         |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"experiment"`        | Contains information about the experimental design of the sequencing                                                                                                |
| `"study"`             | Information about the study                                                                                                                                         |
| `"sample"`            | Information about the used samples                                                                                                                                  |
| `"individual"`        | Information about the participants (i.e. humans) of the study                                                                                                       |
| `"submission"`        | Information about the submission actions                                                                                                                            |
| `"assay"`             | Contains information about the specific assays (either sequencing or array assays) from the experiment                                                              |
| `"dataset"`           | Contains the collection of assay/analysis data files to be subject to controlled access                                                                             |
| `"analysis"`          | Contains the analysis metadata and data files                                                                                                                       |
| `"policy"`            | Contains information related to the Data Access Agreement (DAA) the dataset is subject to                                                                           |
| `"DAC"`               | Contains information about the Data Access Committee (DAC)                                                                                                          |
| `"protocol"`          | Contains information about a planned process.                                                                                                                       |
| `"externalAccession"` | An external accession among the ones Entrez (NCBI's text search) contemplates (search for the terms here: https\://www\.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?) |
| `"externalURL"`       | An external URL resource, of any type                                                                                                                               |

### objectType Examples

```json
"sample"
```
