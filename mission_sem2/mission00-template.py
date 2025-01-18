# CS1010S --- Programming Methodology
# Mission 0

############################################################################
# Note that written answers are commented out to allow us to run your code #
# easily while grading your problem set.                                   #
#                                                                          #
# The expected answer is what you think the line of code will produce if   #
# it were to be run in IDLE.                                               #
#                                                                          #
# The final answer is the actual output after running the line of code.    #
# You may leave the final answer blank if the output is what you expected. #
############################################################################

############################################################################
# The first line has already been uncommented for you.                     #
# If a line causes an error, you should leave it commented out.            #
#                                                                          #
# Just press F5 to run this file in IDLE.                                  #
# On Mac, the shortcut for running your script is <fn> + F5 or <cmd> + F5. #
# In some Windows systems, it may be <fn> + F5 or <ctrl> + F5.             #
############################################################################

##########
# Task 1 #
##########

############
# Examples #
############

# Example 1:
# My expected result is zero but upon printing the result is 0.
print(0)
# expected answer: zero
# final answer: 0

# Example 2:
# My expected result is 1 which turns out to be correct after I run the
# print statements, so I don't need to do anything for the final answer.
print(1)
# expected answer: 1
# final answer:

# Example 3:
# This print statement results in an error,
# so I need to comment it and put the specific error as shown.
#print(a)
# expected answer: NameError: name 'a' is not defined
# final answer:

##############################
## YOUR MISSION STARTS HERE ##
##############################

#print(42)
# expected answer: 42
# final answer:

#print(0000)
# expected answer: 0000
# final answer:0

#print("the force!")
# expected answer: the force!
# final answer:

#print("Hello World")
# expected answer: Hello World
# final answer:

#print(6 * 9)
# expected answer:54
# final answer:

#print(2 + 3)
# expected answer:5
# final answer:

#print(2 ** 4)
# expected answer:16
# final answer:

#print(2.1**2.0)
# expected answer:4.41
# final answer:

#print(15 > 9.7)
# expected answer:True
# final answer:

#print((5 + 3) ** (5 - 3))
# expected answer:64
# final answer:

#print(--4)
# expected answer:4
# final answer:

#print(1 / 2)
# expected answer:0.5
# final answer:

#print(1 / 3)
# expected answer:0.33333333333
# final answer:0.3333333333333333

#print(1 / 0)
# expected answer: ZeroDivisionError
# final answer: ZeroDivisionError: division by zero

#print(7 / 3 == 7 / 3.0)
# expected answer: False
# final answer:True

#print(3 * 6 == 6.0 * 3.0)
# expected answer: True
# final answer:

#print(11 % 3)
# expected answer: 2
# final answer:

#print(2 > 5 or (1 < 2 and 9 >= 11))
# expected answer:False
# final answer:

#print(3 > 4 or (2 < 3 and 9 > 10))
# expected answer:False
# final answer:

#print("2" + "3")
# expected answer:Int error
# final answer:23

#print("2" + "3" == "5")
# expected answer:False
# final answer:

#print("2" <= "5")
# expected answer:True
# final answer:

#print("2 + 3")
# expected answer:5
# final answer:2 + 3

#print("May the force" + " be " + "with you")
# expected answer:May the force be with you
# final answer:

#print("force"*2)
# expected answer:forceforce
# final answer:

#print('daw' in 'padawan')
# expected answer:True
# final answer:

a, b = 3, 4 # Do not comment or remove this line

#print(a)
# expected answer: 3
# final answer:

#print(b)
# expected answer:4
# final answer:

a, b = b, a # Do not comment or remove this line

#print(a)
# expected answer:4
# final answer:

#print(b)
# expected answer:3
# final answer:

#print(red == 44)
# expected answer:Undefined
# final answer:NameError: name 'red' is not defined

red, green = 44, 43 # Do not comment or remove this line

#print(red == 44)
# expected answer:True
# final answer:

#print(red = 44)
# expected answer:44
# final answer:TypeError: print() got an unexpected keyword argument 'red'

#print("red is 1") if red == 1 else print("red is not 1")
# expected answer:red is not 1
# final answer:

#print(red - green)
# expected answer:1
# final answer:

purple = red + green # Do not comment or remove this line

#print("purple")
# expected answer:purple
# final answer:

#print("purple"[7])
# expected answer:IndexError
# final answer:IndexError: string index out of range

#print(red + green != purple + purple / purple - red % green)
# expected answer:False
# final answer:

#print(green > red)
# expected answer:False
# final answer:

#print("green bigger") if green > red else print("red equal or bigger")
# expected answer:red equal or bigger
# final answer:

#print(green + 5)
# expected answer:48
# final answer:

#print(round(3.8))
# expected answer:4
# final answer:

#print(int(3.8))
# expected answer:TypeError
# final answer:3

#print(int("3.8"))
# expected answer:TypeError
# final answer:ValueError: invalid literal for int() with base 10: '3.8'

# Run these lines of code before proceeding to the next question!
# Do not comment these lines or remove it from your submission!
def f(n):
    if n == 1: return 1
    return n + f(n - 1)

#print(f(4))
# expected answer: 10
# final answer:

#print(f(f(2)))
# expected answer:6
# final answer:

#print(f(0))
# expected answer:RecursionError
# final answer:RecursionError: maximum recursion depth exceeded

d = {1: 2} # Do not comment or remove this line

#print(d[1])
# expected answer:2
# final answer:

#print(d[2])
# expected answer:Error
# final answer:KeyError: 2

d[2] = "apple" # Do not comment or remove this line

#print(d[2])
# expected answer:p
# final answer:apple

#############################################################
# The following question is to ensure that you have         #
# installed all the package(s) correctly:                   #
# - PILLOW                                                  #
#                                                           #
# Just uncomment the line "from <package> import *",        #
# run the line, and observe the output.                     #
#                                                           #
# If there is no output, the package(s) have been installed #
# correctly, so answer "Nothing" to let us know that it's   #
# working properly. Otherwise, if you see some errors, do   #
# refer to the troubleshooting guide in the PDF file.       #
#############################################################

#from PIL import *
# expected answer:Nothing
# final answer:
