# Tuples
## 1. Tuples are immutable
```python
tup = (1, 2, 3)
tup[0] = 10  # TypeError: 'tuple' object does not support item assignment
```
## 2. Slicing of Tuples even though out of range will not throw an error
```python
tup = (1,2,3,4,5)
new_tup = tup[:9]
print(new_tup)
# (1, 2, 3, 4, 5)
```
## 3. Similar to a string
- Both are immutable.
- Both support indexing and slicing.

## 4. Tuples can store different data types
```python
tup = ("CS1010S", 1,2,3)
print(tup)
# ('CS1010S', 1, 2, 3)
```
## 5. Can iterate through Tuples
```python
tup = ('apple', 'banana', 'cherry')
for item in tup:
    print(item)
# Output:
# apple
# banana
# cherry
```
## 6. 12 Things you can do with a Tuple

### 1. Indexing
Access elements using their index.
```python
# Example
 tup = (10, 20, 30, 40)
 print(tup[1])  # Output: 20
```

### 2. Slicing
Extract a portion of a tuple.
```python
# Example
tup = (1, 2, 3, 4, 5)
print(tup[1:4])  # Output: (2, 3, 4)
```

### 3. Concatenation
Combine two tuples using `+`.
```python
# Example
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
result = tup1 + tup2
print(result)  # Output: (1, 2, 3, 4, 5, 6)
```

### 4. Repetition
Repeat elements using `*`.
```python
# Example
tup = (1, 2)
print(tup * 3)  # Output: (1, 2, 1, 2, 1, 2)
```

### 5. Length of Tuple
Get the number of elements using `len()`.
```python
# Example
tup = (10, 20, 30)
print(len(tup))  # Output: 3
```

### 6. Membership Testing
Check if an element exists in a tuple using `in`.
```python
# Example
tup = (1, 2, 3, 4)
print(3 in tup)   # Output: True
print(5 in tup)   # Output: False
```

### 7. Tuple Unpacking
Assign tuple elements to variables.
```python
# Example
tup = (10, 20, 30)
a, b, c = tup
print(a, b, c)  # Output: 10 20 30
```

### 8. Iterating Over a Tuple
Loop through a tuple.
```python
# Example
tup = ('apple', 'banana', 'cherry')
for item in tup:
    print(item)
```

### 9. Finding Index of an Element
Use `.index()` to find the first occurrence.
```python
# Example
tup = (10, 20, 30, 40)
print(tup.index(30))  # Output: 2
```

### 10. Counting Occurrences
Count occurrences of a value using `.count()`.
```python
# Example
tup = (1, 2, 2, 3, 2, 4)
print(tup.count(2))  # Output: 3
```

### 11. Converting Tuple to List and Vice Versa
```python
# Example
tup = (1, 2, 3)
lst = list(tup)  # Convert to list
new_tup = tuple(lst)  # Convert back to tuple
```

### 12. Sorting a Tuple
Convert to a list first since tuples are immutable.
```python
# Example
tup = (3, 1, 4, 2)
sorted_tup = tuple(sorted(tup))
print(sorted_tup)  # Output: (1, 2, 3, 4)
```

### 13. Enumerate Fuction
```python
tup = ("hi" , "hello" , "nihao")
for i, c in enumerate(tup):
    print("index " + str(i) + ": " + str(c))
# Output:
# index 0: hi
# index 1: hello
# index 2: nihao
```

### 14. Keeping distinct group inside one big tuple
Start with empty structure and insert them dynamically
```python
big_group = ()
tuple1 = (1,2,3)
tuple2 = (4,5,6)
big_group += (tuple1,)  # Adding group1
big_group += (tuple2,)  # Adding group2
# ^^ note that even though tuple2 is the last group, to keep them distinct still add the , behind
print(big_group)
# Output: ((1, 2, 3), (4, 5, 6))
```
## 7 Tuple Iteration with Multiple Assignments

```python
for c , v in ((1,2) , (3,5)):
    print(str(c) + " and " + str(v))
# Output: 
# 1 and 2
# 3 and 5
```


