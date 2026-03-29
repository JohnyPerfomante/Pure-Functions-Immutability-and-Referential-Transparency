# Умова: Переписати функції так, щоб вони стали чистими.
tax_rate = 0.2

def calculate_price(price):
    return price * (1 + tax_rate)

# Переписана функція
def calculate_price(price, tax_rate):
    return price * (1 + tax_rate)

calculate_price(100, 0.2)