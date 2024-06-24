import json
import os
import sys

from utils.json_validation import request_validation, get_errors_response

# Handling arguments
dirname = sys.argv[1]
curl_URL = sys.argv[2]

# Hardcoded values
extension = ".json"

# Running validations
error_dict = {}
validated_files = []
total_files = 0
files_with_errors = 0

# Iterate over the JSON documents to validate
for file in os.scandir(dirname):
    if not file.path.endswith(extension):
        continue

    total_files += 1
    validated_files.append(file.name)
    
    request = request_validation(
        data_filepath=file,
        validator_url=curl_URL
    )

    val_error = get_errors_response(
        response=request,
        filename=file.name
    )
    if val_error:
        error_dict[file.name] = val_error
        files_with_errors += 1

# If the dictionary is not empty, fail the script returning it
summary = {
    "n_total_files": total_files,
    "n_files_with_errors": files_with_errors,
    "error_files": error_dict,
    "all_files": validated_files
}

if error_dict:
    sys.exit(json.dumps(summary, sort_keys=True, indent=4))
else:
    print(json.dumps(summary, sort_keys=True, indent=4))
