
# def multiple_numbers(num):

# def multiple_numbers(*num):
#     print(num)

# multiple_numbers(1, 2, 3, 4, 5)
# multiple_numbers(1, 2, 3)
# multiple_numbers(1, 2, 3, 4)

# raise error
# def multiple_numbers_with_list(num):
#     print(num)

# multiple_numbers_with_list([1, 2, 3, 4, 5])

# raise Error
# def multiple_numbers_with_list(a, b, num):
#     print(a)
#     print(b)
#     print(num)

# multiple_numbers_with_list(*[1, 2, 3, 4, 5])


# def multiple_numbers_with_list(a, b, *num):
#     print(a)
#     print(b)
#     print(num)
    # for num in num:
    #     print(num)

# multiple_numbers_with_list(*[1, 2, 3, 4, 5])
# multiple_numbers_with_list(*[1, 2])
# multiple_numbers_with_list(*[1])


# Postional-Only Arguments

# def posFun(a, b, /, c):
#     print(a + b + c)


# posFun(a=1, b=2, c=3)
# posFun(1, 2, c=3)


# Keyword-Only Arguments

# def posFun(*, a, b, c):
#     print(a + b + c)


# # posFun(1, 2, c=3)
# posFun(a=1, b=2, c=3)



# def posFun(a, /, b, *, c):
#     print(a + b + c)


# # posFun(a=1, b=2, c=3)
# posFun(1, 2, c=3)


# def add(): # Function Definition / Statement / Declaration
#     a = 10
#     b = 20
#     sum = a + b
#     return sum

# # print(sum)
# result = add() # Function Calling / Invoction
# print(result)


# Anonymouse Function / Lambda Function

# def my_func(x, y):
#     return x + y

# One Liner Code Using Lambda Function
# my_lambda = lambda a, b: a + b
# print(my_lambda(1,2))


total = 0

def func(arg1, arg2):
    total = arg1 + arg2
    print(f"Inside the Function Local Total {total}")
    return total

func(10, 20)
print(f"Outside the Function Global Total {total}")



# def my_func(**kwargs):
#     print(kwargs)

# # my_func("Ali", 20, "Developer")
# my_func(name="Ali", age=20, profession="Developer")


