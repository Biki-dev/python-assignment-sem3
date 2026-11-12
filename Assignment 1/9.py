import math
num1 = int(input("Enter numerator of first fraction: "))
den1 = int(input("Enter denominator of first fraction: "))
num2 = int(input("Enter numerator of second fraction: "))
den2 = int(input("Enter denominator of second fraction: "))
if den1 == 0 or den2 == 0:
    print("Denominator cannot be zero")
else:
    numerator = num1 * den2 + num2 * den1
    denominator = den1 * den2
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    if denominator < 0:
        numerator = -numerator
        denominator = -denominator
    print("Sum of fractions:", numerator, "/", denominator)