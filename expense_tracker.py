def show_menu():
    print("\n=== PERSONAL EXPENSE TRACKER ===")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. Exit")


expenses = []


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
    print("Expense added successfully!")


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
        print("Expense tracker closed.")
        break
    else:
        print("Please choose an option from 1 to 4.")
    
  


