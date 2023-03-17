# The European Genome-phenome Archive (EGA) metadata standards: JSON Browser

Within this directory you will find visual representations of the EGA JSON schemas. They were created using the repository [scripts](../.github/scripts/). See all details in the [Jupyter-notebook](./creating_schemas.ipynb) in this directory.

These diagrams were done manually on ``20.02.2023``, containing the changes of the JSON schemas at this point. In the future, they'll be updated automatically upon changes.

## Where to start

Before getting overwhelmed by the amount of diagrams, let's first summarize the structure of the directories and where to find the information:

````
json_diagrams/
...json_documents/
......[1 directory per object type in the examples]
.........puml_files/
............[PUML files used to generate the SVG files]
.........[SVG files for this object type]

...json_schemas/
......[1 directory per object type]
.........puml_files/
............[PUML files used to generate the SVG files]
.........[SVG files for this object type]
````

Each example in the [example directory](../../examples/json_validation_tests/) will have multiple files, differentiated by a suffix at the end of their filenames. The types of SVGs and PUML files are determined by different, bespoke, combinations manually configured within the [Jupyter-notebook](./creating_schemas.ipynb). **The easiest place to start would be with the ``..._small.svg`` files** (e.g. [analysis_valid-1_small.svg](json_documents/analysis/analysis_valid-1_small.svg)).

A summary of what to expect based on the suffix:
- ``...cardinality.svg``: subset of the original JSON file, only containing paths with: properties named ``objectId``; or relationship properties (e.g. ``rSource``).
- ``...ontologiesHighlight.svg``: The whole JSON object, but with highlighted ``termId`` in properties (ontology validation)
- ``...ontologiesSubset.svg``: Subset of the original JSON file, only containing paths with ``termId`` in the properties (ontology validation) 
- ``...CVhighlights.svg``: The whole JSON object, but with highlighted ``enum`` in properties (Controlled Vocabulary)
- ``...CVsubset.svg``: Subset of the original JSON file, only containing paths with ``enum`` in their properties (Controlled Vocabulary)
- ``...small.svg``: subset of the original JSON file, with only 2 levels of depth. Additionally, having highlighted properties whose leaves have with ``termId`` in the properties (ontology validation)
- ``...wholeUnresolved.svg``: The whole JSON object but without resolved references (``$ref``).
- ``...whole.svg``: The whole JSON object with resolved references (``$ref``).