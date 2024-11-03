import tkinter as tk
from tkinter import ttk


class ECommerceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HOME ESSENTIALS App")
        self.geometry("800x600")

        # Create a Notebook for category tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Dictionary to store product information (name and quantity)
        self.products = {}

        # Create category tabs
        self.create_category_tab("VEGETABLES")
        self.create_category_tab("FRUITS")
        self.create_category_tab("MILK AND PRODUCTS")
        self.create_category_tab("EGGS")
        self.create_category_tab("MEAT")
        self.create_category_tab("LEAF POWDERS")
        self.create_category_tab("OILS")
        self.create_category_tab("SOLAR DRIED PRODUCTS")

    def create_category_tab(self, category_name):
        category_tab = ttk.Frame(self.notebook)
        self.notebook.add(category_tab, text=category_name)

        # Create a Scrollbar for products
        scrollbar = tk.Scrollbar(category_tab, orient=tk.HORIZONTAL)
        scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Create a Canvas to hold products
        canvas = tk.Canvas(category_tab, xscrollcommand=scrollbar.set)
        canvas.pack(fill=tk.BOTH, expand=True)

        # Configure Scrollbar
        scrollbar.config(command=canvas.xview)

        # Create a Frame to hold product items
        product_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=product_frame, anchor="nw")

        # Add product items to the frame
        for i, product_name in enumerate(f"Product {i+1}" for i in range(20)):
            self.products[product_name] = 0  # Initialize quantity to 0
            product_label = tk.Label(product_frame, text=product_name)
            product_label.bind("<Button-1>", lambda event, name=product_name: self.add_quantity(name))
            product_label.pack(pady=10)

            # Create a button for adding quantity
            quantity_button = tk.Button(product_frame, text="+", command=lambda name=product_name: self.add_quantity(name))
            quantity_button.pack(pady=10)

        # Update canvas scroll region
        canvas.config(scrollregion=canvas.bbox("all"))

    def add_quantity(self, product_name):
        self.products[product_name] += 1
        print(f"Added {product_name} to cart (Quantity: {self.products[product_name]})")  # Update based on your needs


if __name__ == "__main__":
    app = ECommerceApp()
    app.mainloop()