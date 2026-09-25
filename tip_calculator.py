print("Hello, Jackson! My coding journey starts here.")
print("I am learning python")
name = input("What is your name? ")
print("Hello, " + name + "!")
print("Welcome, Jackson! Let's learn Python.")
try:
    bill = float(input("Enter the bill amount: $"))
except ValueError:
    print("Please enter a valid number.")
    quit()
tip_percent = float(input("Tip percentage? Enter 15 for 15%: "))
tip = bill * tip_percent / 100
tax_percent = float(input("Sales tax percentage? Enter 7 for 7%: "))
tax = bill * tax_percent / 100
print(f"Tax: ${tax:.2f}")
print(f"Tip: ${tip:.2f}")
total = bill + tip + tax
print(f"Total including tip and tax: ${total:.2f}")
people = int(input("How many people are splitting the bill? "))

if people > 0:
    per_person = total / people
    print(f"Each person pays: ${per_person:.2f}")
else:
    print("Please enter at least one person.")