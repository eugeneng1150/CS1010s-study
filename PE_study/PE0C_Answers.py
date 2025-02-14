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



# STEP 1:

# INPUT ANALYSIS
# We are given integer n >= 1.

# HIGH-LEVEL IDEA ON OUTPUT
# The question tells us that a SINGLE DIGIT will only be
# a happy number if it is 1 or 7. So, the general solution
# should be to keep replacing n with SDS(n) until it is a
# single digit and return true if it is 1 or 7, else return
# false.



# STEP 2:

# PLANNING THE SOLUTION (PSEUDOCODE)

# while n has more than 1 digit:
#   n = SDS(n)
# if n (now 1 digit) == 1 or 7:
#   return true
# else:
#   return false
# ## Note: the above assumes that SDS is implemented.


# STEP 3:

# IMPLEMENT THE SOLUTION

# Decomposition of SDS
# -- perform problem-solving on this sub-problem
#    ---- you should already be familiar with a 
#         solution to this sub-problem
#         - i.e., based on iterating through an int
# -- we thus get the following
def SDS(n):
  res = 0
  while n > 0:
    res = res + (n % 10)**2
    n = n // 10
  return res

# Decomposition of count_digits
# -- once again, solve as a sub-problem
#    ---- again, the solution is very similar to
#         the solution for SDS
#         - i.e., based on iterating through an int
def count_digits(n):
  if n == 0:
    return 1
  count = 0
  while n > 0:
    count = count + 1
    n = n // 10
  return count

# Then follow the PSEUDOCODE given above:

# while n has more than 1 digit:
#   n = SDS(n)
# if n (now 1 digit) == 1 or 7:
#   return true
# else:
#   return false

# We thus get the following:
def is_happy_iter(n):
  while count_digits(n) > 1:
    n = SDS(n)
  return n == 1 or n == 7



# STEP 4:

# TEST THE IMPLEMENTATION OF THE SOLUTION

# YOU MAY CONSIDER TESTING THE DECOMPOSED
# SUB-PROBLEM SOLUTIONS SEPARATELY AS WELL

### Uncomment to Test
print("iterative")
print(is_happy_iter(13))      # True
print(is_happy_iter(16))      # False
print(is_happy_iter(37))      # False
print(is_happy_iter(83))      # False
print(is_happy_iter(849))     # False
print(is_happy_iter(10888))   # True
print(is_happy_iter(100093))  # True



# STEP 5: No need to do this in an exam setting.
# -- However, after the exam, you can always analyse
#    the solution to see if any useful patterns for
#    future use





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



# STEP 1:
# -- Since it is the same problem, we need
#    not redo Step 1



# STEP 2:
# -- Simply convert our iterative solutions
#    to iterative ones
# -- Recall the process to do this:
#    ---- (A) take the complement of the
#             loop condition as the base case
#    ---- (B) take the initial loop variable
#             value as the return value for the
#             base case (note, you should always
#             check this later)
#    ---- (C) in the recursive case, define 2
#             variables, one for the result from
#             the current fn call, and the other
#             for the result of the recursive call
#    ---- (D) the value for the current fn call
#             should be the same as the loop body
#    ---- (E) the value for the recursive call
#             should be the result of the recurive
#             call where the new argument is the
#             loop update
#    ---- (F) once you have done the above, trace
#             the recursion tree for a small input
#             (i.e., one that will only make 2-3
#             recursive calls) to ensure the logic
#             behind your implementation is correct



# STEP 3:
# Convert all iterative solutions to recursive ones
# as described in Step 2

# Decomposition of SDS
'''
def SDS(n):
  res = 0
  while n > 0:
    res = res + (n % 10)**2
    n = n // 10
  return res
'''
def SDS(n):
  if not (n > 0): # complement of loop condition
    return 0
  else:
    c = (n % 10)**2 # loop body (update to res)
    r = SDS(n // 10) # make recursive call with loop var update
    return c + r # accumulate res via returns

# Decomposition of count_digits
'''
def count_digits(n):
  if n == 0:
    return 1
  count = 0
  while n > 0:
    count = count + 1
    n = n // 10
  return count
'''
def count_digits(n):
  if n == 0: # special case
    return 1
  else:
    def helper(n): # to avoid special case
      if not (n > 0): # complement of loop condition
        return 0
      else:
        c = 1 # loop body (update to res)
        r = helper(n // 10) # make recursive call with loop var update
        return c + r # accumulate res via returns
    return helper(n)

'''
def is_happy_iter(n):
  while count_digits(n) > 1:
    n = SDS(n)
  return n == 1 or n == 7
'''
def is_happy_rec(n):
  if not (count_digits(n) > 1):
    return n == 1 or n == 7
  else:
    return is_happy_rec(SDS(n)) # res computed after iteration



# STEP 4:

# REMEMBER THAT YOU SHOULD TEST EACH SOLUTION
# AND SUB-SOLUTION SEPARATELY (NOTE: I HAVE
# OMITTED THE TESTING OF SUB-SOLUTIONS HERE)

### Uncomment to Test
print("recursive")
print(is_happy_rec(13))      # True
print(is_happy_rec(16))      # False
print(is_happy_rec(37))      # False
print(is_happy_rec(83))      # False
print(is_happy_rec(849))     # False
print(is_happy_rec(10888))   # True
print(is_happy_rec(100093))  # True



# STEP 5: Consider adding any useful patterns
#         (after the assessment)
