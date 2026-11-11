n = int(input("Enter a number: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(f"The even numbers are: {even}")
print(f"The odd numbers are: {odd}")