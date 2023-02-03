# NCBI's Assembly descriptor Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/referenceAlignmentDetails/items
```

Node describing a sequence assembly referenced in [NCBI's Assembly database](https://www.ncbi.nlm.nih.gov/assembly). Assembly is a database providing information on the structure of assembled genomes, assembly names and other meta-data, statistical reports, and links to genomic sequence data. An assembly is defined as the set of chromosomes, unlocalized and unplaced (sometimes called 'random') and alternate sequences used to represent an organism's genome. Assemblies are constructed from 1 or more assembly units.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`object` ([NCBI's Assembly descriptor](ega-4-definitions-ncbis-assembly-descriptor.md))

# items Properties

| Property                              | Type   | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                              |
| :------------------------------------ | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ncbiAssembly](#ncbiassembly)         | Merged | Required | cannot be null | [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssembly")          |
| [ncbiAssemblyUnit](#ncbiassemblyunit) | Merged | Optional | cannot be null | [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssemblyUnit") |

## ncbiAssembly

Node defining an Assembly (e.g. 'GCF\_000001405.26'). For example, the assembly accession for the GenBank version of the public human reference assembly ('termLabel' being 'GRCh38.p14') is 'GCA\_000001405.29' ('termId'). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbiAssembly`

*   is required

*   Type: `object` ([NCBI Assembly](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssembly")

### ncbiAssembly Type

`object` ([NCBI Assembly](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")

## ncbiAssemblyUnit

NCBI's identifier of the assembly unit. An assembly unit is defined as the collection of sequences used to define discrete parts of an assembly. Commonly, assembly units are entire chromosomes (e.g. Chromosome 1 of human genome), scaffolds or different types of sequences (e.g. Mitochondrial DNA). Again, it follows an 'ontologyTerm' structure, having a 'termId' (e.g. 'refseq:NC\_000001.11') and 'termLabel' (e.g. 'chromosome 1'). See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

`ncbiAssemblyUnit`

*   is optional

*   Type: `object` ([NCBI assembly unit](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md))

*   cannot be null

*   defined in: [EGA common metadata definitions](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md "https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/ncbiAssemblyDescriptor/properties/ncbiAssemblyUnit")

### ncbiAssemblyUnit Type

`object` ([NCBI assembly unit](ega-4-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-unit.md))

all of

*   [Ontology term](ega-4-definitions-ontology-term.md "check type definition")
