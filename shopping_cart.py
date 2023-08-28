def CalculateTotal(cart):
    total = 0
    total_items = len(cart)
    for item in cart:
        total += item['price']
    return total

def display_total(total):
    print("Total price: " + total)

CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = CalculateTotal(CART)
display_total(shopping_cart_total)

