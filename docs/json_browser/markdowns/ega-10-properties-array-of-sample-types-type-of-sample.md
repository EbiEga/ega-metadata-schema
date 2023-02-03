# Type of sample Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleTypes/items
```

Sample type item. Term chosen from a list of controlled vocabulary (CV). If you cannot find your term in the CV list, please create an issue at our [metadata GitHub repository](https://github.com/EbiEga/ega-metadata-schema/issues/new/choose) proposing its addition.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## items Type

`string` ([Type of sample](ega-10-properties-array-of-sample-types-type-of-sample.md))

## items Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                  | Explanation                                                                                                                        |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `"DNA"`                | \[CHEBI:16991]                                                                                                                     |
| `"RNA"`                | \[CHEBI:33697]                                                                                                                     |
| `"metabolite"`         | \[EFO:0004727]                                                                                                                     |
| `"protein"`            | \[CHEBI:36080]                                                                                                                     |
| `"cDNA"`               | \[EFO:0008481]                                                                                                                     |
| `"genomic DNA"`        | \[EFO:0008479]                                                                                                                     |
| `"mitochondrial DNA"`  | \[EFO:0008480]                                                                                                                     |
| `"messenger RNA"`      | \[CHEBI:33699]                                                                                                                     |
| `"ncRNA"`              | \[SO:0000655]                                                                                                                      |
| `"non polyA RNA"`      | \[EFO:0005017]                                                                                                                     |
| `"long non polyA RNA"` | \[EFO:0005018]                                                                                                                     |
| `"nuclear RNA"`        | \[EFO:0030052]                                                                                                                     |
| `"polyA RNA"`          | \[OBI:0000869]                                                                                                                     |
| `"long polyA RNA"`     | \[EFO:0005019]                                                                                                                     |
| `"snRNA"`              | \[SO:0000274]                                                                                                                      |
| `"total RNA"`          | \[EFO:0004964]                                                                                                                     |
| `"cell culture"`       | \[BTO:0000214]: Cells taken from a living organism and grown under controlled conditions (in culture).                             |
| `"biofilm"`            | \[BTO:0002690]                                                                                                                     |
| `"tissue culture"`     | \[BTO:0001384]: Fragments of tissue from an animal transferred to an artificial environment to continue its survival and function. |
