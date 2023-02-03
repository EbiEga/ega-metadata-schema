# EGA Relationships object Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocolRelationships/items/allOf/0
```

Object containing the base metadata attributes of a relationship object in the EGA. Comprises metadata (e.g. Source or Target) of a directional association between two entities. One of the entitis **needs** to be the current instance. For instance, a study JSON document should not contain relationships between a sample and an individual. Therefore, only one end of the relationship is given: if the source is present, the target is inferred to be the current instance; if the target is given, then it's the source the one inferred as the current instance. Examples of common relationships: (1) a sample being referenced in an experiment; (2) an study being the same as another study at a different archive (e.g. in BioStudies); (3) an individual being the parent of another individual; (4) hundreds of samples being grouped with each other for broad reasons.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## 0 Type

`object` ([EGA Relationships object](ega-4-definitions-ega-relationships-object.md))

one (and only one) of

*   [The source is given (i.e. the target is inferred as the current instance)](ega-4-definitions-ega-relationships-object-oneof-the-source-is-given-ie-the-target-is-inferred-as-the-current-instance.md "check type definition")

*   [The target is given (i.e. the source is inferred as the current instance)](ega-4-definitions-ega-relationships-object-oneof-the-target-is-given-ie-the-source-is-inferred-as-the-current-instance.md "check type definition")

# 0 Properties

| Property            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                             |
| :------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rType](#rtype)     | `string` | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-relationship-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rType")                 |
| [rSource](#rsource) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rSource")      |
| [rTarget](#rtarget) | Merged   | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rTarget")      |
| [rLabel](#rlabel)   | `string` | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rLabel") |

## rType

ID (e.g. sameAs) of the type of the relationship. To be chosen from a controlled vocabulary (CV) list. If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

`rType`

*   is required

*   Type: `string` ([Relationship type](ega-4-definitions-ega-relationships-object-properties-relationship-type.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-relationship-type.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rType")

### rType Type

`string` ([Relationship type](ega-4-definitions-ega-relationships-object-properties-relationship-type.md))

### rType Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                      | Explanation    |
| :------------------------- | :------------- |
| `"referencedBy"`           | \[SIO:000252]  |
| `"developsFrom"`           | \[RO:0002202]  |
| `"sameAs"`                 | \[NCIT:C64637] |
| `"memberOf"`               | \[RO:0002350]  |
| `"groupedWith"`            |                |
| `"familyRelationshipWith"` | \[EFO:0004424] |
| `"childOf"`                | \[GSSO:000728] |
| `"isAfter"`                | \[SIO:000211]  |
| `"publishedIn"`            | \[EFO:0001796] |
| `"submittedBy"`            | \[NCIT:C25695] |
| `"contactOf"`              | \[NCIT:C25461] |
| `"mainContactOf"`          |                |

### rType Examples

```json
"referencedBy"
```

## rSource

Object reference of the relationship's source. In other words, the starting point of the relationship: in 'sample\_A developsFrom sample\_B' the source is 'sample\_A'.

`rSource`

*   is optional

*   Type: `object` ([Source of the relationship](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rSource")

### rSource Type

`object` ([Source of the relationship](ega-4-definitions-ega-relationships-object-properties-source-of-the-relationship.md))

all of

*   all of

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

## rTarget

Object reference of the relationship's target. In other words, the ending point of the relationship: in 'sample\_A developsFrom sample\_B' the target is 'sample\_B'.

`rTarget`

*   is optional

*   Type: `object` ([Target of the relationship](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rTarget")

### rTarget Type

`object` ([Target of the relationship](ega-4-definitions-ega-relationships-object-properties-target-of-the-relationship.md))

all of

*   all of

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

## rLabel

Custom free-form label of the relationship, used to add extra details of the relationship if needed.

`rLabel`

*   is optional

*   Type: `string` ([Custom label of the relationship](ega-4-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/relationshipObject/properties/rLabel")

### rLabel Type

`string` ([Custom label of the relationship](ega-4-definitions-ega-relationships-object-properties-custom-label-of-the-relationship.md))

### rLabel Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### rLabel Examples

```json
"Source individual is the third child of the target individual"
```

```json
"Grouped samples by colour of the medium"
```

```json
"Both samples are the same because of an error in the submission at..."
```
