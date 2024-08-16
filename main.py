import tkinter as tk
from tkinter import messagebox

class CafeBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Billing System")

        # Dictionary to store menu items and their prices
        self.menu = {"Coffee": 3.00, "Tea": 2.50, "Cake": 4.50, "Sandwich": 5.00}

        # Variables to store order details
        self.order_items = {}  # Dictionary to store item and its quantity
        self.total_amount = tk.DoubleVar()
        self.total_amount.set(0.0)

        # GUI components
        self.create_gui()

    def create_gui(self):
        # Menu Label
        menu_label = tk.Label(self.root, text="Menu", font=("Helvetica", 16))
        menu_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Menu Listbox
        self.menu_listbox = tk.Listbox(self.root, height=len(self.menu), selectmode="multiple")
        for item in self.menu:
            self.menu_listbox.insert(tk.END, f"{item} - ${self.menu[item]:.2f}")
        self.menu_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Order Label
        order_label = tk.Label(self.root, text="Your Order", font=("Helvetica", 16))
        order_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Order Listbox
        self.order_listbox = tk.Listbox(self.root, height=10)
        self.order_listbox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Quantity Label
        quantity_label = tk.Label(self.root, text="Quantity:")
        quantity_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Quantity Entry
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        # Add to Order Button
        add_button = tk.Button(self.root, text="Add to Order", command=self.add_to_order)
        add_button.grid(row=3, column=0, padx=10, pady=10)

        # Calculate Total Button
        calculate_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        calculate_button.grid(row=3, column=1, padx=10, pady=10)

        # Total Amount Label
        total_label = tk.Label(self.root, text="Total Amount: $", font=("Helvetica", 12))
        total_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        # Total Amount Display
        total_display = tk.Label(self.root, textvariable=self.total_amount, font=("Helvetica", 12))
        total_display.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    def add_to_order(self):
        selected_items = [self.menu_listbox.get(index) for index in self.menu_listbox.curselection()]

        for item in selected_items:
            item_name = item.split(" - ")[0]
            quantity = int(self.quantity_entry.get())
            if item_name in self.order_items:
                self.order_items[item_name] += quantity
            else:
                self.order_items[item_name] = quantity
            self.order_listbox.insert(tk.END, f"{item_name} x{quantity}")

    def calculate_total(self):
        total = sum(self.menu[item] * quantity for item, quantity in self.order_items.items())
        self.total_amount.set(f"{total:.2f}")

        # Display a message box with the receipt
        receipt = "\n".join([f"{item} x{quantity} - ${self.menu[item] * quantity:.2f}" for item, quantity in self.order_items.items()])
        messagebox.showinfo("Receipt", f"Your Order:\n{receipt}\nTotal Amount: ${total:.2f}")

        # Clear order details
        self.order_items = {}
        self.order_listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    cafe_app = CafeBillingSystem(root)
    root.mainloop()
