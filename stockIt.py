#!/usr/bin/env python3

import os
import sys
import subprocess
import platform

class StockManager:
    def __init__(self):
        # Dynamically determine the script's directory
        self.script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.imports = {
            "product_name": ["quantity", "buying_price", "total_buying_price", "import_date"]
        }
        self.exports = {
            "product_name": ["quantity", "selling_price", "total_sold_price", "export_date", "Profit/loss"]
        }
        self.stocked_products = {
            "product_name": ["remaining_quantity", "selling_price", "total_selling_price"]
        }

    def main_menu(self):
        while True:
            print("\n____ MAIN PAGE ____\n")
            print("1. Import Your Products")
            print("2. Exports Your Sold Products")
            print("3. Check Your Stock")
            print("4. Get Report")
            print("5. Exit")
            choice = int(input("Enter your choice: N°_"))

            if choice == 1:
                self.import_menu()
            elif choice == 2:
                self.export_menu()
            elif choice == 3:
                self.stock_menu()
            elif choice == 4:
                self.report_menu()
            elif choice == 5:
                print("\nEXITTING....")
                break
            else:
                print("\nWrong Input Please Try again!")

    def import_menu(self):
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

    def export_menu(self):
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

    def stock_menu(self):
        print("\n____YOUR STOCK____\n")
        while True:
            print("1. Check Your Stock")
            # print("#. Delete Option for products in the stock")
            # print("#. Update Option for products in the stock")
            print("2. Return To The 'Main Page'")
            choose = int(input("Enter your choice: N°_"))

            if choose == 1:
                pass
            elif choose == 2:
                break
        print("\n")

    def report_menu(self):
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

    def set_working_hours(self):
        print("\n____ SET WORKING HOURS ____\n")
        start_hour = int(input("Enter your start hour (0-23): "))
        start_minute = int(input("Enter your start minute (0-59): "))
        end_hour = int(input("Enter your end hour (0-23): "))
        end_minute = int(input("Enter your end minute (0-59): "))
        frequency = int(input("Enter the frequency in hours (e.g., 1 for every hour): "))

        if (
            0 <= start_hour <= 23 and 0 <= start_minute <= 59 and
            0 <= end_hour <= 23 and 0 <= end_minute <= 59 and
            (start_hour < end_hour or (start_hour == end_hour and start_minute < end_minute))
        ):
            # Schedule the main cron job
            cron_expression = f"{start_minute} {start_hour}-{end_hour}/{frequency} * * *"
            script_path = os.path.abspath(sys.argv[0])
            log_path = os.path.join(self.script_dir, "stockIt.log")

            cron_command = f"{cron_expression} {script_path} >> {log_path} 2>&1"
            self.add_cron_job(cron_command)

            # Schedule the reminder 30 minutes before closing
            reminder_hour = end_hour
            reminder_minute = end_minute - 30
            if reminder_minute < 0:
                reminder_minute += 60
                reminder_hour -= 1
                if reminder_hour < 0:
                    reminder_hour = 23

            if platform.system() == "Windows" or platform.system() == "Linux":
                reminder_command = f"{reminder_minute} {reminder_hour} * * * python3 -c \"print('Reminder: Closing in 30 minutes!')\""
            else:
                reminder_command = f"{reminder_minute} {reminder_hour} * * * echo 'Reminder: Closing in 30 minutes!'"
            self.add_cron_job(reminder_command)

        else:
            print("Invalid input. Please try again.")

    def add_cron_job(self, cron_command):
        if platform.system() == "Linux":
            print("\nAdding the following cron job:")
            print(cron_command)
            subprocess.run(f'(crontab -l; echo "{cron_command}") | crontab -', shell=True, check=True)
            print("Cron job added successfully!")
        elif platform.system() == "Windows":
            print("\nWindows detected. Please use Task Scheduler to set up the following task manually:")
            print(cron_command)
        else:
            print("\nUnsupported operating system. Please set up the following task manually:")
            print(cron_command)

if __name__ == "__main__":
    manager = StockManager()
    print("Do you want to set working hours for automation? (yes/no)")
    if input().strip().lower() == "yes":
        manager.set_working_hours()
    manager.main_menu()