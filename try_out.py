# CODES THAT ARE IN COMMENTS ARE FOR LATER USE. DON'T REMOVE THEM

imports = {}
exports = {}
stocked_products = {}

# Usage of join to make a report of what has been bought, sold, income, and the remaining products.
def add_to_imports():
    """Add a new product to the imports dictionary."""
    product_name = input("Enter the product name: ").strip().lower()
    quantity = int(input("Enter the quantity: "))
    buying_price = float(input("Enter the buying price per unit: "))
    total_buying_price = quantity * buying_price
    import_date = input("Enter the import date (YYYY-MM-DD): ").strip()

    imports[product_name] = [quantity, buying_price, total_buying_price, import_date]
    print(f"Product '{product_name}' added to imports successfully!")

def add_to_exports():
    """Add a new product to the exports dictionary."""
    product_name = input("Enter the product name: ").strip().lower()
    if product_name not in imports:
        print(f"Error: '{product_name}' is not in imports. Add it to imports first.")
        return

    quantity = int(input("Enter the quantity sold: "))
    selling_price = float(input("Enter the selling price per unit: "))
    total_sold_price = quantity * selling_price
    export_date = input("Enter the export date (YYYY-MM-DD): ").strip()
    profit_loss = total_sold_price - (imports[product_name][1] * quantity)

    exports[product_name] = [quantity, selling_price, total_sold_price, export_date, profit_loss]
    print(f"Product '{product_name}' added to exports successfully!")
    
while True:
    print("\n____ MAIN PAGE ____\n")
    print("1. Import Your Products")
    print("2. Export Your Sold Products")
    print("3. Check Your Stock")
    print("4. Get Report")
    print("5. Exit")
    choice = int(input("Enter your choice: N°_"))

    if choice == 1:
        print("\n____IMPORTS____\n")
        while True:
            print("1. View Imported Products")
            print("2. Import New Product(s)")
            print("3. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                print("\nImported Products:")
                for product, details in imports.items():
                    print(f"{product}: {details}")
            elif choose == 2:
                add_to_imports()
            elif choose == 3:
                break
        print("\n")

    elif choice == 2:
        print("\n____EXPORTS____\n")
        while True:
            print("1. View Exported Products")
            print("2. Export Sold Product(s)")
            print("3. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                print("\nExported Products:")
                for product, details in exports.items():
                    print(f"{product}: {details}")
            elif choose == 2:
                add_to_exports()
            elif choose == 3:
                break
        print("\n")

    elif choice == 3:
        print("\n____YOUR REPORT____\n")
        while True:
            print("1. Generate Full Report")
            print("2. Generate Report For A Specific Product")
            print("3. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                print("\nFull Report:")
                print("Imports:", imports)
                print("Exports:", exports)
                print("Stock:", stocked_products)
            elif choose == 2:
                product_name = input("Enter the product name: ").strip()
                print("\nReport for Product:")
                print("Imports:", imports.get(product_name, "Not Found"))
                print("Exports:", exports.get(product_name, "Not Found"))
                print("Stock:", stocked_products.get(product_name, "Not Found"))
            elif choose == 3:
                break
        print("\n")

    elif choice == 4:
        print("\nEXITING....")
        break

    else:
        print("\nWrong Input. Please Try Again!")