vegetarian = input("Is anyone in your party a vegetarian? ").lower()
vegan = input("Is anyone in your party a vegan? ").lower()
gluten = input("Is anyone in your party gluten-free? ").lower()

print("Here are your restaurant choices:")

if vegan == "no":
    if vegetarian == "no" and gluten == "no":
        print("   Joe's Gourmet Burgers")
    print("   Main Street Pizza Company")

print("   Corner Cafe")

if vegan == "no":
    if gluten == "no":
        print("   Mama's Fine Italian")

print("   The Chef's Kitchen")