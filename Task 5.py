# Умова: Є словник: user = {"name": "Alice", "age": 25}. Написати функцію: def update_age(user, new_age):
def update_age(user, new_age):
    return {**user, "age": new_age}

# Приклад
user = {"name": "Artem", "age": 25}

updated_user = update_age(user, 30)

print(user)         # {'name': 'Artem', 'age': 25}
print(updated_user) # {'name': 'Artem', 'age': 30}