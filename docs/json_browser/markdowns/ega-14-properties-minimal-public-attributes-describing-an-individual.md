# Minimal public attributes describing an individual Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes
```

Among all attributes describing an individual, some may contain identifiable metadata and thus must be private. Nevertheless, there are three required attributes (even if they are unknown): subject id, biological sex and phenotype. These shall be displayed and queryable.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## minimal\_public\_attributes Type

`object` ([Minimal public attributes describing an individual](ega-14-properties-minimal-public-attributes-describing-an-individual.md))

# minimal\_public\_attributes Properties

| Property                           | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                     |
| :--------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [subject\_id](#subject_id)         | `string` | Required | cannot be null | [EGA individual metadata schema](ega-12-definitions-subject-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/subject_id")                           |
| [biological\_sex](#biological_sex) | `string` | Required | cannot be null | [EGA individual metadata schema](ega-12-definitions-biological-sex-of-the-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/biological_sex") |
| [phenotype](#phenotype)            | `object` | Required | cannot be null | [EGA individual metadata schema](ega-12-definitions-experimental-condition.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/phenotype")                |

## subject\_id

A unique identifier (e.g. 'Donor-10031') for the subject the sample derives from, providing context for the sample to be better understood through its provenance. It **shall not** contain personal sensitive data, since it will be publicly displayed for queries and searches.

`subject_id`

*   is required

*   Type: `string` ([Subject ID](ega-12-definitions-subject-id.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-subject-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/subject_id")

### subject\_id Type

`string` ([Subject ID](ega-12-definitions-subject-id.md))

### subject\_id Constraints

**minimum length**: the minimum number of characters for this string is: `1`

### subject\_id Examples

```json
"Donor-10031"
```

```json
"ID001"
```

```json
"9001"
```

```json
"AX_Dli"
```

## biological\_sex

An organismal quality inhering in a bearer by virtue of the bearer's physical expression of sexual characteristics. In other words, the trait that determines the individual's (from which the sample derives) reproductive function: mainly male or female. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

`biological_sex`

*   is required

*   Type: `string` ([Biological sex of the individual](ega-12-definitions-biological-sex-of-the-individual.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-biological-sex-of-the-individual.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/biological_sex")

### biological\_sex Type

`string` ([Biological sex of the individual](ega-12-definitions-biological-sex-of-the-individual.md))

### biological\_sex Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation                                                                                                                                                                                                             |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"male"`          | \[PATO:0000384]: A biological sex quality inhering in an individual or a population whose sex organs contain only male gametes.                                                                                         |
| `"female"`        | \[PATO:0000383]: A biological sex quality inhering in an individual or a population that only produces gametes that can be fertilised by male gametes.                                                                  |
| `"hermaphrodite"` | \[PATO:0001340]: An organism having both male and female sexual characteristics and organs. A biological sex quality inhering in an organism or a population with both male and female sexual organs in one individual. |
| `"unknown"`       | The biological sex is unknown.                                                                                                                                                                                          |

### biological\_sex Examples

```json
"male"
```

## phenotype

A state of being, an external or environmental factor or a treatment observed or administered prior to or concurrent with an investigative procedure such as an assessment of a morphological or physiological state or property in a single individual or sample or in a group of individuals or samples, especially a state, factor or treatment which has the potential to influence the outcome of such an assessment. We highly recommend the usage of ontologies to describe experimental conditions (search at '<https://www.ebi.ac.uk/ols/ontologies/efo>').

`phenotype`

*   is required

*   Type: `object` ([Experimental condition](ega-12-definitions-experimental-condition.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-experimental-condition.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/phenotype")

### phenotype Type

`object` ([Experimental condition](ega-12-definitions-experimental-condition.md))
