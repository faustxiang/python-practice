pocket = int(input("Enter a pocket number (0-36): "))

if pocket >= 0 and pocket <= 36:
    if pocket == 0:
        print("The pocket is green.")
    elif pocket >= 1 and pocket <= 10:
        if pocket % 2 == 1:
            print("The pocket is red.")
        else:
            print("The pocket is black.")
    elif pocket >= 11 and pocket <= 18:
        if pocket % 2 == 1:
            print("The pocket is black.")
        else:
            print("The pocket is red.")
    elif pocket >= 19 and pocket <= 28:
        if pocket % 2 == 1:
            print("The pocket is red.")
        else:
            print("The pocket is black.")
    else:
        if pocket % 2 == 1:
            print("The pocket is black.")
        else:
            print("The pocket is red.")
else:
    print("Error: please enter a number from 0 to 36.")