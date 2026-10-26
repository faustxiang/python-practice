meal = float(input("Enter the charge for the meal: "))
tip = meal * 0.18
tax = meal * 0.07
total = meal + tip + tax
print("The tip is: $", format(tip, ".2f"))  
print("The tax is: $", format(tax, ".2f"))
print("The total is: $", format(total, ".2f"))