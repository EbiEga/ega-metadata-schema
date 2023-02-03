# Resources (ontologies) Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.submission.json#/properties/resources
```

An array containing metadata of all the ontologies used in the submission. Its only purpose is to enhance traceability of the used ontologies in the future. For example, if an individual's phenotype is diabetes mellitus (which corresponds to curie EFO:0000400), one of the used ontologies would be EFO. Now, if in the future the term EFO:0000400 is changed in a new release of EFO, it's imperative to keep track of what version of EFO the submitter was referring to when it was referenced. Since most submitters would normally use the latest version of the ontologies at the time of the submission, these resources are intended to be automatically populated at every submission (and thus are not required) to ease the process; nonetheless, if provided, they should not be overwritten by that process. Bear in mind that there is only one 'resources' array per submission, and the items need to be unique, which means that different versions of the same ontologies will not be allowed.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## resources Type

`object[]` ([Resource](ega-12-properties-resources-ontologies-resource.md))

## resources Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
