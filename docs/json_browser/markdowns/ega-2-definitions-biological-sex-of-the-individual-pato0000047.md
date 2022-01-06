# Biological sex of the individual \[PATO:0000047] Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.sample.json#/properties/minimal_public_attributes/properties/biological_sex
```

An organismal quality inhering in a bearer by virtue of the bearer's physical expression of sexual characteristics. In other words, the trait that determines the individual's (from which the sample derives) reproductive function: mainly male or female.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json*](../out/EGA.sample.json "open original schema") |

## biological_sex Type

`string` ([Biological sex of the individual \[PATO:0000047\]](ega-2-definitions-biological-sex-of-the-individual-pato0000047.md))

## biological_sex Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"male"`          |             |
| `"female"`        |             |
| `"hermaphrodite"` |             |
| `"unknown"`       |             |

## biological_sex Examples

```json
"male"
```
