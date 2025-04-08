# Importing necessary modules
import os

def modify_content(content):
    """
    Function to modify the content of the file.
    For example, this function converts all text to uppercase.
    You can customize it as needed.
    """
    return content.upper()  # Converts the text to uppercase

def read_and_modify_file():
    """
    This function reads a file provided by the user,
    modifies its content, and writes the modified content to a new file.
    It also includes error handling for common file operation errors.
    """
    try:
        # Prompt user for the input filename
        input_filename = input("Enter the filename to read from (with extension): ")
        
        # Check if the file exists
        if not os.path.isfile(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")
        
        # Open the file for reading
        with open(input_filename, 'r') as file:
            content = file.read()  # Read the entire file content
            
        # Modify the content using a custom function
        modified_content = modify_content(content)
        
        # Specify the output filename
        output_filename = f"modified_{input_filename}"
        
        # Open the output file for writing
        with open(output_filename, 'w') as file:
            file.write(modified_content)  # Write the modified content
            
        # Inform the user of success
        print(f"Modified content has been written to '{output_filename}' successfully!")
    
    except FileNotFoundError as e:
        # Handle the case where the file does not exist
        print(f"Error: {e}")
    except IOError as e:
        # Handle input/output errors
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        # Catch-all for any other exceptions
        print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    print("Welcome to the File Read & Write Program!")
    print("This program reads a file, modifies its content, and writes it to a new file.")
    print("Let's get started!")
    read_and_modify_file()
