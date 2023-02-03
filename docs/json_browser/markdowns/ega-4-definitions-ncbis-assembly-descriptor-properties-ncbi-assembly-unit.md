# NCBI assembly unit Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssemblyUnit
```

NCBI's identifier of the assembly unit. An assembly unit is defined as the collection of sequences used to define discrete parts of an assembly. Commonly, assembly units are entire chromosomes (e.g. Chromosome 1 of human genome), scaffolds or different types of sequences (e.g. Mitochondrial DNA). Again, it follows an 'ontologyTerm' structure, having a 'termId' (e.g. 'refseq:NC\_000001.11') and 'termLabel' (e.g. 'chromosome 1'). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## ncbiAssemblyUnit Type

`object` ([NCBI assembly unit](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

# ncbiAssemblyUnit Properties

| Property          | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                         |
| :---------------- | :------------ | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [termId](#termid) | Not specified | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssemblyUnit/properties/termId") |

## termId



`termId`

*   is optional

*   Type: unknown ([Ontology constraints for this specific termId](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-properties-ontology-constraints-for-this-specific-termid.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-properties-ontology-constraints-for-this-specific-termid.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssemblyUnit/properties/termId")

### termId Type

unknown ([Ontology constraints for this specific termId](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit-properties-ontology-constraints-for-this-specific-termid.md))

### termId Examples

```json
"refseq:NC_000001.11"
```

```json
"refseq:NC_012920.1"
```
