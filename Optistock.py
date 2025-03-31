from datetime import datetime
import MySQLdb
from MySQLdb import Error
from connection import connection   # Connect to MySQL database


# Create tables if they don't exist
def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS imports (
        product_name VARCHAR(255) PRIMARY KEY,
        quantity INT ,
        unit VARCHAR(50) ,
        buying_price INT ,
        total_buying_price INT ,
        import_date DATE
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exports (
        product_name VARCHAR(255),
        quantity INT,
        unit VARCHAR(50),
        selling_price INT, 
        total_sold_price INT,
        export_date DATE,
        profit_loss VARCHAR(50)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stocked_products (
        product_name VARCHAR(255) PRIMARY KEY,
        quantity INT,
        unit VARCHAR(50),
        buying_price INT,
        total_buying_price INT,
        selling_price INT
    )''')

    connection.commit()


# Import class
class Import:
    def __init__(self, connection):
        self.connection = connection

    def view_imports(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM imports")
        rows = cursor.fetchall()
        print("____Imported Products:\n")
        print(f"{'Product Name':<20} | {'Remaining Quantity(Unit)':<30}| {'Buying Price(FRW)':<20} | {'Total Buying Price(FRW)':<25} | {'Import Date':<20}")
        print("-" * 120)
        for row in rows:
            remaining_quantity_with_unit = f"{row[1]} {row[2]}"
            import_date = str(row[5])
            print(f"{row[0]:<20} | {remaining_quantity_with_unit:<30}| {row[3]:<20} | {row[4]:<25} | {import_date:<20}")
            print()
        print("-" * 120)
        cursor.close()

    def add_import(self, product_name, quantity, unit, buying_price, selling_price, import_date):
        total_buying_price = quantity * buying_price
        cursor = self.connection.cursor()
        cursor.execute('''
        INSERT INTO imports (product_name, quantity, unit, buying_price, total_buying_price, import_date)
        VALUES (%s, %s, %s, %s, %s, %s)''', (product_name, quantity, unit, buying_price, total_buying_price, import_date))
        
        cursor.execute('''
        INSERT INTO stocked_products (product_name, quantity, unit, buying_price, total_buying_price, selling_price)
        VALUES (%s, %s, %s, %s, %s, %s)''', (product_name, quantity, unit, buying_price, total_buying_price, selling_price))

        self.connection.commit()
        print(f"\n____{product_name} imported successfully!____")
        print("&")
        print(f"____{product_name} was added into your stock!____\n")
        cursor.close()

    def delete_import(self, product_name):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM imports WHERE product_name = %s", (product_name,))
        cursor.execute("DELETE FROM stocked_products WHERE product_name = %s", (product_name,))
        self.connection.commit()
        print(f"\nProduct {product_name} deleted successfully!")
        cursor.close()

# Export class
class Export:
    def __init__(self, connection):
        self.connection = connection

    def view_exports(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM exports")
        rows = cursor.fetchall()
        print("____Exported Products:\n")
        print(f"{'Product Name':<20} | {'Quantity(Unit)':<25}| {'Selling Price(FRW)':<22} | {'Total Sold Price(FRW)':<25} | {'Export Date':<20} | {'Profi/Loss':<15}")
        print("-" * 135)
        for row in rows:
            quantity_with_unit = f"{row[1]} {row[2]}"
            export_date = str(row[5])
            print(f"{row[0]:<20} | {quantity_with_unit:<25} | {row[3]:<22} | {row[4]:<25} | {export_date:<20} | {row[6]:<15}")
            print()
        print("-" * 135)
        cursor.close()

    def add_export(self, product_name, quantity, selling_price, export_date):
        cursor = self.connection.cursor()
        cursor.execute("SELECT quantity FROM stocked_products WHERE product_name = %s", (product_name,))
        result = cursor.fetchone()

        if result:
            remaining_quantity = result[0]
            if quantity <= remaining_quantity:
                total_sold_price = quantity * selling_price

                cursor.execute("SELECT unit FROM stocked_products WHERE product_name = %s", (product_name,))
                unit = cursor.fetchone()

                cursor.execute("SELECT buying_price FROM stocked_products WHERE product_name = %s", (product_name,))
                buying_price_result = cursor.fetchone()
                if buying_price_result:
                    buying_price = buying_price_result[0]
                    profit_loss = "PROFIT" if selling_price > buying_price else "LOSS"

                    cursor.execute('''
                    UPDATE stocked_products
                    SET quantity = quantity - %s, total_buying_price = total_buying_price - (%s * %s)
                    WHERE product_name = %s''', (quantity, quantity, buying_price, product_name))

                    cursor.execute('''
                    INSERT INTO exports (product_name, quantity, unit, selling_price, total_sold_price, export_date, profit_loss)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)''', 
                    (product_name, quantity, unit, selling_price, total_sold_price, export_date, profit_loss))
                    
                    self.connection.commit()
                    print(f"\n____{product_name} exported successfully!____")
                    print("&")
                    print(f"____{product_name} was updated from your stock!____\n")
                else:
                    print("\n____Buying price not found for the product.____\n")
            else:
                print("\n____Not enough stock to fulfill the export.____\n")
        else:
            print("\n____Product not found in stock.____\n")
        cursor.close()

    def delete_export(self, product_name):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM exports WHERE product_name = %s", (product_name,))
        self.connection.commit()
        print(f"\nProduct {product_name} deleted successfully!")
        cursor.close()

# Stock class
class Stock:
    def __init__(self, connection):
        self.connection = connection

    def view_stock(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM stocked_products")
        rows = cursor.fetchall()
        print("____Current Stock:\n")
        print(f"{'Product Name':<20} | {'Remaining Quantity(Unit)':<30}| {'Buying Price(FRW)':<20} | {'Selling Price(FRW)':<20} | {'Total Buying Price(FRW)':<25}") 
        print("-" * 125)
        for row in rows:
            remaining_quantity_with_unit = f"{row[1]} {row[2]}"
            print(f"{row[0]:<20} | {remaining_quantity_with_unit:<30}| {row[3]:<20} | {row[5]:<20} | {row[4]:<25}")
            print()
        print("-" * 125)
        cursor.close()

    def delete_stock(self, product_name):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM stocked_products WHERE product_name = %s", (product_name,))
        self.connection.commit()
        print(f"\nProduct {product_name} was deleted successfully!")
        cursor.close()

    def update_stock(self, product_name, quantity, unit, buying_price, selling_price):
        cursor = self.connection.cursor()
        total_buying_price = quantity * buying_price

        cursor.execute('''UPDATE stocked_products SET quantity = %s, unit = %s, buying_price = %s, total_buying_price = %s, selling_price = %s WHERE product_name = %s''',
        (quantity, unit, buying_price, total_buying_price, selling_price, product_name))
        self.connection.commit()
        print(f"\nProduct {product_name} was updated successfully!")
        cursor.close()

# Search class
# Report class
class Report:
    def __init__(self, connection):
        self.connection = connection

    def generate_full_report(self):
        cursor = self.connection.cursor()
        print("\n____FULL REPORT____\n")

        # Imports
        print("____Imported Products:\n")
        cursor.execute("SELECT * FROM imports")
        imports = cursor.fetchall()
        print(f"{'Product Name':<20} | {'Quantity(Unit)':<25} | {'Buying Price(FRW)':<20} | {'Total Buying Price(FRW)':<25} | {'Import Date':<20}")
        print("-" * 120)
        for row in imports:
            remaining_quantity_with_unit = f"{row[1]} {row[2]}"
            import_date = str(row[5])
            print(f"{row[0]:<20} | {remaining_quantity_with_unit:<25} | {row[3]:<20} | {row[4]:<25} | {import_date:<20}")
        print("-" * 120)

        # Exports
        print("\n____Exported Products:\n")
        cursor.execute("SELECT * FROM exports")
        exports = cursor.fetchall()
        print(f"{'Product Name':<20} | {'Quantity(Unit)':<25} | {'Selling Price(FRW)':<20} | {'Total Sold Price(FRW)':<25} | {'Export Date':<20} | {'Profit/Loss':<15}")
        print("-" * 138)
        for row in exports:
            quantity_with_unit = f"{row[1]} {row[2]}"
            export_date = str(row[5])
            print(f"{row[0]:<20} | {quantity_with_unit:<25} | {row[3]:<20} | {row[4]:<25} | {export_date:<20} | {row[6]:<15}")
        print("-" * 138)

        # Stock
        print("\n____Current Stock:\n")
        cursor.execute("SELECT * FROM stocked_products")
        stock = cursor.fetchall()
        print(f"{'Product Name':<20} | {'Remaining Quantity(Unit)':<30} | {'Buying Price(FRW)':<20} | {'Selling Price(FRW)':<20} | {'Total Buying Price(FRW)':<25}")
        print("-" * 125)
        for row in stock:
            remaining_quantity_with_unit = f"{row[1]} {row[2]}"
            print(f"{row[0]:<20} | {remaining_quantity_with_unit:<30} | {row[3]:<20} | {row[5]:<20} | {row[4]:<25}")
        print("-" * 125)

        #Report summary
        print("\n", " " * 20, "____Report Summary____\n")
        imports_count = len(imports)
        export_counts = len(exports)
        stock_count = len(stock)
                

        print("____IMPORTS____")
        print(f"{'Total Imported Products':<40} : {imports_count:<20}")
        print(f"{'Total Spent on Imports(FRW)':<40} : {sum(row[4] for row in imports):<20}")
        var_point = 0
        for count_import in imports:
            for count_stock in stock:
                var_point = count_import[1] * count_stock[5] + var_point
        print(f"{'Expected Total Selling Point(FRW)':<40} : {var_point:<20}")
        print(f"{'Expected Income(FRW)':<40} : {var_point - sum(row[4] for row in imports):<20}")
        print("_" * 60)
        print()

        print("____STOCK____")
        print(f"{'Total Products In The Stock':<45} : {stock_count:<20}")
        print(f"{'Total Value Of The Remaining Products(FRW)':<45} : {sum(row[4] for row in stock):<20}")
        print("_" * 60)
        print()

        cursor.close()

    def generate_product_report(self, product_name):
        cursor = self.connection.cursor()
        print(f"\n____REPORT FOR PRODUCT: {product_name}____\n")

        # Import details
        cursor.execute("SELECT * FROM imports WHERE product_name = %s", (product_name,))
        import_row = cursor.fetchone()
        if import_row:
            print("____Import Details:\n")
            print(f"{'Quantity(Unit)':<25} | {'Buying Price(FRW)':<20} | {'Total Buying Price(FRW)':<25} | {'Import Date':<20}")
            print("-" * 90)

            quantity_with_unit = f"{import_row[1]} {import_row[2]}"
            import_date = str(import_row[5])
            print(f"{quantity_with_unit:<25} | {import_row[3]:<20} | {import_row[4]:<25} | {import_date:<20}")
            print("-" * 90)
        else:
            print("No import records found for this product.\n")

        # Export details
        cursor.execute("SELECT * FROM exports WHERE product_name = %s", (product_name,))
        row = cursor.fetchall()
        if row:
            print("\n____Export Details:\n")
            print(f"{'Quantity(Unit)':<25} | {'Selling Price(FRW)':<20} | {'Total Sold Price(FRW)':<25} | {'Export Date':<20} | {'Profit/Loss':<15}")
            print("-" * 120)
            for row in row:
                quantity_with_unit = f"{row[1]} {row[2]}"
                export_date = str(row[5])
                print(f"{quantity_with_unit:<25} | {row[3]:<20} | {row[4]:<25} | {export_date:<20} | {row[6]:<15}")
            print("-" * 120)
        else:
            print("No export records found for this product.\n")

        # Stock details
        cursor.execute("SELECT * FROM stocked_products WHERE product_name = %s", (product_name,))
        stock_row = cursor.fetchone()
        if stock_row:
            print("\n____Stock Details:\n")
            print(f"{'Remaining Quantity(Unit)':<30} | {'Buying Price(FRW)':<20} | {'Selling Price(FRW)':<20} | {'Total Buying Price(FRW)':<25}")
            print("-" * 102)
            remaining_quantity_with_unit = f"{stock_row[1]} {stock_row[2]}"
            print(f"{remaining_quantity_with_unit:<30} | {stock_row[3]:<20} | {stock_row[5]:<20} | {stock_row[4]:<25}")
            print("-" * 102)
        else:
            print("No stock records found for this product.\n")

        cursor.close()

# Main program
create_tables(connection)

manage_import = Import(connection)
manage_export = Export(connection)
manage_stock = Stock(connection)
manage_report = Report(connection)



while True:
    print("\n", " " * 20, "____ MAIN PAGE ____\n")

    print("1. Import Your Products")
    print("2. Exports Your Sold Products")
    print("3. Check Your Stock")
    print("4. Search Menu")
    print("5. Generate Report")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: N°_"))
        if choice == 1:
            print("\n", " " * 20, "____IMPORTS____\n")

            while True:
                print("1. View Imported Products")
                print("2. Import New Product(s)")
                print("3. Delete Option for Imported products")
                print("4. Return To The 'Main Page'")
                try:
                    choose = int(input("Enter your choice: N°_"))

                    if choose == 1:
                        print("\n", " " * 20, "____RECORDS FOR IMPORTED PRODUCTS____\n")
                        manage_import.view_imports()
                        print("\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____IMPORTING NEW PRODUCT(S)____\n")
                        import_times = int(input("How many products do you want to import?:  "))
                        print()
                        for count in range(import_times):
                            product_name = input(f"Enter the name of your product_{count + 1}:  ")
                            cursor = connection.cursor()
                            cursor.execute("SELECT product_name FROM imports WHERE product_name = %s", (product_name,))
                            result = cursor.fetchone()

                            if not result:
                                quantity = int(input(f"Enter the quantity for your product({product_name}):  "))

                                while True:
                                    print("1. Kilograms")
                                    print("2. Litters")
                                    print("3. Pieces")
                                    try:
                                        unit_choice = int(input(f"Enter the unit of your product({product_name}): N°_"))
                                        if unit_choice == 1:
                                            unit = "KG"
                                            break
                                        elif unit_choice == 2:
                                            unit = "L"
                                            break
                                        elif unit_choice == 3:
                                            unit = "Pcs"
                                            break
                                        else:
                                            print("\n____Invalid Input! Please choose a valid unit.____\n")
                                    except ValueError:
                                        print("\n____Invalid Input! Please enter a valid number.____\n")

                                buying_price = int(input(f"Enter the buying price per one product(Price Per Unit): "))
                                selling_price = int(input(f"Set the selling price for your product(Price Per Unit): "))
                                import_date = datetime.now().strftime("%Y-%m-%d")

                                manage_import.add_import(product_name, quantity, unit, buying_price, selling_price, import_date)
                            else:
                                print(f"\n____{product_name} is already imported, please check your imports!____")
                                break
                        print()
                        cursor.close()

                    elif choose == 3:
                        print("\n", " " * 20, "____DELETING PRODUCT IN IMPORTS____\n")
                        product_name = input("Enter the name of the product you want to delete(!Be aware that this product will be removed from your stock):\n")
                        cursor = connection.cursor()
                        cursor.execute("SELECT product_name FROM imports WHERE product_name = %s", (product_name,))
                        result = cursor.fetchone()

                        if result:
                            manage_import.delete_import(product_name)
                        else:
                            print(f"\n____{product_name} is not found in imports!____")
                        cursor.close()

                    elif choose == 4:
                        break

                    else:
                        print("\n____Invalid Input! Please enter a valid option.____\n")

                except ValueError:
                    print("\n____Invalid Input! Please enter a valid number.____\n")

        elif choice == 2:
            print("\n", " " * 20, "____EXPORTS____\n")

            while True:
                print("1. View Exported Products")
                print("2. Export Sold Product(s)")
                print("3. Delete Option for exported products")
                print("4. Return To The 'Main Page'")
                try:
                    choose = int(input("Enter your choice: N°_"))

                    if choose == 1:
                        print("\n", " " * 20, "____RECORDS FOR EXPORTED PRODUCTS____\n")
                        manage_export.view_exports()
                        print("\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____EXPORTING SOLD PRODUCT(S)____\n")
                        export_times = int(input("How many products do you want to export?:  "))
                        print()
                        for count in range(export_times):
                            product_name = input("Enter the name of the product you want to export:  ")
                            cursor = connection.cursor()
                            cursor.execute("SELECT product_name FROM stocked_products WHERE product_name = %s", (product_name,))
                            result = cursor.fetchone()
                            if result:
                                quantity = int(input(f"Enter the quantity for {product_name} you want to export:  "))
                                selling_price = int(input(f"Enter the selling price per product({product_name}) you sold:  "))
                                export_date = datetime.now().strftime("%Y-%m-%d")

                                manage_export.add_export(product_name, quantity, selling_price, export_date)
                            else:
                                print(f"\n____{product_name} is not found in your stock(you have to export what's in the stock!)____")
                        print()
                        cursor.close()

                    elif choose == 3:
                        print("\n", " " * 20, "____DELETING PRODUCT IN EXPORTS____\n")
                        product_name = input("Enter product name to delete: ")
                        cursor = connection.cursor()
                        cursor.execute("SELECT product_name FROM exports WHERE product_name = %s", (product_name,))
                        result = cursor.fetchone()

                        if result:
                            manage_export.delete_export(product_name)
                        else:
                            print(f"\n____{product_name} is not found in your exports!____")
                        cursor.close()

                    elif choose == 4:
                        break

                    else:
                        print("\n____Invalid Input! Please enter a valid option.____\n")

                except ValueError:
                    print("\n____Invalid Input! Please enter a valid number.____\n")

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
                        manage_stock.view_stock()
                        print("\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____DELETING PRODUCT IN THE STOCK____\n")
                        product_name = input("Enter product name to delete: ")
                        cursor = connection.cursor()
                        cursor.execute("SELECT product_name FROM stocked_products WHERE product_name = %s", (product_name,))
                        result = cursor.fetchone()

                        if result:
                            manage_stock.delete_stock(product_name)
                        else:
                            print(f"\n____{product_name} is not found in your stock!____")
                        cursor.close()

                    elif choose == 3:
                        print("\n", " " * 20, "____UPDATING PRODUCT IN THE STOCK____\n")
                        product_name = input("Enter the name of the product you want to update:  ")
                        cursor = connection.cursor()
                        cursor.execute("SELECT product_name FROM stocked_products WHERE product_name = %s", (product_name,))
                        result = cursor.fetchone()

                        if result:
                            quantity = int(input(f"Enter the new quantity for {product_name}:  "))

                            while True:
                                print("1. Kilograms")
                                print("2. Litters")
                                print("3. Pieces")
                                try:
                                    unit_choice = int(input(f"Update the unit of your product({product_name}): N°_"))
                                    if unit_choice == 1:
                                        unit = "KG"
                                        break
                                    elif unit_choice == 2:
                                        unit = "L"
                                        break
                                    elif unit_choice == 3:
                                        unit = "Pcs"
                                        break
                                    else:
                                        print("\n____Invalid Input! Please choose a valid unit.____\n")
                                except ValueError:
                                    print("\n____Invalid Input! Please enter a valid number.____\n")

                            buying_price = int(input(f"Enter the new buying price per product({product_name}):  "))
                            selling_price = int(input(f"Enter the new selling price per product({product_name}):  "))

                            manage_stock.update_stock(product_name, quantity, unit, buying_price, selling_price)
                        else:
                            print(f"\n____{product_name} is not found in your stock!____")
                        cursor.close()

                    elif choose == 4:
                        break

                    else:
                        print("\n____Invalid Input! Please enter a valid option.____\n")

                except ValueError:
                    print("\n____Invalid Input! Please enter a valid number.____\n")

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
                        product_name = input("Enter the name of the product you want to search:  ")
                        manage_search.search_imports(product_name)
                        print("\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____SEARCHING IN EXPORTS____\n")
                        product_name = input("Enter the name of the product you want to search:  ")
                        manage_search.search_exports(product_name)
                        print("\n")

                    elif choose == 3:
                        print("\n", " " * 20, "____SEARCHING IN STOCK____\n")
                        product_name = input("Enter the name of the product you want to search:  ")
                        manage_search.search_stock(product_name)
                        print("\n")

                    elif choose == 4:
                        break

                    else:
                        print("\n____Invalid Input! Please enter a valid option.____\n")

                except ValueError:
                    print("\n____Invalid Input! Please enter a valid number.____\n")

        elif choice == 5:
            print("\n", " " * 20, "____YOUR REPORT____\n")

            while True:
                print("1. Generate Full Report")
                print("2. Retrieve Records for a Specific Product")
                print("3. Return To The 'Main Page'")
                try:
                    choose = int(input("Enter your choice: N°_"))

                    if choose == 1:
                        print("\n", " " * 20, "____FULL REPORT____\n")
                        manage_report.generate_full_report()
                        print("\n")

                    elif choose == 2:
                        print("\n", " " * 20, "____SPECIFIC PRODUCT REPORT____\n")
                        product_name = input("Enter the name of the product: ")
                        manage_report.generate_product_report(product_name)
                        print("\n")

                    elif choose == 3:
                        break

                    else:
                        print("\n____Invalid Input! Please enter a valid option.____\n")

                except ValueError:
                    print("\n____Invalid Input! Please enter a valid number.____\n")

        elif choice == 6:
            print("\nEXITING....")
            break

        else:
            print("\n____Invalid Input! Please enter a valid option.____\n")

    except ValueError:
        print("\n____Invalid Input! Please enter a valid number.____\n")