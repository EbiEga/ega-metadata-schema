import sys
import os
from requests import get

def download_files_git(output_dir, raw_file_url_list, file_extension = ".xsd"):
    """
    Function that will dump the contents of each URL within the given URL list into their corresponding file based
        on the filenames list and the output directory.
        
    Parameters:
        - output_dir (string): relative or absolute output directory where the "downloaded" files will be saved.
        - raw_file_url_list (list of strings): list of raw URLs to download into the output_dir. 
                                               example:
                                                   [https://raw.githubusercontent.com/enasequence/schema/master/src/main/resources/uk/ac/ebi/ena/sra/schema/EGA.dac.xsd]
        - file_extension (string): file extension of the files you need to download, by default ".xsd" (XML schemas)
    """
    # Check if output_dir exists, create it if not.
    dir_exists = os.path.isdir(output_dir)
    if not dir_exists and output_dir != '':
        os.makedirs(output_dir)
    
    if not isinstance(raw_file_url_list, list):
        print("ERROR in git_downloader.py - download_files_git(): the given list of URLs to download was not of type list.\n\t- Given URLs: %s" \
                % raw_file_url_list, file=sys.stderr)
        sys.exit()

    for raw_file_url in raw_file_url_list:
        # We extract the basename (and its extension) of the file based on the URL
        filename = os.path.basename(raw_file_url)
        extension = os.path.splitext(filename)[1]
        # We construct its final filepath with the given name and output directory
        filename_path = os.path.join(output_dir, filename)
        
        # If the extension does not match the required one or the file already exists, we skip this file
        if not extension == file_extension or os.path.isfile(filename_path):
            continue       
        
        # We "get" the request object with the given URL
        response = get(raw_file_url)

        # We make sure that the response was affirmative (status code = 200)
        if response.status_code != 200:
            print("ERROR in git_downloader.py - download_files_git(): encountered an issue when requesting URL prior download of its content.\n\t- Filename: %s\n\t- URL: %s" \
                    % (filename, raw_file_url), file=sys.stderr)
            sys.exit()

        # We open the file in binary mode to dump the response content within it (i.e. write its text)
        with open(filename_path, "wb") as file:
            # write to file
            file.write(response.content)