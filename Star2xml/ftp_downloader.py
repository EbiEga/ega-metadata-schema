import sys
from ftplib import FTP
import os

def download_files_ftp(download_directory, server = "ftp.ebi.ac.uk", username = "", password = "", output_dir = "downloaded_schemas", file_extension = ""):
    """
    Function to download a all files within a FTP server (and its download_directory) that fit into a specified file extension.

    Parameters:
        - server (str): FTP server to which the function will connect to (e.g. 'ftp.ebi.ac.uk')
        - username (str): username to log in the server (e.g. ebi_test)
        - password (str): password to log in the server (e.g. Xdw24)
        - output_dir (str): directory path to store the downloaded files (e.g.'path/to/dir/').
        - download_directory (str): directory where the files to download reside within the server (e.g. 'path/to/dir')
        - file_extension (str): file extension of the files to download (e.g. "xsd"). If empty, all files are downloaded.

    Dependencies:
        - ftplib
        - os.path
    """
    # We connect to the FTP server (using credentials if given)
    ftp = FTP(server, username, password)
    try:
        ftp.login()
    except:
        print("ERROR in ftp_downloader.py - download_files_ftp(): could not login into the given server '%s'" % server, file=sys.stderr)
        sys.exit()

    # Check if output_dir exists, create it if not
    dir_exists = os.path.isdir(output_dir)
    if not dir_exists and output_dir != '':
        os.makedirs(output_dir)

    # Change to the directory that contains the files to download and list them
    try:
        ftp.cwd(download_directory)
    except:
        print("ERROR in download_files_ftp(): could not change directories to the given one '%s'" % download_directory, file=sys.stderr)
        sys.exit()

    try:
        files = ftp.nlst()
    except:
        print("ERROR in download_files_ftp(): could not list the files in the given directory '%s'" % download_directory, file=sys.stderr)
        sys.exit()

    # We iterate over the filenames, check their extensions and download them if they fit into the given one
    for filename in files:
        extension = os.path.splitext(filename)[1]
        filename_path = os.path.join(output_dir, filename)

        # If the file extension is not the correct one or the file already exists in the download directory
        if file_extension not in extension or os.path.isfile(filename_path):
            continue

        with open(filename_path, 'wb') as f:
            ftp.retrbinary('RETR ' + filename, f.write)
