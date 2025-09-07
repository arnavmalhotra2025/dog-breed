

dog1 = {
    "breed": "Golden Retriever",
    "color": "Golden",
    "name": "Buddy"
}


dog2 = {
    "breed": "German Shepherd",
    "color": "Black and Tan",
    "name": "Max"
}


animals = [dog1, dog2]


print("Dog 1:")
for key, value in dog1.items():
    print(f"  {key.capitalize()}: {value}")

print("\nDog 2:")
for key, value in dog2.items():
    print(f"  {key.capitalize()}: {value}")


print("\nComparison Results:")
if dog1["breed"] == dog2["breed"]:
    print("Both dogs are of the same breed.")
else:
    print("The dogs are of different breeds.")

if dog1["color"] == dog2["color"]:
    print("Both dogs have the same color.")
else:
    print("The dogs have different colors.")