# Task 1: Accept user input to create a list of integers and compute their sum
# Prompt the user to enter integers separated by spaces
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
# Calculate and print the sum of all numbers in the list
print("Sum of numbers:", sum(numbers))

# Task 2: Tuple of favorite books and print each one
# Define a tuple containing five favorite book names
favorite_books = ("Book 1", "Book 2", "Book 3", "Book 4", "Book 5")

# Print a heading
print("\nFavorite Books:")

# Iterate through the tuple and print each book name on a separate line
for book in favorite_books:
    print(book[5])

# Task 3: Dictionary to store information about a person
# Create an empty dictionary and store user input for name, age, and favorite color
person = {
    "name": input("\nEnter your name: "),  # Store user's name as a string
    "age": int(input("Enter your age: ")),  # Convert user's input into an integer
    "favorite_color": input("Enter your favorite color: ")  # Store favorite color as a string
}

# Print the entire dictionary to display the stored information
print("\nPerson Information:", person)

# Task 4: Accept user input to create two sets of integers and find the common elements
# Prompt the user to enter integers for the first set, split input into individual numbers, convert them to integers, and store in a set
set1 = set(map(int, input("\nEnter integers for Set 1 separated by spaces: ").split()))

# Repeat the process for the second set
set2 = set(map(int, input("Enter integers for Set 2 separated by spaces: ").split()))

# Find the intersection (common elements) between the two sets
common_elements = set1.intersection(set2)

# Print the set of common elements
print("Common elements:", common_elements)

# Task 5: List comprehension to filter words with an odd number of characters
# Define a list of words
words = ["apple", "banana", "cherry", "grape", "mango"]

# Use list comprehension to filter words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 == 1]

# Print the words that have an odd number of characters
print("\nWords with an odd number of characters:", odd_length_words)
