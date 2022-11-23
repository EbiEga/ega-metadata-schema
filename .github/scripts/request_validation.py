import requests
import json
import sys
import os

#---------#
# Handling arguments
#---------#
dirname = sys.argv[1]
curl_URL = sys.argv[2]
extension = ".json"

#---------#
# Function definition
#---------#
def request_validation(data_filepath, curl_URL, headers = {'Content-Type': 'application/json'}):
    """
        Function that, given a fata_filepath (e.g. "path/to/file.json"), a URL (e.g. http://localhost:3020/validate)
            and the HTTP headers, will do a post request and return the response
    """ 
    with open(data_filepath) as f:
        data = f.read().replace('\n', '').replace('\r', '').encode('utf-8')
        
    response = requests.post(url = curl_URL, headers = headers, data = data)    
    return response

def get_errors_response(response):
    """
        Function that, given a "requests.models.Response" object, will interpret it, asserting that the request
            was successful and no validation errors (i.e. empty list of errors) were found. If not, it will
            exit with an error.
    """
    assert type(response) == requests.models.Response
    assert response.status_code == 200
    
    # We load the result of the validation
    val_response_list = json.loads(response.text)
    
    # If the list is empty "[]", the validation found no errors
    if not len(val_response_list) == 0:
        return val_response_list

#---------#
# Running validations
#---------#
error_dict = {}
# We iterate over the JSON documents to validate
for file in os.scandir(dirname): 
    # Check if it's a JSON file
    if not file.path.endswith(extension):
        continue

    request = request_validation(data_filepath = file,
                                 curl_URL = curl_URL)
    
    val_error = get_errors_response(request)
    # If there was a validation error, we add it to the dictionary
    if val_error:
        error_dict[file.name] = val_error

# If the dictionary is not empty, fail the script returning it
if error_dict:
    sys.exit(error_dict)