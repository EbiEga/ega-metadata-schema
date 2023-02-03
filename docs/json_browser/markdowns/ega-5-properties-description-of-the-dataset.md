# Description of the dataset Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.dataset.json#/properties/objectDescription
```

More extensive free-form description of the Dataset. It should include the content of the dataset (number of samples, file types, technology/protocol used to obtain the data…) and not extend more than 4 sentences.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                     |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.dataset.json\*](../../../schemas/EGA.dataset.json "open original schema") |

## objectDescription Type

`string` ([Description of the dataset](ega-5-properties-description-of-the-dataset.md))

## objectDescription Examples

```json
"This dataset is related to Project X by grant Y and encompasses samples from group Z, whose DNA was hybridized against a microarray designed for SNPs."
```
