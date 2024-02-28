import os
import csv
import requests
import sys
import datetime

def post_to_erpnext(item_data):
    # Your existing post_to_erpnext function code here...
    api_endpoint = 'http://192.168.0.58:8000/api/resource/Item'

    # Replace 'YOUR_ERP_NEXT_API_KEY' with your API key or other authentication method
    headers = {'Authorization': 'Bearer 36378cc91a2561b:db8d3143c5c9e6f'}

    # Prepare data for the POST request
    data = {
        'doctype': 'Item',
        'Item Code': item_data['Item Code'],
        'Item Name': item_data['Item Name'],
        'Default Unit of Measure' : item_data['Default Unit of Measure'],
        # Add other fields as needed
    }

    # Make the POST request
    response = requests.post(api_endpoint, headers=headers, json={'data': [data]})

    # Check the response status
    if response.status_code == 200:
        print(f"Item '{item_data['Item Code']}' posted successfully.")
    else:
        print(f"Failed to post item '{item_data['Item Code']}': {response.text}")

def process_csv(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            post_to_erpnext(row)

if __name__ == "__main__":
    csv_file_path = os.getenv('CSV_FILE_PATH')
    
    if csv_file_path is None:
        print("No CSV file found. Exiting.")
        sys.exit(0)

    try:
        process_csv(csv_file_path)
        print(f"Processing completed successfully for CSV file: {csv_file_path}")
    except Exception as e:
        print(f"Error during processing: {e}")

        # Log the error to a file
        log_file_path = 'error_log.txt'
        with open(log_file_path, 'a') as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - Error processing CSV file '{csv_file_path}': {str(e)}\n")
        
        sys.exit(1)