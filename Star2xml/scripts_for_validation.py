import sys
import lxml.etree as etree
import os

def check_xml_is_valid(xml_tree, schema_file, verbose = False, schema_key = None):
    """
    Function that checks if a given XML is valid against a certain XML schema.

    Parameters:
        - xml_tree (etree._Element | str): the XML object to validate (e.g. <Element SAMPLE_SET at 0x2d9ac453f08>).
                                           Alternatively it can be a string containing a filepath to a text file containing the XML.
        - schema_file (str): filepath of the schema file (e.g. Path/To/Schemas/SRA.sample.xsd)
        - verbose (bool): if False, the function will only return True/False based on the validation
                          if True, the function will additionally print all validation errors.
        - schema_key (str): schema key to add information to the verbose report (e.g. "sample" or "study")

    Dependencies:
        - lxml.etree
    """
    original_xml_tree = xml_tree
    # If the given xml_tree is not a etree object, but a file containing the XML, we parse it:
    if not isinstance(xml_tree, etree._Element) and not isinstance(xml_tree, etree._ElementTree):
        # We check that the schema file exists:
        if not os.path.isfile(xml_tree):
            print("ERROR in check_xml_is_valid(): the given filepath containing an XML tree '%s' does not exist" % xml_tree, file=sys.stderr)
            sys.exit()
        try:
            xml_tree = etree.parse(xml_tree)
        except:
            print("ERROR in check_xml_is_valid(): the given filepath containing an XML tree '%s' could not be parsed" % xml_tree, file=sys.stderr)
            sys.exit()

    if not os.path.isfile(schema_file):
        print("ERROR in check_xml_is_valid(): the schema file '%s' does not exist. If you have not downloaded the schema files (.xsd) yet, use '--download_xsd' when running the command" % schema_file, file=sys.stderr)
        sys.exit()

    # We create the validator
    try:
        xml_validator = etree.XMLSchema(file = schema_file)
    except:
        print("ERROR in check_xml_is_valid(): the schema file '%s' could not be passed to the lxml.etree.XMLSchema() module." % schema_file, file=sys.stderr)
        sys.exit()

    # We check if the XML tree is valid following the schema
    is_valid = xml_validator.validate(xml_tree)

    # If we want to see all the validation errors (verbose = True) we get them from lxml.etree
    if verbose:
        # Based on the returned boolean of is_valid we print different veredicts
        if is_valid:
            veredict = "- Correctly validated:"
        else:
            veredict = "-/- Errors during validation:"

        if schema_key:
            print("%s '%s'\t\tXML file: '%s'" % (veredict, schema_key, original_xml_tree))
        else:
            print("%s \t\tXML file: '%s'" % (veredict, original_xml_tree))

        try:
            xml_validator.assertValid(xml_tree)

        # If the assert throws a validation error it will be of type lxml.etree.DocumentInvalid
        except etree.DocumentInvalid:
            print("\tValidation error(s):")
            for error in xml_validator.error_log:
                print("\t - Line {} ({}) --> {}".format(error.line, error.path, error.message))

    return is_valid
