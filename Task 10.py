# Умова: def double(x): return x * 2. Переписати вираз: double(5) + double(5) використовуючи принцип referential transparency.
def double(x):
    return x * 2

# double(5) + double(5)
# (5 * 2) + (5 * 2)

# (5 * 2) + (5 * 2)
# 10 + 10
# 20