import time # for measuring execution time
from functools import wraps # for creating decorators

def log_execution(func):
    @wraps(func)
    def wrapper(*args):
        print("\n========== EXECUTION LOG ==========")
        print("Function Name :", func.__name__)
        print("Arguments     :", args)
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        print("Execution Time:", end - start, "seconds")
        print("===================================")
        return result
    return wrapper

@log_execution
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 999
result = factorial(number)
print("\nFactorial of", number, "calculated successfully!")
print("Number of digits:", len(str(result)))