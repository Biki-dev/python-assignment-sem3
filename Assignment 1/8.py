first = float(input("Enter first term: "))
second = float(input("Enter second term: "))
n = int(input("Enter term number (N): "))
d = second - first
nth_term = first + (n - 1) * d
print("Common Difference:", d)
print("Nth Term:", nth_term)