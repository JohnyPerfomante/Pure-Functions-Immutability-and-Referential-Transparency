# Умова: order = { "items": [100, 200, 300], "discount": 0.1 }. Побудувати систему: чиста функція обчислення суми, функція застосування знижки, функція застосування податку. Без мутацій, всі функції referentially transparent.

# Обчислення суми
def calculate_total(items):
    return sum(items)

# Застосування знижки
def apply_discount(total, discount):
    return total * (1 - discount)

# застосування податку
def apply_tax(total, tax_rate):
    return total * (1 + tax_rate)

# Pipeline
def process_order(order, tax_rate):
    total = calculate_total(order["items"])
    discounted = apply_discount(total, order["discount"])
    final = apply_tax(discounted, tax_rate)
    return final

# Приклад
order = {
    "items": [100, 200, 300],
    "discount": 0.1
}

result = process_order(order, 0.2)

print(result)
# (100 + 200 + 300) = 600
# 600 * 0.9 = 540
# 540 * 1.2 = 648