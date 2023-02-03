# NCBI Assembly Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssembly
```

Node defining an Assembly (e.g. 'GCF\_000001405.26'). For example, the assembly accession for the GenBank version of the public human reference assembly ('termLabel' being 'GRCh38.p14') is 'GCA\_000001405.29' ('termId'). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## ncbiAssembly Type

`object` ([NCBI Assembly](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# ncbiAssembly Properties

| Property          | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                |
| :---------------- | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Merged | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssembly/properties/termId") |

## termId



`termId`

*   is optional

*   Type: merged type ([Ontology constraints for this specific termId](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssembly/properties/termId")

### termId Type

merged type ([Ontology constraints for this specific termId](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-properties-ontology-constraints-for-this-specific-termid.md))

all of

*   all of

    *   [Compact URI (CURIE) pattern](ega-4-definitions-ncbi-assembly-curie-pattern-allof-compact-uri-curie-pattern.md "check type definition")

### termId Examples

```json
"assembly:GCF_000001405.26"
```

```json
"assembly:GCA_000001405.1"
```

```json
"assembly:GCF_000005845.2"
```
