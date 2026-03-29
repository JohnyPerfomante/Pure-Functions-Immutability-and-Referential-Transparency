# Переписати: from datetime import datetime def is_morning(): return datetime.now().hour < 12. Зробити функцію референтно прозорою.
def is_morning(hour):
    return hour < 12

# Приклад
is_morning(10)  # True
is_morning(15)  # False