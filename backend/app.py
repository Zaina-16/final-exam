# Products list
products = [
    ["Product 1", 10],
    ["Product 2", 20],
    ["Product 3", 30],
    ["Product 4", 40],
    ["Product 5", 50]
]

# Start the program loop
while True:

    # Show products
    print("\nChoose a product number:")
    print("1 - Product 1")
    print("2 - Product 2")
    print("3 - Product 3")
    print("4 - Product 4")
    print("5 - Product 5")

    # Ask user to choose
    choice = input("Enter the number: ")

    # Check if input is a number
    if choice.isdigit():
        choice = int(choice)

        # Check if number is between 1 and 5
        if 1 <= choice <= 5:
            product_name = products[choice - 1][0]
            product_price = products[choice - 1][1]

            # Calculate tax
            tax = product_price * 0.15
            total_price = product_price + tax

            print(f"Total price for {product_name} (with tax): {total_price} SAR")
        else:
            print("Error: Number not found. Please choose between 1 and 5.")
    else:
        print("Error: Please enter numbers only.")

    # Ask if user wants to continue
    again = input("Do you want to choose another product? (yes/no): ").lower()

    if again == "no":
        print("Thank you! Program ended.")
        break
