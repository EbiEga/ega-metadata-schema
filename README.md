# EGA Metadata Schema
## Overview
This repository is intended to be the **source of truth for EBI-EGA's metadata schemas**. For data to be submitted to the [EGA-archive](https://ega-archive.org/submission/quickguide), apart from the data files themselves (_e.g._ `.bam` files), you will need an **appropriate metadata architecture** both describing your data and the underlying relationships between its objects (_e.g._ what experiments encompass which samples).

Depending on the nature of your data (raw sequences, variant calling, arrays...) the metadata and its submission procedure will differ:
* [**Array based metadata**](https://ega-archive.org/submission/array_based/metadata): must be submitted using EGA submitter portal and completing the [Array-based format (AF) spreasheet](https://github.com/EbiEga/ega-metadata-schema/blob/8dca24c694b0c005f1b0d665f1c6900e766f38d7/templates/array-based-metadata/EGA_Array_based_Format_V4.3.xlsx) ([_direct download_](https://github.com/EbiEga/ega-metadata-schema/raw/8dca24c694b0c005f1b0d665f1c6900e766f38d7/templates/array-based-metadata/EGA_Array_based_Format_V4.3.xlsx)).
* [**Sequence**](https://ega-archive.org/submission/sequence) **based metadata**: must be submitted either using the [EGA submitter portal](https://ega-archive.org/submission/tools/submitter-portal) or through the [programmatic submission](https://ega-archive.org/submission/sequence/programmatic_submissions) procedure. For the latter you will need to create correctly formatted XMLs containing your metadata:
    * You will find examples of such XMLs (one file for each metadata object) within this repository: (1) [descriptive XMLs](examples/sequence-based-metadata/XML/XMLs_examples-descriptive) display what type of information corresponds to which part of the XML's structure; (2) [true example XMLs](examples/sequence-based-metadata/XML/XMLs_examples-true_values) contain fabricated information for you to see what a finished (and ready to be submitted) XML would look like.
    * To ease this process, you could make use of the tool [Star2xml](Star2xml/). Follow its README to create these XMLs from the given [``joint template``](templates/sequence-based-metadata/EGA_metadata_submission_template_v1.xlsx). 
    
    
    
