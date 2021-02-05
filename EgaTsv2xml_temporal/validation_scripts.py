import sys
import lxml.etree as etree

def check_xml_is_valid(xml_tree, schema_file):
    """
    Function that checks if a given XML is valid against a certain XML schema.

    Parameters:
        - xml_tree (etree._Element | str): the XML object to validate (e.g. <Element SAMPLE_SET at 0x2d9ac453f08>).
                                           Alternatively it can be a string containing a filepath to a text file containing the XML.
        - schema_file (str): filepath of the schema file (e.g. Path/To/Schemas/SRA.sample.xsd)

    Dependencies:
        - lxml.etree
    """
    # If the given xml_tree is not a etree object, but a file containing the XML, we parse it:
    if not isinstance(xml_tree, etree._Element):
        try:
            xml_tree = etree.parse(xml_tree)
        except:
            print("ERROR in check_xml_is_valid(): the given filepath containing an XML tree '%s' could not be parsed" % xml_tree, file=sys.stderr)
            sys.exit()

    # We create the validator
    try:
        xml_validator = etree.XMLSchema(file = schema_file)
    except:
        print("ERROR in check_xml_is_valid(): the schema file '%s' could not be accessed" % schema_file, file=sys.stderr)
        sys.exit()

    is_valid = xml_validator.validate(xml_tree)

    return is_valid
