x, y = 1, 4
x, y = y, x #4,1

def ding(x):
    if x % 2 == 1:
        print("Alright")
    elif x % 3 == 1:
        print("Okay")
    if x**0.5 == y + 1:
        print("Awesome")
    else:
        print("This question sucks")

ding(x) # since there is a print statement in the funciton ding(x), 'okay' is printed
# Awesome is printed too

ding(y) # awesome is printed
## Alright
## This question sucks

ding(9) # aright is printed
print(ding(3))  # error is thrown
## ding(3) will print "Alright" and "This question sucks" 
## then it will print none