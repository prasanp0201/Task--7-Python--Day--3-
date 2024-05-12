#Write a python program using function to which will do the following: 1. the function will create a text file with current timestamp, 2. the file content should have the content of the current timestamp

from datetime import datetime

def create_file_with_timestamp_content():
    # Get the current timestamp
    current_time = datetime.now()
    
    # Format the timestamp as a string
    timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create a file with the timestamp as its name
    file_name = f"timestamp_{timestamp_str}.txt"
    with open(file_name, 'w') as file:
        # Write the content of the timestamp into the file
        file.write(timestamp_str)
    
    print(f"File '{file_name}' created with timestamp content.")

# Call the function to create the file
create_file_with_timestamp_content()