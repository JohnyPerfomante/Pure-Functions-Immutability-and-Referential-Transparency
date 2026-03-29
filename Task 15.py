# Реалізувати: state0 → state1 → state2 → state3. Можливість: undo, зберігати історію
def create_store(initial_state):
    return {
        "history": [initial_state],
        "current": 0
    }


def get_state(store):
    return store["history"][store["current"]]


def set_state(store, new_state):
    new_history = store["history"][:store["current"] + 1] + [new_state]
    
    return {
        "history": new_history,
        "current": store["current"] + 1
    }


def undo(store):
    if store["current"] == 0:
        return store
    
    return {
        "history": store["history"],
        "current": store["current"] - 1
    }

# Приклад
store = create_store({"count": 0})

store = set_state(store, {"count": 1})
store = set_state(store, {"count": 2})
store = set_state(store, {"count": 3})

print(get_state(store))  # {'count': 3}

store = undo(store)
print(get_state(store))  # {'count': 2}

store = undo(store)
print(get_state(store))  # {'count': 1}