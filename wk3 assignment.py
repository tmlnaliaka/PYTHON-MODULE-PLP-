"""
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to be applied.

    Returns:
        float: The final price after the discount is applied, or the original price
               if the discount is less than 20%.
    """

def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user to enter the original price
try:
    original_price_str = input("Enter the original price of the item: ")
    original_price = float(original_price_str)
except ValueError:
    print("Invalid input. Please enter a valid number for the price.")
    exit()

# Prompt the user to enter the discount percentage
try:
    discount_percent_str = input("Enter the discount percentage (e.g., 10 for 10%): ")
    discount_percent = float(discount_percent_str)
except ValueError:
    print("Invalid input. Please enter a valid number for the discount percentage.")
    exit()

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
if final_price < original_price:
    print(f"Discount applied! The final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {final_price:.2f}")