# ------ #
# Utils for JSON Validation
# ------ #

# In this file there are functions, classes or variables that are used widely
#   in the GitHub actions of this repository and imported accordingly in other
#   scripts.

# - #
# System imports
# - #
import os
from typing import Union
import requests


# -#
# Helper functions
# -#
def request_validation(
    data_filepath: Union[str, os.DirEntry[str]], curl_URL: str, headers: dict = None
) -> requests.models.Response:
    """
    Function that, given a data_filepath (e.g. "path/to/file.json"), a URL (e.g. http://localhost:3020/validate)
        and the HTTP headers, will do a post request and return the response
    """
    if headers is None:
        headers = {"Content-Type": "application/json"}

    with open(data_filepath) as f:
        data = f.read().replace("\n", "").replace("\r", "").encode("utf-8")

    response = requests.post(url=curl_URL, headers=headers, data=data)
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
            f" the status code was '{response.status_code}' when validating file '{filename}'"
        )
        return error_message

    val_response_list = response.json()

    # If the list is empty "[]", the validation found no errors
    if not len(val_response_list) == 0:
        return val_response_list
    else:
        return None


# - #
# Class definition
# - #
