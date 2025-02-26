x = (1, 2, 3, 4)
def my_f(x):
    print(x)
    
def my_g(x):
    return x * x

print(tuple(map(lambda x: 10, x)))
print(tuple(map(lambda x: x + 1, x)))
print(tuple(map(lambda x: x is not True, x)))
print(tuple(map(print, x)))
print(tuple(map(str, x)))
print(tuple(map(my_f, x)))
print(tuple(map(my_g, x)))

print((1,2,3) == (1,2,3))