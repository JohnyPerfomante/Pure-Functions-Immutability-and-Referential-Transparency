# Реалізувати кешування для чистої функції: def slow_function(x): ...
def memoize(func):
    cache = {}

    def wrapper(x):
        if x in cache:
            return cache[x]
        result = func(x)
        cache[x] = result
        return result

    return wrapper

# Застосування
@memoize
def slow_function(x):
    print("Calculating...")
    return x * x

# Приклад
print(slow_function(5))  # Calculating...  25
print(slow_function(5))  # без Calculating...  25 (з кешу)