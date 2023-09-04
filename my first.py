# # sep(), end() <><><>><><><><>><><><><><

# print("shammas", "kaleel", "fahad", end=" * ")
# print("age","number","address")


# # user input


# name = input ("ENTER YOUR NAME:")
# print("hi ", name)

# # method-1   ><><><><>>>>><><><><><><><>><

# Num1 = int (input("enter num1"))
# Num2 = input ("enter num2") 
# sum = Num1 + int (Num2)
# print("result is :", sum)


# # #method-2  ><><><><><><><><><><><><><><><

# print("enter two number")
# num1,num2=input(),input()
# print("result :", int(num1)+int(num2))


# # Basic data Type  <><><><><><><>><><><><><

# a = "shammas"
# b=5
# c=1.5
# d=True,False  #this all are basic data type
# e=36j

# print(type(e))


# Arithamatic oparetors ><><><><><><><>><><><>

# (+),(-),(*),(/),(%),(**),(//)

# a=50
# b=3
# result=a**3 
# print(result)


# Assignment Operators <>><>>><><><><>><<><><

# (=),(+=),(-=),(*=),(/=),(%=),(//=),(**=)

# Comparison Operetors ><><><>>><><><><><><><>

# (==),(!=),(>),(<),(>=),(<=)


# string <><><>>><><><><><><><><><><><>

# string words have index value

# (" "), (""" """)

# len(), strip(), lower(), upper(), (+)-> adding
# replace(), (+), format(), split(), capitalize(two strings )

# format()<><><><><><><><>>><><><><><><>

# a="hallo {} world {} {} "
# b="this is 2023"
# c=" my "

# print(a.format(c,b,c))

# ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# collection data type ><><><><><><><><><

# (list), (tuple), (set), (dict)

# # [list] >>>>>> append(), insert(), remove(), clear(), del()

# list1=["apple","banana","orange"]
# list2=[10,20,30,40]

# list1.append("hallo")
# list1.insert(2,"cabage") 
# list1[1]="shmmas"
# list1.remove("shmmas")

# # list1.clear()
# print(len(list1))
# #del list1

# print(list1)

# for x in list2:
#   print(x)

# (Tuple) ><><><> this canot add or delete content 


tuple1={'key':[("apple","banana","orenge",2)],'key2':[("suchin","vaishnav","shammas",2)]}
tuple2=(5,3,6,9,4)
# tuple3=dict((tuple1+tuple2))
print(tuple1)
# print(tuple3)


# Set >>>>>>>>  ()  add, remove, discard, pop, clear, union,

set1={"apple","banana","orange"}

print("banana" in set1)
set1.add("shammas")
set1.update(["ab","bc","cd"])
set1.clear()
print(set1)
print(set1)
for x in set1:
 print(x)


# Dictinory ><><><><><><>

dict1={
    "name" : "shammas",
    "age" : 24,
    "address" : "vavad"
}
print(dict1.values())
dict1["name"]="fiyas"
print(dict1)

for x,y in dict1.items():
    print(x,y)
# ><>>>>><><><><>>>>>>>><><><<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>><<<<<<<<

# if else statement ><><><><><><><>><><<>><


a= int ( input("enter a number"))

if a > 0:
    print("posetive number")
elif a < 0:
    print("negative number")
else:
     print("zero")

# nested if else statement <<<<<>>>>>>

a= int (input("enter a number"))

if a >= 0:
    if a > 0:
        print("posative number")
    else:
        print("zero")
else:
    print("negative number")


# Loop ><><><>><><><><><><>><><><><><><
# while, for in,

a=1 
while a <= 5:
    print(a)
    a+=1

a =["shammas","apple","orenge","banana"]

for x in a:
    print(x)

for x in range(1,10): 
    print(x)        


# Functions >>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<

def a(b,c,d):
    print("hello "+ b + c + d)

a("shammas"," vavad"," koduavally")
a("asda"," aadadf"," adfadf")


num1=int (input("first number"))
num2=int(input("second number"))

def sum(num1,num2,):

    sum=num1+num2
    print(sum)
    return sum

sum(num1,num2)    

# ><><><><>>><><><><><>><><><><><><>.<><><><><><><><><><>


# Recursion >>>>>>>><<<<<<<<


def recursion(num):
    if num == 1 :
        return num
    else:
        return num + recursion(num-1)

print (recursion(3))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

# a={"shammas" :"muhammed",    #>
# "vavad 16 ":"koduvally"}     #>
#                              #> 
# a["city"]= "kozhikode"       #>  dictionary
# a.pop("vavad 16 ")           #>
# for x,y in a.items():        #>
#  print(x,y)                  #>

# >>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<

a=-5
if a>=0:

    if a>0:

        print("posative")
    else:
        print("zero")

else:
    print("negative")            

# <<<<<<>>>>>>>>>>><<<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<>>>>>>>>>

for x in range(10,20):
    print(x,end=",")

# >>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>><<<<<<<<

def shammas(c):

    if c==1:
        return c
    else:
        return c + shammas(c-1)

print(shammas(4))

# >>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<


# Lambda <><><><><><><><><><><><><><><><><><><><><><><><><><><

# b=lambda a: a+a
# print(b(12))

# list1=[45,65,3,25,44,12,26,2,6,11,13]

# def even(y):
#     if y % 2 == 0:
#         return y 
#                          #<<<Noramal function<<<

# v = filter(even,list1) 
# print(list(v)) 


# list2=[45,65,3,25,44,12,26,2,6,11,13]

# z = filter(lambda a:   a % 2 == 1 , list2)     #<<<Lambda function<<


# print(list(z))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OOPS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class Bikes:
    def __init__(self, name ,price, color) -> None:
        self.name = name
        self.price = price
        self.colo = color

    def start(self):
        print(self.name + " engin started")

    def run(self):
        print(self.name + " running") 

    def stop(self):
        print(self.name + " stoped")        


bike1= Bikes(" glamor",52655,"red")
bike2= Bikes(" splender",265484,"green")
bike1.price="150000"
bike2.colo="blue"
# del bike1.price

print(bike1.name,  bike1.colo, bike1.price,end="  #")
print(bike2.name, bike2.colo, bike2.price)


bike1.start()
bike1.run()
bike1.stop()

bike2.start()
bike2.run()
bike2.stop()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Inheritence 


# < parent class >
class Person:
    def __init__(self,name,contact) -> None:
        self.name = name
        self.contact = contact

    def   address(self):
        print(self.name , self.contact)  

# # < Child class >

class Doctor(Person):
    pass

class Employee(Person):
    pass

class Patiant(Person):
    pass

doc1= Doctor("shammas",62827269)
doc2=Doctor("fiyas",5236569812)

emp1=Employee("kuru",51684654)
emp2=Employee("kannamma",65484)

pati1=Patiant("ajnas",354435)
pati2=Patiant("kuppi",35115684)


doc1.address()
emp2.address()
pati1.address()

# >>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<


# Math function

a= min(26,226,565,56,32,596,23,5)
print(a)

b=pow(2,4)
print(b)

import math

c= math.pi
print(c)

d= math.sqrt(100)
print(d)

e= math.gcd(10,14)
print(e)

# import mymodule
# mymodule.messege("shammas")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# input function

num1=float( input("enter first number"))
num2=float( input("enter second number"))
sum=num1+num2
print(sum)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# File handling

a= open("smaple.txt", "a")
a.write("learn c++ programming\n")
a.close()

print("shammas")

def a(f):
   b =f**f
   print((b))



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<
fruits = frozenset(["apple", "banana", "orange"])

print(type(fruits))

print("pear" in fruits)
print("apple" in fruits)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<

import random

print(random.randrange(1000,9999))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# genarator <><><><><><

def a():
    yield "hallo"
    yield "abc"
    yield "shmmas"
b=a()
print(next(b))
print(next(b))
print(next(b))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# arbitery keyword argument <><><>><><>><>

def a(**y):
    for key, value in y.items():
        print(f"{key} = {value}")


a(name="shammmas",age=26,place="vavad")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# functions (decorator)


# Iterator <<>><>><><><><<>><

class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

#  Using the iterator
my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for value in my_iterator:
    print(value)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#   >>>>>OOPS<<<<<<


class Bike:

    def __init__(self,name,dob):
        self.name=name
        self.dob=dob


    def start(self):
        print("started")

    def print_details(self):
        print("bike name is {} and year is {}".format(self.name, self.dob)) #calling calss Argument with format()

a= Bike("glamor",2021)  #creting object and passing class method and proporties
b= Bike("pulsor",2018)

print(a.dob)
print(a.name)
a.start()
a.print_details()
b.print_details()

# <><><><><>>><><><><>><><><><><><><><><

# class Account:
#     def __init__(self, account_number, account_balance):
#         self.text = None
#         self.account_number = account_number
#         self.account_balance = account_balance

#     def withdraw(self, amount):
#         if self.account_balance - amount > 0:
#             self.account_balance = self.account_balance - amount
#         else:
#             print("withdrawel falied")

#     def deposit(self, amount):
#         self.account_balance = self.account_balance + amount

#     def display(self):
#         print("account balance is {}".format(self.account_balance))


# account_one = Account("shammas", 10000)
# account_two = Account("fiyas", 5000)

# amount = int(input("enter withdraw amount"))
# account_one.withdraw(amount)
# account_one.display()

# Damount = int(input("enter deposit amount"))
# account_one.deposit(Damount)
# account_one.display()


# >>>>>>>>>>>>>>>>>>>>>>>>><><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>

# >>>>>>>>>> EXEPTION HANDLING <<<<<<<<<<<<<

# x = int(input("enter first number"))
# y = int(input("enter second number"))

# try:
#     z = x / y



# except:
#     z = x

# else:
#     print("no exception")
# finally:
#     print("final block")
#     print(z)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>> abstraction <<<<<<<
# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# r = Rectangle(5, 10)
# print(r.area())  # prints 50
# print(r.perimeter())  # prints 30

# l = []

# for i in range(5):
#     x = int(input("enter a number"))
#     l.append(x)

# print(sum(l))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# SUM OF MULTIPLE NUMBER IN A FUNCTION

# def a(n, *y):
#     sumu = 0
#     for x in y:
#         sumu = sumu + x

#     return sumu + n


# print(a(100, 50, 59, 41))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ITERETOR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# EG - 1

# mySecret = ["I", "Love", "Python"]

# myIter = iter(mySecret)
# print(myIter)

# print(next(myIter))
# print(next(myIter))
# print(next(myIter))

# eg - 2

# a=[2,6,7,8,5]

# b=iter(a)

# print(next(b))
# print(next(b))
# print(next(b))

# class person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sing(self):
#         print(self.name, "sing a song")


# person1 = person("shammas ", 24)
# person2 = person("vaishnav", 22)
# person3 = person("fahad",23)

# person1.sing()
# person2.sing()
# person3.sing()

# print(person1.name + str(person1.age))
# print(person2.name + str(person2.age))


# >>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<

# WHILE LOOP USING WITH PYTHON

# def add(*x):
#     sum = 0
#     for i in x:
#         sum = sum + i
#         yield sum


# a = add(10, 20, 40, 60)
# while True:
#     try:
#      r = next(a)
#      print(r)
#     except StopIteration:
#         print("Fahad Loves________")
#         break





# WILE LOOP

# x = 0

# while True:
#     if x <= 5:
#         print(x)
#         x = x + 1
# else:
#     print("thank you")





# lista = "abcd"
# Listb = [1,2,3,4]

# # answer = {A:10,B:20,C:30,D:40}

# # def sample(Lista):
# #     return Lista.upper()


# def uppercase_decorator(func):
#     def wrapper(lista):
#         return func(lista.upper())
#     return wrapper

# @uppercase_decorator
# def greeting(lista):
#     return lista

# print(greeting(lista))  # Output: Hello WORLD!


























#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> practice (27-04-2023) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# return statment<<<<<<<<<<<<<<<<<<<<<<<<<

# def multiply_numbers(num1, num2):
#     product = num1 * num2
#     return product
    
# result = multiply_numbers(3, 4)
# print(result)

# global variable and local variable<<<<<<<<<<<<<<<
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print("The sum is:", sum)
    
# num1 = 5
# num2 = 7

# add_numbers(10, 20)
# print("num1 + num2 =", num1 + num2)

# defult argument<<<<<<<<<<<<<<<<<<<<<<
# def greet(name, greeting="Hello"):
#     print(greeting + ", " + name + "!")
    
# greet("John")
# greet("Shammas", "Hi")

# anonymus finction>>>>>>>>>>>>>>>>>>>>>
# double = lambda x: x * 2
# result = double(3)
# print(result)


# decoretor <<<<<<<<<<<<<<<<<<<<<<<<<
# def square(func):
#     def wrapper(x,y,z):
#         result = func(x,y,z)
#         return result ** 3
    
#     return wrapper

# @square
# def add_numbers(num1, num2,num3):
#     return num1 + num2 + num3

# result = add_numbers(1, 2,3)
# print(result)

# recursion>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(3))

# function overloading>>>>>>>>>>>>>>>>>>>>>
# def add(x, y, z=None):
#     if z:
#         return x + y + z
#     else:
#         return x + y

# print(add(2, 3))         
# print(add(2, 3, 4))      
# ,,,,,,,,,,,,,,,,,,,,,,
# def add(*args):
#     if len(args) == 2:
#         return args[0] + args[1]
#     elif len(args) == 3:
#         return args[0] + args[1] + args[2]

# print(add(2, 3))         
# print(add(2, 3, 4))      

# iterator and generator>>>>>>>>>>>>>>>>>>>>>
# numbers = [1, 2, 3, 4, 5]
# it = iter(numbers)

# print(next(it)) # prints 1
# print(next(it)) # prints 2
# print(next(it)) # prints 3
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# def squares(n):
#     for i in range(n):
#         yield i ** 3
# s = squares(4)

# print(next(s)) # prints 0
# print(next(s)) # prints 1
# print(next(s)) # prints 4
# print(next(s))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# API(exampls)

# import os

# # Create a new directory
# os.mkdir('new_directory')

# # Get the current working directory
# current_dir = os.getcwd()

# # Check if a file exists
# file_exists = os.path.exists('file.txt')

# monkey paching>>>>>>>>>>>>>>>>>>>>>>
# Define a function that we want to monkey patch
# def original_function():
#     return "muhammed hjvkhj"

# # Define a new function that we want to replace the original with
# def new_function():
#     return "thauseefn hybkjhb"

# # Replace the original function with the new one

# new_function = original_function

# # Now when we call the original function, we get the new behavior
# print(original_function())  # Output: "Goodbye, world!"

# for num in range(10):
#     if num < 5:
#         continue
#     elif num > 8:
#         break
#     print(num,end='')


