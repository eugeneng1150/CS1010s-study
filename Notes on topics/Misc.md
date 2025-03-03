# Learning points from papers
## NEVER FORGET 'NONE' BEING PRINTED IF IT RETURNS NOTHING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
1) is vs ==
```python
a = (1,2)
b = (1,2,3)
c = a + b
print(b is c[-3:]) # False

b == c[-3:] # checks if the contents are the same
b is c[-3:] # checks if they refer to the same exact object in memeory
```
c[-3:] creates a **new tuple**, even though it has the same value as b  
reference from mar-21 midterms

2) Cannot remove a value in a tuple but can always do slicing
3) 4 % 5 = 4
3) Never ever break abstraction
4) Tuple tracing
```python
a = ()
b = (1,a)    # (1,())
a = a + (1,) # (1,)
c = b + a    # (1,(),1)
print(c)     # (1,(),1)
```
```python
x = (1, 2)
y = (2, (1, 2), x)
x = y[1][0:len(y[1]):1] # x = (1,2)
print(x in y) # True
# Takeaway is that x is a single element of y hence True output
z = () 
for item in y:
    z += (item, )
# z = (2,(1,2), (1,2))

z += x 
print(z) # z = (2, (1,2), (1,2), 1,2) 
# note how z looks like
# z += x unpacks x = (1,2) and appends 1 and 2 as separate elements.
# To Keep x as a Single Tuple Element
# Use z += (x,) instead.
# This would make z = (2, (1,2), (1,2), (1,2)), treating x as one entity.
print(y in z)
# False 
# Since y = (2, (1, 2), (1,2)) and z = (2, (1,2), (1,2), (1,2))
# y is not a SINGLE ELEMENT OF Z hence output False
print(x in z[2:len(z):1])
```
- z += x → Unpacks x and adds its elements.
- z += (x,) → Keeps x as a single tuple inside z.
```python
a = (1, 2, 3)
b = (8, 9)
t = a + b
print(t)
print(a in t) # False

u = (b[1:-1:1], a[1:-1:1])
# note that b = (8,9)
# start at 9 end before 9, meaningless slice, hence EMPTY TUPLE
print(u) # u = ((), (2,))
print(2 in u) # False since 2 is not a SINGLE ELEMENT OF u

b = (b, b) # b = ((8,9), (8,9))
print(b in b)
# False as reason as ^ 
```

5) String and tracing
```python
course = ("CS",1,0,10,"S")
print(course[1:-2:1] * 2) # (1,0,1,0) 
# since course[1:-2:1] produces (1,0) 
# Takeaway is that if we take more than 1 element from a tuple, it produces another tuple and not a single element
# Note that -2 is excluded, hence we stop one before -2 
```
```python
course = ("CS",1,0,10,"S")
print(course[1:0:-10] ) # even though the skip step is out of range, it still takes the first value
```
```python
course = ("CS",1,0,10,"S")
print(course[::-1][course[2]]) # evaulate the right hand side first then at the end go from Left to Right
```

6) Scope (Global vs Local Scope)
```python
x, y, z = 5, 4, 8  # Global variables

def foo(x, y):
    z = x + y  # Local 'z' is created but immediately overwritten
    z = bar(x) + bar(y)  # Overwrites 'z' with new values from bar(x) and bar(y)
    print(z)  # Prints the new value of 'z'
    return bar(z)  # Calls bar() with 'z' and returns its result

def bar(y):
    # No local 'z' defined here, so Python uses the global 'z = 8'
    x = z + y  # This refers to global 'z'
    print(x)  # Prints the computed value of 'x'
    return x  # Returns the computed value

print(foo(4, x))  # Calls foo() with x = 4, y = 5
```

```python
x, y, z = 2, 3, 5  # Global variables

def f(y):
    print(y * 4)  # Prints the value of y * 4 before modifying y
    y = 4  # Local change, does not affect global y
    x = 6  # Local x, does not affect global x
    return g(x, y)  # Function returns here, so the next print(x) never executes
    print(x)  # This line does not run due to the return statement above

def g(x, y):
    return h(y, x)  # Calls h() with swapped arguments

def h(x, y):
    print(z + y)  # Uses global z (5) and local y
    print(y + x)  # Adds local x and y

print(f(x))  # Prints None because f(x) returns nothing explicitly
```