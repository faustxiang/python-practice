quantity = int(input ("Enter the number of packages purchased: "))
if quantity >= 100:
    discount_rate = 0.40
elif quantity >= 50:
    discount_rate = 0.30
elif quantity >= 20:
    discount_rate = 0.20
elif quantity >= 10:
    discount_rate = 0.10
else:
    discount_rate = 0
subtotal = quantity * 99
discount_amount = subtotal * discount_rate
total = subtotal - discount_amount
print("Subtotal: $", format(subtotal, ".2f"))
print("Discount amount: $", format(discount_amount, ".2f"))
print("Total amount due: $", format(total, ".2f"))