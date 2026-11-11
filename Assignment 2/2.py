# Taking Input from the user
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

# Checking if the triangle is valid or not
istri = 0
if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        istri = 1

# Classify the triangle based on the sides        
if istri == 1:
    if a == b and b == c:
        print("The triangle is equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The triangle is not valid.")
    