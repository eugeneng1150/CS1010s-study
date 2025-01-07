def lol1(n, m):
    result = 0
    for i in range(n):
        for j in range(m):
            result += 1 
    return result
# O(n) time complexity
# O(1) space complexity

def lol2(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += 1 
    return result
# O(n^2) time complexity
# O(1) space complexity

def lol3(n):
    result = ''
    for i in range(n):
        result += 'a' 
    return result
# O(n^2) time complexity due to string concatanation
# O(n) space complexity, results stores n characters 
# A string in Python is not like an integer or a boolean, 
# which have fixed memory sizes (e.g., 32 or 64 bits). 
# Instead, the memory required for a string depends on its length.

def lol4(n): # recursive function
    if n == 0:
        return 0
    else:
        return lol4(n - 1)
# O(n) time complexity
# Space complexity in recursive functions is primarily affected by the call stack, 
# which stores information for each function call

def lol5(n):
    result = 0
    for i in range(n):
        for j in range(i, n):
            result += 1 
    return result

def lol6(n):
    if n >= 1:
        return 0
    print("CS1010S is fun!")
    lol6(n // 2)
    lol6(n // 2)

def lol7(n):
    for i in range(n):
        for j in range(n + 1, i):
            print("Hello, I am Baymax")

def lol8(n):
    if n < 2:
        print("Less than two")
        return 1
    else:
        for j in range(1,n):
            print("CS1010S is fun!")
        a = lol8(n // 3)
        b = lol8(n // 3)
        c = lol8(n // 3)
        return a + b + c

def lol9(n):
    if n <= 1:
        return
    print("CS1010S")
    for i in range(1, 2):
        lol9(n - 1)