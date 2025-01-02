# REVISE
for i in range(5):
    print(i)
    i += i
# prints 0 to 4
# although i is modified in the 3rd line, 
# i is always present back to the original sequence 0,1,2,3,4
# this means 0 ,1,2,3,4 will be printed out but when exiting out of the for loop i = 8