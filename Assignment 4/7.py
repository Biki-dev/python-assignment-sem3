def nested_sum(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total

numbers = [1, [2, [3, 4], 5], 6]
result = nested_sum(numbers)
print("Nested List:", numbers)
print("Total Sum:", result)

# Nested List: [1, [2, [3, 4], 5], 6]
# Total Sum: 21