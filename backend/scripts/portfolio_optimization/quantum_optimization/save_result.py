import os
import csv

def save_result(file_name, result):
    # Define the output directory
    output_dir = '../output'

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define the full path to the file
    file_path = os.path.join(output_dir, file_name)
    
    # Check if file exists
    file_exists = os.path.isfile(file_path)
    
    # Open the file in append mode
    with open(file_path, 'a', newline='') as csvfile:
        # Get the fieldnames from the dictionary keys
        fieldnames = result.keys()

        # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file doesn't exist, write the header
        if not file_exists:
            writer.writeheader()

        # Write the dictionary data
        writer.writerow(result)
