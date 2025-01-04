# Space Complexity in Recursive Functions

## Key Concepts

Space complexity measures the **total additional memory** required by an algorithm as a function of the input size. For recursive functions, space complexity is heavily influenced by the **call stack**, which stores the information needed for each function call.

---

## Example Recursive Function

Here is the function we are analyzing:

```python
def lol4(n):  # Recursive function
    if n == 0:
        return 0
    else:
        return lol4(n - 1)
```

---

## Analysis of Space Complexity

### 1. **Call Stack Behavior**
- Every recursive call stores information on the call stack, including:
  - The function's parameters (`n` in this case).
  - The return address (where the function will resume after returning).
  - Other bookkeeping information.

### 2. **Recursive Depth**
- The function recursively calls itself until it reaches the base case (`n == 0`).
- For an input of size `n`, there will be exactly `n` recursive calls.
- Each recursive call adds one frame to the call stack.

### 3. **Space Used per Stack Frame**
- Each stack frame consumes a constant amount of memory (`O(1)`), regardless of the value of `n`.
- This memory includes storage for:
  - The parameter `n`.
  - The return address.

### 4. **Total Space Complexity**
- Since the depth of recursion is proportional to `n`, and each stack frame requires constant space (`O(1)`), the total space complexity is:

**O(n)**

---

## Why Space Complexity is O(n)

- At any point during execution, the call stack contains at most `n` stack frames (one for each recursive call).
- The memory for previous calls is not released until the base case is reached and the recursion unwinds.
- For large values of `n`, the call stack grows linearly, making the space complexity **O(n)**.

---

## Example Call Stack for `n = 5`
If `lol4(5)` is called, the call stack will look like this before unwinding:

```
lol4(5)
lol4(4)
lol4(3)
lol4(2)
lol4(1)
lol4(0)  # Base case
```

Once the base case (`n == 0`) is reached, the stack starts to unwind, releasing one stack frame at a time.

---

## Optimizing Space Complexity

The space complexity can be reduced by rewriting the recursive function as an iterative one:

### Iterative Solution
```python
def lol4_iterative(n):
    while n > 0:
        n -= 1
    return 0
```

### Analysis of Iterative Solution
- **Time Complexity:** Still \( O(n) \) because the loop runs \( n \) times.
- **Space Complexity:** \( O(1) \), as no recursive calls are made and the call stack does not grow.

---

## Summary

| **Metric**         | **Recursive Function** | **Iterative Function** |
|---------------------|-------------------------|-------------------------|
| **Time Complexity** | O(n)                   | O(n)                   |
| **Space Complexity**| O(n)                   | O(1)                   |

---

## Takeaway
Recursive functions often have higher space complexity due to the growth of the call stack. Iterative solutions are more space-efficient, as they do not require additional memory for recursive calls. Consider using iterative approaches if memory usage is a concern.
