n = int(input("Enter a number: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    
largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(f"The largest number is: {largest}")
print(f"The second largest number is: {second_largest}")