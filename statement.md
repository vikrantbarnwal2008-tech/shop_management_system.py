# Shop Management System

## Problem Statement
Small retail businesses often struggle with manual inventory tracking and billing processes, leading to calculation errors, slow customer service, and discrepancies between actual stock and recorded stock. There is a need for a simplified, digital solution that automates the billing process while maintaining real-time visibility of available inventory to prevent selling out-of-stock items.

## Scope of the Project
The project involves developing a desktop-based Graphical User Interface (GUI) application using Python and Tkinter. 
* **In-Scope:** * Displaying a pre-defined inventory of technical products (e.g., Gaming Mouse, Keyboards).
    * Handling user inputs for item quantity selection.
    * Validating stock availability before adding items to the cart.
    * Real-time calculation of bills and total amounts.
    * Generating a digital receipt summary.
* **Out-of-Scope:** * Persistent database storage (currently using runtime memory).
    * User authentication or multi-user login roles.
    * Integration with physical hardware (barcode scanners/printers).

## Target Users
* **Shop Owners:** Who need to monitor stock levels and pricing.
* **Billing Clerks:** Who require a fast and accurate interface to process customer purchases.
* **Small Electronics Retailers:** Specifically those transitioning from paper-based logs to digital systems.

## High-Level Features
1.  **Interactive Inventory Dashboard:** A visual display of all available products, their unit prices, and current stock levels using a Treeview table.
2.  **Smart Cart Management:** Allows users to add specific quantities of items to a shopping cart with automated checks to ensure requested quantities do not exceed available stock.
3.  **Real-Time Stock Updates:** Automatically decrements inventory counts the moment an item is added to the cart to maintain data integrity during the session.
4.  **Automated Billing Engine:** Calculates line-item totals and the grand total dynamically as items are added.
5.  **Receipt Generation:** Produces a formatted text-based bill summary via a pop-up window, displaying bought items, quantities, and the final payable amount.
