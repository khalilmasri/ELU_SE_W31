def calculate_total(cart):
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

CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)

