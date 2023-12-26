import os
import requests
import pandas as pd
from urllib.parse import urlparse

def download_and_save_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def process_csv_file(csv_path, output_directory):
    df = pd.read_csv(csv_path)

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    for index, row in df.iterrows():
        document_url = row['document_url']
        vehicle_mynid = row['vehicle_mynid']
        document_type = row['document_type']

        # Parse the filename from the URL
        parsed_url = urlparse(document_url)
        filename = os.path.basename(parsed_url.path)

        # Save the file in the specified directory with the desired name (without file extension)
        new_filename = f"{vehicle_mynid}_{document_type}"
        output_path = os.path.join(output_directory, new_filename)
        download_and_save_file(document_url, output_path)

if __name__ == "__main__":
    csv_path = "/home/sree/download_script_for_drivers_RC/Drivers_driving_license.csv"  
    output_directory = "dl_k"  
    process_csv_file(csv_path, output_directory)
