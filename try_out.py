# CODES THAT ARE IN COMMENTS ARE FOR LATER USE. DON'T REMOVE THEM

imports = {}  #"Spaghetti": ["20", "2100", "20 * 2100 ", "27/March/2025 "],
    #"Cabbage ": ["13", 1200", "13 * 1200" , "27/March/2025 "]"   

exports = {} # "product_name": ["quantity", "selling_price", "total_sold_price", "export_date", "Profit/loss"]

stocked_products = {}   #"product_name": ["remaining_quantity", "selling_price", "total_selling_price"]

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
                print(imports)

            elif choose == 2:
                product_name =input("Enter product's name ")
                quantity =int(input("What is the total quantity of your product "))
                unit_buying_price =int(input("What is the price for one quantity"))
                total_buying_price = quantity * unit_buying_price 
                date_imported = input("Enter the date in this format:date/month/year ")
                
                imports[product_name] = [quantity,unit_buying_price,total_buying_price,date_imported]

                stocked_products[product_name] = [quantity,unit_buying_price,total_buying_price]
                

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
                print(exports)

            elif choose == 2:
                product_name =input("What is the product name ")
                quantity =int(input("What is the quantity"))
                unit_selling_price =int(input("What is the unit selling price"))
                total_selling_price = quantity * unit_selling_price
                date_exported =input("Enter the date in this format:Date/Month/Year")

                if unit_selling_price > stocked_products[product_name][1]:
                    profit_loss = "profit"

                elif unit_selling_price <= stocked_products[product_name][1]:    
                    profit_loss = "loss"

                exports[product_name] = [quantity,unit_selling_price,total_selling_price,date_exported,profit_loss] 

                remaining_quantity = stocked_products[product_name][0] - exports[product_name][0]

                total_buying_price = remaining_quantity * stocked_products[product_name][1]

                stocked_products.update({product_name: [remaining_quantity,stocked_products[product_name][1],total_buying_price]})


                
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
                print(stocked_products)

            elif choose == 2:
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