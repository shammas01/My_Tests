text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # Output: ["apple", "banana", "cherry"]


fruits = ["apple", "banana", "cherry"]
text = ",".join(fruits)
print(text)  # Output: "apple,banana,cherry"


text = "Hello, World!"
replaced = text.replace("World", "Python")
print(replaced)  # Output: "Hello, Python!"


text = "Hello, World!"
starts_with_hello = text.startswith("Hello")
ends_with_exclamation = text.endswith("!")
print(starts_with_hello)    # Output: True
print(ends_with_exclamation)  # Output: True


alpha_check = "Hello"
digit_check = "123"
alpha_numeric_check = "hallo123"
print(alpha_check.isalpha())           # Output: True
print(digit_check.isdigit())           # Output: True
print(alpha_numeric_check.isalnum())   # Output: True



text = "hello world"
capitalized = text.capitalize()
title_case = text.title()
print(capitalized)  # Output: "Hello world"
print(title_case)   # Output: "Hello World"


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# map_functoin........

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)

squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)


#reduce_function......

from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]

product = reduce(multiply, numbers)

print(product)