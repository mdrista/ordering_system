##############################
### Sports Ordering System ###
##############################

# This sports ordering system is designed for telemarketers to take customer orders for sports equipment. 
# It collects customer information, validates inputs, and processes orders efficiently.
# The program uses advanced programming techniques such as functions, loops, 
# and validation to ensure a smooth ordering experience.


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



def main():
    """Function to run all other functions in the program."""
    print("Sports Ordering System")
    customer_name = get_name()
    print(f"Customer Name: {customer_name}")



if __name__ == "__main__":
    main()