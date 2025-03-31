# Stock Management System

## Overview
The **Stock Management System** is a command-line interface (CLI) application designed to help businesses efficiently track and manage their inventory. This system enables users to import products, record sales (exports), monitor stock levels, generate reports, and search for specific products, ensuring accurate and organized inventory management.

## Features
- **Product Importation:** Add new products to the inventory with details such as name, quantity, unit (KG, L, or Pcs), buying price, selling price, and import date.
- **Product Exportation:** Register sold products and update stock levels automatically.
- **Stock Management:** View, update, or remove products from the stock database.
- **Search Functionality:** Find specific products within the imports, exports, and stock records.
- **Report Generation:** Create reports summarizing stock activities, including imports, exports, and profit calculations.
- **User-Friendly Interface:** The menu-driven CLI approach makes navigation seamless.
- **Error Handling:** Prevents invalid inputs and ensures data accuracy.

## Installation
To install and run the Stock Management System, follow these steps:

1. Clone this repository:
```sh
git clone https://github.com/Christian-Regnante/stock_management_system.git
```
2. Navigate to the project directory:
```sh
cd stock_management_system
```
3. Ensure you have Python installed (version 3.x recommended).
4. Run the application:
```sh
python Optistock.py
```

## Usage
1. **Launch the application** and navigate the menu.
2. **Choose an option** to import products, export sales, check stock, search for items, or generate reports.
3. **Follow on-screen prompts** to enter necessary details.
4. **Review confirmations** and system-generated messages.
5. **Repeat or exit** when finished.

## Project Structure
```
stock-management-system/
│-- connection.py # Handles database connections
│-- Optistock.py # Main Program
│-- welcome_msg.py # ASCII Welcome message
│-- README.md # Project documentation
```

## Future Enhancements
- Implement a graphical user interface (GUI) for better usability.
- Add reminder functionality
- Automate the program to generate reports and save them.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

Happy coding!
