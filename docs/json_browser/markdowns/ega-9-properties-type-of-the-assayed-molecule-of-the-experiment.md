# Type of the assayed molecule of the experiment Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assayed_molecule_type
```

Node containing information about the assayed molecule: the material entity (e.g. DNA) that was used to generate the data. Choose the specific terms if possible (e.g. if the assayed molecule is cDNA, pick 'cDNA' instead of just 'DNA'). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json*](../out/EGA.experiment.json "open original schema") |

## assayed_molecule_type Type

`string` ([Type of the assayed molecule of the experiment](ega-9-properties-type-of-the-assayed-molecule-of-the-experiment.md))

## assayed_molecule_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation |
| :--------------------- | :---------- |
| `"DNA"`                |             |
| `"RNA"`                |             |
| `"metabolite"`         |             |
| `"protein"`            |             |
| `"cDNA"`               |             |
| `"genomic DNA"`        |             |
| `"mitochondrial DNA"`  |             |
| `"messenger RNA"`      |             |
| `"ncRNA"`              |             |
| `"non polyA RNA"`      |             |
| `"long non polyA RNA"` |             |
| `"nuclear RNA"`        |             |
| `"polyA RNA"`          |             |
| `"long polyA RNA"`     |             |
| `"snRNA"`              |             |
| `"total RNA"`          |             |
