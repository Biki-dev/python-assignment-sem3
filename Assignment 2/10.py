num = int(input("Enter a number: "))

if num <= 0 or num % 2 == 0:
    print("Invalid! Enter a positive odd number.")

else:
    # Upper half
    for i in range(1, (num // 2) + 2):
        spaces = (num // 2) - (i - 1)
        stars = 2 * i - 1

        for j in range(spaces):
            print(" ", end="")
        for k in range(stars):
            print("*", end="")

        print()

    # Lower half
    for i in range(num // 2, 0, -1):
        spaces = (num // 2) - (i - 1)
        stars = 2 * i - 1

        for j in range(spaces):
            print(" ", end="")
        for k in range(stars):
            print("*", end="")

        print()