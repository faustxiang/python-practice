pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))
total_cents = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25)
if total_cents == 100:
    print("Congratulations! You have exactly one dollar.")
elif total_cents < 100:
    print("You have less than one dollar.")
else:
    print("You have more than one dollar.")