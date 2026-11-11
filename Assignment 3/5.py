n1 = int(input("Enter a number: "))
list1 = []

for i in range(n1):
    num = int(input(f"Enter number {i + 1}: "))
    list1.append(num)
    
n2 = int(input("Enter a number: "))
list2 = []

for i in range(n2):
    num = int(input(f"Enter number {i + 1}: "))
    list2.append(num)
    
common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print(f"The common numbers are: {common}")