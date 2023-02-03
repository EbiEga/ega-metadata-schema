# Array of sample statuses Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.sample.json#/properties/sampleStatus
```

Array of statuses of the sample. Used to specify the condition(s) under study **if** the diagnosis of the individual is not enough to describe the status of the sample. In other words, if the differenciation between affected and unaffected groups is done at the sample level and not at the individual level. This differentiation exists when the study design is of case-control \[[EFO:0001427](http://www.ebi.ac.uk/efo/EFO_0001427)].
For example, if two samples derive from an individual with 'renal cell carcinoma', one deriving from the affected tissue and the other from an unaffected tissue, this node can be used to specify whether the sample belongs to the unaffected group (i.e. control) or the affected one (i.e. case). On the other hand, if two samples derived from different probands each, one person being affected and the other unaffected by the condition under study, this node **is not** required.
Same could be applied, for instance, for treated or untreated samples, but not for treated or untreated individuals.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.sample.json\*](../../../schemas/EGA.sample.json "open original schema") |

## sampleStatus Type

`object[]` ([Sample status item](ega-10-properties-array-of-sample-statuses-sample-status-item.md))

## sampleStatus Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
