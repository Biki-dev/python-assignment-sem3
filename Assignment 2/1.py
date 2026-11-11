input = int(input("Enter a year: "))

if input % 400 == 0:
    print(input, "is a leap year.")
elif input % 100 == 0:
    print(input, "is not a leap year.")
elif input % 4 == 0:
    print(input, "is a leap year.")
else:
    print(input, "is not a leap year.")