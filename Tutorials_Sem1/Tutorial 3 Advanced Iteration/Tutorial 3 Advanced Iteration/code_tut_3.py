def baz(): # revise again
    count = 0
    for i in range(1, 6, 1):
        if i % 3 > 0:
            count = count + 3
        if i % 2 == 0:
            continue
        print(count)
    while count != 0:
        count = count // 2
        if count <= 1:
            break
        print(count)
# print(baz())
# 3 , 6 , 12 , 6, 3 None (since no return statement)

def num_pairs(word):
    pair = 0
    for i in range(len(word) - 1): # len(word) - 1 is crucial if not will raise IndexError
        if word[i] == word[i + 1]:
            pair += 1
        else:
            continue
    return pair
# print(num_pairs("ss"))

