# Input can be positive # or negative numbers, but we want to ensure
# that the inputs are positive before proceeding with the operation.
def validate_positive(func):
    def wrapper(*args):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:   # [If arg is a number and it's negative, then do something (raise an error)]
                raise ValueError(f"Invalid input: {arg} is negative.")
        return func(*args)
    return wrapper

# Example usage
@validate_positive
def multiply(a, b):
    return a * b

# Test cases
print(multiply(5, 3))      # Valid
# print(multiply(-2, 4))     # Will raise ValueError
