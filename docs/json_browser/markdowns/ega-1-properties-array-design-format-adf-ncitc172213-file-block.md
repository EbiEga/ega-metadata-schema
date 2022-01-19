# Array Design Format (ADF) \[NCIT:C172213] file block Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.ArrayExperiment.json#/properties/adf_files
```

The array design format (ADF) \[NCIT:C172213] is the unique set of probes (with their coordinates) found on the microarray chip. They can be standard (sold by a company) or custom. Its format is of a spreadsheet-like tab-delimited text file with metadata header rows, followed by a multi-column table of probe information. This object shall only be used if the EGA is the one storing such file. Otherwise, the Relationships object shall be used to point from the ArrayExperiment to the ADF submitted elsewhere.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                          |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.ArrayExperiment.json*](../out/EGA.ArrayExperiment.json "open original schema") |

## adf_files Type

`object[]` ([EGA File object](ega-4-definitions-ega-file-object.md))

## adf_files Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
