enemies = 0

def increase_enemies():
    # global enemies
    #this works but people don't do that, you want to avoid modifying global scope
    print(f"enemies inside function: {enemies}")
    return enemies + 1
    


enemies = increase_enemies()
print(f"enemies outisde function: {enemies}")

# no such thing as block scope in Python, if you create a new variable inside block of code, it still has the same scope as its enclosing function

# Modifying global scope