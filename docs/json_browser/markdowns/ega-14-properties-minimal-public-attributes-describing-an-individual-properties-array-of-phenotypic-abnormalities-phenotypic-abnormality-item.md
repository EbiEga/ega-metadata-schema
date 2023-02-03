# Phenotypic abnormality item Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities/items
```

One individual Phenotypic abnormality of the array. Keep in mind that in order to correctly interprete the phenotype it is **imperative** to check the 'excluded' property: each item of the array can be either specifying that the phenotipic abnormality was present or the opposite (i.e. logical negation).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## items Type

`object` ([Phenotypic abnormality item](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities-phenotypic-abnormality-item.md))

# items Properties

| Property                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                              |
| :---------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [excluded](#excluded)                           | `boolean` | Optional | cannot be null | [EGA individual metadata schema](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities-phenotypic-abnormality-item-properties-excluded.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities/items/properties/excluded") |
| [phenotypicAbnormality](#phenotypicabnormality) | Merged    | Required | cannot be null | [EGA individual metadata schema](ega-12-definitions-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities/items/properties/phenotypicAbnormality")                                                                                                            |

## excluded

Property that specifies whether the phenotype was observed or not. Similar to phenopacket's 'excluded' property, by default it is 'false', which means that the phenotype was observed (i.e. not excluded). This flag is only required to indicate that the phenotype was looked for, but found to be absent. The terms 'not excluded' (i.e. false) and 'excluded' (i.e. true) correlate with the common notation of 'case' versus 'control', respectively.

`excluded`

*   is optional

*   Type: `boolean` ([Excluded](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities-phenotypic-abnormality-item-properties-excluded.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities-phenotypic-abnormality-item-properties-excluded.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities/items/properties/excluded")

### excluded Type

`boolean` ([Excluded](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-phenotypic-abnormalities-phenotypic-abnormality-item-properties-excluded.md))

## phenotypicAbnormality

Property to describe any abnormal (i.e. deviation from normal or average) phenotype (i.e. detectable outward manifestations of a specific genotype).

`phenotypicAbnormality`

*   is required

*   Type: `object` ([Phenotypic abnormality](ega-12-definitions-phenotypic-abnormality.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-phenotypic-abnormality.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/phenotypicAbnormalities/items/properties/phenotypicAbnormality")

### phenotypicAbnormality Type

`object` ([Phenotypic abnormality](ega-12-definitions-phenotypic-abnormality.md))

all of

*   [Ontology term](ega-12-definitions-ontology-term.md "check type definition")
