# Type of used assay Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayType
```

Node defining the type of assay applicable to the experiment. Notice how, depending on the complexity of the assay type (i.e. how many subtypes it may have), the assay type can be a high level term (e.g. 'single cell sequencing') or very specific (e.g. '454 Sequencing'). We recommend to use the most specific term possible if available: for example, in case your assay was an 'RNA-seq of coding RNA from single cells' \[EFO:0005684], we advise to provide the specific term \[EFO:0005684], instead of the generic 'assay by high throughput sequencer' \[EFO:0002697].

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## assayType Type

`object` ([Type of used assay](ega-1-properties-type-of-used-assay.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# assayType Properties

| Property          | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                |
| :---------------- | :----- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [termId](#termid) | Merged | Optional | cannot be null | [EGA Experiment metadata schema](ega-1-properties-type-of-used-assay-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayType/properties/termId") |

## termId



`termId`

*   is optional

*   Type: merged type ([Ontology constraints for this specific termId](ega-1-properties-type-of-used-assay-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA Experiment metadata schema](ega-1-properties-type-of-used-assay-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.experiment.json#/properties/assayType/properties/termId")

### termId Type

merged type ([Ontology constraints for this specific termId](ega-1-properties-type-of-used-assay-properties-ontology-constraints-for-this-specific-termid.md))

any of

*   [Ontology validation of terms below 'assay by sequencer'](ega-1-properties-type-of-used-assay-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-terms-below-assay-by-sequencer.md "check type definition")

*   [Ontology validation of terms below 'assay by array'](ega-1-properties-type-of-used-assay-properties-ontology-constraints-for-this-specific-termid-anyof-ontology-validation-of-terms-below-assay-by-array.md "check type definition")

### termId Examples

```json
"EFO:0002697"
```

```json
"EFO:0030006"
```

```json
"EFO:0002765"
```

```json
"EFO:0005517"
```
