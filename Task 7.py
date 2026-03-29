# Реалізувати pipeline: data = [1,2,3,4,5,6]. Кроки: відфільтрувати парні, піднести до квадрату, повернути результат. Без зміни вихідного спику.
def process_data(data):
    return [x**2 for x in data if x % 2 == 0]

# Приклад
data = [1, 2, 3, 4, 5, 6]

result = process_data(data)

print(data)   # [1, 2, 3, 4, 5, 6]
print(result) # [4, 16, 36]