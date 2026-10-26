color1 = input("Enter the first primary color: ").lower()
color2 = input("Enter the second primary color: ").lower()
if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("The resulting color is purple.")
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("The resulting color is orange.")
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print("The resulting color is green.")
else:
    print("Invalid input. Please enter two primary colors (red, blue, yellow).")