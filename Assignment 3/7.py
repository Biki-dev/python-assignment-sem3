n = int(input("Enter the number of elements: "))

if n <= 0:
    print("Invalid input! List must contain at least one element.")

else:
    numbers = []

    for i in range(n):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)

    current_sum = numbers[0]
    max_sum = numbers[0]

    # Traverse the list
    for i in range(1, n):
        current_sum = max(numbers[i], current_sum + numbers[i])
        max_sum = max(max_sum, current_sum)

    # Print result
    print("Original List:", numbers)
    print("Maximum Contiguous Subarray Sum:", max_sum)