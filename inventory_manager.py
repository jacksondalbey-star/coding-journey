import json

DATA_FILE = "inventory.json"


class sku:
    """Case-insensitive product SKU value object."""

    def __init__(self, value):
        value = str(value).strip()
        if not value:
            raise ValueError("SKU cannot be empty")
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"sku({self.value!r})"

    def __eq__(self, other):
        if isinstance(other, sku):
            other = other.value
        return self.value.casefold() == str(other).strip().casefold()

    def __hash__(self):
        return hash(self.value.casefold())


def load_inventory():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


products = load_inventory()


def save_inventory():
    with open(DATA_FILE, "w") as file:
        json.dump(products, file, indent=4)


def show_menu():
    print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
    print("1. Add a product")
    print("2. View all products")
    print("3. Update product quantity")
    print("4. Search for a product")
    print("5. Remove a product")
    print("6. View low-stock products")
    print("7. Exit")


def add_product():
    name = input("Product name: ").strip()
    sku = input("Product ID: ").strip()
    for existing_product in products:
        if existing_product["sku"].lower() == sku.lower():
            print("That Product ID already exists.")
            return

    try:
        quantity = int(input("Quantity: "))
        price = float(input("Price per item: $"))

        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative.")
            return
    except ValueError:
        print("Please enter valid numbers.")
        return

    product = {
        "name": name,
        "sku": sku,
        "quantity": quantity,
        "price": price
    }

    products.append(product)
    save_inventory()
    print("Product added successfully!")


def view_products():
    if not products:
        print("No products are currently stored.")
        return

    print("\n=== CURRENT INVENTORY ===")

    for product in products:
        total_value = product["quantity"] * product["price"]

        print(
            f"ID: {product['sku']} | "
            f"Product: {product['name']} | "
            f"Quantity: {product['quantity']} | "
            f"Price: ${product['price']:.2f} | "
            f"Value: ${total_value:.2f}"
        )


def update_quantity():
    sku = input("Enter the Product ID to update: ").strip()

    for product in products:
        if product["sku"].lower() == sku.lower():
            try:
                new_quantity = int(input("Enter the new quantity: "))

                if new_quantity < 0:
                    print("Quantity cannot be negative.")
                    return

                product["quantity"] = new_quantity
                save_inventory()
                print("Quantity updated successfully!")
                return
            except ValueError:
                print("Please enter a valid whole number.")
                return

    print("Product not found.")


def search_product():
    query = input("Enter a product name or ID: ").strip().lower()
    matches = [
        product for product in products
        if query in product["name"].lower() or query in product["sku"].lower()
    ]
    if not matches:
        print("Product not found.")
        return

    for product in matches:
        print(
            f"ID: {product['sku']} | Product: {product['name']} | "
            f"Quantity: {product['quantity']} | Price: ${product['price']:.2f}"
        )


def remove_product():
    sku = input("Enter the Product ID to remove: ").strip()
    for product in products:
        if product["sku"].lower() == sku.lower():
            products.remove(product)
            save_inventory()
            print("Product removed successfully!")
            return
    print("Product not found.")


def view_low_stock():
    try:
        threshold = int(input("Show products with quantity at or below: "))
        if threshold < 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid non-negative whole number.")
        return

    low_stock = [product for product in products if product["quantity"] <= threshold]
    if not low_stock:
        print("No low-stock products found.")
        return

    for product in low_stock:
        print(
            f"ID: {product['sku']} | Product: {product['name']} | "
            f"Quantity: {product['quantity']}"
        )

def remove_product():
    sku = input("Enter the Product ID to remove: ").strip()

    for index, product in enumerate(products):
        if product["sku"].lower() == sku.lower():
            confirmation = input(
                f"Delete {product['name']}? Enter yes or no: "
            ).strip().lower()

            if confirmation == "yes":
                removed = products.pop(index)
                save_inventory()
                print(f"Removed: {removed['name']}")
            else:
                print("Removal cancelled.")
            return

    print("Product not found.")


def view_low_stock():
    low_stock_products = []

    for product in products:
        if product["quantity"] <= 5:
            low_stock_products.append(product)

    if not low_stock_products:
        print("No products are currently low in stock.")
        return

    print("\n=== LOW-STOCK PRODUCTS ===")

    for product in low_stock_products:
        print(
            f"ID: {product['sku']} | "
            f"Product: {product['name']} | "
            f"Quantity: {product['quantity']}"
        )


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        update_quantity()
    elif choice == "4":
        search_product()
    elif choice == "5":
        remove_product()
    elif choice == "6":
        view_low_stock()
    elif choice == "7":
        print("Inventory manager closed.")
        break
    elif choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Please choose an option from 1 to 7.")