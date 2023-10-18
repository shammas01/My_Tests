# practice with while loop

# count = 0
# while count < 5:
#     print("Count is", count)
#     count += 1


# numbers = [10,4,3,7,8,3]
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1


# Lists:

# Use Case: Lists are ordered collections of items. 
# They are used to store a collection of items, 
# which can be of different data types, and you can access, modify, or iterate through the elements.
# Operations:
# Creating a list: my_list = [1, 2, 3]
# Accessing elements: first_element = my_list[0]
# Modifying elements: my_list[1] = 42
# Adding elements: my_list.append(4)
# Removing elements: my_list.remove(3)
# Iterating through the list: for item in my_list:

# Tuples:...............

# Use Case: Tuples are similar to lists but are immutable, 
# meaning you can't change their contents after creation. 
# They are often used for fixed collections of items.
# Operations:
# Creating a tuple: my_tuple = (1, 2, 3)
# Accessing elements: first_element = my_tuple[0]
# Iterating through the tuple: for item in my_tuple:

# Sets:.................

# Use Case: Sets are unordered collections of unique elements. 
# They are useful for storing a collection of distinct items and performing set operations like union, intersection, and difference.
# Operations:
# Creating a set: my_set = {1, 2, 3}
# Adding elements: my_set.add(4)
# Removing elements: my_set.remove(3)
# Set operations: union, intersection, difference, etc.

# Dictionaries:.........

# Use Case: Dictionaries are collections of key-value pairs. 
# They are used for associating data with unique keys, 
# making it efficient to retrieve values based on keys.
# Operations:
# Creating a dictionary: my_dict = {"name": "John", "age": 30}
# Accessing values: name = my_dict["name"]
# Modifying values: my_dict["age"] = 31
# Adding key-value pairs: my_dict["city"] = "New York"
# Iterating through keys or values: for key in my_dict: or for value in my_dict.values():


# cluosor....
def outer(decora):

    def inner(a,b):
        print("inner func")
        return decora(a,b)
    
    return inner

# result=outer(10,20)
# result()

# decorator.....

@outer
def decora(a,b):
    c=a+b
    return f"hallow world {c}"

deco = outer(decora)
print(deco(12,23))



