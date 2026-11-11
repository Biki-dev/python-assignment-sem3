num = int(input("Enter a number: "))
isPrime = True
if num <= 1:
    isPrime = False
else:
    # Upto square root of the number, beyond that, factors will repeat if it have any
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isPrime = False
            break

if isPrime:
    print("The number is prime.")
else:
    print("The number is not prime.")