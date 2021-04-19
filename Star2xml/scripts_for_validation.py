import sys
import lxml.etree as etree
import os
from utils import report_error_messages

def check_xml_is_valid(xml_tree, schema_file, verbose = False, schema_key = None, dontExitOn_ParsingErrors = False):
    """
    Function that checks if a given XML is valid against a certain XML schema.

    Parameters:
        - xml_tree (etree._Element | str): the XML object to validate (e.g. <Element SAMPLE_SET at 0x2d9ac453f08>).
                                           Alternatively it can be a string containing a filepath to a text file containing the XML.
        - schema_file (str): filepath of the schema file (e.g. Path/To/Schemas/SRA.sample.xsd)
        - verbose (bool): if False, the function will only return True/False based on the validation
                          if True, the function will additionally print all validation errors.
        - schema_key (str): schema key to add information to the verbose report (e.g. "sample" or "study")
        - dontExitOn_ParsingErrors (bool): a boolean switch that will indicate if the function should exit upon errors while parsing the XMLs) or 
                                           simply tag them as non-validated XMLs. Use it if you wish to avoid stopping the validation on other
                                           scripts due to an error on the XML that we are validating.

    Dependencies:
        - lxml.etree
    """
    original_xml_tree = xml_tree
    # If the given xml_tree is not an etree object, but a file containing the XML, we parse it:
    if not isinstance(xml_tree, etree._Element) and not isinstance(xml_tree, etree._ElementTree):
        # We check that the schema file exists:
        if not os.path.isfile(xml_tree):
            print("ERROR in check_xml_is_valid(): the given filepath containing an XML tree '%s' does not exist" % xml_tree, file=sys.stderr)
            sys.exit()
        try:
            xml_tree = etree.parse(xml_tree)
        except etree.XMLSyntaxError as XMLSyntaxError:
            # If we want to tag parsing errors as "validation" errors, instead of stopping the function. 
            if dontExitOn_ParsingErrors:
                is_valid = False
                if verbose:
                    print_ValidationVerdict(is_valid = is_valid, 
                                            schema_key = schema_key,
                                            original_xml_tree = original_xml_tree,
                                            parsing_error = True)
                return is_valid
            else:
                print("ERROR in check_xml_is_valid(): the given filepath containing an XML tree '%s' could not be parsed due to a syntax error." % xml_tree, file=sys.stderr)
                report_error_messages(sys.exc_info()[0], XMLSyntaxError.msg)
                sys.exit()

        except:
            print("ERROR in check_xml_is_valid(): the given filepath containing an XML tree '%s' could not be parsed" % xml_tree, file=sys.stderr)
            report_error_messages(sys.exc_info()[0], sys.exc_info()[1])
            sys.exit()

    if not os.path.isfile(schema_file):
        print("ERROR in check_xml_is_valid(): the schema file '%s' does not exist. If you have not downloaded the schema files (.xsd) yet, use '--download_xsd' when running the command" % schema_file, file=sys.stderr)
        sys.exit()

    # We create the validator
    try:
        xml_validator = etree.XMLSchema(file = schema_file)
    except:
        print("ERROR in check_xml_is_valid(): the schema file '%s' could not be passed to the lxml.etree.XMLSchema() module." % schema_file, file=sys.stderr)
        report_error_messages(sys.exc_info()[0], sys.exc_info()[1])
        sys.exit()

    # We check if the XML tree is valid following the schema
    is_valid = xml_validator.validate(xml_tree)

    # If we want to see all the validation errors (verbose = True) we get them from lxml.etree
    if verbose:
        print_ValidationVerdict(is_valid = is_valid, 
                                schema_key = schema_key,
                                original_xml_tree = original_xml_tree)

        # If not valid, we get deeper into the issue to report what is the part that was not validated
        if not is_valid:
            try:
                xml_validator.assertValid(xml_tree)

            # If the assert throws a validation error it will be of type lxml.etree.DocumentInvalid
            except etree.DocumentInvalid:
                print("\tValidation error(s):")
                for error in xml_validator.error_log:
                    print("\t - Line {} ({}) --> {}".format(error.line, error.path, error.message))

    return is_valid

def print_ValidationVerdict(is_valid, schema_key, original_xml_tree, parsing_error = False):
    """
    Function that prints the verdict of the validation.
    """
    # Based on the returned boolean of is_valid we print different verdicts
    if is_valid:
        verdict = "-- Correctly validated:"
    elif parsing_error:
        # To add more details, we also account for a parsing error if dontExitOn_ParsingErrors was True at check_xml_is_valid().
        verdict = "-/- Parsing errors [WARNING]:"
    else:
        verdict = "-/- Errors during validation:"

    # If we were given a schema key, we add it to get a clearer report
    if schema_key:
        print("%s '%s'\t\tXML file: '%s'" % (verdict, schema_key, original_xml_tree))
    else:
        print("%s \t\tXML file: '%s'" % (verdict, original_xml_tree))
