##############################
### Sports Ordering System ###
##############################

# This sports ordering system is designed for telemarketers to take customer orders for sports equipment. 
# It collects customer information, validates inputs, and processes orders efficiently.
# The program uses advanced programming techniques such as functions, loops, 
# and validation to ensure a smooth ordering experience.


# Nested dictionary stores product categories, item names, and prices.
# This avoids hardcoding products throughout the program and makes it easy to update.

sports_inventory = {
    "Clothing": {
        "Running Shirt": 30,
        "Sweatpants": 50,
        "Compression Shorts": 25
    },

    "Shoes": {
        "ASICS Running Shoes": 80,
        "Nike Casual Shoes": 75,
        "Adidas Football Boots": 85
    },

    "Accessories": {
        "Drippy Sunglasses": 15,
        "Garmin Watch": 160,
        "Tuff Socks": 10
    }
}



def get_name():
    """Gets and validates the customer's name."""
   
    while True:
        customer_name = input("Customer Name: ").strip().title()


        # Check for empty input
        if customer_name == "":
            print("Error: Name cannot be empty.")
            continue


        # Allow letters, spaces, hyphens and apostrophes
        if customer_name.replace(" ", "").replace("-", "").replace("'", "").isalpha():
            return customer_name


        # Tell user what characters are allowed
        print("Error: Please use only letters, spaces, hyphens or apostrophes.")



def display_categories():
    """Displays all available product categories."""

    print("\nProduct Categories")

    # Display each category stored in the inventory dictionary.
    for number, category in enumerate(sports_inventory, start=1):
        print(f"{number}. {category}")

    print("Q. Quit")



def select_category():
    """Allows the user to select a product category and validates the input."""
    while True:
        # Use of derived values (len(sports_inventory)) which prevent hardcoding and makes the program more flexible and robust.
        category_choice = input(f"Select a category (1-{len(sports_inventory)}) or Q to quit: ").strip().upper()

        # Allow user to quit
        if category_choice == "Q":
            return None

        # Validate that input is a number and within the valid range.
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(sports_inventory):
            selected_category = list(sports_inventory.keys())[int(category_choice) - 1]
            return selected_category

        print(f"Error: Please enter a valid number (1-{len(sports_inventory)}) or Q to quit.")



def display_items(category):
    """Displays all items in the selected category."""

    print(f"\nItems in {category}:")

    # Display each item and its price from the selected category.
    for number, (item, price) in enumerate(sports_inventory[category].items(), start=1):
        print(f"{number}. {item} - ${price}")


def select_item(category):
    """Allows the customer to select a product or go back."""

    items = list(sports_inventory[category].items())

    while True:
        item_choice = input(
            f"Select an item (1-{len(items)}) or B to go back: "
        ).strip().upper()

        if item_choice == "B":
            return None

        if item_choice.isdigit() and 1 <= int(item_choice) <= len(items):
            item_name, price = items[int(item_choice) - 1]
            return item_name, price

        print(
            f"Error: Please enter a number between 1 and {len(items)}, "
            "or B to go back."
        )


def get_quantity():
    """Gets and validates the quantity of an item."""

    while True:
        quantity = input("Enter quantity: ").strip()

        # Check that the quantity is a positive whole number
        if quantity.isdigit() and int(quantity) > 0:
            return int(quantity)

        print("Error: Please enter a positive whole number.")



def add_to_cart(shopping_cart, item_name, price, quantity):
    """Adds an item to the shopping cart."""

    if item_name in shopping_cart:
        # Increase the quantity if the item is already in the cart
        shopping_cart[item_name]["quantity"] += quantity

    else:
        # Store the item, price and quantity in the cart
        shopping_cart[item_name] = {
            "price": price,
            "quantity": quantity
        }

    print(f"Added {quantity} x {item_name} to your cart.")



def display_cart(shopping_cart):
    """Displays all items currently in the shopping cart."""

    print("\nShopping Cart")

    if not shopping_cart:
        print("Your cart is empty.")
        return

    for item_name, details in shopping_cart.items():
        price = details["price"]
        quantity = details["quantity"]
        line_total = price * quantity

        print(
            f"{item_name} - ${price} x {quantity} = ${line_total}"
        )
        print(f"Total items in cart: {sum(item['quantity'] for item in shopping_cart.values())}")
    print(f"Total cost: ${sum(item['price'] * item['quantity'] for item in shopping_cart.values())} (excluding GST)")


def select_order_action():
    """Asks the customer what they want to do next."""

    print("\nWhat would you like to do?")
    print("1. Continue shopping")
    print("2. Checkout")
    print("3. Cancel order")

    while True:
        choice = input("Select an option (1-3): ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("Error: Please enter 1, 2 or 3.")


def main():
    """Function to run all other functions in the program."""
    print("Sports Ordering System")
    customer_name = get_name()

    shopping_cart = {}

    while True:
        display_categories()
        selected_category = select_category()

        # Quit if the customer chooses Q
        if selected_category is None:
            print("Order cancelled.")
            return

        display_items(selected_category)
        selected_item = select_item(selected_category)

        # Return to the category menu if the customer chooses B
        if selected_item is None:
            continue

        item_name, price = selected_item
        print(f"Selected: {item_name} - ${price}")

        quantity = get_quantity()
        print(f"Quantity selected: {quantity}")

        add_to_cart(shopping_cart, item_name, price, quantity)
        display_cart(shopping_cart)

        order_action = select_order_action()

        if order_action == "1":
            continue

        elif order_action == "2":
            print("_____Checkout_____.")
            return

        elif order_action == "3":
            shopping_cart.clear()
            print("Order cancelled.")
            return

if __name__ == "__main__":
    main()
