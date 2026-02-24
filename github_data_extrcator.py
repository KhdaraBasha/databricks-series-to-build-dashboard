"""
DATA EXTRACTION PIPELINE FROM GITHUB
"""

# List of modules to perform data extraction

import os
from dotenv import load_dotenv
from utility.extractors import csv_files_data_extract, json_files_data_extract

# Load environment variables from .env file
load_dotenv('.config')  # Change to your .env file name if needed

# Access environment variables
baseurl = os.getenv('url')

# DECLARE LIST OF FILES
# List of CSV Files
csv_files = [
    "Emissions_Data_2023.csv",
    "customerscsv.csv",
    "orderscsv.csv",
    "productscsv.csv"
]

# List of JSON Files
json_files = [
    "customersjson.json",
    "ordersjson.json",
    "productsjson.json"
]

# CREATE A MAIN FUNCTION TO RUN THE PIPELINE
if __name__ == "__main__":
    # Create the 'extracted_data' directory if it doesn't exist
    if not os.path.exists('extracted_data'):
        os.makedirs('extracted_data')
    # Extract CSV files
    for file in csv_files:
        csv_files_data_extract(file, baseurl)
    # Extract JSON files
    for file in json_files:
        json_files_data_extract(file, baseurl)
