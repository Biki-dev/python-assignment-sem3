def power(base, exponent):
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 5)) # Output - 32
print(power(3, 3)) # Output - 27
print(power(10, 0)) # Output - 1