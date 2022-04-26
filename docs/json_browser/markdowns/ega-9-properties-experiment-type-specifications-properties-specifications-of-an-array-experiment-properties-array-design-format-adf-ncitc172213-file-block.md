# Array Design Format (ADF) \[NCIT:C172213] file block Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/array_experiment/properties/adf_files
```

The array design format (ADF) \[NCIT:C172213] is the unique set of probes (with their coordinates) found on the microarray chip. They can be standard (sold by a company) or custom. Its format is of a spreadsheet-like tab-delimited text file with metadata header rows, followed by a multi-column table of probe information. For example, see ADF for [arrayexpress:E-MTAB-3050](https://www.ebi.ac.uk/arrayexpress/files/A-GEOD-28079/A-GEOD-28079.adf.txt) or [arrayexpress:E-MEXP-1712](https://www.ebi.ac.uk/arrayexpress/files/A-AFFY-125/A-AFFY-125.adf.txt). This node is an array of file nodes in case the ADF is given in several formats (e.g. tsv, xlsx, csv...).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## adf\_files Type

`object[]` ([EGA File object](ega-12-definitions-ega-file-object.md))

## adf\_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
