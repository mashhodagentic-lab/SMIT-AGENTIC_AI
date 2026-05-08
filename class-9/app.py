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



####----------------- SETS -------------------####

my_set: set = {123, 452, 5, 6}
my_set2: set = set([123, 452, 5, 6])  # List Convert to Set 
unknown: set = {} # set or dectionary
empty_set: set = set()

# print("my_set            = ", my_set)
# print("my_set2           = ", my_set2)
# print("type(my_set)      = ", type(my_set))
# print("type(my_set2)     = ", type(my_set2))
# print("type(unknown)     = ", type(unknown))
# print("type(empty_set)   = ", type(empty_set))
# print("my_set == my_set2 = ", my_set == my_set2)
# check id
# print("my_set == my_set2 = ", my_set is my_set2)


# my_set = {[123, 452, 5, 6]} # TypeError: unhashable type: 'list'
# print(my_set)


# multi_type_set: set = {7, 9.0, False, True, "Hello! World", (1,5,9,'hi') }
# print(multi_type_set)


# set2: set = {'Java', 'Python', 'JavaScript', 'java'}
# print(set2)

set1: set = {1, 2, 3, 4, 5, 'A', 'a'}

# print(set1)

# try:
#     set1[0] = 7

# except TypeError as e:
#     print(e)

# set1.remove(1)
# set1.remove('a')

# Error
# set1.remove(7)

# print(set1)

set1.add(6)
# print(set1)


# my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
# print("my_set = ", my_set)

# discard() only removes a single element.
# print(my_set.discard({1,2,3}))

# print("After: my_set = ", my_set) # return None


# To remove multiple elements, iterate and discard each one individually:
# for item in {1, 2, 3}:
#     my_set.discard(item)

# print("After removing multiple elements: my_set = ", my_set)

# None
# remove_items = set1.discard(7)

# print(remove_items)



# my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
# print("Before: my_set = ", my_set)
# my_set.difference_update({1, 5, 3, 'A'})
# print("After:  my_set = ", my_set)


# print("Before: ", my_set)
# # Add multiple items
# my_set.update([7, 8, 9, "Hello"])
# print(my_set)  # Output: {4, 5, 6, 7, 8, 9}

# my_set.update([10, 2, 3, "a"])
# print(my_set)  


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


# print("Before pop() = ", my_set)

#When you call `my_set.pop()`, it removes and returns an arbitrary element from the set.
#Since sets are unordered data structures, the element that is removed and returned is not predictable.
my_set.pop()
# print("Before pop() = ", my_set)


# my_set = {1,2,3}

# my_set.discard(4) # method
# print(my_set)


# a: str = "Hello! World"
# b: str = "Hello! World"

# print("id(a) = ", id(a))
# print("id(b) = ", id(b))

# print("hash(a) = ", hash(a))
# print("hash(b) = ", hash(b))
# print("-----------")
# print("hash(a)      = ",hash(a))
# print("a.__hash__() = ", a.__hash__()) # __dunder__()


# TypeError: unhashable type: 'set'
# my_set: set   = {1,2,3,4,5, "Hello! World"}
# my_dict: dict = {my_set: "Hello! World"} # dictionary only accept immutable objects as a key
# print(my_dict)


# my_frozenset: frozenset = frozenset([1,2,3, "Hello! World"])
# print("my_frozenset  = ", my_frozenset)

# my_set: set = {1,2,3, "Hello! World"}
# my_frozenset2: frozenset = frozenset(my_set)
# print("my_frozenset2 = ",my_frozenset2)



####------------ SET METHODS -------------####


# my_set:  set = {1,2,3, "Hello! World", 4,5,6}
# my_set2: set = {1,2,3, "Hello! World", 8,9}
# my_set3: set = {1,2,3, "Hello! World", 77}


# print("difference()           = ", my_set.difference(my_set2, my_set3)) #Returns a set containing the difference between two or more sets
# print("intersection()         = ", my_set.intersection(my_set2, my_set3)) #Return a set that contains the items that exist in both set
# print("union()                = ", my_set.union(my_set2, my_set3)) #Return a set that contains all items from both sets, duplicates are excluded
# print("symmetric_difference() = ", my_set.symmetric_difference(my_set2)) #One argument only, #Return a set that contains only unique items from both sets

# #my_set = {55,66}

# print("isdisjoint()           = ", my_set.isdisjoint(my_set2))#Return True if no items in set x is present in set y

# my_set2 = {1,2,3, "Hello! World"}
# print("issuperset()           = ", my_set.issuperset(my_set2))#Return True if all items in set x are present in set y
# print("issubset()             = ", my_set2.issubset(my_set))



# Initialize two sets for demonstration
set1: set = {1, 2, 3, 4, 5}
set2: set = {4, 5, 6, 7, 8}

# 1. add(): Adds an element to the set.
set1.add(6)
print(f"add(6): {set1}")  # Output: {1, 2, 3, 4, 5, 6}

# 2. clear(): Removes all elements from the set.
set_copy: set = set1.copy()
set_copy.clear()
print(f"clear(): {set_copy}")  # Output: set()


# 3. copy(): Returns a copy of the set.
set_copy: set = set1.copy()
print(f"copy(): {set_copy}")  # Output: {1, 2, 3, 4, 5, 6}

# 4. difference(): Returns a set containing the difference between two or more sets.
difference_set: set = set1.difference(set2)
print(f"difference(): {difference_set}")  # Output: {1, 2, 3}

# 5. difference_update(): Removes the items in this set that are also included in another, specified set.
set1.difference_update(set2)
print(f"difference_update(): {set1}")  # Output: {1, 2, 3}
set1: set = {1, 2, 3, 4, 5,6} #reset set1

# 6. discard(): Remove the specified item.
set1.discard(6)
print(f"discard(6): {set1}")  # Output: {1, 2, 3, 4, 5}

# 7. intersection(): Returns a set, that is the intersection of two other sets.
intersection_set: set = set1.intersection(set2)
print(f"intersection(): {intersection_set}")  # Output: {4, 5}

# 8. intersection_update(): Removes the items in this set that are not present in other, specified set(s)
set1.intersection_update(set2)
print(f"intersection_update(): {set1}") # Output: {4, 5}
set1 = {1, 2, 3, 4, 5,6} #reset set1

# 9. isdisjoint(): Returns whether two sets have a intersection or not.
print(f"isdisjoint(): {set1.isdisjoint(set2)}")  # Output: False
print(f"isdisjoint(): {set1.isdisjoint({9,10})}") # Output: True

# 10. issubset(): Returns whether another set contains this set or not.
print(f"issubset(): {set1.issubset(set2)}")  # Output: False
print(f"issubset(): {{1,2}}.issubset({set1})")  # Output: True
print(f"issubset(): {{1,2}}.issubset({{1,2}})")  # Output: True


# 11. issuperset(): Returns whether this set contains another set or not.
print(f"issuperset(): {set1.issuperset(set2)}")  # Output: False
print(f"issuperset(): {set1.issuperset({1,2})}")  # Output: True
print(f"issuperset(): {{1,2}}.issuperset({{1,2}})")  # Output: True

# 12. pop(): Removes a random element from the set.
removed_element: int = set1.pop()
print(f"pop(): {removed_element}")  # Output: (random element)
print(f"set after pop(): {set1}")  # Output: (set without removed_element)
set1.add(removed_element)#put back the element for others test

# 13. remove(): Removes the specified element. Raises an error if the element is not present.
set1.remove(1)
print(f"remove(1): {set1}")  # Output: {2, 3, 4, 5,6}
set1.add(1)#put back the element for others test

# 14. symmetric_difference(): Returns a set with the symmetric differences of two sets.
symmetric_difference_set: set = set1.symmetric_difference(set2)
print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: {1, 2, 3, 7, 8}

# 15. symmetric_difference_update(): Inserts the symmetric differences from this set and another
set1.symmetric_difference_update(set2)
print(f"symmetric_difference_update(): {set1}")  # Output: {1, 2, 3, 7, 8}
set1 = {1, 2, 3, 4, 5,6} #reset set1

# 16. union(): Returns a set containing the union of sets.
union_set = set1.union(set2)
print(f"union(): {union_set}")  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# 17. update(): Update the set with the union of this set and others
set1.update(set2)
print(f"update(): {set1}") # Output: {1, 2, 3, 4, 5, 6, 7, 8}
