def sum_even_factorial(n):
    if n <= 1:
        return 1
    else:
        if n % 2 == 0:
            return n * sum_even_factorial(n-1)
        else:
            sum_even_factorial(n-1)
print(sum_even_factorial(6))


def star_wars_function_iter(n):
    iter = ""
    for i in range(n):
        if i % 2 == 0:
            iter += "*-"
        else:
            iter += "*--"
    return iter
print(star_wars_function_iter(1))

# def star_wars_function_res(n):
#     if n == 0:
#         return ""
#     else:
#         return "*-" + star_wars_function_res(n-1)
# print(star_wars_function_res(4))

def star_wars_function_res(n): # revise this again
    if n == 0:
        return ""
    beam = "*-" if n % 2 == 1 else "*--"
    return star_wars_function_res(n-1) + beam # position of beam matters
print(star_wars_function_res(6))
print(star_wars_function_res(5))



def count_digits(number):
    digit = 0
    while number > 0:
        digit += 1
        number = number // 10
    return digit
print(count_digits(12334))


print(2 % 3)
