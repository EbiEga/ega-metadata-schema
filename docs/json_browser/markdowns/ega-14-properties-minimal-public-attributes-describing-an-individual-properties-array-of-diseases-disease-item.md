# Disease item Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases/items
```

One individual disease of the array. Keep in mind that in order to correctly interprete the disease it is **imperative** to check the 'excluded' property: each item of the array can be either specifying that the disease was present or the opposite (i.e. logical negation).

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.individual.json\*](../../../schemas/EGA.individual.json "open original schema") |

## items Type

`object` ([Disease item](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases-disease-item.md))

# items Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                |
| :-------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [excluded](#excluded) | `boolean` | Optional | cannot be null | [EGA individual metadata schema](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases-disease-item-properties-excluded.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases/items/properties/excluded") |
| [disease](#disease)   | Merged    | Required | cannot be null | [EGA individual metadata schema](ega-12-definitions-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases/items/properties/disease")                                                                                                          |

## excluded

Property that specifies whether the disease was observed or not. Similar to phenopacket's 'excluded' property, by default it is 'false', which means that the disease was observed (i.e. not excluded). This flag is only required to indicate that the disease was looked for, but found to be absent. The terms 'not excluded' (i.e. false) and 'excluded' (i.e. true) correlate with the common notation of 'case' versus 'control', respectively.

`excluded`

*   is optional

*   Type: `boolean` ([Excluded](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases-disease-item-properties-excluded.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases-disease-item-properties-excluded.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases/items/properties/excluded")

### excluded Type

`boolean` ([Excluded](ega-14-properties-minimal-public-attributes-describing-an-individual-properties-array-of-diseases-disease-item-properties-excluded.md))

## disease

Property to describe a disease (i.e. a disposition to undergo pathological processes because of one or more disorders).

`disease`

*   is required

*   Type: `object` ([Disease](ega-12-definitions-disease.md))

*   cannot be null

*   defined in: [EGA individual metadata schema](ega-12-definitions-disease.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.individual.json#/properties/minimalPublicAttributes/properties/diseases/items/properties/disease")

### disease Type

`object` ([Disease](ega-12-definitions-disease.md))

all of

*   [Ontology term](ega-12-definitions-ontology-term.md "check type definition")
