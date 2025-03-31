from welocme_msg import welcome_msg
from datetime import datetime

# CODES THAT ARE IN COMMENTS ARE FOR LATER USE. DON'T REMOVE THEM

imports = {}    #"product_name": ["quantity", "buying_price", "total_buying_price", "import_date"]

exports = {}    #"product_name": ["quantity", "selling_price", "total_sollling_price", "export_date", "Profit/loss"]

stocked_products = {}   #"product_name": ["remaining_quantity", "selling_price", "total_selling_price"]

#Usage of join to make a report of what have been bought, sold, income and the remaining products.

print(welcome_msg)
while True:
    print("\n", " " * 20, "____ MAIN PAGE ____\n")

# print("Welcome to the Inventory Management System")
    print("1. Import Your Products")
    print("2. Exports Your Sold Products")
    print("3. Check Your Stock")
    print("4. Search Menu")
    print("5. Get Report")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: N°_"))
        if choice == 1:
            print("\n", " " * 20, "____IMPORTS____\n")

            while True:
                print("1. Imported Products")
                print("2. Import New Product(s)")
                print("3. Delete Option for Imported products")
                print("4. Update Option for exported products")
                print("5. Return To The 'Main Page'")
                try:
                    choose = int(input("Enter your choice: N°_"))

                    if choose == 1:
                        print("\n", " " * 20, "_RECORDS FOR IMPORTED PRODUCTS_\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____IMPORTING NEW PRODUCT(S)____\n")
                        import_times = int(input("How many products do you want to import?:  "))
                        print()
                        for count in range(0, import_times):
                            product_name = input(f"Enter the name of your product_{count + 1}:  ")
                            quantity = int(input(f"Enter the quantity for your product({product_name}):  "))
                            buying_price = int(input(f"Enter the price per one product(Price Per Unit): "))
                            # import_date = datetime.today().date().time()
                            imports_date = datetime.now().strftime("%a %d/%B/%Y")
                            total_buying_price = quantity * buying_price
                            print()
                            
                            imports[product_name] = [quantity, buying_price, total_buying_price, imports_date]
                            stocked_products[product_name] = [quantity, buying_price, total_buying_price]
                        print(imports)
                        print(stocked_products)
                        print()
                    elif choose == 3:
                        print("\n", " " * 20, "____DELETING PRODUCT IN IMPORTS____\n")

                    elif choose == 4:
                        print("\n", " " * 20, "____UPDATING PRODUCT IN IMPORTS____\n")

                    elif choose == 5:
                        break

                    # else:
                    #     print("\nWrong Input Please Try again!\n")

                except ValueError:
                    print("\nWrong input, Please enter a valid number!\n")

            print("\n")
        
        elif choice == 2:
            print("\n"," " * 20,"____EXPORTS____\n")

            while True:
                print("1. View Exported Products")
                print("2. Export Sold Product(s)")
                print("3. Delete Option for exported products")
                print("4. Update Option for exported products")
                print("5. Return To The 'Main Page'")
                try:
                    choose = int(input("Enter your choice: N°_"))

                    if choose == 1:
                        print("\n", " " * 20, "____RECORDS FOR EXPORTED PRODUCTS____\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____EXPORTING SOLD PRODUCT(S)____\n")
                        export_times = int(input("How many products do you want to export?:  "))
                        print()
                        for count in range(0, export_times):
                            while True:
                                Eproduct_name = input("Enter the name of the product you want to export:  ")
                                if Eproduct_name not in stocked_products:
                                    print(f"____{Eproduct_name} is not found in your stock(you have to export what's in the stock!)\n")
                                elif Eproduct_name in imports:
                                    quantity = int(input(f"Enter the quantity for quantity of {Eproduct_name}:  "))
                                    selling_price = int(input(f"Enter the selling price per product({Eproduct_name}) you sold:  "))
                                    export_date = datetime.now().strftime("%a %d/%B/%Y")
                                    total_selling_price = quantity * selling_price
                                    if selling_price > stocked_products[Eproduct_name][1]:
                                        income_msg = "PROFIT"
                                    elif selling_price < stocked_products[Eproduct_name][1]:
                                        income_msg = "LOSS"
                                    print()
                                    exports[Eproduct_name] = [quantity, selling_price, total_selling_price, export_date, income_msg]
                                    remaining_quantity = stocked_products[Eproduct_name][0] - quantity
                                    remaining = remaining_quantity * stocked_products[Eproduct_name][1]

                                    stocked_products.update({Eproduct_name: [remaining_quantity, stocked_products[Eproduct_name][1], total_buying_price]})
                                    break
                        print(exports)
                        print(stocked_products)
                        print()

                    elif choose == 3:
                        print("\n", " " * 20, "____DELETING PRODUCT IN EXPORTS____\n")

                    elif choose == 4:
                        print("\n", " " * 20, "____UPDATING PRODUCT IN EXPORTS____\n")

                    elif choose == 5:
                        break

                    # else:
                    #     print("\nWrong Input Please Try again!\n")

                except ValueError:
                    print("\nWrong input, Please enter a valid number!\n")

            print("\n")

        elif choice == 3:
            print("\n", " " * 20, "____YOUR STOCK____\n")

            while True:
                print("1. View Your Stock")
                print("2. Delete Option for products in the stock")
                print("3. Update Option for products in the stock")
                print("4. Return To The 'Main Page'")
                try:
                    choose = int(input("Enter your choice: N°_"))

                    if choose == 1:
                        print("\n", " " * 20, "____PRODUCTS IN THE STOCK____\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____DELETING PRODUCT IN THE STOCK____\n")

                    elif choose == 3:
                        print("\n", " " * 20, "____UPDATING PRODUCT IN THE STOCK____\n")

                    elif choose == 4:
                        break

                    # else:
                    #     print("\nWrong Input Please Try again!\n")

                except ValueError:
                    print("\nWrong input, Please enter a valid number!\n")

            print("\n")

        elif choice == 4:
            print("\n", " " * 20, "____SEARCH MENU____\n")

            while True:
                print("1. Search In Imports")
                print("2. Search In Exports")
                print("3. Search In Stock")
                print("4. Return To The 'Main Page'")
                try:
                    choose = int(input("Enter your choice: N°_"))

                    if choose == 1:
                        print("\n", " " * 20, "____SEARCHING IN IMPORTS____\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____SEARCHING IN EXPORTS____\n")

                    elif choose == 3:
                        print("\n", " " * 20, "____SEARCHING IN STOCK____\n")

                    elif choose == 4:
                        break

                    # else:
                    #     print("\nWrong Input Please Try again!\n")

                except ValueError:
                    print("\nWrong input, Please enter a valid number!\n")

            print("\n")

        elif choice == 5:
            print("\n", " " * 20, "____YOUR REPORT____\n")

            while True:
                print("1. Generate Full Report")
                print("2. Generate Report For A Specific Product")
                print("3. Return To The 'Main Page'")
                try:
                    choose = int(input("Enter your choice: N°_"))

                    if choose == 1:
                        print("\n", " " * 20, "____FULL REPORT____\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____REPORT ON A SPECIFIC PRODUCT____\n")

                    elif choose == 3:
                        break

                    # else:
                    #     print("\nWrong Input Please Try again!\n")

                except ValueError:
                    print("\nWrong input, Please enter a valid number!\n")

            print("\n")

        elif choice == 6:
            print("\nEXITTING....")
            break

        # else:
        #     print("\nWrong Input Please Try again!\n")

    except ValueError:
        print("\nWrong input, Please enter a valid number!\n")