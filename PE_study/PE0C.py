###############
# Question 1  #
###############

"""
A happy number is a number that is defined by
the process involving sum of squares of digit.
We repeat the process until 1 for happy number.
Otherwise, the number is a sad number.
"""


###############
# Task 1A     #
###############

"""
Implement the function is_happy_iter(n)
that returns True for happy number and
False for sad number.

The function must be implemented using iteration
and without any recursion.  Make sure any helper
function is non-recursive (or built-in).
"""


def calculate(n):
  if n // 10 == 0:
    return n**2
  else:
    res = 0
    n = str(n)
    for i in range(len(n)):
      res += int(n[i]) ** 2
    return res
  
def is_happy_iter(n):
  res = 0
  n = str(n)
  while len(str(n)) > 1:
    n = str(calculate(int(n)))
    print(n)
  if int(n) == 1 or int(n) == 7:
    return True
  else:
    return False
    
    


### Uncomment to Test
print(is_happy_iter(13))      # True
print(is_happy_iter(16))      # False
print(is_happy_iter(37))      # False
print(is_happy_iter(83))      # False
print(is_happy_iter(849))     # False
print(is_happy_iter(10888))   # True
print(is_happy_iter(100093))  # True



###############
# Task 1B     #
###############

"""
Implement the function is_happy_rec(text)
that returns True for happy number and
False for sad number.

The function must be implemented using recursion
and without any iteration.  Make sure any helper
function is non-iterative (or built-in).
"""
 #happy number is 1 or7

##
##def calculate(n):
##  if n == 0:
##    return 0
##  else:
##    digit = int(n) % 10
##    return calculate(n //10) + digit**2
##
## 
##def is_happy_rec(n):
##  n = str(n)
##  if int(n) == 1:
##    return True
##  if int(n) == 7:
##    return True
##  if len(n) == 1 and (int(n) != 7 or int(n) != 1):
##    return False
##  else:
##    n = int(n)
##    last_digit = n % 10
##    n = n // 10
##    return is_happy_rec(calculate(n) + last_digit **2)
##    



def sum(n):
    if n == 0:
        return 0
    else:
        last = n % 10
        
        return sum(n // 10) + last**2

def is_happy_rec(n):
    n = str(n)
    if int(n) == 1 or int(n) == 7:
        return True
    if len(n) == 1 and (int(n) != 1 or int(n) != 7):
        return False
    else:
        n = int(n)
        return is_happy_rec(sum(n))

  



### Uncomment to Test
##print(is_happy_rec(13))      # True
##print(is_happy_rec(16))      # False
##print(is_happy_rec(37))      # False
##print(is_happy_rec(83))      # False
##print(is_happy_rec(849))     # False
##print(is_happy_rec(10888))   # True
##print(is_happy_rec(100093))  # True
