num = int(input("Enter the number of terms: "))

if num <= 0:
    print("Invalid input")

else:
    fib1, fib2 = 0, 1
    for i in range(num):
        print(fib1, end=" ")
        fib1, fib2 = fib2, fib1 + fib2
    print()