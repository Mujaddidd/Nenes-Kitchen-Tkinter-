import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# MenuItem class to store menu item details
class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

# Main Application class
class NenesKitchenOrderingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Nenes Kitchen Ordering System")
        self.root.geometry("800x600")
        self.cart = []

        # Sample menu items
        self.menu_items = [
            MenuItem("Thieboundienne", "Senegalese Jollof", 15.99),
            MenuItem("Yassa", "Sauted Onions ", 12.99),
            MenuItem("Attieke", "Fermentaed Casva", 9.99),
        ]

        # Load images and create ImageTk objects
        self.image1 = Image.open("image1.jpeg")
        self.image1 = self.image1.resize((100, 100), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.image2 = Image.open("image2.jpeg")
        self.image2 = self.image2.resize((100, 100), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.image2)

        self.create_menu()
        self.show_login()

    # Create the main menu for navigation
    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Home", command=self.show_home)
        file_menu.add_command(label="Login", command=self.show_login)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    # Display the login window
    def show_login(self):
        self.clear_frame()
        login_frame = tk.Frame(self.root)
        login_frame.pack(pady=100)

        # Display image1 in login window
        image_label = tk.Label(login_frame, image=self.photo1)
        image_label.grid(row=0, column=0, rowspan=3, padx=20)

        username_label = tk.Label(login_frame, text="Username")
        username_label.grid(row=0, column=1)
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.grid(row=0, column=2)

        password_label = tk.Label(login_frame, text="Password")
        password_label.grid(row=1, column=1)
        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=2)

        login_button = tk.Button(login_frame, text="Log In", command=self.login)
        login_button.grid(row=2, column=2)

    # Login validation and navigation to home window
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not self.validate_username(username) or not self.validate_password(password):
            messagebox.showerror("Error", "Invalid username or password.")
        else:
            self.show_home()

    # Function to validate the entered username
    def validate_username(self, username):
        if len(username) < 3 or len(username) > 20:
            return False
        return True

    # Function to validate the entered password
    def validate_password(self, password):
        if len(password) < 8 or len(password) > 50:
            return False
        return True

    # Display the home window with menu items
    def show_home(self):
        self.clear_frame()

        home_frame = tk.Frame(self.root)
        home_frame.pack(pady=20)

        # Display image2 in home window
        image_label = tk.Label(home_frame, image=self.photo2)
        image_label.grid(row=0)

        # Display image2 in home window
        image_label = tk.Label(home_frame, image=self.photo2)
        image_label.grid
        welcome_label = tk.Label(home_frame, text="Welcome to Nenes Kitchen!", font=("Helvetica", 16))
        welcome_label.grid(row=0, column=1)

        for i, item in enumerate(self.menu_items):
            item_label = tk.Label(home_frame, text=f"{item.name} - {item.description} - ${item.price}")
            item_label.grid(row=i+1, column=0)

            add_to_cart_button = tk.Button(home_frame, text="Add to Cart", command=lambda i=i: self.add_to_cart(i))
            add_to_cart_button.grid(row=i+1, column=1)

        proceed_button = tk.Button(home_frame, text="Proceed to Payment", command=self.show_payment)
        proceed_button.grid(row=len(self.menu_items)+1, column=1)

# Add an item to the cart
    def add_to_cart(self, item_index):
        self.cart.append(self.menu_items[item_index])
        messagebox.showinfo("Added", f"{self.menu_items[item_index].name} added to the cart.")

# Enter card payment information 
    def show_payment(self):
        self.clear_frame()

 # Create a new frame for the payment window
        payment_frame = tk.Frame(self.root)
        payment_frame.pack(pady=100)

 # Create and display the card number label and entry field
        card_number_label = tk.Label(payment_frame, text="Card Number")
        card_number_label.grid(row=0, column=0)
        self.card_number_entry = tk.Entry(payment_frame)
        self.card_number_entry.grid(row=0, column=1)

 # Create and display the CVV label and entry field
        cvv_label = tk.Label(payment_frame, text="CVV")
        cvv_label.grid(row=1, column=0)
        self.cvv_entry = tk.Entry(payment_frame)
        self.cvv_entry.grid(row=1, column=1)

# Create and display the pay button
        pay_button = tk.Button(payment_frame, text="Pay", command=self.process_payment)
        pay_button.grid(row=2, column=1)

# Process the payment and validate the entered details
    def process_payment(self):
        card_number = self.card_number_entry.get()
        cvv = self.cvv_entry.get()

        if not self.validate_card_number(card_number) or not self.validate_cvv(cvv):
            messagebox.showerror("Error", "Invalid card number or CVV.")
        else:
            self.show_confirmation()

    # Function to validate the entered card number
    def validate_card_number(self, card_number):
        if not re.match(r"^\d{13,16}$", card_number):
            return False
        return True

    # Function to validate the entered CVV
    def validate_cvv(self, cvv):
        if not re.match(r"^\d{3,4}$", cvv):
            return False
        return True

# Show the order confirmation window & Create a new frame for the confirmation window 
    def show_confirmation(self):
        self.clear_frame()

        confirmation_frame = tk.Frame(self.root)
        confirmation_frame.pack(pady=100)

# Create and display the order confirmation label
        confirmation_label = tk.Label(confirmation_frame, text="Order Confirmed!", font=("Helvetica", 16))
        confirmation_label.pack()

# Create and display the exit button
        exit_button = tk.Button(confirmation_frame, text="Exit", command=self.root.quit)
        exit_button.pack()

# Function to clear the existing frame, removing all widgets except the menu
    def clear_frame(self):
        for widget in self.root.winfo_children():
            if not isinstance(widget, tk.Menu):
                widget.destroy()

# Main function to initialize the application
if __name__ == "__main__":
    root = tk.Tk()
    app = NenesKitchenOrderingSystem(root)
    root.mainloop()

