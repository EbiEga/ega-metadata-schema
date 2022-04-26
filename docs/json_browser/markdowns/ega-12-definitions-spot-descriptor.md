# Spot descriptor Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.experiment.json#/properties/experiment_type_specifications/properties/sequencing_experiment/properties/spot_descriptor
```

The 'spot\_descriptor' specifies how to decode the individual reads of interest from the monolithic spot sequence. The spot descriptor contains aspects of the experimental design, platform, and processing information. There will be two methods of specification: one will be an index into a table of typical decodings, the other being an exact specification. This construct is needed for loading data and for interpreting the loaded sequencing assays. It can be omitted if the loader can infer read layout (from multiple input files or from one input files).

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Forbidden             | none                | [EGA.experiment.json\*](../../../schemas/EGA.experiment.json "open original schema") |

## spot\_descriptor Type

`object[]` ([Spot decode spec](ega-12-definitions-spot-descriptor-spot-decode-spec.md))

## spot\_descriptor Constraints

**minimum number of items**: the minimum number of items for this array is: `1`
