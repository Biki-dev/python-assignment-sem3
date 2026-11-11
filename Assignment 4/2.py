def compute_stats(numbers):
    if len(numbers) == 0:
        return None, None, None
    
    total = 0
    for num in numbers:
        total += num
    mean = total / len(numbers)
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1: # for odd length
        median = sorted_numbers[n // 2]
    else: # for even length
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    squared_diffs = 0
    for num in numbers:
        squared_diffs += (num - mean) ** 2
    variance = squared_diffs / len(numbers)
    
    return mean, median, variance


data = [10, 20, 30, 40, 50]
mean, median, variance = compute_stats(data)
print("Mean     :", mean)
print("Median   :", median)
print("Variance :", variance)