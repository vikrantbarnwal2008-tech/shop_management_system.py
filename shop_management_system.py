import tkinter as tk
from tkinter import ttk, messagebox

class ShopManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Shop Management System")
        self.root.geometry("1000x600")
        
        self.products = {
            "Gaming Mouse": {"price": 2500, "stock": 10},
            "Mechanical Keyboard": {"price": 4500, "stock": 15},
            "HD Monitor": {"price": 12000, "stock": 5},
            "USB-C Cable": {"price": 500, "stock": 50},
            "Headphones": {"price": 3000, "stock": 8},
            "Webcam": {"price": 4000, "stock": 12}
        }
        
        
        self.cart_items = []
        self.total_bill_amount = 0

       
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=('Arial', 10), rowheight=25)
        style.configure("Treeview.Heading", font=('Arial', 11, 'bold'))

        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        title_label = tk.Label(header_frame, text="Tech Shop Inventory & Billing",font=("Helvetica", 24, "bold"), bg="#2c3e50", fg="white")
        title_label.pack(pady=20)

       
        content_frame = tk.Frame(self.root, padx=20, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)

        
        left_frame = tk.LabelFrame(content_frame, text="Available Products", font=("Arial", 12, "bold"))
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

      
        cols = ("Item Name", "Price", "Stock Left")
        self.inventory_tree = ttk.Treeview(left_frame, columns=cols, show='headings', height=15)
        self.inventory_tree.heading("Item Name", text="Item Name")
        self.inventory_tree.heading("Price", text="Price (₹)")
        self.inventory_tree.heading("Stock Left", text="Stock Left")
        self.inventory_tree.column("Item Name", width=150)
        self.inventory_tree.column("Price", width=80)
        self.inventory_tree.column("Stock Left", width=80)
        self.inventory_tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
       
        self.refresh_inventory()

      
        control_frame = tk.Frame(left_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(control_frame, text="Quantity:").pack(side=tk.LEFT, padx=5)
        self.qty_entry = tk.Entry(control_frame, width=10)
        self.qty_entry.pack(side=tk.LEFT, padx=5)
        
        add_btn = tk.Button(control_frame, text="Add to Cart", bg="#27ae60", fg="white",command=self.add_to_cart, font=("Arial", 10, "bold"))
        add_btn.pack(side=tk.LEFT, padx=20)

        
        right_frame = tk.LabelFrame(content_frame, text="Current Cart", font=("Arial", 12, "bold"))
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)

       
        cart_cols = ("Item", "Qty", "Total")
        self.cart_tree = ttk.Treeview(right_frame, columns=cart_cols, show='headings', height=15)
        self.cart_tree.heading("Item", text="Item")
        self.cart_tree.heading("Qty", text="Qty")
        self.cart_tree.heading("Total", text="Total (₹)")
        self.cart_tree.column("Item", width=140)
        self.cart_tree.column("Qty", width=50)
        self.cart_tree.column("Total", width=80)
        self.cart_tree.pack(fill=tk.BOTH, expand=True, pady=10)

      
        footer_frame = tk.Frame(right_frame)
        footer_frame.pack(fill=tk.X, pady=10)

        self.total_label = tk.Label(footer_frame, text="Total: ₹0.0", font=("Arial", 14, "bold"), fg="#c0392b")
        self.total_label.pack(side=tk.TOP, pady=5)

        bill_btn = tk.Button(footer_frame, text="Generate Bill", bg="#2980b9", fg="white",command=self.generate_bill, font=("Arial", 12, "bold"), width=20)
        bill_btn.pack(side=tk.TOP, pady=10)

    def refresh_inventory(self):
        
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)
        
        for name, details in self.products.items():
            self.inventory_tree.insert("", tk.END, values=(name, details['price'], details['stock']))

    def add_to_cart(self):
       
        
   
        selected_item_id = self.inventory_tree.selection()
        if not selected_item_id:
            messagebox.showwarning("Selection Error", "Please select an item from the inventory list.")
            return
        
        item_values = self.inventory_tree.item(selected_item_id)['values']
        item_name = item_values[0]
        current_stock = int(item_values[2])
        item_price = float(item_values[1])

        
        try:
            qty_requested = int(self.qty_entry.get())
            if qty_requested <= 0:
                raise ValueError("Negative or Zero")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid positive number for quantity.")
            return

      
        if qty_requested > current_stock:
            messagebox.showerror("Out of Stock", f"Only {current_stock} units of {item_name} available!")
            return

  
        self.products[item_name]['stock']=self.products[item_name]['stock']-qty_requested
        
       
        total_cost = item_price * qty_requested
        
    
        self.cart_items.append({
            "name": item_name,
            "qty": qty_requested,
            "total": total_cost
        })
        self.total_bill_amount += total_cost


        self.refresh_inventory() # Updates the stock number in the left panel
        self.cart_tree.insert("", tk.END, values=(item_name, qty_requested, total_cost))
        self.total_label.config(text=f"Total: ₹{self.total_bill_amount:.2f}")
        
 
        self.qty_entry.delete(0, tk.END)

    def generate_bill(self):
  
        if not self.cart_items:
            messagebox.showinfo("Empty Cart", "No items to bill.")
            return

        bill_text = "====== SHOP RECEIPT ======\n\n"
        bill_text += f"{'Item':<20} {'Qty':<5} {'Price':<10}\n"
        bill_text += "-"*40 + "\n"
        
        for item in self.cart_items:
            bill_text += f"{item['name']:<20} {item['qty']:<5} ₹{item['total']:<10}\n"
            
        bill_text += "-"*40 + "\n"
        bill_text += f"GRAND TOTAL: ₹{self.total_bill_amount:.2f}\n"
        bill_text += "=========================="

   
        messagebox.showinfo("Bill Generated", bill_text)

        self.cart_items = []
        self.total_bill_amount = 0.0
        for item in self.cart_tree.get_children():
            self.cart_tree.delete(item)
        self.total_label.config(text="Total: ₹0.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShopManagementSystem(root)
    root.mainloop()
