# question 2a
def make_product(name, shelf_life):
    product_turple = (name, shelf_life)
    return product_turple

# print(make_product("milk", 2))

def get_name(product):
    print(product[0])

def get_shelf_life(product):
    print(product[1])
# milk = make_product("milk", 2)
# get_name(milk)
# get_shelf_life(milk)
    
def new_inventory():
    return ()

def add_product(inv, product):
    return inv + (product,)

def add_one_day(inv):
    return tuple((product[0], product[1] - 1) for product in inv)

def get_expired(inv):
    return tuple(product[0] for product in inv if product[1] <= 0)


inv = new_inventory()
inv = add_product(inv, make_product("bread", 4))  # Add bread with shelf life 4
print(inv)
inv = add_one_day(inv)  # Day 1
print(inv)
inv = add_product(inv, make_product("milk", 3))  # Add milk with shelf life 3
inv = add_one_day(inv)  # Day 2
print(inv)
inv = add_product(inv, make_product("milk", 3))  # Add another milk
inv = add_one_day(inv)  # Day 3
print(inv)

print(get_expired(inv))  # Expected Output: ()

inv = add_one_day(inv)  # Day 4
print(inv)
expired = get_expired(inv)
print(expired)
print("bread" in expired)

