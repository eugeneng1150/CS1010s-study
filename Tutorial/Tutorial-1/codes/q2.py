x = 1

def add_one(x):
    print(x + 1)
    
print(add_one(2))
# prints 3 and returns none

y = add_one(x)
# this will print 2

print(add_one(y))
# Raise a TypeError, since y = none. 