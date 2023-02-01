# Biovalidator & EGA: Benchmarks (``create_benchmarks.py`` and ``object_set_creator.py``)

## Description
During the adaptation of EGA to the new validation system, using [Biovalidator](https://github.com/elixir-europe/biovalidator) and the new [JSON schemas](https://github.com/EbiEga/ega-metadata-schema/tree/main/schemas), there was a need to check how efficient validation could be. In order to do this, we created two scripts:
* [**``object_set_creator.py``**](../../.github/scripts/object_set_creator.py): a script to build ``object-sets`` (see [details](../../schemas/README.md)) with ease, adding or removing properties and objects to the set. This allowed us to create multiple and diverse object-sets using other preexisting objects in order to test the capabilities of Biovalidator with differently sized JSON documents.
* [**``create_benchmarks.py``**](../../.github/scripts/create_benchmarks.py): a script that allows for a standardized workflow to collect parameters over a set of JSON documents in a directory.

Making use of these two scripts, different combinations of JSON documents, purely created for testing, were validated against both endpoints of Biovalidator: local (``http://localhost:3020/validate``) and EGA's server (``http://biovalidator.ega.ebi.ac.uk/validate``). The parameters (e.g. the time of validation) were collected and stored in this directory with the date they were generated at, following the structure below:

````bash
ega-metadata-schema/
....docs/
........biovalidator_benchmarks/
............[date]_benchmarks/
................json_docs/
................local_endpoint/
................EGAs_endpoint/
````


## Scripts usage
The two python scripts are differently used, based on the flexibility we desired for each: ``object_set_creator.py`` is expected to be imported and used within a python3 environment; while ``create_benchmarks.py`` can be executed given a few arguments. The former is more interactive than the second, on purpose.

### ``object_set_creator.py``
From within a python3 environment we can run the following:
````python
from object_set_creator import CreateObjectSet
# To instance the new object set
new_objectset = CreateObjectSet("../../examples/json_validation_tests/object-set_valid-1.json")
# To empty the objectArray, but keep the other values of the taken object-set
new_objectset.empty_objectArray()
# To only keep the structure of the taken object-set
new_objectset.empty_all_properties()
# To check how the new object-set looks so far
new_objectset.template_json_obj
# To add other JSON objects as items in the objectArray of your new object-set
new_objectset.add_new_json("../../examples/json_validation_tests/experiment_valid-1.json")
new_objectset.add_new_json("../../examples/json_validation_tests/sample_valid-1.json")
new_objectset.add_new_json("../../examples/json_validation_tests/assay_valid-2_sequencing.json")
# To count the number of items (i.e. objects) in the objectArray
new_objectset.count_n_objects()
# And finally to save the new object-set
new_objectset.save_json(output_filepath = "my_new_object_set.json", add_suffix= True)
````
The idea of taking an existing object-set (e.g. ``object-set_valid-1.json``) as template is because it will have the correct structure of properties, and we will just have to empty it, populate it with the JSON objects we want, save it, and finally fill in the properties whose values we emptied.

### ``create_benchmarks.py``
The script can be called from the terminal:
````bash
$ python3 create_benchmarks.py --help
usage: create_benchmarks.py [-h] --endpoint ENDPOINT --input_directory INPUT_DIRECTORY [--output_directory OUTPUT_DIRECTORY] [--number_of_iterations NUMBER_OF_ITERATIONS] [--n_parallel_threads N_PARALLEL_THREADS] [--stop_at_errors]
                            [--not_just_summary_df] [--only_print_complete_df]

Create benchmarks for a Biovalidator server. Check details at https://github.com/EbiEga/ega-metadata-schema/tree/main/docs/biovalidator_benchmarks.

optional arguments:
  -h, --help            show this help message and exit
  --endpoint ENDPOINT   The endpoint of the Biovalidator server. Example: "http://localhost:3020/validate"
  --input_directory INPUT_DIRECTORY
                        The filepath to a directory that contains the JSON documents to validate. Example: "examples/json_validation_tests/"
  --output_directory OUTPUT_DIRECTORY
                        The filepath to a directory in which the results will be stored. Example: "2023_benchmarks/". Default value: "./"
  --number_of_iterations NUMBER_OF_ITERATIONS
                        The amount of iterations of validation of each JSON document within the input directory. Example: 10. Default value: 1
  --n_parallel_threads N_PARALLEL_THREADS
                        The amount of parallel threads for each validation iteration. Example: 5. Default value: 1
  --stop_at_errors      A boolean switch by which we tell the script to stop the execution when a validation error is raised.
  --not_just_summary_df
                        A boolean switch by which we tell the script to not just print the summary dataframe with parameters, but instead save the parameters in files and generate a README.
  --only_print_complete_df
                        A boolean switch by which we tell the script that we do not want any files to be saved and, instead, we just want the complete table of parameters to be printed.
````
There are three major ways in which this script is intended to be used:
````bash
# Just printing the summary of all validated files, to check that all are validated
$ python3 create_benchmarks.py --endpoint "http://localhost:3020/validate" --input_directory "../../examples/json_validation_tests/"
# Printing all details of every validation attempt
$ python3 create_benchmarks.py --endpoint "http://localhost:3020/validate" --input_directory "../../examples/json_validation_tests/" --only_print_complete_df
# Creating the full set of benchmarks, including summaries and graphs
$ python3 create_benchmarks.py --endpoint "http://localhost:3020/validate" --input_directory "../../examples/json_validation_tests/" --output_directory "benchmark_results" --number_of_iterations 20 --not_just_summary_df
````
Additionally, to test how well the validation endpoint handles **parallel calls**, one can add to the last command a number of parallel threads. For example ``--n_parallel_threads 5``. This would make every validation iteration a set of 5 parallel validations, thus testing how the server would behave if 5 different users were to send their JSON files at the same time. The summary statistics will reflect these, since all parallel validations will belong to the same dataframe from which the summary is made.

### Additional Notes
There are two caveats to obtain the representative benchmarks:
* **Local validation endpoint**. In some of these examples we are using ``http://localhost:3020/validate`` as the validation endpoint. Now, this endpoint will only be available if you deployed Biovalidator locally (see [documentation](https://github.com/elixir-europe/biovalidator#using-biovalidator-as-a-server)). Alternatively, if one wants to use EGA's exposed endpoint, ``http://biovalidator.ega.ebi.ac.uk/validate`` can be used.
* **First run after local deployment**. Whenever an EGA schema is referenced (e.g. ``"$ref": "..."``) for the first time since deployment, Biovalidator needs to fetch it from our GitHub page and save it in cache. This means that the time of validation is not representative if you have just deployed Biovalidator locally without running one round of validation first: the schemas will be fetched and that time will be added to the response time, going from milliseconds to seconds. Therefore, if it is advised to execute the script first to get the summaries with one single iteration (i.e. default value of ``--number_of_iterations``) before compiling the benchmarks, so that the schemas are ready for when they are going to be used.