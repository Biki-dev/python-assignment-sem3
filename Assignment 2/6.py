num = int(input("Enter a +ve number: "))
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print("The sum of the digits is:", total)