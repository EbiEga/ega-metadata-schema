# Subtype of the protocol Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.protocol.json#/properties/protocol_type_descriptor/properties/protocol_subtype
```

Name of the protocol's subtype. We highly recommend the usage of names given to ontologized protocols, specially those at the [Experimental Factor Ontology (EFO)](https://www.ebi.ac.uk/ols/ontologies/efo). For example, if the protocol corresponds to a data transformation of a genome, you may find your subtype at [genome analysis](http://edamontology.org/operation_3918); while treating a patient with a drug would correspond to a [clinical treatment](http://www.ebi.ac.uk/efo/EFO_0007056).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.protocol.json\*](../../../schemas/EGA.protocol.json "open original schema") |

## protocol\_subtype Type

`string` ([Subtype of the protocol](ega-17-properties-protocol-type-descriptor-properties-subtype-of-the-protocol.md))

## protocol\_subtype Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## protocol\_subtype Examples

```json
"clinical treatment"
```

```json
"array scanning and feature extraction"
```

```json
"Genome alignment"
```

```json
"Genome annotation"
```

```json
"Genome assembly"
```

```json
"Genome comparison"
```

```json
"Genome feature comparison"
```

```json
"Genome indexing"
```

```json
"Genome visualisation"
```

```json
"Whole genome methylation analysis"
```
