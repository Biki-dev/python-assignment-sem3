# need to use lambda function which help to create anonymous functions
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

def my_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

numbers = [1, 2, 3, 4, 5, 6]
mapped = my_map(lambda x: x * 2, numbers) # double every num
filtered = my_filter(lambda x: x % 2 == 0, numbers) # filter even numbers

print("Original List :", numbers)
print("Mapped List   :", mapped)
print("Filtered List :", filtered)