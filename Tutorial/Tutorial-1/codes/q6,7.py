def total_legs(chickens, cows):
    total = 0
    num_legs_chickens = chickens * 2
    num_legs_cows = cows *4
    total = num_legs_chickens +num_legs_cows
    return total

print(total_legs(2,2)) 

def tax_count(chickens, cows):
    tax = total_legs(chickens, cows) * 2
    return tax
print(tax_count(2,2))

def too_many(chickens, cows):
    number_animals = chickens + cows
    if number_animals > 10:
        return True # 5 taxs
    else:
        return False
    
print(too_many(2,2))
print(too_many(7,4))

def total(chickens, cows):
    total_tax = 0
    if too_many(chickens, cows) == True:
        total_tax = 5 + tax_count(chickens, cows)
    else:
        total_tax = tax_count(chickens, cows)
    return total_tax
print(total(2,2))
print(total(10,1))

# If the word is shorter than
# 4 letters, the entire word is masked. This function will be called maskify that takes in a
# word and returns the new masked word.

def maskify(word):
    password = ""
    if len(word) < 4:
        for _ in word:
            password += "*"
    else:
        for i in range(len(word) - 4):
            password += word[i]
        password += "****"
    return password


print(maskify("SKIBIDI TOILET RIZZS")) 


