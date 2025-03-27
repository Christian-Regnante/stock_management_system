# CODES THAT ARE IN COMMENTS ARE FOR LATER USE. DON'T REMOVE THEM

imports = {
    "product_name": ["quantity", "buying_price", "total_buying_price", "import_date"]
}

exports = {
    "product_name": ["quantity", "selling_price", "total_sold_price", "export_date", "Profit/loss"]
}

stocked_products = {
    "product_name": ["remaining_quantity", "selling_price", "total_selling_price"]
}

#Usage of join to make a report of what have been bought, sold, income and the remaining products.

while True:
    print("\n____ MAIN PAGE ____\n")

    print("1. Import Your Products")
    print("2. Exports Your Sold Products")
    print("3. Check Your Stock")
    print("4. Get Report")
    print("5. Exit")
    choice = int(input("Enter your choice: N°_"))

    if choice == 1:
        print("\n____IMPORTS____\n")

        while True:
            print("1. Imported Products")
            print("2. Import New Product(s)")
            # print("#. Delete Option for Imported products")
            # print("#. Update Option for exported products")
            print("3. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                pass

            elif choose == 2:
                pass

            elif choose == 3:
                break

        print("\n")
    
    elif choice == 2:
        print("\n____EXPORTS____\n")

        while True:
            print("1. Exported Products")
            print("2. Export Sold Product(s)")
            # print("#. Delete Option for exported products")
            # print("#. Update Option for exported products")
            print("3. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                pass

            elif choose == 2:
                pass

            elif choose == 3:
                break

        print("\n")

    elif choice == 3:
        print("\n____YOUR STOCK____\n")

        while True:
            print("1. Check Your Stock")
            # print("#. Delete Option for products in the stock")
            # print("#. Update Option for products in the stock")
            print("2. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                pass

            elif choose == 3:
                break

        print("\n")

    elif choice == 4:
        print("\n____YOUR REPORT____\n")

        while True:
            print("1. Generate Full Report")
            print("2. Generate Report For A Specific Product")
            print("3. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                pass

            elif choose == 2:
                pass

            elif choose == 3:
                break

        print("\n")

    elif choice == 5:
        print("\nEXITTING....")
        break

    else:
        print("\nWrong Input Please Try again!")
