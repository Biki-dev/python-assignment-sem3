a = float(input("Enter first coefficient (a): "))
b = float(input("Enter second coefficient (b): "))
c = float(input("Enter third coefficient (c): "))

D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + D**0.5) / (2*a)
    root2 = (-b - D**0.5) / (2*a)
    print("The roots are real and different.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif D == 0:
    root = -b / (2*a)
    print("The roots are real and the same.")
    print("Root:", root)
else:
    real_part = -b / (2*a)
    imaginary_part = (abs(D)**0.5) / (2*a)
    print("The roots are complex and different.")
    print("Root 1:", complex(real_part, imaginary_part))
    print("Root 2:", complex(real_part, -imaginary_part))