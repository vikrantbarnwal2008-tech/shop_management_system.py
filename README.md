# Shop Management System

## Overview
The **Shop Management System** is a desktop-based Graphical User Interface (GUI) application designed to streamline inventory tracking and billing for a small technical electronics shop. This project provides a digital solution to replace manual bookkeeping, allowing users to view available products, manage a shopping cart, and generate accurate bills dynamically.

## Features
* **Inventory Display:** View a structured list of products including Item Name, Price, and Live Stock levels.
* **Stock Management:** Real-time updates to inventory stock as items are added to the cart to prevent overselling.
* **Shopping Cart System:** * Add items to the cart with specific quantities.
    * Automatic cost calculation per item based on quantity.
* **Validation & Error Handling:**
    * Prevents entering negative or non-numeric quantities.
    * Prevents adding more items than currently available in stock.
    * Alerts the user if they try to bill an empty cart.
* **Billing Generation:** Generates a formatted text-based receipt displaying all items, quantities, prices, and the grand total.

## Technologies/Tools Used
* **Programming Language:** Python 3.x
* **GUI Framework:** Tkinter (Python standard library)
    * `ttk.Treeview` for tabular data display.
    * `messagebox` for alerts and receipts.

## Steps to Install & Run the Project
1.  **Prerequisites:** Ensure you have Python installed on your system. You can check this by running:
    ```bash
    python --version
    ```
2.  **Download:** Download the `main.py` file (or clone this repository).
3.  **Run the Application:**
    Open your terminal or command prompt, navigate to the project directory, and run:
    ```bash
    python main.py
    ```
    *(Note: Replace `main.py` with the actual name of your python file if different).*

## Instructions for Testing
To verify the functionality of the application, follow these test scenarios:

1.  **Happy Path (Normal Flow):**
    * Select "Gaming Mouse" from the inventory.
    * Enter Quantity `2`.
    * Click "Add to Cart".
    * *Result:* Item appears in the cart, total updates, and inventory stock decreases by 2.

2.  **Input Validation Test:**
    * Select an item.
    * Enter `-5` or `abc` in the Quantity field.
    * Click "Add to Cart".
    * *Result:* An "Input Error" popup appears requesting a valid positive number.

3.  **Stock Limit Test:**
    * Select "HD Monitor" (Stock: 5).
    * Enter Quantity `10`.
    * Click "Add to Cart".
    * *Result:* An "Out of Stock" popup appears indicating only 5 are available.

4.  **Billing Test:**
    * Add items to the cart.
    * Click "Generate Bill".
    * *Result:* A receipt popup appears with the correct itemized list and Grand Total.
