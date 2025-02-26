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
