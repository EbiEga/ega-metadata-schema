# ------ #
# Utils for JSON Validation
# ------ #

# In this file there are functions, classes or variables that are used widely
#   in the GitHub actions of this repository and imported accordingly in other
#   scripts.

# - #
# System imports
# - #
from typing import Union
import requests
import jsonschema


# -#
# Helper functions
# -#
def request_validation(
    data_filepath: str, validator_url: str, headers: dict = None
) -> requests.models.Response:
    """
    Function that, given a data_filepath (e.g. "path/to/file.json"), a validation URL (e.g. http://localhost:3020/validate)
        and the HTTP headers, will do a post request and return the response
    """
    if headers is None:
        headers = {"Content-Type": "application/json"}

    with open(data_filepath) as f:
        data = f.read().replace("\n", "").replace("\r", "").encode("utf-8")

    response = requests.post(url=validator_url, headers=headers, data=data)
    return response


def get_errors_response(
    response: requests.models.Response, filename: str
) -> Union[list, str, None]:
    """
    Function that, given a "requests.models.Response" object, will interpret it, asserting that the request
        was successful and no validation errors (i.e. empty list of errors) were found. If not, it will
        return the error.
    """
    assert (
        type(response) == requests.models.Response
    ), "The POST response was not of the correct type"

    if not response.status_code == requests.codes.ok:
        error_message = (
            f"The POST response was not successful: instead of {requests.codes.ok},"
            f" the status code was '{response.status_code}' when validating file '{filename}'."
            f" Response content: {response.content.decode('utf-8')}"
        )
        return error_message

    try:
        val_response_list = response.json()
    except ValueError:
        return f"Invalid JSON response when validating file '{filename}'. Response content: {response.content.decode('utf-8')}"

    # If the list is empty "[]", the validation found no errors
    if not len(val_response_list) == 0:
        return val_response_list
    else:
        return []


def validate_json(json_obj:dict, json_schema:dict, strict_mode:bool = False) -> bool:
    """
    Validates a given JSON object (data dictionary) against a given JSON schema (schema dictionary) and returns
        True if it validates and False otherwise.
    Additionally, if strict_mode is True, it will raise an exception when validation is not met.
    """
    if not isinstance(json_obj, dict):
        raise TypeError(
            f"The given JSON object ('json_obj') is not of type dictionary."
        )
    if not isinstance(json_schema, dict):
        raise TypeError(
            f"The given JSON schema ('json_schema') is not of type dictionary."
        )
    try:
        jsonschema.validate(instance=json_obj, schema=json_schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        if strict_mode:
            raise e
        return False
