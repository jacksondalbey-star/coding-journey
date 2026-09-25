def show_menu():
    print("\n=== PERSONAL EXPENSE TRACKER ===")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. Delete an expense")
    print("5. Exit")
    print("6. View totals by category")

import json

DATA_FILE = "expenses.json"
def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


expenses = load_expenses()

def save_expenses():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)



def add_expense():
    description = input("Expense description: ")
    category = input("Category: ")
    while True:
        try:
            amount = float(input("Amount: $"))
            if amount > 0:
                break
            print("Amount must be greater than $0.")
        except ValueError:
            print("Please enter a valid amount.")

    expenses.append({
        "description": description,
        "category": category,
        "amount": amount,
    })
    save_expenses()
    print("Expense added successfully!")

def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("Enter the expense number to delete: "))
        deleted = expenses.pop(number - 1)
        save_expenses()
        print(f"Deleted: {deleted['description']}")
    except (ValueError, IndexError):
        print("Please enter a valid expense number.")


def view_expenses():
    if not expenses:
        print("No expenses have been added.")
        return

    print("\n=== ALL EXPENSES ===")
    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['description']} | "
            f"{expense['category']} | ${expense['amount']:.2f}"
        )


def view_total_spending():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ${total:.2f}")
def view_category_totals():
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    if not category_totals:
        print("No expenses have been added.")
        return

    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total_spending()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        print("Expense tracker closed.")
        break
    elif choice == "6":
        view_category_totals()
    else:
        print("Please choose an option from 1 to 6.")
    
  


