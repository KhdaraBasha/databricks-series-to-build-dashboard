import pandas as pd
import requests
import io
import os


# Function to extract CSV files from a remote GitHub repository and save locally
def csv_files_data_extract(file_name: str, baseurl: str):
    """
    Downloads a CSV file from a given base URL and saves it to the extracted_data directory.
    Args:
        file_name (str): Name of the CSV file to download (e.g., 'customerscsv.csv').
        baseurl (str): Base URL where the files are hosted.
    Returns:
        None
    """
    url = baseurl + file_name  # Construct the full URL
    response = requests.get(url)  # Download the file
    response.raise_for_status()  # Raise error if download fails
    print(f"Extracting data from {file_name}...")
    if response.status_code == 200:
        # Read CSV content into a DataFrame
        df = pd.read_csv(io.StringIO(response.text))
        print(f"Data from {file_name} extracted successfully!")
        name = file_name.replace(".csv", "")
        # Save DataFrame to local CSV
        df.to_csv(f"extracted_data/{name}.csv", index=False)
        print(f"✅ Loaded {file_name} — {df.shape[0]} rows, {df.shape[1]} cols")


# Function to extract JSON files from a remote GitHub repository and save locally
def json_files_data_extract(file_name: str, baseurl: str):
    """
    Downloads a JSON file from a given base URL and saves it to the extracted_data directory.
    Args:
        file_name (str): Name of the JSON file to download (e.g., 'customersjson.json').
        baseurl (str): Base URL where the files are hosted.
    Returns:
        pd.DataFrame: DataFrame created from the JSON data.
    """
    url = baseurl + file_name  # Construct the full URL
    response = requests.get(url)  # Download the file
    response.raise_for_status()  # Raise error if download fails
    print(f"Extracting data from {file_name}...")
    if response.status_code == 200:
        # Parse JSON content into a DataFrame
        json_data = response.json()
        df = pd.DataFrame(json_data)
        print(f"Data from {file_name} extracted successfully!")
        name = file_name.replace(".json", "")
        # Save DataFrame to local JSON
        df.to_json(f"extracted_data/{name}.json", orient='records', indent=2)
        print(f"✅ Loaded {file_name} — {df.shape[0]} rows, {df.shape[1]} cols")
        return df
