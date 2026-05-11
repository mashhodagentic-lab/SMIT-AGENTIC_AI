# import calc.arthmetic


# Static Function

# def greeting(name):
#     print(f"Hello{name}")

# greeting()
# greeting()
# greeting()

# Dynamic Function

# def greeting(name):
#     print(f"Hello {name}")

# guests = ["Alice", "John", "Eve"]

# for guest in guests:
#     greeting(guest)



# def greeting(name = "Guest", age = 0, profession ="Unknown"):
#     print(f"Hello, {name}! You are {age} Years Old Work as a {profession}")

#! Positional Arguments
# greeting("Ali", "25", 'VE')

#! Keyword Argumkents
# greeting(name="Alice", age=25, profession="VE")
# greeting(age=25, profession="VE", name="Alice")


# greeting("Alice", 30, "Designer")
# greeting("Ali", 30, "Hr")
# greeting("Fahad", 30, "Software Developer")
# greeting("Ahsan", 30, "Manager")
# greeting("Hammad", 30, "VE")


# def modify_value(x):  # Pass By Value
#     x = 10
#     print("Within function:", x)

# # Immutable object (integer)
# x = 5
# print("Original:", x)
# modify_value(x)
# print("After function:", x)



# def modify_value(last):  # Pass By Reference
#     last.append(10) 
#     print("Within function:", last)

# # Mutable object (integer)
# my_list = [1, 2, 3]
# print("Original:", my_list)
# modify_value(my_list)
# print("After function:", my_list)


# def greet():
#     name = "Ali"
#     print((f"Hello, {name}!"))

#     return name

# greet()



# def add(x: int,y: int=0) -> float:
#    return float(x + y)

# print(float(add(10,20)))

# print(add(y=50.0, x=2.0)) # type hints are not enforced in Python

# print(add(x=5))


# def multipl_fuction(a, b, c, d, e, f, g, h, i, j):
#     return a * b * c * d * e * f * g * h * i * j

# print(multipl_fuction(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Unpacking Iterable

# def multipl_fuction(a, b, *args):
#     print("First Two Numbers:", a, b)
#     print("Type:", type(args))
#     # return "Received Numbers:", args

#     sum = a + b
#     for num in args:

#         return sum

# print(multipl_fuction(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(multipl_fuction(1, 2, 3, 4, 5))
# print(multipl_fuction(1, 2, 3, 4, 5, 6, 7, 8))



# def my_sum(*nums):
#   print(type(nums),", ", nums)

#   return sum(nums)

# print("Sum     = ", my_sum(1,2,3,4,5,8,5),"\n")
# print("Sum *[] = ", my_sum(*[1,2,3,4,5,8,5]), "\n") # *  unpacking list
# print("Sum *() = ", my_sum(*(1,2,3,4,5,8,5))) 


# This code raise a error
# def my_sum(a, b , *nums):
#   print(type(nums),", ", nums)
#   print("a:", a)
#   print("b:", b)
#   print("nums:", nums)
#   return sum(nums)

# print("Sum *[] = ", my_sum([1,2,3,4,5,8,5]), "\n") # *  unpacking list
# print("Sum *() = ", my_sum((1,2,3,4,5,8,5))) # *  unpacking tuple




# def my_sum(a, b , *nums):
#   print(type(nums),", ", nums)
#   print("a:", a)
#   print("b:", b)
#   print("nums:", nums)
#   return sum(nums)

# print("Sum     = ", my_sum(1,2,3,4,5,8,5),"\n")
# print("Sum *[] = ", my_sum(*[1,2,3,4,5,8,5]), "\n") # *  unpacking list
# print("Sum *() = ", my_sum(*(1,2,3,4,5,8,5))) # *  unpacking tuple
