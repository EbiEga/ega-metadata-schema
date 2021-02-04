import requests
from bs4 import BeautifulSoup
import lxml.etree as etree
import os

def list_web_FullDirectory(url, extension = ''):
    """
    Function to list the full content of a web directory (HTTP) whose extension matches with the given extension.

    Parameters:
        - url (str): the web's directory whose content you want to list (e.g. http://ftp.ebi.ac.uk/pub/databases/ena/doc/xsd/sra_1_5/)
        - extension (str): the extension of the files you are looking for (e.g. '.xsd')

    Dependencies:
        - requests
        - bs4.BeautifulSoup
    """
    # We retrieve the whole HTML of the given URL
    html_page = requests.get(url).text

    # We parse the HTML and create a BeautifulSoup object
    html_soup = BeautifulSoup(html_page, 'html.parser')

    # We return a list with all files (href = file) that end with the given extension
    return [url + '/' + node.get('href') for node in html_soup.find_all('a') if node.get('href').endswith(extension)]


def download_files(file_list, output_dir = "downloaded_schemas/"):
    """
    Function to download a list of files through "request" package.

    Parameters:
        - file_list (list): list of strings that represent the URLs of the files to download
                            (e.g. ['http://ftp.ebi.ac.uk/pub/databases/ena/doc/xsd/sra_1_5//SRA.sample.xsd'])
        - output_dir (str): directory path to store the downloaded files (e.g.'path/to/dir/').

    Dependencies:
        - request
        - os.path
    """
    # Check if output_dir exists, create it if not
    dir_exists = os.path.isdir(output_dir)
    if not dir_exists:
        os.makedirs(output_dir)

    for file_url in file_list:
        # Assign filenames
        file_basename = os.path.basename(file_url)
        outut_file = os.path.join(output_dir, file_basename)

        # If the file exists, we don't need to download it
        if not os.path.isfile(outut_file):
            url_request = requests.get(file_url)
            with open(outut_file, 'wb') as f:
                f.write(url_request.content)


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
