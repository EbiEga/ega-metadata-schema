# NCBI Assembly accession Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/ncbi_assembly_descriptor/properties/ncbi_assembly_accession
```

Assembly's identifier (e.g. GCF\_000001405.26) of the assembly. For example, the assembly accession for the GenBank version of the public human reference assembly (GRCh38.p14) is GCA\_000001405.29. See further details here: <https://www.ncbi.nlm.nih.gov/assembly/model/>.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## ncbi\_assembly\_accession Type

`string` ([NCBI Assembly accession](ega-12-definitions-ncbis-assembly-descriptor-properties-ncbi-assembly-accession.md))

all of

*   all of

    *   [Compact URI (CURIE) pattern](ega-12-definitions-compact-uri-curie-pattern.md "check type definition")

## ncbi\_assembly\_accession Examples

```json
"assembly:GCF_000001405.26"
```

```json
"assembly:GCA_000001405.1"
```

```json
"assembly:GCF_000005845.2"
```
