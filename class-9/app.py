# Create Dictionary 

persons: dict = {
    "name": "Ali",
    "age": 25,
    "city": "Karachi"
}

# print(persons["cnic"])

# print(persons["age"])

# print(persons.get("age"))

# print(persons.get("cnic", "CNIC IS Not Found"))



####----------------- SETS -------------------###




# Create a Set

set1: set = {1, 2, 3, 4, 5, 6}

# print(set1)

# try:
#     set1[0] = 7

# except TypeError as e:
#     print(e)

# set1.remove(1)
# set1.remove(7)

# print(set1)

# remove_items = set1.discard(7)

# print(remove_items)



# my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
# print("Before: my_set = ", my_set)
# my_set.difference_update({1, 5, 3, 'A'})
# print("After:  my_set = ", my_set)


# print("Before: ", my_set)
# Add multiple items
# my_set.update([7, 8, 9, "Hello"])
# print(my_set)  # Output: {4, 5, 6, 7, 8, 9}


# my_set: set   = {1, 2, 3, 5}
# my_set_2: set = {1, 5, 6, 7}

# my_set3: set  = my_set.union(my_set_2)
# print(my_set3)


# my_set: set   = {1, 2, 3, 5}
# my_set_2: set = {1, 5, 6, 7}

# my_set3: set  = my_set | my_set_2 # | operator
# print(my_set3)


# my_set: set = {1,2,3,4,5, "Hello! World"}
# print("Before : ", my_set)

# my_set.add(2)
# my_set.add("Hello! World")

# print("After  : ", my_set)



# Lets create an error to understand
my_set: set = {1,2,3}

# my_set.remove(4)
# print(my_set)



print("Before pop() = ", my_set)

#When you call `my_set.pop()`, it removes and returns an arbitrary element from the set.
#Since sets are unordered data structures, the element that is removed and returned is not predictable.
my_set.pop()
print("Before pop() = ", my_set)