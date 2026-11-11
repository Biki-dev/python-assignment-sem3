n = int(input("Enter a number: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(f"The numbers you entered are: {numbers}")
print(f"The unique numbers are: {unique}")