import pandas as pd
import requests
import os

folder_name = "ts_rc_back"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

df = pd.read_csv("TS_Drivers_RC_Back (1).csv")

links = df['document_url']

for idx, link in enumerate(links):
    if isinstance(link, str) and link.startswith('http'):
        response = requests.get(link)
        if response.status_code == 200:
            file_name = f"document_{idx}.jpeg"
            file_path = os.path.join(folder_name, file_name)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"File {file_name} downloaded successfully.")
        else:
            print(f"Failed to download file from {link}")
    else:
        print(f"Issue with link at index {idx}: {link}")

print("All files downloaded and saved in the 'drivers_license' folder.")

