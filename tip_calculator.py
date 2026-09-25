print("Hello, Jackson! My coding journey starts here.")
print("I am learning python")
name = input("What is your name? ")
print("Hello, " + name + "!")
print("Welcome, Jackson! Let's learn Python.")
bill = float(input("How much was your bill? "))
tip_percent = float(input("Tip percentage? Enter 15 for 15%: "))
tip = bill * tip_percent / 100
print(f"Tip: ${tip:.2f}")
total = bill + tip
print(f"Total including tip: ${total:.2f}")