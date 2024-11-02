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

        # Create category tabs
        self.create_category_tab("Electronics")
        self.create_category_tab("Clothing")
        self.create_category_tab("Books")

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
        for i in range(20):
            product_label = tk.Label(product_frame, text=f"Product {i+1}")
            product_label.pack(pady=10)

        # Update canvas scroll region
        canvas.config(scrollregion=canvas.bbox("all"))

if __name__ == "__main__":
    app = ECommerceApp()
    app.mainloop()