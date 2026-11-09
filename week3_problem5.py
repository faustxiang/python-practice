mass = float(input("Enter the object's mass in kilograms: "))
weight = mass * 9.8
print("The object's weight is:", weight, "Newtons.")
if weight > 500:
    print("The object is too heavy.")
elif weight < 100:
    print("The object is too light.")
else:
    print("The object has a normal weight.")