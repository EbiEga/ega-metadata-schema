# Biological sex of the individual Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/biologicalSex
```

An organismal quality inhering in a bearer by virtue of the bearer's physical expression of sexual characteristics. In other words, the trait that determines the individual's (from which the sample derives) reproductive function: mainly male or female. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## biologicalSex Type

`string` ([Biological sex of the individual](ega-4-definitions-biological-sex-of-the-individual.md))

## biologicalSex Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation                                                                                                                                                                                                             |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"male"`                | \[PATO:0000384]: A biological sex quality inhering in an individual or a population whose sex organs contain only male gametes.                                                                                         |
| `"female"`              | \[PATO:0000383]: A biological sex quality inhering in an individual or a population that only produces gametes that can be fertilised by male gametes.                                                                  |
| `"hermaphrodite"`       | \[PATO:0001340]: An organism having both male and female sexual characteristics and organs. A biological sex quality inhering in an organism or a population with both male and female sexual organs in one individual. |
| `"pseudohermaphrodite"` | \[PATO:0001827]: A biological sex quality inhering in an individual or a population by virtue of having internal reproductive organs of one sex and external sexual characteristics of the other sex.                   |
| `"unknown"`             | \[NCIT:C17998]: The biological sex is unknown, not assesed or not available.                                                                                                                                            |

## biologicalSex Examples

```json
"male"
```
