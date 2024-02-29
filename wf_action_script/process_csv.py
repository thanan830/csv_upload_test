import os
import csv
import requests
import sys
import datetime

BATCH_SIZE = 10  # Adjust the batch size as needed

def post_to_erpnext(items):
    # Your existing post_to_erpnext function code here...
    api_endpoint = 'https://rangsutra-test-v14.frappe.cloud/api/resource/Item'

    # Replace 'YOUR_ERP_NEXT_API_KEY' with your API key or other authentication method
    headers = {'Authorization': 'token 36378cc91a2561b:63cef04404341a9',
               'Content-Type': 'application/json',
               'Accept': 'application/json',}

    # Prepare data for the POST request
    data = {'data': items}

    try:
        # Make the POST request
        response = requests.post(api_endpoint, headers=headers, json=data)

        # Check the response status
        response.raise_for_status()

        if response.status_code == 200:
            print(f"Items posted successfully.")
        else:
            handle_server_error(response)

    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 401:
            log_error("Unauthorized access. Check API key and permissions.")
        else:
            log_error(f"HTTP error during post request: {str(http_err + data)}")
    except requests.exceptions.RequestException as e:
        log_error(f"Error during post requests: {str(e)}")

def handle_server_error(response):
    if response.status_code == 500:
        error_message = "Internal Server Error. Check ERPNext server logs for details."
        log_error(error_message)
        log_error(f"Server Response: {response.text}")  # Log the full response content
    else:
        log_error(f"Failed to post items: {response.text}")

def log_error(error_message):
    # Log the error to a file
    log_file_path = 'error_log.txt'
    with open(log_file_path, 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - {error_message}\n")
        
    print(f"Error: {error_message}")

def process_csv(csv_file_path):
    items = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            item_data = {
                #'doctype': 'Item',
                'item_code': row['Item Code'],
                'item_name': row['Item Name'],
                'stock_uom': row['Default Unit of Measure'],
                'gst_hsn_code':row['HSN/SAC'],
                'description':row['Description'],
                'item_group':row['Item Group'],
                # Add other fields as needed
            }
            items.append(item_data)

            if len(items) >= BATCH_SIZE:
                post_to_erpnext(items)
                items = []

    # Post any remaining items
    if items:
        post_to_erpnext(items)

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
        log_error(f"Error during processing: {str(e)}")
        sys.exit(1)
