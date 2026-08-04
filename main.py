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


def main():
    """Function to run all other functions in the program."""
    print("Sports Ordering System")
    customer_name = get_name()

    shopping_cart = {} #create an empty shopping cart to store items and their quantities
    
    display_categories()



if __name__ == "__main__":
    main()