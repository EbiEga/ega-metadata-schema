import sys

def report_error_messages(error_type, error_message):
    """
    Function that prints to standard error both the type of error and the error message. 

    Parameters:
        - error_type (anything convertible to string): the type of error (e.g. taken from sys.exc_info()[0] after an unsuccesful "try")
        - error_message (anything convertible to string): the error message (e.g. taken from sys.exc_info()[1] after an unsuccesful "try")
    """
    print(f"\t- Type of error: {str(error_type)}", file=sys.stderr)
    print(f"\t- Error message: {str(error_message)}", file=sys.stderr)


def check_for_invalid_chars(string_toCheck, chars_dict, stop_if_invalid = False):
    """
    Function that will check if a given string (e.g. my/path?:_to_file) has invalid characters (e.g. '?'), and will either stop
        the execution of the script if found, or translate the invalid string into a valid one (changing such characters)
    
    Parameters:
        - string_toCheck (str): string that will be checked for invalid characters
        - chars_dict (dir): dictionary with the invalid characters as keys and their valid counterparts as values (e.g. {"?": "_"})
        - stop_if_invalid (bool): a boolean switch that decides if the function shall stop if those characters are found or continue.
    """
    # We check that the given string is indeed a string. If not, we return it as it is. 
    if type(string_toCheck) is not str:
        return string_toCheck

    # We iterate over the given dictionary, and if found, we replace their keys with their values
    for character in chars_dict.keys():
        if character in string_toCheck:
            if stop_if_invalid:
                print("ERROR in check_for_invalid_chars(): given string contains invalid characters. If you wish to translate it into a valid string use 'stop_if_invalid = False'.\n\t- String: \t%s\n\t- Invalid characters dictionary: \t%s" \
                  % (string_toCheck, chars_dict), file=sys.stderr)
                sys.exit()
                
            else:
                string_toCheck = string_toCheck.replace(character, chars_dict[character])                

    return string_toCheck



