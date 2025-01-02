result = 0
for i in range(1, 13, 3): # 1 ,4 , 7, 10
    if i % 2 == 0:
        i += 2
    else:
        result //= i
    result += i
# results: 1, 7, 8, 20  ## revise this again
print(result)
# 20