import datetime


def main():
    inventory = {}

    while True:
        print("\nStock Management System")
        print("1. Add New Goods")
        print("2. Mark Goods as Sold")
        print("3. Remove Sold Goods")
        print("4. View Inventory Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_goods(inventory)
        elif choice == "2":
            mark_sold(inventory)
        elif choice == "3":
            remove_sold(inventory)
        elif choice == "4":
            view_report(inventory)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


def add_goods(inventory):
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    date_added = datetime.date.today().strftime("%Y-%m-%d")

    if name in inventory:
        inventory[name]['quantity'] += quantity
    else:
        inventory[name] = {'quantity': quantity, 'price': price, 'date_added': date_added, 'sold': 0, 'sold_price': 0.0}

    print(f"Added {quantity} of {name} to inventory.")


def mark_sold(inventory):
    name = input("Enter item name: ")
    if name in inventory:
        quantity_sold = int(input("Enter quantity sold: "))
        if quantity_sold > inventory[name]['quantity']:
            print("Not enough stock available.")
            return
        sold_price = float(input("Enter price sold at per unit: "))

        inventory[name]['quantity'] -= quantity_sold
        inventory[name]['sold'] += quantity_sold
        inventory[name]['sold_price'] = sold_price
        print(f"Marked {quantity_sold} of {name} as sold.")
    else:
        print("Item not found in inventory.")


def remove_sold(inventory):
    sold_items = [name for name, details in inventory.items() if details['quantity'] == 0 and details['sold'] > 0]
    for item in sold_items:
        del inventory[item]
    print("Removed sold goods from inventory.")


def view_report(inventory):
    date_added = datetime.date.today().strftime("%Y-%m-%d")
    print("\nInventory Report:")
    for name, details in inventory.items():
        print(f"{date_added}. {name} - Quantity: {details['quantity']}, Sold: {details['sold']}, Price: {details['price']}")


if __name__ == "__main__":
    main()

