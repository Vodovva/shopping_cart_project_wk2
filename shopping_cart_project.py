def shopping_cart():
    shopping_cart = []
    price = []
    item = []

    while True:
        choice = input("Welcome to your shopping cart!")
        print("Add Item")
        print("Delete Item")
        print("View Shopping List")
        print("Quit")
        choice = input("Enter your choice")
        if choice == "Add Item":
            item_name = input("Enter item name").lower()
            item_quantity = int(input("Enter quantity"))
            item = {"name": item_name, "quantity": item_quantity}
            shopping_cart.append(item)
            print(f"{item_quantity} {item_name}(s) added to your cart.")

        elif choice == "Delete Item":
            item_name = input("Enter item name to delete")
            for item in shopping_cart:
                if item["name"] == item_name:
                    shopping_cart.remove(item)
                    print(f"{item_name} removed from your cart.")
                    break
            else:
                print(f"{item_name} not found in your cart.")

        elif choice == "View Shopping List":
            print("Your Shopping List")
            for item in shopping_cart:
                print(f"{item['quantity']} {item['name']}(s)")

        elif choice == "Quit":
            for item in shopping_cart:
                print("Receipt(item)")
            price = 0
            for item in shopping_cart:
                print(f"{item['quantity']} {item['name']}(s)")
                price += item['quantity']
            print(f"Total Items {len(shopping_cart)}")
            print(f"Total cost ${price:.2}")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
