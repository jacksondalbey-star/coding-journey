print("Hello, Jackson! My coding journey starts here.")
print("I am learning python")
name = input("What is your name? ")
print("Hello, " + name + "!")
print("Welcome, Jackson! Let's learn Python.")
while True:
    try:
        bill = float(input("Enter the bill amount: $"))
        break
    except ValueError:
        print("Please enter a valid number.")
while True:
    try:
        tip_percent = float(input("Tip percentage? Enter 15 for 15%: "))
        break
    except ValueError:
        print("Please enter a valid tip percentage.")

tip = bill * tip_percent / 100
while True:
    try:
        tax_percent = float(input("Sales tax percentage? Enter 7 for 7%: "))
        break
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