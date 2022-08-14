weight = float(input("Enter your weight: "))

unit = input("(L)bs or (K)gs: ").lower()

if unit != "l" and unit != "k":
    print("Enter a valid unit")
elif unit == "l":
    result = round(weight * 0.454, 2)
    print(f"You are {result} kgs")
else:
    result = round(weight * 2.205, 2)
    print(f"You are {result} lbs")