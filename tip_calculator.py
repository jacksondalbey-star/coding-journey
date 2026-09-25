print("Hello, Jackson! My coding journey starts here.")
print("I am learning python")
name = input("What is your name? ")
print("Hello, " + name + "!")
print("Welcome, Jackson! Let's learn Python.")
while True:
    try:
        bill = float(input("Enter the bill amount: $"))
        if bill > 0:
            break
        print("The bill must be greater than $0.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    try:
        tip_percent = float(input("Tip percentage? Enter 15 for 15%: "))
        if tip_percent >= 0:
            break
        print("Tip percentage cannot be negative.")
    except ValueError:
        print("Please enter a valid tip percentage.")
tip = bill * tip_percent / 100
while True:
    try:
        tax_percent = float(input("Sales tax percentage? Enter 7 for 7%: "))
        if tax_percent >= 0:
            break
        print("Sales tax percentage cannot be negative.")
    except ValueError:
        print("Please enter a valid sales-tax percentage.")

tax = bill * tax_percent / 100
print(f"Tax: ${tax:.2f}")
print(f"Tip: ${tip:.2f}")
total = bill + tip + tax
print(f"Total including tip and tax: ${total:.2f}")
while True:
    try:
        people = int(input("How many people are splitting the bill? "))
        if people > 0:
            break
        print("Please enter at least one person.")
    except ValueError:
        print("Please enter a whole number of people.")

per_person = total / people
print(f"Each person pays: ${per_person:.2f}")
print("\n" + "=" * 32)
print("          BILL SUMMARY")
print("=" * 32)
print(f"Customer:          {name}")
print(f"Original bill:     ${bill:.2f}")
print(f"Tip:               ${tip:.2f}")
print(f"Sales tax:         ${tax:.2f}")
print(f"Final total:       ${total:.2f}")
print(f"Number of people:  {people}")
print(f"Each person pays:  ${per_person:.2f}")
print("=" * 32)