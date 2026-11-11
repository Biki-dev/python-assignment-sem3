
def pipeline(*funcs):

    for func in funcs:
        if not callable(func):
            raise TypeError("All arguments must be callable")

    def composite(x):
        result = x
        for func in funcs:
            result = func(result)
        return result
    return composite

def add_five(x):
    return x + 5
def multiply_two(x):
    return x * 2
def square(x):
    return x * x

operation = pipeline(add_five, multiply_two, square)

result = operation(10)
print("Final Result:", result)
