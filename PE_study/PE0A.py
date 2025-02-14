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
def store_digit(text):
  count = 1
  res = ""
  for i in range(len(text)-1):
    left_pointer = text[i]
    right_pointer = text[i+1]
    if left_pointer == right_pointer:
      count += 1
    else:
        res += str(count)
        count = 1
  res += str(count)
  return str(res)

def reduce_text(text):
  first_letter = text[0]
  res = "" 
  for i in range(len(text)-1):
    if text[i] != text[i+1]:
      res += text[i]
    else:
      continue
  res += text[-1]
  return res

def run_length_iter(text):
  res = ""
  rizz = reduce_text(text) #ahem
  number = store_digit(text) #5342
  for i in range(len(rizz)):
    res += rizz[i] + number[i]

  return res



# ### Uncomment to Test
# print(run_length_iter("AAAAAHHHEEEEMM"))                 # 'A5H3E4M2'
# print(run_length_iter("AAAABBAAAB"))                     # 'A4B2A3B1'
# print(run_length_iter("AAAAAAAAABBBBBBBBBC"))            # 'A9B9C1'
# print(run_length_iter("Z"))                              # 'Z1'
# print(run_length_iter("TTT"))                            # 'T3'
# print(run_length_iter("AAAAAAAAABAAAAAAAAABAAAAAAAAA"))  # 'A9B1A9B1A9'


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

# def store_digit(text):
#   count = 1
#   res = ""
#   for i in range(len(text)-1):
#     left_pointer = text[i]
#     right_pointer = text[i+1]
#     if left_pointer == right_pointer:
#       count += 1
#     else:
#         res += str(count)
#         count = 1
#   res += str(count)
#   return str(res)

def store_digit_rec(text, count = 1):
  if len(text) == 1 :
    return str(count)
  else:
    if text[0] == text[1]:
      return  store_digit_rec(text[1:], count = count + 1)
    else:
      return str(count) + store_digit_rec(text[1:], count =1)

def reverse_digit(s1):
  return s1[::-1]
# def reduce_text(text):
#   first_letter = text[0]
#   res = "" 
#   for i in range(len(text)-1):
#     if text[i] != text[i+1]:
#       res += text[i]
#     else:
#       continue
#   res += text[-1]
#   return res

def reduce_text_rec(text):
  if len(text) == 1:
    return text
  else:
    if text[0] != text[1]:
      return text[0] + reduce_text_rec(text[1:])
    else:
      return reduce_text_rec(text[1:])

#AHEM
#5342
def count_first_seq_rec(text):
  if len(text) == 1 or len(text) > 1 and text[0] != text[1]:
    return 1
  else:
    return 1 + count_first_seq_rec(text[1:])
print(count_first_seq_rec("AAAB"))

def run_length_rec(text):
  if len(text) == 0:
    return ""
  else:
    curr_seq_count = count_first_seq_rec(text)
    res = text[0] + str(curr_seq_count)
    return res + run_length_rec(text[curr_seq_count:])

## Uncomment to Test
print(run_length_rec("AAAAAHHHEEEEMM"))                 # 'A5H3E4M2'
print(run_length_rec("AAAABBAAAB"))                     # 'A4B2A3B1'
#print(run_length_rec("AAAAAAAAABBBBBBBBBC"))            # 'A9B9C1'
#print(run_length_rec("Z"))                              # 'Z1'
#print(run_length_rec("TTT"))                            # 'T3'
#print(run_length_rec("AAAAAAAAABAAAAAAAAABAAAAAAAAA"))  # 'A9B1A9B1A9'
