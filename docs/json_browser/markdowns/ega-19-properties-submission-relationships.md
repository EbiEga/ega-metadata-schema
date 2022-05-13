# Submission relationships Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.submission.json#/properties/submission_relationships
```

Comprises metadata (e.g. Source or Target) of a directional association between two entities. This relationships node contains all the possible relationships between metadata objects, both outside of (e.g. an Array Design Format that was submitted to ArrayExpress being linked to their microarray data within EGA) and within (e.g. a policy being linked to a submission) the EGA.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.submission.json\*](../../../schemas/EGA.submission.json "open original schema") |

## submission\_relationships Type

an array of merged types ([Details](ega-19-properties-submission-relationships-items.md))

## submission\_relationships Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
