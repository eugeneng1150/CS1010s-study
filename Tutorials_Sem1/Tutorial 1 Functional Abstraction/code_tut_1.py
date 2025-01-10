# Question 1
from math import sqrt
def sum_of_squares(a,b,c):
    if a > b or a > c:
        if b > c:
            return a**2 + b**2
        return a**2 + c**2
    return b**2 + c**2

print(sum_of_squares(10,2,3))

def magnitude(x1 ,y1, x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)
print(magnitude(2,2,5,6))

def is_leap_year(year):
    if year % 4 != 0: # checks for years that are not divisible by 4, immediately not leap year
        return False
    if year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    else:
        return False
print(is_leap_year(2000))
