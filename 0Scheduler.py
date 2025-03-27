import os
import glob

def get_latest_report_csv(folder_path):
    # Construct the search pattern
    pattern = os.path.join(folder_path, 'report*.csv')
    
    # Get all matching files
    files = glob.glob(pattern)
    
    # If no files found, return None
    if not files:
        return None
    
    # Sort the files by modified time and return the latest one
    latest_file = max(files, key=os.path.getmtime)
    
    return latest_file

# Example usage
folder_path = '/path/to/your/folder'
latest_file = get_latest_report_csv(folder_path)

if latest_file:
    print("Latest report file:", latest_file)
else:
    print("No report CSV files found.")