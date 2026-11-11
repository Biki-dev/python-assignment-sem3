num = int(input("Enter a number: "))

if num <= 0:
    print("Invalid input")
else:
    steps = 0
    print(num, end=" ")
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        print(num, end=" ")
        steps += 1
    print("\nTotal steps:", steps)