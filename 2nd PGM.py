#Write another python function to read from a text file. The function will take the name of the text file and display the content of the file into the console

def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print("Content of the file:")
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
file_name = "Samplefile.txt"  # Replace with the actual file name
read_text_file(file_name)