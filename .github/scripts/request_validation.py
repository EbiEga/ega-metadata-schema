import json
import os
import sys

from utils.json_validation import request_validation, \
    get_errors_response

# --------- #
# Handling arguments
# --------- #
dirname = sys.argv[1]
curl_URL = sys.argv[2]

# - #
# Hardcoded values
# - #
extension = ".json"

# --------- #
# Running validations
# --------- #
error_dict = {}
# We iterate over the JSON documents to validate
for file in os.scandir(dirname):
    if not file.path.endswith(extension):
        continue

    request = request_validation(
        data_filepath=file,
        curl_URL=curl_URL
    )

    val_error = get_errors_response(
        response=request,
        filename=file.name
    )
    if val_error:
        error_dict[file.name] = val_error

# If the dictionary is not empty, fail the script returning it
if error_dict:
    sys.exit(json.dumps(error_dict, sort_keys=True, indent=4))
