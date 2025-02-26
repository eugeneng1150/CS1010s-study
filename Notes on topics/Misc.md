# Learning points from papers
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