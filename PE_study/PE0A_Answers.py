###############
# Question 1  #
###############

"""
A run-length encoding is a form of lossless data compression
in which runs of data are stored as a single data value
together with the count.
"""


###############
# Task 1A     #
###############

"""
Implement the function run_length_iter(text)
that returns the RLE encoded text.

The function must be implemented using iteration
and without any recursion.  Make sure any helper
function is non-recursive (or built-in).
"""



# STEP 1:

# INPUT ANALYSIS
# We are given a str, text
# - len(text) >= 1
# - text only includes UPPERCASE ALPHABET
#   (i.e., ABCDEFGHIJKLMNOPQRSTUVWXYZ)
# - there will be AT MOST 9 consecutive characters
#   in each segment

# HIGH-LEVEL IDEA ON OUTPUT
# For each sequence, i.e., a consecutive sequence of the
# same letter, we need to only print the letter once,
# followed by a digit (1 to 9) representing how many times
# that letter as occured in that sequence. Note that before
# the start and end of the sequence, there should exist
# either a different letter, or the start/end of the str,
# text.



# STEP 2:

# PLANNING THE SOLUTION (PSEUDOCODE)

# - starting from the left of text (i.e., index 0)
# - count the number of times text[0] is repeated;
#   denote the number of repeats of text[0] as k
#   (remember that 1 <= k <= 9)
# - record the encoding text[0] + k (as str)
# - then separate the sequence just considered;
#   i.e., remove the first sequence from text
# - repeat the process until text is an empty str



# STEP 3:

# IMPLEMENT THE SOLUTION

# Notice from our solution that we needed to
# "count the number of times text[0] is repeated".
# Let us perform decomposition and solve this
# sub-problem. Here, we can summarise the problem
# into finding the last index with the same character
# as text[0] (consecutive).

# Decomposition of "count the number of times
# text[0] is repeated"
# -- perform problem-solving on this sub-problem
#    ---- you should already be familiar with a 
#         solution to this sub-problem
#         - i.e., iterate through str and stop
#                 once the next char is diff from
#                 the previous char.
# -- we thus get the following
def count_first_seq(text):
  count = 1 # let's count the first character
  i = 0
  while i+1 < len(text) and \
        text[0] == text[i+1]: # text[i] == text[i+1] also ok 
    count = count + 1
    i = i + 1
  return count

# Then follow the PSEUDOCODE given above:

# - starting from the left of text (i.e., index 0)
# - count the number of times text[0] is repeated;
#   denote the number of repeats of text[0] as k
#   (remember that 1 <= k <= 9)
# - record the encoding text[0] + k (as str)
# - then separate the sequence just considered;
#   i.e., remove the first sequence from text
# - repeat the process until text is an empty str

# We thus get the following:
def run_length_iter(text):
  res = ""
  while len(text) > 0: # we will remove seq. already done
                       # so keep iterating until no more seq.
    curr_seq_count = count_first_seq(text) # use decomposition
    res = res + text[0] + str(curr_seq_count) # record encoding
    text = text[curr_seq_count:] # remove the first seq.
    # notice that if there are 3 characters in the seq.,
    # curr_seq_count = 3, which is the index of the character
    # after the first 3 characters!
  return res



# STEP 4:

# TEST THE IMPLEMENTATION OF THE SOLUTION

# First, test count_first_seq(text):
print("count_first_seq")
s = "AAAAAHHHEEEEMM"
print(s, count_first_seq(s))
s = "AAAABBAAAB"
print(s, count_first_seq(s))
s = "AAAAAAAAABBBBBBBBBC"
print(s, count_first_seq(s))
s = "Z"
print(s, count_first_seq(s))
s = "TTT"
print(s, count_first_seq(s))
s = "AAAAAAAAABAAAAAAAAABAAAAAAAAA"
print(s, count_first_seq(s))
print()

# Then, test run_length_iter(text):
### Uncomment to Test
print(run_length_iter("AAAAAHHHEEEEMM"))                 # 'A5H3E4M2'
print(run_length_iter("AAAABBAAAB"))                     # 'A4B2A3B1'
print(run_length_iter("AAAAAAAAABBBBBBBBBC"))            # 'A9B9C1'
print(run_length_iter("Z"))                              # 'Z1'
print(run_length_iter("TTT"))                            # 'T3'
print(run_length_iter("AAAAAAAAABAAAAAAAAABAAAAAAAAA"))  # 'A9B1A9B1A9'
print()



# STEP 5: No need to do this in an exam setting.
# -- However, after the exam, you can always analyse
#    the solution to see if any useful patterns for
#    future use





###############
# Task 1B     #
###############

"""
Implement the function run_length_rec(text)
that returns the RLE encoded text.

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

# Decomposition of "count the number of times
# text[0] is repeated"
'''
def count_first_seq(text):
  count = 1
  i = 0
  while i+1 < len(text) and text[0] == text[i+1]:
    count = count + 1
    i = i + 1
  return count
'''
def count_first_seq_rec(text):
  if len(text) == 1 or len(text) > 1 and text[0] != text[1]:
    return 1
  else:
    return 1 + count_first_seq_rec(text[1:])

'''
def run_length_iter(text):
  res = ""
  while len(text) > 0: # we will remove seq. already done
                       # so keep iterating until no more seq.
    curr_seq_count = count_first_seq(text) # use decomposition
    res = res + text[0] + str(curr_seq_count) # record encoding
    text = text[curr_seq_count:]
'''
def run_length_rec(text):
  if len(text) == 0:
    return ""
  else:
    curr_seq_count = count_first_seq_rec(text)
    res = text[0] + str(curr_seq_count)
    return res + run_length_rec(text[curr_seq_count:])



# STEP 4:

# TEST THE IMPLEMENTATION OF THE SOLUTION

# First, test count_first_seq_rec(text):
print("count_first_seq_rec")
s = "AAAAAHHHEEEEMM"
print(s, count_first_seq_rec(s))
s = "AAAABBAAAB"
print(s, count_first_seq_rec(s))
s = "AAAAAAAAABBBBBBBBBC"
print(s, count_first_seq_rec(s))
s = "Z"
print(s, count_first_seq_rec(s))
s = "TTT"
print(s, count_first_seq_rec(s))
s = "AAAAAAAAABAAAAAAAAABAAAAAAAAA"
print(s, count_first_seq_rec(s))
print()

# Then, test run_length_rec(text):
### Uncomment to Test
print("run_length_rec:")
print(run_length_rec("AAAAAHHHEEEEMM"))                 # 'A5H3E4M2'
print(run_length_rec("AAAABBAAAB"))                     # 'A4B2A3B1'
print(run_length_rec("AAAAAAAAABBBBBBBBBC"))            # 'A9B9C1'
print(run_length_rec("Z"))                              # 'Z1'
print(run_length_rec("TTT"))                            # 'T3'
print(run_length_rec("AAAAAAAAABAAAAAAAAABAAAAAAAAA"))  # 'A9B1A9B1A9'
print()



# STEP 5: Consider adding any useful patterns
#         (after the assessment)
