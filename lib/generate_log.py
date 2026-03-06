import os
import requests
from datetime import datetime

def generate_log(log_data):
    """
    Writes a list of log entries to a timestamped file.
    
    Args:
        log_data (list): A list of strings representing log entries.
        
    Returns:
        str: The name of the generated log file.
    """
    # Raise ValueError if input is not a list
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list of log entries.")

    # Format the filename with today's date
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    # Write data to the log file (File I/O)
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # Print confirmation message
    print(f"Log written to {filename}")

    return filename

def fetch_data():
    """Fetches sample data using the external 'requests' library."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json()
    except requests.RequestException as e:
        print(f"Network error occurred: {e}")
    return {}

# Modular execution block
if __name__ == "__main__":
    print("Executing script from command line...")
    
    # Use third-party package to collect data
    post = fetch_data()
    post_title = post.get("title", "No title found")
    
    # Create log entries combining static text and fetched data
    daily_logs = [
        "System automation started.",
        f"Successfully fetched API post title: '{post_title}'",
        "System automation finished without errors."
    ]
    
    # Generate the log file
    log_file = generate_log(daily_logs)