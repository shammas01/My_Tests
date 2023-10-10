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
