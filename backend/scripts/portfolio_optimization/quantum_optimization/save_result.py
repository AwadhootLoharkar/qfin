import os
import csv

def save_result(file_name, result):
    try:
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
    
    except Exception as e:
        print(f"Error encountered while saving result: {e}")

def save_multiple_results(file_name, all_results):
  try:
    # Define the output directory
    output_dir = '../output'

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define the full path to the file
    file_path = os.path.join(output_dir, file_name)

    # Check if file exists
    file_exists = os.path.isfile(file_path)
    
     # Get the fieldnames from the dictionary keys
    fieldnames = all_results[0].keys()

    with open(file_path, 'a', newline='') as csvfile:
        # Create a DictWriter object
        dict_writer = csv.DictWriter(csvfile, fieldnames)
        
        # If the file doesn't exist, write the header
        if not file_exists:
            dict_writer.writeheader()
            
        # Write the dictionary data
        dict_writer.writerows(all_results)

  except Exception as e:
    print(f"Error encountered while saving result: {e}")
