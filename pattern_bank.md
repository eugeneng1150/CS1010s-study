# Coding bank

## How to Reverse a Sequence Using Recursion

```python
def reverse_recursion(seq):
    if seq == ():  # Base case: an empty sequence
        return ()
    else:
        # Recursive case: reverse the rest of the sequence and append the first element
        return reverse_recursion(seq[1:]) + (seq[0],) #create a new tuple
```

## How to Reverse a Sequence Using Iteration

```python
def reverse_iter(seq):
    ans = ()
    for item in seq:
        ans = (item, ) + ans #note the position of the ans
    return ans 
```

## Scaling a Sequence using Recursion

```python
def scale_recursion(seq, k):
    if seq == ():
        return ()
    else:
        return (seq[0] * k) + scale_recursion(seq[1:], k)
    # handle first element
    # handle the rest
```
## Scaling a Sequence using Iteration

```python
def scale_iter(seq, k):
    ans = ()
    for item in seq:
        ans += (item * k,)
    return ans
```

