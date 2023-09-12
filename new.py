# x = input('enter a number')
# y = print(str(x))

# if y % 1:
#     print("this os odd")
# print("this is even number")

# x = {
#     1:{'kannur':"district"},
#     2:{"idukki":"district"},
#     3:{"goa":"state"}
#     }


# for y in x:

#     print(y)


# def a(request,x,y):
#     z = x + y
#     return z


# def a(*args, **kwargs):
#     b = args
#     c = kwargs
#     x = print(b,c)
#     return x   

# a(1,2,3 ,{"key":"value"})






#1

count =0
a=14
print(a%2)
for i in range(1,a//2+1):
    if a%i == 0:
        count = count+1
if count>2:
    print('not prime')
else:
    print('prime')
    



#2
def print_diamond(n):
    for i in range(1, n + 1, 2):
        spaces = (n - i) // 2
        stars = i
        print(" " * spaces + "*" * stars)

    for i in range(n - 2, 0, -2):
        spaces = (n - i) // 2
        stars = i
        print(" " * spaces + "*" * stars)

size = 7 
print_diamond(size)


#3
def print_butterfly(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        for j in range(1, 2 * (n - i) + 2):
            print(" ", end="")
        for j in range(1, i + 1):
            print("*", end="")
        print()
    
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        for j in range(1, 2 * (n - i) + 2):
            print(" ", end="")
        for j in range(1, i + 1):
            print("*", end="")
        print()


size = 5  
print_butterfly(size)


#4
items = [
    "Kannur - district",
    "Idukki - district",
    "Goa - state",
    "Up - state",
    "Kottayam - district",
    "Assam - state"
]   

for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")


#5
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

class MyClass(MyAbstractClass):
    def my_abstract_method(self):
        print("This is the implementation of the abstract method.")


#6
#dynamic polimorfisom
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
def animal_sound(animal):
    return animal.speak()    

dog = Dog()
cat = Cat()

print(animal_sound(dog))
print(animal_sound(cat))


#7
#clousures
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


closure1 = outer_function(10)
closure2 = outer_function(20)


result1 = closure1(5) 
result2 = closure2(5)  

print(result1)
print(result2)


#8
#febinashe
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

n = 10  

fib_series = fibonacci(n)
print("Fibonacci Series:")
print(fib_series)



#9
#Example for classic and static method
class MyClass:
    class_variable = 10  

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  

    
    def instance_method(self):
        return f"Instance method called with instance_variable = {self.instance_variable}"

    
    @classmethod
    def class_method(cls):
        return f"Class method called with class_variable = {cls.class_variable}"

    
    @staticmethod
    def static_method():
        return "Static method called"


obj = MyClass(5)


print(obj.instance_method())  
print(obj.class_method())     
print(MyClass.static_method()) 


#10
# Example for argument and keywordargument
def example_function(arg1, arg2, kwarg1="default_value", kwarg2=0):
    print("Positional Arguments:")
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")

    print("\nKeyword Arguments:")
    print(f"kwarg1: {kwarg1}")
    print(f"kwarg2: {kwarg2}")


example_function("Value1", "Value2")


example_function(kwarg2=42, kwarg1="CustomValue", arg2="AnotherValue")
