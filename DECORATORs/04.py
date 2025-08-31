# Memoized Fibonacci Calculator using a Decorator.
# This code calculates Fibonacci numbers using a recursive approach with memoization to improve performance.


import time

# Caching decorator
def memoize(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

# Recursive Fibonacci
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test it
start = time.time()
print(f"Fibonacci(35): {fibonacci(35)}")
end = time.time()

print(f"Took {end - start:.2f} seconds")
