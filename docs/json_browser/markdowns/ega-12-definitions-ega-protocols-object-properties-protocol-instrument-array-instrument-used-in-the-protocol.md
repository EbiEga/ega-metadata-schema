# Instrument used in the protocol Schema

```txt
https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas/EGA.common-definitions.json#/definitions/protocols_object/properties/protocol_instrument/items
```

Free form text to specify the device, which provides a mechanical or electronic function, and was used by the performer of the protocol. We highly recommend the usage of ontologized terms (e.g. 'Oligonucleotide synthesizer') from the [Experimental Factor Ontology (EFO)](http://www.ebi.ac.uk/efo/EFO_0000548) along their CURIEs between square brackets (e.g. '\[OBI:0400113]').

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## items Type

`string` ([Instrument used in the protocol](ega-12-definitions-ega-protocols-object-properties-protocol-instrument-array-instrument-used-in-the-protocol.md))

## items Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## items Examples

```json
"Computer [OBI:0400107]"
```

```json
"Oligonucleotide synthesizer [OBI:0400113]"
```

```json
"Sonicator [OBI:0400114]"
```
