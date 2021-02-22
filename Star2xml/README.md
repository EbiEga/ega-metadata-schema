# Star2xml
## Overview
The Star2xml tool eases the process of XML creation prior metadata submission.
* **What?**
    * A compilation of Python scripts that automatically generate correctly formatted XMLs containing metadata. Additionally it can validate such XMLs against ENA's schemas (`.xsd` files).
* **How?**
    * Given an input file (`.csv`, `.tsv` or `.xlsx`) the tool follows an XML structure (defined in a `YAML` schema file) assigning each field of the input file to its corresponding XML node's characteristics.
* **Where?**
    * Tool's scripts can be found in [Star2xml directory](./).
    * Required Python packages can be found at [requirements.txt](requirements.txt).
    * Input files templates can be found in the [template directory](../templates/sequence-based-metadata/). Further information about their formats and how to fill them exists in their section on this [README](#Filling-out-templates).
    * Configuration files (`input_configuration.yaml` and `xml_schema.yaml`) reside in the [configurations directory](configuration_files/). Information regarding their structure and how to modify them is located both within the files themselves and their section on this [README](#Configuration-files).

## Usage
### Pre-requisites
This tool was programmed in **Python** (**version 3.8+**) and depends on the following packages:


| Package        | Version  | Description  |
| -------------: |:-------------|:-------------|
| pandas | 1.2.2 | Fast, powerful, flexible and easy to use open source data analysis and manipulation tool |
| PyYAML  | 5.4.1 | YAML parser and emitter |
| argparse | 1.4.0 | Module to write user-friendly command-line interfaces |
| lxml | 4.6.2 | library for processing XML and HTML |
| datetime | 4.3 | Supplies classes for manipulating dates and times |
| openpyxl | 3.0.6 | Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files |

You may want to install the latest versions of this packages and check if it works (running the [mock command line examples](#Mock-examples) provided in this README). In case you want to install the specific versions we used to develop this tool, you are advised to create a **virtual environment** (to avoid overwriting other versions you may use).

To install Python dependencies:
```bash
# Step 1. Cloning the tools repository
git clone https://github.com/EbiEga/ega-metadata-schema/star2xml
# Step 2. Creating and activating the virtual environment
virtualenv -p python3 venv_star2xml
source venv_star2xml/bin/activate
# Step 3. Installing dependencies
pip3 install -r requirements.txt
# Step 4. Deactivating the virtual environment
deactivate
```
If you wish to install dependencies on your working environment, you will only need to run the two commands from steps 1 and 3. In case you do create a virtual environment, remember to always activate it (`source venv_star2xml/bin/activate`) prior running the scripts.

### Scripts
There are two main scripts you can run:
* **star2xml.py**: used to **generate** XMLs
* **validateXML.py**: used to **validate** XMLs

Information of both scripts can be obtained using the command line help option [`-h`] (_e.g._ `./star2xml.py -h`).

### star2xml.py
```
usage: star2xml.py [-h] [--schema-file [SCHEMA_FILE]] [--configuration-file [CONF_FILE]] [--verbose] [--debug]
                   schema_key input_file output_xml

A script to transform an input file (.csv, .tsv or .xlsx) into a dataframe, and then build an XML (which will be
validated against ENA's schemas .XSD) with its information following the XML structure described in a YAML file

positional arguments:
  schema_key            Schema key for the metadata object (e.g. "sample", "run", "experiment"...)
  input_file            Input file (.csv, .tsv or .xlsx) with metadata information to be transformed into a dataframe
                        (e.g. "sample.xlsx")
  output_xml            Output XML filepath, i.e. file that will contain the generated XML (e.g. "sample.xml")

optional arguments:
  -h, --help            show this help message and exit
  --schema-file [SCHEMA_FILE]
                        YAML file containing the schema for the metadata object(s) (e.g. "xml_schema.yaml")
  --configuration-file [CONF_FILE]
                        YAML file containing the configuration (i.e. required fields) of the input file (e.g.
                        "input_configuration.yaml")
  --verbose             A boolean switch to add verbosity to the function (printing initial parameters, final XML...)
  --debug               A boolean switch to set the functions in "debug" mode, which will add even more verbosity to
                        the function (printing every step of the XML creation...)

```
For example, if we had an excel spreadsheet (`run.xlsx`), with one run per row, and wanted to create its corresponding XML (`run.xml`), we would run the following command:
``` Bash
./star2xml.py  'run' 'test_data/filled_examples/run.xlsx' 'test_data/XML_examples/run.xml' --schema-file 'configuration_files/xml_schema.yaml' --configuration-file 'configuration_files/input_configuration.yaml'
```
Both `--schema-file` and `--configuration-file` arguments can be omitted if their corresponding filepaths have not been modified (by default in `configuration_files/`). Thus, the command can be simplified:
``` Bash
./star2xml.py  'run' 'test_data/filled_examples/run.xlsx' 'test_data/XML_examples/run.xml'
```

### validateXML.py
```
usage: validateXML.py [-h] [--schemas-dir [SCHEMA_DIR]] [--schema-file [SCHEMA_FILE]] [--download_xsd] [--verbose]
                      schema_keys input_xmls

A script to validate one (or more) input XML files based on some XML schemas (.xsd files). If schemas are missing, it
downloads them from a given FTP server. The function returns a list full of boolean values defined by the outcome of
the validation (e.g. [False, True, True] if only the last 2 XMLs were correctly validated)

positional arguments:
  schema_keys           Schema key(s) (comma delimited) for the metadata object(s) (e.g. "sample,run" or
                        "experiment"...)
  input_xmls            Input XML(s) (comma delimited) with metadata information to be validated (e.g.
                        "sample.xml,run.xml")

optional arguments:
  -h, --help            show this help message and exit
  --schemas-dir [SCHEMA_DIR]
                        Directory containing all the XSD schema files (e.g. "downloaded_schemasXSD/"). If --download-
                        xsd is given, the XSD files will be downloaded into this directory.
  --schema-file [SCHEMA_FILE]
                        YAML file containing the schema for the metadata object(s) (e.g. "xml_schema.yaml")
  --download_xsd        A boolean switch to give if you want the schemas (.xsd files) to be downloaded instead of
                        providing them
  --verbose             A boolean switch to add verbosity to the function (will print into the terminal extra
                        information, as well as the validation errors and results with a friendlier format)
```
In this case we can validate as many XML files as we want in one go. For instance, in the following example we validate two XML files (`sample.xml` and `run.xml`) that correspond to two different metadata objects (`sample` and `run`). It is important to notice that, if we have not downloaded yet the metadata schema files (`.xsd`), we should provide the option `--download_xsd` the first time we run `validateXML.py`.
```Bash
./validateXML.py "sample,run" "test_data/XML_examples/test_sample.xml,test_data/XML_examples/test_run.xml" --schemas-dir "downloaded_schemasXSD/" --schema-file "configuration_files/xml_schema.yaml" --verbose --download_xsd
```
Once again, if we have not modified the schema filepath, option `--schema-file` can be omitted. Besides, if we already downloaded the `.xsd` files, we can also omit the option `--download_xsd`. Thus, a simpler command would be:
```Bash
./validateXML.py "sample,run" "test_data/XML_examples/test_sample.xml,test_data/XML_examples/test_run.xml" --schemas-dir "downloaded_schemasXSD/" --verbose
```

### Mock examples
Pre-defined files are ready for you to run the following commands, checking the tool's functionality and its output.
```Bash
./star2xml.py  'run' 'test_data/filled_examples/run.xlsx' 'test_data/XML_examples/test_run.xml' --verbose
```
```Bash
./star2xml.py  'sample' 'test_data/filled_examples/sample.xlsx' 'test_data/XML_examples/test_sample.xml' --verbose
```
```Bash
./validateXML.py "sample,run" "test_data/XML_examples/test_sample.xml,test_data/XML_examples/test_run.xml" --download_xsd --verbose
```

## Filling out templates
Depending on what type of submission you want to perform, you need to **choose its corresponding template** from the [available set](../templates/sequence-based-metadata). Since the most user-friendly formats tend to be spreadsheets, the templates we provide are ``.xlsx`` files. These can also be converted to ``.tsv`` and ``.csv`` if needed.

In all templates, **each row will represent one repetition of a metadata object**. For example, each of the rows in a sample spreadsheet given as input will represent one ``<SAMPLE>`` node in the final XML. All information that row contains will be associated with its corresponding ``<SAMPLE>`` node (its alias, description, etc.).

There are two types of columns in the input files:

1. **Non-repetitive columns**. These fields describe a characteristic (text or attribute) of **one single node** (*e.g.* `text: "Scientific_name"`) **for each metadata object** (*e.g.* ``<SAMPLE>``). In the following image, we have 2 rows with 6 of these columns. These columns are alternatively coloured in yellow in the templates and shall not be deleted from the input file, but you can leave them empty for some or all rows.

![2 rows of the sample template - Non repeated fields](miscellaneous/Sample_template_2rows_non-repeated.png)

2. **Repetitive columns**. These fields contain characteristics for **a node that can be repeated** (*e.g.* ``<SAMPLE_ATTRIBUTE>`` or ``<FILE>``) **within each metadata object**. In the following image we have 2 rows with 6 of these columns, which correspond to 2 repetitions of the same ***repetitive block*** (in this case ``Tag-Value-Units``). These blocks are alternatively coloured and can be added or deleted depending on your needs, but if there is a column from a repetitive block, their sibling columns are also required (even if left empty): in our example, if we add a new repetition with columns ``Tag`` and ``Value``, there needs to be a third one, ``Units``.  

![2 rows of the sample template - Repeated fields](miscellaneous/Sample_template_2rows_repeated.png)

Column names in the templates are **linked to the configuration files** (`input_configuration.yaml` and `xml_schema.yaml`), which leads to an important constraint: if there is a field described in a configuration file (e.g. ``center_name: "Center_name"``) there **needs** to be its corresponding column name within the input file (e.g. `Center_name`). In other words, unless the configuration file is properly modified, you shall not delete *non-repetitive columns* or completely delete all *repetitive blocks* from the input file. What you can do is leave them empty for some or all rows, or delete additional repetitive blocks that you don't need. At least one of each complete (with all its fields) repetitive block needs to be present within the input file, even if you leave it empty for some or all rows.

The **order of columns is not relevant** as long as the repeated blocks' columns are not severely mixed (*e.g.* filling first `Tag` with the string corresponding to the second `Tag`). In fact, repeated columns can be mixed provided the order is maintained, thus making the following input valid.

![2 rows of the sample template - Mixed, though correct, fields](miscellaneous/Sample_template_2rows_mixed.png)

This allows for a handy way of dealing with **hundreds or thousands of columns** in an easy way (being able to put all columns of the same type in a sequence). For instance, we may want to generate an Analysis XML based on its spreadsheet, but the analysis encompasses thousand of samples (*i.e.* thousands of columns). Although there are multiple ways to input such columns, an easy approach is to use the **transpose function** (*e.g.* from excel - [help from microsoft](https://support.microsoft.com/en-us/office/transpose-rotate-data-from-rows-to-columns-or-vice-versa-3419f2e3-beab-4318-aae5-d0f862209744)). In our example the sample repetitive block contains 3 columns (``Sample_alias``, ``Sample_centerName`` and ``Label``). Therefore, we can do the following:
![Example of using transpose to add columns](miscellaneous/Transpose_example.png)

## Configuration files

There are **two configuration files**: `input_configuration.yaml` and ``xml_schema.yaml``. The former simply **lists the required fields for each input file** (i.e. if the column name "Sample alias" needs to be present or not). The latter **describes the structure of the corresponding XML** (i.e. which nodes are children of which) and **associates each column name of the input file with its corresponding node's characteristic** (either an attribute or text). Both are `YAML` files, which are easy-to-read information holders, and can be interpreted as dictionaries/lists of elements. Besides the information displayed here, additional clues reside within the files themselves.

### Basic structure - xml_schema.yaml
At base level, the file contains **information of the tool itself** (`tool_info` - used to add details to reports), the **metadata schemas** (`XML_schemas_info` - used to both download `.xsd` files and create XMLs) and **one element for each metadata object** (e.g. `sample`) describing its architecture.

A simple example of *what is what*, with content from the `xml_schema.yaml` (_up_), the input file (_right_) and the output XML (_down_), is the following:

![Configuration files - What is what schema](miscellaneous/Conf_arrow_schema.png)

### Modifying the schema
If the metadata requirements change and existing fields need to be removed or new ones added, we will need to modify the two configuration files as well as the input files.


## ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) Common mistakes ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)

* Missing fields of a repetitive block (in this case fields ``Value`` and ``Units`` are missing from the block ``Tag-Value-Units``)
![2 rows of the sample template - Missing fields](miscellaneous/Sample_template_2rows_incorrect1.png)

* Not using the option `--download_xsd` the first time you try to validate XMLs: the schemas (`.xsd`) will be missing and the tool will throw the following error message:
``` Bash
ERROR in check_xml_is_valid(): the schema file 'downloaded_schemasXSD/SRA.sample.xsd' could not be accessed. If you have not downloaded the schema files (.xsd) yet, use '--download_xsd' when running the command.
```
