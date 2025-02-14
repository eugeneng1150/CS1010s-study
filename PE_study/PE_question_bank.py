################################################################################
# CS1010S --- Programming Methodology
#
# CONSULTATION REVIEW NOTES 3 - PATTERNS FOR PROBLEM-SOLVING
################################################################################



# RECALL OUR GENERAL LEARNING OBJECTIVES: DESCRIBED IN RECITATION NOTES,
# WHICH ARE ABOUT THE PROBLEM-SOLVING FRAMEWORK:

# 1. PROBLEM-SOLVING 
#    - Be able to apply the general problem-solving steps to solve CS1010S Qs.
#    - "General" above means "board" -- you will refine how to perform these
#      steps as you learn more during the course (and with practice).
#       - Step 1: know your problem, and in particular the inputs
#       - Step 2: define a SPECIFIC solution (need not be expressed with code)
#       - Step 3: translate your solution into code (if not already in code)
#       - Step 4: test and analyse your solution (to make sure it is working)
#       - Step 5: try to generalise your code to solve other similar problems

# 2. PATTERNS -> THINGS THAT GO ONTO YOUR PATTERN BANK (I.E., CHEAT SHEET)
#    - Patterns corresponds to solutions and code to COMMON PROBLEMS.
#    - This should help you with STEP 2 of PROBLEM SOLVING since it gives
#      ideas about functionality that you can perform (i.e., it suggests
#      the things that you can do.
#    - Typically, these happen to common pieces of functionality that you
#      often encounter during the course.
#    - You can consider these the solutions to SUB-PROBLEMS.

# 3. EXAMPLE PATTERNS
#    - To get you started, we can think about the following.
#       - str patterns
#       - int patterns
#    - I will add some of these during the session - these will appear below.

# 4. REMEBER TO MAINTAIN YOUR PATTERN BANK
#    - Once in a while, you should consider removing patterns from your
#      pattern bank. The patterns you remove should be the patterns
#      that you have come to know well (i.e., you need not reference any
#      longer).
#    - Another option is to GENERALISE patterns. If you notice that two (or
#      more) patterns are very similar, then you should try to replace both
#      with the more generalised version.



################################################################################
# str PATTERNS
################################################################################

# str PATTERN 1: Find substring sub in str S
def str_find(S, sub):
    for i in range(len(S)):
        if S[i:i+len(sub)] == sub:
            return True
    return False
print("str_find test:", str_find("123213221", "32"))
print()

# str PATTERN 2: Count number of substrings sub in str S
print("<str>.count test:", "123213221".count("32")) 
print()

# str PATTERN 3: insert substring sub into str S at index i
def str_insert(S, sub, i):
    return S[:i] + sub + S[i:]
print("str_insert test:", str_insert("0123456789", "abc", 5))
print()

# str PATTERN 4: delete character from str S at index i
def str_del(S, i):
    return S[:i] + S[i+1:]
print("str_del test:", str_del("0123456789", 5))
print()

# str PATTERN 5: reverse the str S
def str_reverse(S):
    return S[::-1]
print("str_reverse test:", str_reverse("0123456789"))
print()

# str PATTERN 6a: iterating through str S (from right to left)
def str_itr_r2lv1(S):
    for i in range(len(S)-1,-1,-1):
        print(S[i]) # can replace this with any desired functionality on S[i]
print("str_itr_r2lv1 test:")
str_itr_r2lv1("0123456789")
print()

# str PATTERN 6b: iterating through str S (from right to left)
def str_itr_r2lv2(S):
    S = str_reverse(S)
    for i in range(len(S)):
        print(S[i]) # can replace this with any desired functionality on S[i]
print("str_itr_r2lv2 test:")
str_itr_r2lv2("0123456789")
print()

# int PATTERN 7a: Determine if a given str S is Palindrome (recursive impl.)
def str_palin_v1(S):
    if len(S) < 2:
        return True
    else:
        return S[0] == S[-1] and str_palin_v1(S[1:-1])
print("str_palin_v1 test:", str_palin_v1("racecar"))
print()

# int PATTERN 7b: Determine if a given str S is Palindrome (iterative impl.)
def str_palin_v2(S):
    while len(S) > 2:
        if S[0] != S[-1]:
            return False
        S = S[1:-1]
    return True
print("str_palin_v2 test:", str_palin_v2("racecar"))
print()

# other PATTERNS 8: Print the anagrams of str S
def str_anagram(S):
    def helper(r, S):
        if len(S) < 2:
            print(r+S)
        else:
            for i in range(len(S)):
                helper(r+S[i], S[:i]+S[i+1:])    
    helper("",S)
print("str_anagram test:")
str_anagram("ABC")
print()

# sum patterns with added counter
def num_cards(h):
    count = 2
    adder = 5
    for i in range(1,h):
        count += adder
        adder += 3
    return count

# Count first few consecative alphabet
def count_first_seq_rec(text):
    if len(text) == 1 or len(text) > 1 and text[0] != text[1]:
        return 1
    else:
        return 1 + count_first_seq_rec(text[1:])
print("Count first seq test: ", count_first_seq_rec("AAAB"))
print()
# How to reduce many alphabet into numbers like A5B4
def run_length_rec(text):
    if len(text) == 0:
        return ""
    else:
        curr_seq_count = count_first_seq_rec(text)
        res = text[0] + str(curr_seq_count)
        return res + run_length_rec(text[curr_seq_count:])
print("Run_length_rec test", run_length_rec("AAABBBCCC"))
print()

# Interleave example
def interleave(s1,s2,k):
    if s1 == "" or s2 == "":
        return s1 + s2
    else:
        new = s1[:k] + s2[:k]
        s1 = s1[k:]
        s2 = s2[k:]
        return new + interleave(s1,s2,k)
    
# Count pairs in a string (slice a string during recursion)
def num_pair_rec(s):
    if len(s) < 2:
        return 0
    else:
        if s[0] != s[1]:
            return num_pair_rec(s[1:]) 
        else:
            return 1 + num_pair_rec(s[1:]) # note the +1

################################################################################
# int PATTERNS
################################################################################

# int PATTERN 1: How do we interate through int x (from right to left)
def int_itr(x):
    while x > 0:
        print(x % 10) # can replace this with any desired functionality on digit
        x = x // 10

# int PATTERN 2: Count the number of digits in int x
def int_count_digits(n): 
    count = 0
    while n > 0: # uses idea of int PATTERN 1
        last = n % 10
        if last != 0:
            count += 1
        n = n // 10
    return count
print("int_count_digits test:", int_count_digits(1234567))
print()

# int PATTERN 3a: Determine if int (with fewer digits) x exists in int y
#                (Given that you cannot convert to str.)
def int_findv1(x, y):
    digits_in_x = int_count_digits(x)
    while y > 0:
        if (y % 10**digits_in_x) == x:
            return True
        y = y // 10
    return False    
print("int_findv1 test:", int_findv1(5678, 1234567890))
print()

# int PATTERN 3b: Determine if int (with fewer digits) x exists in int y
def int_findv2(x, y):
    return str_find(str(y), str(x))
print("int_findv2 test:", int_findv2(5678, 1234567890))
print()

# int PATTERN 4: Count the Number of Times X Appears as a Subsequence in Y
def count(main, sub):
    res = 0
    if int_count_digits(sub) > int_count_digits(main):
        return 0
    length_of_sub = int_count_digits(sub)
    while main > 0:
        remainder = main - sub
        if remainder % (10 ** length_of_sub) == 0:
            res += 1
        main = main // 10
    return res
print("count test:", count(121212 , 121))

# int Number of pairs of X in Y (2 Pointer)
def num_pairs_iterative(s):
    count = 0
    for i in range(len(s) - 1):
        left_pointer = s[i]
        right_pointer = s[i+1]
        if left_pointer == right_pointer:
            count += 1
        else:
            continue
    return count
print("Number of pairs test:", num_pairs_iterative("AAAAAHHHH"))

# Int calculation of Area (trival)
def area(n):
    if n == 0 :
        return 1
    else:
        return area(n-1) * 0.75 # main idea is to remember to add operations at return function
    
def exponential(x , n):
    if n ==0:
        return 1
    elif n % 2 == 0 :
        rec = exponential(x , n // 2)
        return rec * rec
    else:
        rec = exponential(x , n // 2)
        return rec * rec * x
    
# How to reverse a string though recursion
def reverse_rec(s):
    if s == "":
        return ""
    else:
        return s[-1] + reverse_rec(s[:-1])
print("reverse_rec test: ", reverse_rec("ABCDEF"))
    




################################################################################
# NOTES 
################################################################################
# Integer operations:
# n - 1 , n // 2, n // 10, n // m
# use % to get last digit
# use // to isolate front few digits

# Sequence operations:
# s[1:] or s[:-1] # remove 1
# s [1:-1] remove edges
# often seq[1:] is paired with s[0]

################################################################################
