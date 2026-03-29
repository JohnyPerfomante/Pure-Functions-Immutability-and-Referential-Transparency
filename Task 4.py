# Умова: Заборонити мутацію. Переписати функцію так, щоб вона не змінювала вхідний список.
def add_item(items, item):
    items.append(item)
    return items

# Без мутації
def add_item(items, item):
    return items + [item]

# Приклад
items = [1, 2, 3]

new_items = add_item(items, 4)

print(items)      # [1, 2, 3]
print(new_items)  # [1, 2, 3, 4]