import mysql.connector
from mysql.connector import Error

# Connect to MySQL database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="908efb808296.7c3476c2.alu-cod.online",
            user="PLACIDE",
            port=36512,
            password="Placide12",
            db="inventory"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Create tables if they don't exist
def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS imports (
        product_name VARCHAR(255) PRIMARY KEY,
        quantity INT,
        buying_price DECIMAL(10, 2),
        total_buying_price DECIMAL(10, 2),
        import_date DATE
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exports (
        product_name VARCHAR(255) PRIMARY KEY,
        quantity INT,
        selling_price DECIMAL(10, 2),
        total_sold_price DECIMAL(10, 2),
        export_date DATE,
        profit_loss DECIMAL(10, 2)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stocked_products (
        product_name VARCHAR(255) PRIMARY KEY,
        remaining_quantity INT,
        selling_price DECIMAL(10, 2)
    )''')

    connection.commit()

# Automation function
def automate_operations(connection):
    print("\n____ AUTOMATION STARTED ____\n")
    cursor = connection.cursor()

    # Automate imports
    imports_data = [
        ("ProductA", 100, 10.5, "2023-10-01"),
        ("ProductB", 50, 20.0, "2023-10-02"),
    ]
    for product_name, quantity, buying_price, import_date in imports_data:
        total_buying_price = quantity * buying_price
        cursor.execute('''
        INSERT INTO imports (product_name, quantity, buying_price, total_buying_price, import_date)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            quantity = quantity + VALUES(quantity), 
            total_buying_price = total_buying_price + VALUES(total_buying_price)''', 
        (product_name, quantity, buying_price, total_buying_price, import_date))
        
        cursor.execute('''
        INSERT INTO stocked_products (product_name, remaining_quantity, selling_price)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            remaining_quantity = remaining_quantity + VALUES(remaining_quantity), 
            selling_price = VALUES(selling_price)''', 
        (product_name, quantity, buying_price))
    print("Automated imports completed.")

    # Automate exports
    exports_data = [
        ("ProductA", 20, 15.0, "2023-10-03"),
        ("ProductB", 10, 25.0, "2023-10-04"),
    ]
    for product_name, quantity, selling_price, export_date in exports_data:
        cursor.execute("SELECT remaining_quantity FROM stocked_products WHERE product_name = %s", (product_name,))
        result = cursor.fetchone()
        if result and result[0] >= quantity:
            remaining_quantity = result[0]
            total_sold_price = quantity * selling_price

            cursor.execute("SELECT buying_price FROM imports WHERE product_name = %s", (product_name,))
            buying_price_result = cursor.fetchone()
            if buying_price_result:
                buying_price = buying_price_result[0]
                profit_loss = total_sold_price - (quantity * buying_price)

                cursor.execute('''
                UPDATE stocked_products
                SET remaining_quantity = remaining_quantity - %s
                WHERE product_name = %s''', (quantity, product_name))

                cursor.execute('''
                INSERT INTO exports (product_name, quantity, selling_price, total_sold_price, export_date, profit_loss)
                VALUES (%s, %s, %s, %s, %s, %s)''', 
                (product_name, quantity, selling_price, total_sold_price, export_date, profit_loss))
        else:
            print(f"Not enough stock to export {product_name}.")
    print("Automated exports completed.")

    connection.commit()
    cursor.close()
    print("\n____ AUTOMATION COMPLETED ____\n")

# Main program
connection = create_connection()
create_tables(connection)

# Add automation option to the main menu
while True:
    print("\n____ MAIN PAGE ____\n")

    print("1. Import Your Products")
    print("2. Export Your Sold Products")
    print("3. Check Your Stock")
    print("4. Get Report")
    print("5. Automate Operations")
    print("6. Exit")
    choice = int(input("Enter your choice: N°_"))

    if choice == 1:
        print("\n____IMPORTS____\n")

        while True:
            print("1. View Imported Products")
            print("2. Import New Product(s)")
            print("3. Delete Option for Imported Products")
            print("4. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM imports")
                rows = cursor.fetchall()
                print("Imported Products:")
                for row in rows:
                    print(row)
                

            elif choose == 2:
                product_name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                buying_price = float(input("Enter buying price: "))
                total_buying_price = quantity * buying_price
                import_date = input("Enter import date (YYYY-MM-DD): ")

                cursor = connection.cursor()
                cursor.execute('''
                INSERT INTO imports (product_name, quantity, buying_price, total_buying_price, import_date)
                VALUES (%s, %s, %s, %s, %s)''', (product_name, quantity, buying_price, total_buying_price, import_date))
                
                cursor.execute('''
                INSERT INTO stocked_products (product_name, remaining_quantity, selling_price)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                    remaining_quantity = remaining_quantity + VALUES(remaining_quantity), 
                    selling_price = VALUES(selling_price)''', 
                (product_name, quantity, buying_price))

                connection.commit()
                print(f"Product {product_name} imported successfully!")
                cursor.close()

            elif choose == 3:
                product_name = input("Enter product name to delete: ")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM imports WHERE product_name = %s", (product_name,))
                cursor.execute("DELETE FROM stocked_products WHERE product_name = %s", (product_name,))
                connection.commit()
                print(f"Product {product_name} deleted successfully!")
                cursor.close()

            elif choose == 4:
                break

        print("\n")
    
    elif choice == 2:
        print("\n____EXPORTS____\n")

        while True:
            print("1. View Exported Products")
            print("2. Export Sold Product(s)")
            print("3. Delete Option for Exported Products")
            print("4. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM exports")
                rows = cursor.fetchall()
                print("Exported Products:")
                for row in rows:
                    print(row)
                cursor.close()

            elif choose == 2:
                product_name = input("Enter product name: ")
                cursor = connection.cursor()
                cursor.execute("SELECT remaining_quantity FROM stocked_products WHERE product_name = %s", (product_name,))
                result = cursor.fetchone()

                if result:
                    remaining_quantity = result[0]
                    quantity = int(input("Enter quantity sold: "))

                    if quantity <= remaining_quantity:
                        selling_price = float(input("Enter selling price: "))
                        total_sold_price = quantity * selling_price
                        export_date = input("Enter export date (YYYY-MM-DD): ")

                        # Calculate profit/loss correctly
                        cursor.execute("SELECT buying_price FROM imports WHERE product_name = %s", (product_name,))
                        buying_price_result = cursor.fetchone()
                        if buying_price_result:
                            buying_price = buying_price_result[0]
                            profit_loss = total_sold_price - (quantity * buying_price)
                        else:
                            print("Buying price not found for the product.")
                            cursor.close()
                            continue

                        # Update stock
                        cursor.execute('''
                        UPDATE stocked_products
                        SET remaining_quantity = remaining_quantity - %s
                        WHERE product_name = %s''', (quantity, product_name))

                        # Insert the product into the exports table
                        cursor.execute('''
                        INSERT INTO exports (product_name, quantity, selling_price, total_sold_price, export_date, profit_loss)
                        VALUES (%s, %s, %s, %s, %s, %s)''', 
                        (product_name, quantity, selling_price, total_sold_price, export_date, profit_loss))
                        
                        connection.commit()
                        print(f"Product {product_name} exported successfully!")
                    else:
                        print("Not enough stock to fulfill the export.")
                else:
                    print("Product not found in stock.")
                cursor.close()

            elif choose == 3:
                product_name = input("Enter product name to delete: ")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM exports WHERE product_name = %s", (product_name,))
                connection.commit()
                print(f"Product {product_name} deleted successfully!")
                cursor.close()

            elif choose == 4:
                break

        print("\n")

    elif choice == 3:
        print("\n____YOUR STOCK____\n")

        while True:
            print("1. Check Your Stock")
            print("2. Delete Option for Products in the Stock")
            print("3. Update Option for Products in the Stock")
            print("4. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM stocked_products")
                rows = cursor.fetchall()
                print("Current Stock:")
                for row in rows:
                    print(f"Product: {row[0]}, Remaining Quantity: {row[1]}, Selling Price: {row[2]}")
                cursor.close()

            elif choose == 2:
                product_name = input("Enter product name to delete: ")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM stocked_products WHERE product_name = %s", (product_name,))
                connection.commit()
                print(f"Product {product_name} deleted successfully!")
                cursor.close()

            elif choose == 3:
                product_name = input("Enter product name to update: ")
                remaining_quantity = int(input("Enter new remaining quantity: "))
                selling_price = float(input("Enter new selling price: "))
                cursor = connection.cursor()
                cursor.execute('''
                INSERT INTO stocked_products (product_name, remaining_quantity, selling_price)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE remaining_quantity = VALUES(remaining_quantity), selling_price = VALUES(selling_price)''', 
                (product_name, remaining_quantity, selling_price))
                connection.commit()
                print(f"Product {product_name} updated successfully!")
                cursor.close()

            elif choose == 4:
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
                print("Generating Full Report...")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM imports")
                rows = cursor.fetchall()
                for row in rows:
                    product_name, quantity, buying_price, total_buying_price, import_date = row
                    cursor.execute("SELECT remaining_quantity FROM stocked_products WHERE product_name = %s", (product_name,))
                    remaining_quantity = cursor.fetchone()[0]
                    print(f"Product: {product_name}, Imported Quantity: {quantity}, Total Buying Price: {total_buying_price}, Remaining: {remaining_quantity}")
                cursor.close()

            elif choose == 2:
                product_name = input("Enter product name for report: ")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM imports WHERE product_name = %s", (product_name,))
                row = cursor.fetchone()
                if row:
                    quantity, buying_price, total_buying_price, import_date = row[1:]
                    cursor.execute("SELECT remaining_quantity FROM stocked_products WHERE product_name = %s", (product_name,))
                    remaining_quantity = cursor.fetchone()[0]
                    print(f"Product: {product_name}, Imported Quantity: {quantity}, Total Buying Price: {total_buying_price}, Remaining: {remaining_quantity}")
                else:
                    print("Product not found.")
                cursor.close()

            elif choose == 3:
                break

        print("\n")

    elif choice == 5:
        automate_operations(connection)

    elif choice == 6:
        print("\nEXITTING....")
        break

    else:
        print("\nWrong Input Please Try again!")

# Close the database connection
connection.close()
