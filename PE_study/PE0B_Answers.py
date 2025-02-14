###############
# Question 1  #
###############

"""
A tram packing is a packing following the two simple rules.
"""


###############
# Task 1A     #
###############

"""
Implement the function tram_packing_iter(config)
that returns the final seating arrangement given
the initial seating configuration.

The function must be implemented using iteration
and without any recursion.  Make sure any helper
function is non-recursive (or built-in).
"""


# STEP 1:

# INPUT ANALYSIS
# We are given a str, config
# - len(config) >= 3
# - text only includes "X" and "O" characters
#   -- first and last character must be "X"
#   -- rest (i.e., between first and last)
#      must be "O"

# HIGH-LEVEL IDEA ON OUTPUT
# Notice that we are required to need to find
# the longest sequence of "O"s in config, and
# then replace the middle (if odd number of
# "O"s) or left of the two middle indices (if
# even number of "O"s) with an "X", and then
# keep repeating this process until each
# sequence of "O"s is either 1 or 2 in length.



# STEP 2:

# PLANNING THE SOLUTION (PSEUDOCODE)


# Main solution:
# - while the longest sequence of "O"s > 2:
#   -- find middle index of that sequence, M
#   -- replace config[M] with "X"


# Decomposition of finding the longest sequence
# of "O"s in config:
# - let curr_max = 0
# - while len(config) > 0:
#   -- since config[0] is "X", remove it:
#      let config = config[1:]
#   -- if config.find("X") > curr_max:
#      ---- update curr_max to config.find("X")
#           - given "O...OX", "X" index == num "O"s
#           - e.g., "OOOX", "X" at index 3; 3 "O"s
#   -- update config to config[curr_max:]
#      - e.g., with "OOOXOOOOX", curr_max == 3
#              so update to "XOOOOX"


# Decomposition of finding the middle of a sequence
# of "O"s, M

# Notice that given a start index, s, and an
# end index, e, we want the middle, M, to be
# at index (s + e - 1) // 2.

#           INDICES         
#         0 1 2 3 4 5 6     s   e   M
# ------------------------------------
# len 3:  - M - . . . .     0   3   1
# len 4:  - M - - . . .     0   4   1
# len 5:  - - M - - . .     0   5   2
# len 6:  - - M - - - .     0   6   2
# len 7:  - - - M - - -     0   7   3

# So, given the start index, s, and end index, e,
# the middle of that sequence is (s+e-1)//2



# STEP 3:

# IMPLEMENT THE SOLUTION

# Implement decomposition to find the longest
# sequence of "O"s in config:
# - let curr_max = 0
# - while len(config) > 0:
#   -- since config[0] is "X", remove it:
#      let config = config[1:]
#   -- if config.find("X") > curr_max:
#      ---- update curr_max to config.find("X")
#           - given "O...OX", "X" index == num "O"s
#           - e.g., "OOOX", "X" at index 3; 3 "O"s
#   -- update config to config[curr_max:]
#      - e.g., with "OOOXOOOOX", curr_max == 3
#              so update to "XOOOOX"

def max_space_length(config):
  curr_max = 0
  while len(config) > 0:
    config = config[1:]
    count = config.find("X")
    if count > curr_max:
      curr_max = count
    config = config[count:]
  return curr_max


# Now implement the main solution
# - while the longest sequence of "O"s > 2:
#   -- find middle index of that sequence, M
#   -- replace config[M] with "X"

# Recall that given the start index, s, and
# end index, e, # the middle of that sequence
# is (s+e-1)//2.

# Also, note that given we know how long
# the longest sequence is, we can find that
# substring using: "O" * max_Os.

def tram_packing_iter(config):
  max_Os = max_space_length(config)
  while max_Os > 2:
    s = config.find("O" * max_Os)
    e = s + max_Os
    M = (s + e - 1) // 2
    config = config[:M] + "X" + config[M+1:]
    max_Os = max_space_length(config)
  return config



# STEP 4:

# TEST THE IMPLEMENTATION OF THE SOLUTION

# YOU MAY CONSIDER TESTING THE DECOMPOSED
# SUB-PROBLEM SOLUTIONS SEPARATELY AS WELL

### Uncomment to Test
print("iterative:")
print(tram_packing_iter("XOX")=="XOX")
print(tram_packing_iter("XOOX")=="XOOX")
print(tram_packing_iter("XOOOX")=='XOXOX')
print(tram_packing_iter("XOOOOX")=="XOXOOX")
print(tram_packing_iter("XOOOOOX")=="XOOXOOX")
print(tram_packing_iter("XOOOOOOX")=="XOOXOXOX")
print(tram_packing_iter("XOOOOOOOX")=="XOXOXOXOX")
print(tram_packing_iter("XOOOOOOOOX")=="XOXOXOXOOX")
print(tram_packing_iter("XOOOOOOOOOX")=='XOXOOXOXOOX')
print(tram_packing_iter("XOOOOOOOOOOOOOOOOOOOOOOOOOOOX")=='XOOXOXOXOOXOXOXOOXOXOXOOXOXOX')
print()



# STEP 5: No need to do this in an exam setting.
# -- However, after the exam, you can always analyse
#    the solution to see if any useful patterns for
#    future use





###############
# Task 1B     #
###############

"""
Implement the function tram_packing_rec(config)
that returns the final seating arrangement given
the initial seating configuration.

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

# Decomposition of max_space_length
'''
def max_space_length(config):
  curr_max = 0
  while len(config) > 0:
    config = config[1:]
    count = config.find("X")
    if count > curr_max:
      curr_max = count
    config = config[count:]
  return curr_max
'''
def max_space_length_rec(config):
  if len(config) == 0:
    return 0
  else:
    config = config[1:]
    count = config.find("X")
    next_count = max_space_length_rec(config[count:])
    if count > next_count:
      return count
    else:
      return next_count


# Main solution
'''
def tram_packing_iter(config):
  max_Os = max_space_length(config)
  while max_Os > 2:
    s = config.find("O" * max_Os)
    e = s + max_Os
    M = (s + e - 1) // 2
    config = config[:M] + "X" + config[M+1:]
    max_Os = max_space_length(config)
  return config
'''
def tram_packing_rec(config):
  max_Os = max_space_length_rec(config)
  if max_Os <= 2:
    return config
  else:
    s = config.find("O" * max_Os)
    e = s + max_Os
    M = (s + e - 1) // 2
    config = config[:M] + "X" + config[M+1:]
    return tram_packing_rec(config)



# STEP 4:

# REMEMBER THAT YOU SHOULD TEST EACH SOLUTION
# AND SUB-SOLUTION SEPARATELY (NOTE: I HAVE
# OMITTED THE TESTING OF SUB-SOLUTIONS HERE)

print("recursive:")
print(tram_packing_rec("XOX")=="XOX")
print(tram_packing_rec("XOOX")=="XOOX")
print(tram_packing_rec("XOOOX")=='XOXOX')
print(tram_packing_rec("XOOOOX")=="XOXOOX")
print(tram_packing_rec("XOOOOOX")=="XOOXOOX")
print(tram_packing_rec("XOOOOOOX")=="XOOXOXOX")
print(tram_packing_rec("XOOOOOOOX")=="XOXOXOXOX")
print(tram_packing_rec("XOOOOOOOOX")=="XOXOXOXOOX")
print(tram_packing_rec("XOOOOOOOOOX")=='XOXOOXOXOOX')
print(tram_packing_rec("XOOOOOOOOOOOOOOOOOOOOOOOOOOOX")=='XOOXOXOXOOXOXOXOOXOXOXOOXOXOX')
print()



# STEP 5: Consider adding any useful patterns
#         (after the assessment)

### ALTERNATIVE of max_space_length(config):
def max_space_length(config):
  max_len = 0
  curr_len = 0
  i = 1
  while i < len(config):
    if config[i] == "X":
      if curr_len > max_len:
        max_len = curr_len
      curr_len = 0
    else:
      curr_len = curr_len + 1
    i = i + 1
  return max_len
