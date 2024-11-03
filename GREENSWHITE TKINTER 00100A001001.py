import tkinter as tk
from tkinter import ttk


class ECommerceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HOME ESSENTIALS App")
        self.geometry("800x600")

        # Dictionary to store product information by category (nested dictionary)
        self.products = {}
        self.button_map = {}  # Class-level dictionary to store button mappings

        # Create a Notebook for category tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create category tabs
        self.create_category_tab("VEGETABLES")
        self.create_category_tab("FRUITS")
        self.create_category_tab("MILK AND PRODUCTS")
        self.create_category_tab("EGGS")
        self.create_category_tab("MEAT")
        self.create_category_tab("LEAF POWDERS")
        self.create_category_tab("OILS")
        self.create_category_tab("SOLAR DRIED PRODUCTS")

        # Create a frame for the cart
        self.cart_frame = tk.Frame(self)
        self.cart_frame.pack(fill=tk.X)

        # Create a label for the cart title
        self.cart_label = tk.Label(self.cart_frame, text="Cart:")
        self.cart_label.pack()

        # Create a listbox for each category in the cart frame
        self.category_cart_listboxes = {}
        for category in self.products.keys():
            listbox = tk.Listbox(self.cart_frame)
            listbox.pack(fill=tk.Y, expand=True)
            self.category_cart_listboxes[category] = listbox

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
            self.products.setdefault(category_name, {})
            self.products[category_name][product_name] = 0  # Initialize quantity to 0

            product_label = tk.Label(product_frame, text=product_name)
            product_label.bind("<Button-1>", lambda event, name=product_name: self.add_quantity(name, category_name))
            product_label.pack(pady=10)

            # Create a frame for buttons
            button_frame = tk.Frame(product_frame)
            button_frame.pack(pady=5)

            # Create a button for adding quantity
            quantity_button_add = tk.Button(button_frame, text="+", command=lambda name=product_name: self.add_quantity(name, category_name))
            quantity_button_add.pack(side=tk.RIGHT)

            # Create a button for removing quantity (initially disabled)
            quantity_button_remove = tk.Button(button_frame, text="-", state=tk.DISABLED, command=lambda name=product_name: self.remove_quantity(name, category_name))
            quantity_button_remove.pack(side=tk.RIGHT)

            # Map product to its remove button for specific category
            self.button_map[(product_name, category_name)] = quantity_button_remove

        # Update canvas scroll region
        canvas.config(scrollregion=canvas.bbox("all"))

    def add_quantity(self, product_name, category_name):
        if category_name not in self.products:
            self.products[category_name] = {}
        self.products[category_name][product_name] += 1
        self.update_cart_list()
        self.update_button_states((product_name, category_name))
        print(f"Added {product_name} to {category_name} cart (Quantity: {self.products[category_name][product_name]})")

    def remove_quantity(self, product_name, category_name):
        if category_name in self.products and product_name in self.products[category_name]:
            self.products[category_name][product_name] -= 1
            if self.products[category_name][product_name] == 0:
                del self.products[category_name][product_name]
            self.update_cart_list()
            self.update_button_states((product_name, category_name))
            print(f"Removed {product_name} from {category_name} cart (Quantity: {self.products[category_name].get(product_name, 0)})")

    # def update_cart_list(self):
    #     for category, products in self.products.items():
    #         listbox = self.category_cart_listboxes[category]
    #         listbox.delete(0, tk.END)
    #         for product, quantity in products.items():
    #             listbox.insert(tk.END, f"{product} (Qty: {quantity})")
    def update_cart_list(self):
        for category, products in self.products.items():
            listbox = self.category_cart_listboxes[category]
            listbox.delete(0, tk.END)
            for product, quantity in products.items():
                if quantity > 0:  # Only add products with positive quantity
                    listbox.insert(tk.END, f"{product} (Qty: {quantity})")

    def update_button_states(self, product_category_tuple):
        product_name, category_name = product_category_tuple
        button = self.button_map[(product_name, category_name)]
        if self.products[category_name].get(product_name, 0) > 0:
            button.config(state=tk.NORMAL)
        else:
            button.config(state=tk.DISABLED)


if __name__ == "__main__":
    app = ECommerceApp()
    app.mainloop()