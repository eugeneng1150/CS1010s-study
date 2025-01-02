# question 4
def score(pins): # my answer
    score = 0
    pins = str(pins) #O(n) # converting the integer into a string of n character, requiring O(n)
    for digit in pins:
        score += int(digit)
    return score
print(score(999))
# O(n) time complexity 
# The string converstion is O(n), and the loop with n iteration and O(1) operation is also O(n)
# O(n) space complexity

## How to optimize this?
def score(pins):
    score = 0
    while pins > 0:
        score += pins % 10  # Get the last digit
        pins //= 10  # Remove the last digit
    return score
# O(n) time complexity
# O(1) space complexity

def score_recursive(pins): # revise recursive functions 
    #base case
    if pins < 0:
        return pins
    else: 
        return pins % 10 + score_recursive(pins // 10)
# O(n) time complexity
# O(n) space complexity

def strike_count(pins): # iterative approach
    strike = 0
    pins = str(pins)
    for digit in pins:
        if digit == "9":
            strike += 1
    return strike
print(strike_count(919))

def strike_count_recursive(pins): # revise this
    if pins < 10:
        return int(pins == 9)
    return int(pins % 10 == 9) + strike_count_recursive(pins // 10)
print(strike_count_recursive(999))

def score_improved(pins):
    total_score = 0
    total_score += strike_count_recursive(pins) * 5
    total_score += score(pins)
    return total_score
print(score_improved(919))

# question 5
#-----------------------------------------------
def maskify(password):
    mask_pass = ""
    for _ in range(len(password)):
        mask_pass += "*"
    return mask_pass
# O(n) time complexity as iterate through len of password  
## wrong ^
## O(n^2) time complex due to string concatation 
## String concatenation inside a loop is not efficient in Python because strings are immutable.
##Each time you concatenate, a new string is created, and the existing characters are copied to it. 
## This copying takes 𝑂(𝑘), where 𝑘 is the current length of mask_pass.

##  O(n) space complexity since new string of n character is form ## correct
# -----------------------------------------------------------------------------------
def maskify_recursive(word):
    if len(word) == 0:
        return ""
    return "*" + maskify_recursive(word[:-1])
# O(n) time complexity 
# O(1) space complexity since no variable is initialize
## WRONG ^^
## O(n^2) due to string concatation
## Each recursive call adds a new frame to the call stack.
# For a string of length 𝑛, there are 𝑛 recursive calls before reaching the base case.
# So, the call stack uses 𝑂(𝑛) space.

def slot(word):
    if len(word) <= 1:
        return word
    return word[0] + "*" + slot(word[1:]) #slice off the first letter of the word
print(slot("pepepopo"))

def advance_slot(word):
    if len(word) <= 1:
        return word
    if word[0] == word[1]:
        return word[0] + "*" + advance_slot(word[1:])
    return word[0] + advance_slot(word[1:])


# learning points:
# 1) recursive function takes a base case, no need to initialize a variable for it, 2 or more return statement
# 2) n % 10 will return the last digit
# 3) n // 10 removes the last digit and returns a new digit
# 4) in a recursive function, to slice off the word, return word[0] + "*" + advance_slot(word[1:]) 
# this slice off first character