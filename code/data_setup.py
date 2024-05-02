"""
Script Name: Email Processing Script
Description: This script downloads the Enron email dataset, extracts it, processes the email files to extract metadata,
             and stores the results in a Parquet file. This is used for data analysis purposes.
Author: Ryan Simpson
Date: April 26, 2024
Version: 1.0
License: MIT License
"""

import os
from os import walk
import pandas as pd
import subprocess

# Define the paths used in the script.
ROOT_PATH = '/project/'
DATA_PATH = ROOT_PATH + 'data/'
DOWNLOAD_PATH = DATA_PATH + 'downloads/'
XML_PATH = '/project/data/maildir/'
PARQUET_FOLDER = DATA_PATH + 'enron_extracted/'
DATA_URL = 'https://www.cs.cmu.edu/~enron/'
DATA_FILENAME = 'enron_mail_20150507.tar.gz'
OUTPUT_FILENAME = PARQUET_FOLDER + "email_data.parquet"

# Helper function to extract email metadata from a file.
def get_email_meta(file_path):
    try:
        with open(file_path) as file:
            # Initialize flags and variables to capture email metadata.
            is_reply_forward = False
            header = True
            date = ""
            from_address = ""
            to_address = ""
            org_filename = ""
            message = ""

            # Read all lines from the file and strip trailing whitespace.
            lines = [line.rstrip() for line in file]

            for line in lines:
                if line.startswith("Message-ID: "):
                    message_id = line.replace("Message-ID: ", "")
                if not is_reply_forward:
                    if line.startswith("Date: "):
                        date = line.replace("Date: ", "")
                        continue
                    if line.startswith("From: "):
                        from_address = line.replace("From: ", "")
                        continue
                    if line.startswith("To: "):
                        to_address = line.replace("To: ", "")
                        continue
                    if line.startswith("X-FileName: "):
                        org_filename = line.replace("X-FileName: ", "")
                        header = False
                        continue
                    if "Original Message" in line:
                        is_reply_forward = True
                        continue
                    if not header:
                        message += "\n" + line
                        continue

        return {
            'file_path': [file_path],
            'message_id': [message_id],
            'date': [date],
            'from_address': [from_address],
            'to_address': [to_address],
            'org_filename': [org_filename],
            'is_reply_forward': [is_reply_forward],
            'message': [message]
}
    except UnicodeDecodeError:
        # Return a dictionary indicating a file that could not be processed due to encoding issues.
        return {
            'file_path': [file_path],
            'message_id': ["BAD_FILE"],
            'date': ["BAD_FILE"],
            'from_address': ["BAD_FILE"],
            'to_address': ["BAD_FILE"],
            'org_filename': ["BAD_FILE"],
            'is_reply_forward': [True],
            'message': ["BAD_FILE"]}

def setup_dataset(): 
    # Ensure the download directory exists, create if not.
    if not os.path.exists(DOWNLOAD_PATH):
        print("Download path does not exist. Creating it now..")
        os.makedirs(DOWNLOAD_PATH)

    # Ensure the data directory exists, create if not.
    if not os.path.exists(DATA_PATH):
        print("Data path does not exist. Creating it now..")
        os.makedirs(DATA_PATH)

    # Download the dataset using wget command-line utility.
    #!wget $DATA_URL$DATA_FILENAME -P $DOWNLOAD_PATH
    
    data_url = DATA_URL + DATA_FILENAME
    compressed_filename = os.path.join(DOWNLOAD_PATH, DATA_FILENAME)

    if os.path.isfile(compressed_filename):
        print("Tar file exists.")
    else:
        print("Downloading data. This may take several minutes.")
        subprocess.run(["wget", data_url, "-P", DOWNLOAD_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("Raw data downloaded.")

    # Extract the downloaded dataset.
    #!tar -xf $DOWNLOAD_PATH$DATA_FILENAME -C $DATA_PATH
    
    print(f"Extracting dataset from: {compressed_filename}")
    subprocess.run(["tar", "-xf", compressed_filename , "-C", DATA_PATH], check=True)
    print("Extraction complete")

    # Collect all file paths in the XML directory.
    files = []
    for r, d, f in os.walk(XML_PATH):
        for file in f:
            files.append(os.path.join(r, file))

    print("{} email files found.".format(len(files)))

    print("Creating parquet file from data.")
    # Create a DataFrame from the extracted email metadata.
    df = pd.concat([pd.DataFrame(get_email_meta(files[i])) for i in range(len(files))])

    # Ensure the output directory exists, create if not.
    if not os.path.exists(PARQUET_FOLDER):
        print("Output path does not exist. Creating it now..")
        os.makedirs(PARQUET_FOLDER)

    # Save the DataFrame to a Parquet file.
    df.to_parquet(OUTPUT_FILENAME)

if __name__ == "__main__":
    setup_dataset()
