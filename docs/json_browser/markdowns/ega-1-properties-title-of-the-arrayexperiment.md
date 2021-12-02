# Title of the ArrayExperiment Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/title
```

An informative experiment title that should serve as an overview of the experiment, including: used technology, samples, purpose... (e.g. 'Affymetrix-X microarray of human breast cancer cell line MCF-7 treated with tamoxifen compared with untreated controls'). This short text can be used to call out ArrayExperiment records in searches or in displays. This element is technically optional but should be used for all new records.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## title Type

`string` ([Title of the ArrayExperiment](ega-1-properties-title-of-the-arrayexperiment.md))

## title Examples

```json
"Affymetrix-X microarray of human breast cancer cell line MCF-7 treated with tamoxifen compared with untreated controls"
```
