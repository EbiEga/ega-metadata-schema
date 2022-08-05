# Type of the relationship's object Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/one-relationship-end/properties/object_type
```

Type of the relationship's object, chosen from a list of CV (e.g. experiment, dataset, external\_URL...). Both the source or target types can be: (1) the object tag of one of EGA's object (e.g. file, sample...); (2) an 'external\_accession'; (3) or an 'external\_URL'. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## object\_type Type

`string` ([Type of the relationship's object](ega-12-definitions-relationships-object-either-source-or-target-properties-type-of-the-relationships-object.md))

## object\_type Constraints

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
| `"protocol"`           | Contains information about a planned process.                                                                                                                       |
| `"external_accession"` | An external accession among the ones Entrez (NCBI's text search) contemplates (search for the terms here: https\://www\.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?) |
| `"external_URL"`       | An external URL resource, of any type                                                                                                                               |

## object\_type Examples

```json
"sample"
```
