# Type of the assayed molecule of the experiment Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/assayed_molecule_type
```

Node containing information about the assayed molecule: the material entity (e.g. DNA) that was used to generate the data. Choose the specific terms if possible (e.g. if the assayed molecule is cDNA, pick 'cDNA' instead of just 'DNA'). Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## assayed\_molecule\_type Type

`string` ([Type of the assayed molecule of the experiment](ega-9-properties-type-of-the-assayed-molecule-of-the-experiment.md))

## assayed\_molecule\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation    |
| :--------------------- | :------------- |
| `"DNA"`                | \[CHEBI:16991] |
| `"RNA"`                | \[CHEBI:33697] |
| `"metabolite"`         | \[EFO:0004727] |
| `"protein"`            | \[CHEBI:36080] |
| `"cDNA"`               | \[EFO:0008481] |
| `"genomic DNA"`        | \[EFO:0008479] |
| `"mitochondrial DNA"`  | \[EFO:0008480] |
| `"messenger RNA"`      | \[CHEBI:33699] |
| `"ncRNA"`              | \[SO:0000655]  |
| `"non polyA RNA"`      | \[EFO:0005017] |
| `"long non polyA RNA"` | \[EFO:0005018] |
| `"nuclear RNA"`        | \[EFO:0030052] |
| `"polyA RNA"`          | \[OBI:0000869] |
| `"long polyA RNA"`     | \[EFO:0005019] |
| `"snRNA"`              | \[SO:0000274]  |
| `"total RNA"`          | \[EFO:0004964] |
