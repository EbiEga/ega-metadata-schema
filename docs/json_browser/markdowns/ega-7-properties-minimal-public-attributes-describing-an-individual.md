# Minimal public attributes describing an individual Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes
```

Among all attributes describing an individual, some may contain identifiable metadata and thus must be private. Nevertheless, there are three required attributes (even if they are unknown): subject id, biological sex and phenotype. These shall be displayed and queryable.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json*](../out/EGA.individual.json "open original schema") |

## minimal_public_attributes Type

`object` ([Minimal public attributes describing an individual](ega-7-properties-minimal-public-attributes-describing-an-individual.md))

# minimal_public_attributes Properties

| Property                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :-------------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [subject_id](#subject_id)         | `string` | Required | cannot be null | [EGA individual metadata schema](ega-4-definitions-subject-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/subject_id")                                       |
| [biological_sex](#biological_sex) | `string` | Required | cannot be null | [EGA individual metadata schema](ega-4-definitions-biological-sex-of-the-individual-pato0000047.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/biological_sex") |
| [phenotype](#phenotype)           | `object` | Required | cannot be null | [EGA individual metadata schema](ega-4-definitions-experimental-condition-xco0000000.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/phenotype")                 |

## subject_id

A unique identifir (e.g. 'Donor-10031') for the subject the sample derives from, providing context for the sample to be better understood through its provenance.

`subject_id`

*   is required

*   Type: `string` ([Subject ID](ega-4-definitions-subject-id.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-4-definitions-subject-id.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/subject_id")

### subject_id Type

`string` ([Subject ID](ega-4-definitions-subject-id.md))

### subject_id Examples

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

## biological_sex

An organismal quality inhering in a bearer by virtue of the bearer's physical expression of sexual characteristics. In other words, the trait that determines the individual's (from which the sample derives) reproductive function: mainly male or female.

`biological_sex`

*   is required

*   Type: `string` ([Biological sex of the individual \[PATO:0000047\]](ega-4-definitions-biological-sex-of-the-individual-pato0000047.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-4-definitions-biological-sex-of-the-individual-pato0000047.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/biological_sex")

### biological_sex Type

`string` ([Biological sex of the individual \[PATO:0000047\]](ega-4-definitions-biological-sex-of-the-individual-pato0000047.md))

### biological_sex Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"male"`          |             |
| `"female"`        |             |
| `"hermaphrodite"` |             |
| `"unknown"`       |             |

### biological_sex Examples

```json
"male"
```

## phenotype

A state of being, an external or environmental factor or a treatment observed or administered prior to or concurrent with an investigative procedure such as an assessment of a morphological or physiological state or property in a single individual or sample or in a group of individuals or samples, especially a state, factor or treatment which has the potential to influence the outcome of such an assessment. We highly recommend the usage of ontologies to describe experimental conditions (search at '<https://www.ebi.ac.uk/ols/ontologies/efo>').

`phenotype`

*   is required

*   Type: `object` ([Experimental condition \[XCO:0000000\]](ega-4-definitions-experimental-condition-xco0000000.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-4-definitions-experimental-condition-xco0000000.md "https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.individual.json#/properties/minimal_public_attributes/properties/phenotype")

### phenotype Type

`object` ([Experimental condition \[XCO:0000000\]](ega-4-definitions-experimental-condition-xco0000000.md))
