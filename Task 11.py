# Умова: Побудувати pipeline. Всі функції мають бути чистими, без мутацій

# Фільтрація USD
def filter_usd(transactions):
    return [t for t in transactions if t["currency"] == "USD"]

# Конвертація у гривні
def convert_to_uah(transactions, rate):
    return [
        {**t, "amount": t["amount"] * rate, "currency": "UAH"}
        for t in transactions
    ]

# Обчислення суми
def total_amount(transactions):
    return sum(t["amount"] for t in transactions)

# Pipeline
def process_transactions(transactions, rate):
    usd = filter_usd(transactions)
    uah = convert_to_uah(usd, rate)
    return total_amount(uah)

# Приклад
transactions = [
    {"amount": 100, "currency": "USD"},
    {"amount": 200, "currency": "EUR"},
    {"amount": 150, "currency": "USD"},
]

result = process_transactions(transactions, 40)

print(result)  # (100 + 150) * 40 = 10000