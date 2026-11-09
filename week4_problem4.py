number = int(input("Enter a number (1-10): "))

if number >= 1 and number <= 10:
    if number == 1:
        print("The Roman numeral is I")
    elif number == 2:
        print("The Roman numeral is II")
    elif number == 3:
        print("The Roman numeral is III")
    elif number == 4:
        print("The Roman numeral is IV")
    elif number == 5:
        print("The Roman numeral is V")
    elif number == 6:
        print("The Roman numeral is VI")
    elif number == 7:
        print("The Roman numeral is VII")
    elif number == 8:
        print("The Roman numeral is VIII") 
    elif number == 9:
        print("The Roman numeral is IX")
    elif number == 10:
        print("The Roman numeral is X")

else:
    print("Error: please enter a number from 1 to 10.")