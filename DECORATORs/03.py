# [Cache Return Value]-->Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.


import time

def Cache(func):
    Cache_value = {}
    print(Cache_value)
    def wrapper(*args):
        if args in Cache_value:
            return Cache_value[args]
        result=func(*args)
        Cache_value[args]=result
        return result
    return wrapper    
    

@Cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(4, 3))






def cache(func):
    memory = {}
    def wrapper(*args):
        if args in memory:
            print("[Cache] Returning cached result.")
            return memory[args]
        result = func(*args)
        memory[args] = result
        return result
    return wrapper

@cache
def preprocess(data):
    print("Running expensive preprocessing...")
    return [x**2 for x in data]

print(preprocess((1, 2, 3)))
print(preprocess((1, 2, 3)))  # Will be cached
print(preprocess((4, 5, 6)))  # Different input, will not be cached