n = int(input("Enter a number: "))
numbers = []
total = 0

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    total += num

print(f"The numbers you entered are: {numbers}")
print(f"The numbers in reverse order are: ", end="")

for i in reversed(range(n)):
    print(f"{numbers[i]}", end=" ")
print()