heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))

if heads < 0 or legs < 0 or legs % 2 != 0 or legs < 2 * heads or legs > 4 * heads:
    print("Invalid input")
else:
    dogs = (legs - 2 * heads) // 2
    chickens = heads - dogs

    print("Dogs:", dogs)
    print("Chickens:", chickens)