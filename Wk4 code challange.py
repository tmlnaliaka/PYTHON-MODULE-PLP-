def process_file():
    """
    Reads the contents of 'input.txt', counts the number of words,
    converts the text to uppercase, and writes the processed text
    and word count to 'output.txt'.
    """
    try:
        # Step 1: Read the contents of input.txt
        input_filename = "input.txt"
        with open(input_filename, 'r') as input_file:
            content = input_file.read()  # Read all text from the file
        
        # Step 2: Process the content
        # Convert text to uppercase
        processed_text = content.upper()
        # Count the number of words
        word_count = len(content.split())
        
        # Step 3: Write the processed text and word count to output.txt
        output_filename = "output.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write("Processed Text:\n")
            output_file.write(processed_text + "\n")
            output_file.write(f"\nWord Count: {word_count}\n")
        
        # Step 4: Print success message
        print(f"Success! Processed content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        # Error handling if input.txt does not exist
        print(f"Error: '{input_filename}' does not exist. Please create the file with some text.")
    except IOError as e:
        # Handle other I/O errors
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        # Catch-all for any other exceptions
        print(f"An unexpected error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    print("File Processing Challenge 🖋️")
    process_file()
