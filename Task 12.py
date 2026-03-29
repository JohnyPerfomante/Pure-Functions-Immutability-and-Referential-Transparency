# Реалізувати: def pipeline(data, steps): ... де: steps = [ lambda xs: ..., lambda xs: ... ]
def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result

# Приклад
data = [1, 2, 3, 4, 5, 6]

steps = [
    lambda xs: [x for x in xs if x % 2 == 0],
    lambda xs: [x**2 for x in xs],
]

result = pipeline(data, steps)

print(result)  # [4, 16, 36]