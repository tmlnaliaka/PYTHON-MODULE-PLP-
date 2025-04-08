# WEEK 3 CODE CHALLANGE QUESTIONS ON FUNCTIONS
#QUESTION 1: Large Power
 
"""
    Checks if the result of raising a base to an exponent is greater than 5000.

    Args:
        base: The base number.
        exponent: The exponent to raise the base to.

    Returns:
        True if base raised to the power of exponent is greater than 5000,
        False otherwise.
    """
def large_power(base, exponent):
    # Calculate the result of raising the base to the exponent
    result = float(base ** exponent)
    # Output the computed remainder.
    print(f"The result of {base} ^ {exponent} is: {result:.0f}")
    # Check if the result is greater than 5000 using an if statement.
    if result > 5000:
        return True
    else:
        return False

# Enable user to input values for large_power
user_base = float(input("Enter the base number: "))
user_exponent = float(input("Enter the exponent: "))
print(f"Is {user_base} raised to the power of {user_exponent} greater than 5000? {large_power(user_base, user_exponent)}")


#QUESTION 2: Divisible By Ten
"""
    Checks if a given number is divisible by 10.

    Args:
        num (int): The integer number to check.

    Returns:
        bool: True if the number is divisible by 10, False otherwise.
    """

def divisible_by_10(num):
    # Calculate the remainder when the number is divided by 10
    remainder = num % 10
    # Output the computed remainder.
    print(f"The remainder of {num} divided by 10 is {remainder}")
    # Check if the remainder is 0
    if remainder == 0:
        return True
    else:
        return False

# Enable user to input value for divisible_by_10
user_number = int(input("Enter an integer to check for divisibility by 10: "))
print(f"Is {user_number} divisible by 10? {divisible_by_10(user_number)}")
