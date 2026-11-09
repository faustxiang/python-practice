age = float(input("Enter the person's age: " ))
if age <= 1:
    print("The person is an infant.")
elif age >1 and age < 13:
    print("The person is a child.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20:
    print("The person is an adult.")