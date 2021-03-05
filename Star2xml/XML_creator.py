import lxml.etree as etree
from datetime import datetime
import sys
import yaml
import pandas as pd
import os.path

# The next tags will define every element of the schema_file (a YAML file containing XML's structure)
children_tag = "children"
attribute_tag = "attributes"
text_tag = "text"
repetitive_tag = "repetitive_node"
add_empty_node_tag = "add_empty_node"
valid_dict_elements = set([children_tag, attribute_tag, text_tag, repetitive_tag, add_empty_node_tag])
tool_info_tag = "tool_info"
version_tag = "version"
update_date_tag = "update_date"

class XML_creator():
    """
    XML creation class using a YAML file containing the XML's schema and a dataframe containing its
        information (attributes and text).
    """

    def __init__(self, schema_filename, input_dataframe, schema_key, output_xml, verbose = False, debug_mode = False):
        """
        Initialization (constructor) of an instance.

        Parameters:
            - self: not explicitly given, it's the instance itself.
            - schema_filename (str): a filepath to the YAML file containing the structure of the output XML
                                     (e.g. 'path/to/schema_file.yaml').
            - input_dataframe (df): a dataframe object (from Pandas) containing the information that will be put into
                                    the XML. This dataframe can be obtained from an input file using Input_reader().
            - schema_key (str): key string that defines the metadata object (e.g. "sample" or "run") within the YAML file.
            - output_xml (str): filepath of the output XML file where it will be saved (e.g. 'output/sample.xml').
        """
        self.verbose = verbose
        self.debug_mode = debug_mode
        self.schema_key = schema_key
        self.schema_filename = schema_filename
        self.output_xml = output_xml

        if self.debug_mode:
            self.log_filename = "XML_creator.log"

        # We (try to) load the YAML schema (that contains XML element's dependencies, attributes, etc.)
        try:
            with open(schema_filename, "r") as schema_file:
                self.schema_general_dict = yaml.safe_load(schema_file)
        except FileNotFoundError:
            print("ERROR in XML_creator(): given schema filepath '%s' does not exist or could not be found." \
                  % schema_filename, file=sys.stderr)
            sys.exit()

        except yaml.scanner.ScannerError as ScannerError:
            print("ERROR in XML_creator(): in the given schema '%s' there was a scanning issue." \
                  % schema_filename, file=sys.stderr)
            print("\t - Problem: %s" \
                  % ScannerError.problem, file=sys.stderr)
            print("\t - Problem's location: %s" \
                  % ScannerError.context_mark, file=sys.stderr)
            sys.exit()
        except:
            print("ERROR in XML_creator(): unknown error happened trying to yaml.safe_load() the given schema filepath '%s'." \
                  % schema_filename, file=sys.stderr)
            sys.exit()

        # We narrow the general dictionary to the one specific for our configuration key (e.g. "sample")
        try:
            self.schema_dict = self.schema_general_dict[self.schema_key]
        except:
            print("ERROR in XML_creator(): given schema file '%s' does not contain the given schema key '%s' in its first layer" \
                  % (schema_filename, self.schema_key), file=sys.stderr)
            sys.exit()

        # We check that the given input_dataframe is a dataframe (following Pandas' standards)
        if not isinstance(input_dataframe, pd.DataFrame):
            print("ERROR in XML_creator(): given dataframe was of type '%s' instead of a dataframe (%s)" \
                  % (type(input_dataframe), pd.DataFrame), file=sys.stderr)
            sys.exit()

        self.input_dataframe = input_dataframe
        # We remove empty rows (full of NaNs)
        self.input_dataframe.dropna(axis = 0, how = "all", inplace = True)

        # We store the number of rows (number of metadata object repetitions) the dataframe contains
        self.dataframe_nrows = len(self.input_dataframe.index)

    def print_basic_info(self):
        """
        Function to print some basic information about the tool, its schema file, etc.
        """
        # We store the version of the schema file (from the schema itself)
        schema_version = self.schema_general_dict[tool_info_tag][version_tag]
        schema_update_date = self.schema_general_dict[tool_info_tag][update_date_tag]
        date_now = datetime.today().isoformat()

        General_info = """\n######----------------------------######\n### Starting the XML_creator() class ###\n######----------------------------######
        General information:
          - Execution datetime: {date_now}
          - Class object's instance: {object_instance}
          - Schema filepath: {schema_filename}
          - Schema file version: {schema_version}
          - Schema file last oficial update: {schema_update_date}
          - Metadata object (schema key): {schema_key}
          - Number of rows (number of {schema_key}s) in the given dataframe: {dataframe_nrows}
          - Number of columns (attributes or text) in the given dataframe: {dataframe_ncols}
        """.format(date_now = date_now,
                   object_instance = self,
                   schema_filename = self.schema_filename,
                   schema_version = schema_version,
                   schema_update_date = schema_update_date,
                   schema_key = self.schema_key,
                   dataframe_nrows = self.dataframe_nrows,
                   dataframe_ncols = self.input_dataframe.shape[1])

        self.print_or_save_log(General_info)

    def print_or_save_log(self, string_to_print):
        """
        Function to print a string to standard output, and save into a log.file if debug_mode = True.

        Parameters:
            - string_to_print (str): string that will be printed or saved to a log file.
        """
        if self.verbose or self.debug_mode:
            print(string_to_print)

        if self.debug_mode:
            with open(self.log_filename, "a") as log_filename:
                log_filename.write(string_to_print)


    def construct_xml(self):
        """
        Function that will create an XML file based on the instance's dataframe and schema.yaml file.
        """

        # We create the root of the XML tree, and its root_tag (e.g. SAMPLE_SET) will be used as
        #     father element for its children (e.g. SAMPLE)
        self.construct_xml_root()
        father_element = self.root_tag

        # The following list will be populated with nodes that have the add_empty_node_tag. These nodes will not be removed
        #   by the prunning function, since they have a meaning by themselves, although they are empty (e.g. SINGLE in LIBRARY_LAYOUT)
        self.nodesThatNeedToBe_empty_list = []

        # We create the elements of the set (the whole XML tree).
        self.construct_xml_elements(schema_tag = self.schema_key,
                                    dict_element = self.schema_general_dict,
                                    father_element = father_element)

        # We prune empty nodes recursively
        self.prune_empty_nodes()

        if self.verbose or self.debug_mode:
            self.print_or_save_log("\n- Conversion completed! The generated XML is the following:")
            self.save_xml(to_print = True)

        self.save_xml()

    def save_xml(self, to_print = False, schema_tag = False):
        """
        Function to save the (pretty-fied) XML tree into a file. It can also be used to print it into the standard output.

        Parameters:
            - to_print (bool): if True the function prints the XML into the standard output.
                               if False the XML is saved into the output XML file.
            - schema_tag (str): a string with the schema tag, it's only used if given, and for printing.
        """
        xml_tree_toPrint = "etree.tostring(self.{}, pretty_print=True, encoding='UTF-8', xml_declaration=True).decode('UTF-8')".format(self.xml_root_tag)

        # If we only want to print the tree:
        if to_print:
            # If schema_tag was given, we add another line to ease interpretation
            if isinstance(schema_tag, str):
                print_tag = "\n____Adding the node '%s'____" % schema_tag.upper()
                self.print_or_save_log(print_tag)

            exec("self.print_or_save_log({})".format(xml_tree_toPrint))

        # If, instead, we want to save the XML tree to a file:
        else:
            # Check if output_dir where the output_xml will reside exists, create it if not
            output_dir = os.path.dirname(self.output_xml)
            dir_exists = os.path.isdir(output_dir)
            if not dir_exists and output_dir != '':
                os.makedirs(output_dir)
            try:
                with open(self.output_xml, "w") as xml_file:
                    exec("xml_file.write({})".format(xml_tree_toPrint))
            except:
                print("ERROR in XML_creator() - save_xml(): couldn not save the XML tree into the given filename '%s'" \
                  % (self.output_xml), file=sys.stderr)
                sys.exit()

    def construct_xml_root(self):
        """
        Function to construct the root of the metadata XML. It is important to bare in mind that this part
            of an XML is very specific: if the schema validator of ENA changes, this part may need to change
            accordingly.
        """

        # We store the first line of the XML file, which will contain the schema_key with "_SET", and two attributes:
        #    - xmlns:xsi                      (the schema instance, e.g. http://www.w3.org/2001/XMLSchema-instance)
        #    - xsi:noNamespaceSchemaLocation  (where the schema for that object resides, e.g. ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.sample.xsd)
        self.root_tag = (self.schema_key + "_SET").upper()
        self.xml_root_tag = "xmlVar_" + self.root_tag
        schema_instance = self.schema_general_dict["XML_schemas_info"]["schema_instance"]
        object_schema = self.schema_general_dict["XML_schemas_info"]["object_schemas"][self.schema_key]
        schema_instance_reference = self.schema_general_dict["XML_schemas_info"]["schema_instance_reference"]

        # We need to specify the namespaces of the root element. For example, the following lines added to the root:
        #     - xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        #     - xsi:noNamespaceSchemaLocation="ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.<OBJECT>.xsd"
        attributes_qname = etree.QName(schema_instance, schema_instance_reference)
        exec("self.%s = etree.Element(self.root_tag, {attributes_qname: object_schema}, nsmap = {'xsi': schema_instance})" \
             % self.xml_root_tag)

        self.print_or_save_log("- Constructed the root '{}' with variable name '{}'".format(self.root_tag, self.xml_root_tag))

    def construct_xml_elements(self, schema_tag, dict_element, father_element, is_children = False):
        """
        Function that will iterate through a given dataframe and construct a XML file with its information.
            The XML structure will be defined in a YAML file, with the given tags (e.g. for every element
            in the XML there could be some attributes, children (elements), text tags and if it's repetitive).
            Note that the field names in the dataframe shall match the values of these tags in the schema file
            for indexing purposes. E.g.:
                attributes:
                    alias: "Sample_alias"           (alias: attribute tag in the XML; Sample_alias: column header in dataframe)
                    center_name: "Center_name"      (center_name: attribute tag in the XML; Center_name: column header in dataframe)

        In the first iteration we will consider the whole dictionary for each metadata object, given its
            schema_tag (e.g. taking the whole sample schema given "sample" as schema_tag). In the subsequent
            iterations we will get deeper into the XML tree using a restricted dictionary (dict_element) of
            only one of their children (e.g. sample_name as schema_tag), until we reach a child with no more
            children elements (we reach a leaf of the XML tree).

        Parameters:
            - schema_tag (str): a string with the schema_tag (e.g. sample_name or taxon_id) used to index the dictionary.
            - dict_element (dict): dictionary element obtained loading the YAML schema file. It will have
                                   3 additional elements itself: attributes, text and children. More
                                   information about the nature of these elements can be found within
                                   the YAML schema file.
            - father_element (str): the father element's variable name. If we are iterating over children elements, their
                                    father_element will be the schema_tag of their father's element (e.g. sample_name for
                                    common_name).
            - is_children (bool): specifies if we are iterating over children elements (and thus the father element is
                                  not a common root, having to add indexes, etc.)
        """
        # We save the current step in the YAML file (dictionary) XML hierarchy
        current_level_dict = dict_element[schema_tag]

        # We save a comprobations list of the current node (i.e. if it has children, attributes, etc.)
        comprobations_list = self.each_node_comprobations(current_level_dict = current_level_dict, schema_tag = schema_tag)

        # Based on the comprobation list's content, we add the node and all of its characteristics
        self.additionOf_Node(schema_tag = schema_tag,
                             comprobations_list = comprobations_list,
                             father_element = father_element,
                             is_children = is_children)

    def additionOf_Node(self, schema_tag, comprobations_list, father_element, is_children = False):
        """
        Function that deals with the addition of a node and all of its characteristics. If the node has children,
            this function will also call construct_xml_elements() with the next level of depth in the hierarchy.

        Parameters:
            - schema_tag (str): a string with the schema_tag (e.g. sample_name or taxon_id) used to instance the node.
            - comprobations_list (list): a list of dictionaries, boolean values and strings from the YAML file, returned
                                         from executing each_node_comprobations() over the current node.
            - father_element (str): the father element's name, which will be the variable name of the father.
            - is_children (bool): specifies if we are iterating over children elements.
        """
        # We assign each variable of the comprobation list
        is_repetitive, children_elements, has_children, element_attributes, has_attributes, text_column_name, has_text, needsToBe_empty = comprobations_list

        # We use another variable to avoid overwritting the father_element (e.g. SAMPLE_SET)
        given_father_element = father_element

        # We get the number of repetitions of this node (default is 1 unless it's a repetitive node)
        n_repetitions = self.retrieve_numberOf_repetitions(comprobations_list)

        # Given the number of repetitions for this node, we add as many identical nodes (and their children)
        for repetition_index in range(int(n_repetitions)):

            # For this node (in the XML structure) we iterate through the dataframe rows and add this node for them all
            #     at the same time (i.e. all SAMPLE at once; then all TAXON_ID at once, etc.)
            for dataframe_index in range(self.dataframe_nrows):
                # This variable will be used to create the element's instance in the XML tree
                element_name = schema_tag + "_" + str(dataframe_index)

                # If we are dealing with a child's node (e.g. taxon_id_12 - 12 due to the 12th index of the dataframe),
                #     the father needs to be created using the father's tag and the dataframe index (e.g. sample_name_12).
                if is_children:
                    given_father_element = father_element + "_" + str(dataframe_index)

                # We add the node itself, with no characteristics so far
                self.add_one_node(father_element = given_father_element,
                                  element_name = element_name,
                                  schema_tag = schema_tag, 
                                  needsToBe_empty = needsToBe_empty)

                # If this node in the YAML file have attributes or text defined, we add them to the node
                if has_attributes:
                    self.set_attributes(element_name = element_name,
                                  attributes_dict = element_attributes,
                                  dataframe_index = dataframe_index)
                if has_text:
                    self.set_text(element_name = element_name,
                             column_name = text_column_name,
                             dataframe_index = dataframe_index)

            # If debug was given, we print (and write to logfile) the current step of the XML creation
            if self.debug_mode:
                self.save_xml(to_print = True, schema_tag = schema_tag)

            # If we found out this node has children nodes, we call construct_xml_elements() recursively with them
            if has_children:
                # The new "child" will be the key to the next level of depth in the dictionary (e.g. "taxon_id")
                #     while the children_elements will be the dictionary containing the "child" and their siblings.
                for child in children_elements.keys():
                    self.construct_xml_elements(schema_tag = child,
                                                dict_element = children_elements,
                                                father_element = schema_tag,
                                                is_children = True) # It's a child, so the father element has to be modified with the index.

    def retrieve_numberOf_repetitions(self, comprobations_list):
        """
        Function to retrieve how many repetitions of a repetitive node there are.

        Parameters:
            - comprobations_list (list): a list of dictionaries, boolean values and strings from the YAML file, returned
                                         from executing each_node_comprobations() over the current node.
        """
        # We assign each variable of the comprobation list
        is_repetitive, children_elements, has_children, element_attributes, has_attributes, text_column_name, has_text, needsToBe_empty = comprobations_list

        if is_repetitive:
            # If it has text/attributes, we count how many columns they have
            if has_attributes or has_text:
                n_repetitions = self.get_numberOf_fields(comprobations_list)

            # If it's a node with only children, we need to count the number of times a child attribute/text appears
            else:
                # We iterate over its children to get the number of repetitions
                n_repetitions = self.iterate_over_children(children_elements = children_elements)
        else:
            n_repetitions = 1

        return n_repetitions

    def iterate_over_children(self, children_elements):
        """
        Function to iterate over a children hierarchy to find out which has fields of attributes/text
            that will indicate how many times a repetitive node (one of its fathers) is repeated.

        Parameters:
            - children_elements (dict): dictionary of the current node and its siblings (e.g. if its father
                                        is sample_name, this dict would contain taxon_id and common_name)
        """
        # We iterate over children dictionaries to check which one has attributes/text
        for child in children_elements.keys():
            # If the children doesn't have attributes/text we skip it
            children_comprobation_list = self.each_node_comprobations(current_level_dict = children_elements[child], schema_tag = child)
            child_has_children = children_comprobation_list[2]
            child_has_attributes = children_comprobation_list[3]
            child_has_text = children_comprobation_list[6]

            # If we reached a child with attributes/text, we use it to infer the number of repetitions of its fathers
            if child_has_attributes or child_has_text:
                n_repetitions = self.get_numberOf_fields(children_comprobation_list)
                return n_repetitions

            # If this child only has other children we iterate over them to check if some have attributes/text
            elif child_has_children:
                n_repetitions = self.iterate_over_children(children_elements = children_elements[child][children_tag])
                return n_repetitions

        # If we iterated over the whole subelements and none have attributes/text, then little information is within
        #     the dataframe, and thus we only add one (empty) repetitive node
        n_repetitions = 1
        return n_repetitions

    def get_numberOf_fields(self, comprobations_list):
        """
        Function that, given a comprobation_list, retrieves the ammount of fields of a dataframe that represent
            a node's (1) text or (2) its attributes.

        Parameters:
            - comprobations_list (list): a list of dictionarioes, boolean values and strings from the YAML file, returned
                                         from executing self.each_node_comprobations() over the current node.
        """
        # We assign each variable of the comprobation list
        is_repetitive, children_elements, has_children, element_attributes, has_attributes, text_column_name, has_text, needsToBe_empty = comprobations_list

        if has_text:
            field_toLookFor = text_column_name

        elif has_attributes:
            # We take the first value of the attributes (its column name). It shouldn't matter if it's the first
            #     or not, since all of their attribute columns SHOULD be present (even if empty).
            field_toLookFor = next(iter(element_attributes.values()))

        else:
            # If the node has no attributes nor text, little information is in the df, so we only add one node (n_repetitions = 1)
            return 1

        # The following regular expression is used to get one individual block of repetition for this node. if a column
        #     is repeated in a dataframe, pandas will add an index at its end ".[0-9]*", and with this regexp we will
        #     find out how many repeated columns with this column_name are.
        regexp_field = '^{}\.?[0-9]*$'.format(field_toLookFor)

        # We save the number of fields in the df that refer to ONE repetition of this node (text or attribute)
        n_repetitions = len(self.input_dataframe.filter(regex = regexp_field, axis = 1).columns)

        if n_repetitions == 0:
            print("ERROR in XML_creator() - get_numberOf_fields(): field '%s' could not be found in the input dataframe" \
                  % field_toLookFor, file=sys.stderr)
            sys.exit()

        return n_repetitions


    def each_node_comprobations(self, current_level_dict, schema_tag = None):
        """
        Function to check the characteristics of each node from the YAML file. This function will return dictionaries,
            strings and booleans (e.g. if the node has no attributes has_attributes = False)

        Parameters:
            - current_level_dict (dict): dictionary of the current element - i.e. if we are at "sample_name"
                                         as the current node, the current_level_dict would contain up to 5
                                         additional elements: children, text, attributes, repetitive_node and add_empty_node.
            - schema_tag (str): the schema tag (e.g. sample or taxon_id) corresponding to the key of the current_level_dict.
        """
        children_elements = {}
        element_attributes = {}
        text_column_name = None

        # We first check that the current dictionary has some elements (e.g. "children" or "text")
        try:
            current_dict_set = set(current_level_dict.keys())       # e.g. {"children", "text"}
        except:
            # If the dictionary is empty, the node was left empty in the schema, and thus has no information (common mistake)
            print("ERROR in XML_creator() - each_node_comprobations(): the given schema dictionary for schema tag '%s' is empty. This reflects an error (unused node) in the configuration file '%s', check the said schema tag within it." \
                  % (schema_tag, self.schema_filename), file=sys.stderr)
            sys.exit()

        # Now we check if the keys of the current_element are (a subset of) the valid ones (children, text...)
        if not current_dict_set.issubset(valid_dict_elements):
            print("ERROR in XML_creator() - each_node_comprobations(): the given schema dictionary for schema tag '%s' contains non valid keys.\n\t - Valid keys: %s\n\t - Given keys: %s" \
                  % (schema_tag, valid_dict_elements, current_dict_set), file=sys.stderr)
            sys.exit()

        # In each step, we check for the valid keys, associating its corresponding part of the dictionary
        if children_tag in current_dict_set:
            children_elements = current_level_dict[children_tag]
            if children_elements is None:
                print("ERROR in XML_creator() - each_node_comprobations(): the given schema tag '%s' had children characteristic, but was found empty." \
                      % schema_tag, file=sys.stderr)
                sys.exit()
            has_children = True
        else:
            has_children = False

        if attribute_tag in current_dict_set:
            element_attributes = current_level_dict[attribute_tag]
            if element_attributes is None:
                print("ERROR in XML_creator() - each_node_comprobations(): the given schema tag '%s' had attributes characteristic, but was found empty." \
                      % schema_tag, file=sys.stderr)
                sys.exit()
            has_attributes = True
        else:
            has_attributes = False

        if text_tag in current_dict_set:
            text_column_name = current_level_dict[text_tag]
            if text_column_name is None:
                print("ERROR in XML_creator() - each_node_comprobations(): the given schema tag '%s' had text characteristic, but was found empty." \
                      % schema_tag, file=sys.stderr)
                sys.exit()
            has_text = True
        else:
            has_text = False

        # We check if this node is one of the repetitive ones (e.g. repetitive_node: True)
        if repetitive_tag in current_dict_set:
            is_repetitive = True
        else:
            is_repetitive = False
        
        if add_empty_node_tag in current_dict_set:
            needsToBe_empty = True
        else:
            needsToBe_empty = False

        return is_repetitive, children_elements, has_children, element_attributes, has_attributes, text_column_name, has_text, needsToBe_empty

    def add_one_node(self, father_element, element_name, schema_tag, needsToBe_empty):
        """
        Function that adds one node to the XML tree.

        Parameters:
            - father_element (str): the father element's name, which will be the variable name of the father
                                    etree.Element (a XML node) of the current node (e.g. SAMPLE_SET).
            - element_name (str): the name of the current node (e.g. sample_13)
            - schema_tag (str): the schema tag (e.g. sample or taxon_id) that is written within the YAML file.
            - needsToBe_empty (bool): a boolean that specifies if the node has a meaning by itself although
                                      being empty which, if True, will prevent from its removal (after the tree has been 
                                      created) by the prunning function. 
        """
        # We add "xmlVar" first so that no other fixed variable of this scripts coincidentally is the element_name
        # We create the pair "node name" + "father's node name" so that it's a unique identifier we use in the counter. Otherwise
        #   repeated node names (e.g. LABEL) between different father nodes would lead to errors.
        xml_node_tag = "xmlVar_" + str(element_name)
        xml_fatherNode_tag = "xmlVar_" + str(father_element)

        # Using the element's variable content (str) as a variable we create the current node
        exec("self.%s = etree.SubElement(self.%s, schema_tag.upper())" % (xml_node_tag, xml_fatherNode_tag))

        #   prunned in the future. 
        if needsToBe_empty:
            exec("self.nodesThatNeedToBe_empty_list.append(self.%s)" % xml_node_tag)
    
    def get_SameNodes_repetitions(self, xml_node_tag):
        """
        Function that will return the number of repetitions of a specific node within the XML tree. For instance, in the 
            node "ANALYSIS" with an XPath "/ANALYSIS_SET/ANALYSIS/DESCRIPTOR[3]", the function would return "3". 
        
        Parameters:
            - xml_node_tag (string): the name of the node within our function (e.g. xmlVar_DESCRIPTOR_0)
        """
        # In case we are given the node beneath the root (e.g. ANALYSIS_SET/ANALYSIS[2]), its repetition index (e.g. 2) will
        #    not come from different columns, but from different rows (different dimension), and thus we skip it if the root
        #    is its parent.
        exec('global getRepetitions_root; getRepetitions_root = self.%s.getparent()' % xml_node_tag)
        exec('global getRepetitions_equalRoots; getRepetitions_equalRoots = getRepetitions_root == self.%s' % self.xml_root_tag)

        if getRepetitions_equalRoots:   
            return 0
        
        # We use lxml.etree wrapper (ElementTree()) with the node and extract its xpath
        exec('global getRepetitions_tree; getRepetitions_tree = etree.ElementTree(self.%s)' % xml_node_tag)
        exec('global getRepetitions_xpath; getRepetitions_xpath = getRepetitions_tree.getpath(self.%s)' % xml_node_tag)
        
        modified_getRepetitions_xpath = getRepetitions_xpath

        # We parse the complete XPath to remove the repetition of a base metadata object (e.g. from /ANALYSIS_SET/ANALYSIS[1]/ANALYSIS_ATTRIBUTES/ANALYSIS_ATTRIBUTE[3]/TAG 
        #      to /ANALYSIS_ATTRIBUTES/ANALYSIS_ATTRIBUTE[3]/TAG). This is to avoid getting indexes from the base tag, or only accounting for the last tag (which would lead to errors)
        for null in range(3):
            slash_start = modified_getRepetitions_xpath.find("/")
            modified_getRepetitions_xpath = modified_getRepetitions_xpath[slash_start + 1:]

        # And now we get the repetition index from the XPath
        start = modified_getRepetitions_xpath.rfind("[")
        end = modified_getRepetitions_xpath.rfind("]")
        
        # If "[" was not found within the last part of the XPath, we return a 0
        if start == -1:
            return 0
        
        # If we did find an index (e.g. [2]) we return such index (e.g. 2), which will be used as index in the dataframe
        repetition_index = modified_getRepetitions_xpath[start + 1 : end]    
        
        return int(repetition_index)
        

    def set_attributes(self, element_name, attributes_dict, dataframe_index):
        """
        Function to set the attributes of an XML node.

        Parameters:
            - element_name (str): the name of the current node (e.g. sample_13)
            - attributes_dict (dict): dictionary containing the attribute names (keys) and their corresponding
                                      column names in the dataframe.
                                      (e.g. {'alias': 'Sample_ID', 'center_name': 'center_name'})
            - dataframe_index (int): the index of the dataframe (e.g. 13), which represents the row of the df
                                     (i.e. the repetition of a metadata object)
        """
        # We create the pair "node name" + "father's node name" so that it's a unique identifier we use in the counter. Otherwise
        #   repeated node names (e.g. LABEL) between different father nodes would lead to errors.
        xml_node_tag = "xmlVar_" + str(element_name)

        # Here we add a ".X" to every value (which represents the field of the dataframe to search for the attribute)
        #     of the attributes dictionary, since every subsequent repeated column in the dataframe will have ".X"
        #     where X is the times that same node is repeated across the XML (minus 1, since it starts at 0).
        # Except the first index, which will not be ".0" but the column name itself.
        repetitions = self.get_SameNodes_repetitions(xml_node_tag)
        if repetitions > 0:
            attributes_dict = {k: v+'.{}'.format(repetitions - 1) for k, v in attributes_dict.items()}

        # We iterate over the different attributes of this node:
        for attribute_name, column_name in attributes_dict.items():
            attribute_value = self.input_dataframe[column_name][dataframe_index]
            # If the value in the dataframe is empty, NaN, None or only contains white spaces we skip adding this attribute
            if (not attribute_value and attribute_value != 0) or attribute_value is None or pd.isnull(attribute_value) or str.isspace(str(attribute_value)):
                continue
            exec("self.%s.set('''%s''','''%s''')" % (xml_node_tag, str(attribute_name), str(attribute_value)))

    def set_text(self, element_name, column_name, dataframe_index):
        """
        Function to set the text of an XML node.

        Parameters:
            - element_name (str): the name of the current node (e.g. title_13)
            - column_name (str): the name of the column of the dataframe where the text is stored (e.g. Title_text)
            - dataframe_index (int): the index of the dataframe (e.g. 13), which represents the row of the df
                                     (i.e. the repetition of a metadata object)
        """
        # We create the pair "node name" + "father's node name" so that it's a unique identifier we use in the counter. Otherwise
        #   repeated node names (e.g. LABEL) between different father nodes would lead to errors.
        xml_node_tag = "xmlVar_" + str(element_name)

        # We add ".X" at the end of the column name, just like with the attributes           
        repetitions = self.get_SameNodes_repetitions(xml_node_tag)
        if repetitions > 0:
            column_name = column_name + '.{}'.format(repetitions - 1)

        # We extract the node's text from the dataframe
        nodes_text = self.input_dataframe[column_name][dataframe_index]

        # If the value in the dataframe is empty, NaN, None or only contains white spaces we skip setting its text
        if (not nodes_text and nodes_text != 0) or nodes_text is None or pd.isnull(nodes_text) or str.isspace(str(nodes_text)):
            return

        exec("self.%s.text = '''%s'''" % (xml_node_tag, str(nodes_text)))

    def prune_empty_nodes(self, empty_list = None):
        """
        Function that removes empty nodes (with no attributes, no children and no text) of an XML tree recursively.
            Why prune instead of avoid adding empty nodes? Because we don't know if they are empty until we have filled
            the XML tree.
        
        Parameters:
            - empty_list (list): list of empty nodes (of class etree.Element) that needs to be removed from the tree. If
                                 no list is passed, the function gets such list by itself. 
        """        
        if not empty_list:
            # Using XPATH we save a list of the empty nodes ('not(node())') with no attributes ('not(@*)')
            exec("self.empty_nodes_list = self.%s.xpath('.//*[not(@*) and not(node())]')" % self.xml_root_tag)
            
            # We remove from the empty_nodes_list all the nodes that have to be left empty and hold a meaning like that. 
            self.empty_nodes_list = self.remove_betweenLists(self.empty_nodes_list, self.nodesThatNeedToBe_empty_list)
            
        else:
            self.empty_nodes_list = empty_list        
        
        # We iterate over the list and remove empty nodes
        for empty_element in self.empty_nodes_list:
            empty_element.getparent().remove(empty_element)

        # If, after pruning, new nodes are left empty, we prune again
        exec("self.new_empty_nodes_list = self.%s.xpath('.//*[not(@*) and not(node())]')" % self.xml_root_tag)
        # Bare in mind that we again remove all nodes that have to be left empty from the list of nodes to prune
        self.new_empty_nodes_list = self.remove_betweenLists(self.new_empty_nodes_list, self.nodesThatNeedToBe_empty_list)
        
        if self.new_empty_nodes_list:
            self.prune_empty_nodes(empty_list = self.new_empty_nodes_list)
    
    def remove_betweenLists(self, first_list, sublist):
        """
        Function that will remove all elements from a sublist that are in a bigger list (first_list). 
        """
        return list(set(first_list)-set(sublist))