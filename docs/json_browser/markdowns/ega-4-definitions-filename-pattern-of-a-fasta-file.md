# Filename pattern of a FASTA file Schema

```txt
https://raw.githubusercontent.com/EbiEga/ega-metadata-schema/main/schemas/EGA.common-definitions.json#/definitions/fastaFileFilenamePattern
```

This object exists to hold the filename pattern that a 'FASTA' filetypeId would have, for it to be referenced elsewhere within this (or other) JSON schema.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [EGA.common-definitions.json\*](../../../schemas/EGA.common-definitions.json "open original schema") |

## fastaFileFilenamePattern Type

`string` ([Filename pattern of a FASTA file](ega-4-definitions-filename-pattern-of-a-fasta-file.md))

## fastaFileFilenamePattern Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^.+\.(fasta|fa|frn|faa|ffn|fna|seq)(\.(gz|zip|rar|arj|tar|7z|bz2))?(\.gpg)?$
```

[try pattern](https://regexr.com/?expression=%5E.%2B%5C.\(fasta%7Cfa%7Cfrn%7Cfaa%7Cffn%7Cfna%7Cseq\)\(%5C.\(gz%7Czip%7Crar%7Carj%7Ctar%7C7z%7Cbz2\)\)%3F\(%5C.gpg\)%3F%24 "try regular expression with regexr.com")

## fastaFileFilenamePattern Examples

```json
"my_file1.fasta.gz.gpg"
```
