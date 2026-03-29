# Functional Core (чиста функція)
def calculate_total(items, tax_rate):
    return sum(items) * (1 + tax_rate)

# Imperative Shell (обгортка)
def process_order(order):
    print("Processing order...")
    total = calculate_total(order["items"], 0.2)
    return total