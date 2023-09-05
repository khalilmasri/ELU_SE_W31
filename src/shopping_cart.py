"""
Shopping Cart

This script provides functionality for managing a shopping cart. It includes functions
for calculating the total price of items in the cart and displaying the cart's contents.

Functions:
    - calculate_total(cart): Calculate the total price of items in the cart.
    - display_total(total): Display the total price of items in the cart.
"""

def calculate_total(cart):
    """
    Calculate the total price of items in the cart.
    Parameters:
    cart (list): List of dictionaries representing items in the cart.
    Returns:
    float: Total price of all items.
    """
    total = 0
    for item in cart:
        if 'price' in item and isinstance(item['price'], (int, float)):
            total += item['price']
        else:
            print(f"Invalid price for item {item.get('name')}")
    return total

def display_total(total):
    """
    Display items in the cart with their names and prices.
    Parameters:
    cart (list): List of dictionaries representing items in the cart.
    """
    if total:
        print(f"Total price: ${total}")
    else:
        print("Invalid total price. Cart may be empty!")


if __name__ == '__main__':
    shopping_cart = [
        {'name': 'Item A', 'price': 10.99},
        {'name': 'Item B', 'price': 5.99},
        {'name': 'Item C', 'price': 8.49}
    ]

    for cart_item in shopping_cart:
        print(f"Item: {cart_item['name']} - Price: ${cart_item['price']}")

    shopping_cart_total = calculate_total(shopping_cart)

    display_total(shopping_cart_total)
