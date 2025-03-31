# Stock Management System

## Overview
The **Stock Management System** is a command-line application designed to help users manage product stock, track imports and exports, and generate reports. The application allows users to automate stock-related tasks and set reminders using cron jobs.

## Features
- **Product Import:** Add new products to inventory with quantity, price, and timestamp.
- **Product Export:** Register sold products and calculate profits or losses.
- **Stock Tracking:** Check available stock and pricing details.
- **Reports:** Generate detailed stock and sales reports.
- **Automation:** Set working hours and automate stock reminders using cron jobs (Linux) or manual scheduling (Windows).

## Installation
### Prerequisites
- Python 3.x installed
- Linux or Windows operating system

### Clone the Repository
```sh
git clone https://github.com/your-repo/stock-management.git
cd stock-management
```

### Run the Script
```sh
python3 stock_manager.py
```

## Usage
### Main Menu
When you run the script, you'll see the following options:
1. Import Your Products
2. Export Sold Products
3. Check Your Stock
4. Get Report
5. Exit

### Importing Products
1. Choose "Import Your Products" from the main menu.
2. Select "Import New Product(s)".
3. Enter product details (name, quantity, buying price).
4. Product gets stored with a timestamp.

### Exporting Products
1. Choose "Export Sold Products" from the main menu.
2. Select "Export Sold Product(s)".
3. Enter product details (name, quantity, selling price).
4. The system calculates profit/loss automatically.

### Stock Management
- View available stock.
- Future enhancements may include updating and deleting stock items.

### Reports
- Generate full reports or product-specific reports.

### Automation
1. The system allows setting working hours.
2. Creates cron jobs for automated stock reminders (Linux users only).

## Platform Support
- **Linux:** Uses cron jobs for automation.
- **Windows:** Users must manually set up Task Scheduler for automation.

## Future Enhancements
- Database integration for storing product details.
- A graphical user interface (GUI).
- Stock update and deletion functionalities.

## License
This project is open-source and available under the MIT License.

## Author
Developed by **Gilbmura**.

## Contributions
Feel free to contribute by submitting issues or pull requests on GitHub!

