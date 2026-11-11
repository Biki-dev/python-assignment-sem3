num = int(input("Enter a decimal number: "))

if num < 0:
    print("Please enter a non-negative integer.")
elif num == 0:
    print("Binary representation: 0")
    print("Hexadecimal representation: 0")

else:
    original = num
    
    # Decimal to Binary
    binary = ''
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
        
    print("Binary representation:", binary)

    # Decimal to Hexadecimal
    num = original
    hexadecimal = ''
    while num > 0:
        remainder = num % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
        num = num // 16
        
    print("Hexadecimal representation:", hexadecimal)