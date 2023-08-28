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
    if total:
        print(f"Total price: ${total}")
    else:
        print("Invalid total price. Cart may be empty!")

cart = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}
]

for item in cart:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = calculate_total(cart)
display_total(shopping_cart_total)