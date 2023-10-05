

# 1
# n=5

# for i in range(n):
#     for j in range(i+1):
#         print('* ',end='')
#     print()

# 2 left 
 
# for i in range(n):
#     for j in range(i,n):
#         print('  ',end='')
#     for k in range(i+1):
#         print('* ',end='')
#     print()

# 3 piramid>>>>>>>>>>>>>>>>>>
# for i in range(n):
#     for j in range(i,n):
#         print('  ',end='')
#     for k in range(i+1):
#         print('* ',end='')
#     for p in range(i):
#         print('* ',end='')   
#     print()



#4 reverse piramid>>>>>>>>>>>>>>>>

# for i in range(n):
#     for j in range(i+1):
#         print('  ', end='')
#     for j in range(i,n):
#         print('* ',end='')
#     for j in range(i,n-1):
#         print('* ',end='')
#     print()


#5 Diemond >>>>>>>>>>>>
for i in range(n-1):
    for j in range(i,n):
        print('  ',end='')
    for j in range(i):
        print('* ',end='')
    for j in range(i+1):
        print('* ',end='')
    print()

for i in range(n):
    for j in range(i+1):
        print('  ',end='')
    for j in range(i,n):
        print('* ',end='')
    for j in range(i,n-1):
        print('* ',end='')
    print()


# sand galss>>>>>>>>>>>>>>>>>>>>>

for i in range(n):
    for j in range(i):
        print('  ',end='')
    for j in range(2*(n-i)-1):
        print('* ',end='')   
    print()

for i in range(n-2,-1,-1):
    for j in range(i):
        print('  ',end='')
    for j in range(2*(n-i)-1):
        print('* ',end='')
    print()


for i in range(1,6):
    for j in range(1,6):
        if i==3 or j==3:
            print('0 ',end='')
        else:
            print('1 ',end='')
    print()        


# Butter fly >>>>>>>>>>>>>>>>>>>>>>>>
n=5
for i in range(n-1):
    for j in range(i+1):
        print('* ',end='')
    for j in range(((n-i)*2)-2):
        print('  ',end='')
    for j in range(i+1):
        print('* ',end='')
    print()

for i in range(n):
    for j in range(n-i):
        print('* ',end="")
    for j in range(i*2):
        print('  ',end='')
    for j in range(i,n):
        print('* ',end='')
    print()    



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# find prime or non prime >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# num = int(input('enter a positive number '))

# if num>1:
#     for i in range(2,num):
#         if num % i == 0:
#             print(num,'is a not prime number')
#             break
#     else:
#         print(num,'is a prime number')

# find odd or even >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>       
# num = int(input('enter a positive number '))
# if num>1:
#     if num%2==0:
#         print(num,'is even number')
        
#     else:
#         print(num,'is odd number')
# else:       
#     print('enter Greater than 1')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#print Key value pare in Dic >>>>>>>
# dic = {'X':1,'Y':2}
# for key,value in dic.items():
#     print(f"key:{key}, value:{value}")



#iterator>>>>>>>>>>>>>>>>>>
# a = [1,2,3,4,5,6,76]
# iter_object =iter(a)
# print(next(iter_object))
# print(next(iter_object))

# while True:
#     try:
#         element = next(iter_object)
#         print(element)
#     except StopIteration:
#         break


#generator>>>>>>>>>>>>>>

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fib_sequence = fibonacci()

# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))
# print(next(fib_sequence))




# pakage and module


# print(dir('__module__'))
# import sys
# sys
# print(dir(sys))
# from new import Prime_or_not

# print(dir())


# coprehentions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

fruits = ['apple','bannana','orang','kiwi','cherry','mango']

# new_list = []
# for i in fruits:
#     if 'a' in i:
#         new_list.append(i)

# print(new_list)

# this is comprahentions >>>>>>>>>>>>

new_list=(each_fruit for each_fruit in fruits if 'a' in each_fruit) # its working like generator
print(next(new_list))
print(next(new_list))
print(next(new_list))


new_list=[each_fruit for each_fruit in fruits if 'a' in each_fruit] #its list comprahention
new_list=tuple(each_fruit for each_fruit in fruits if 'a' in each_fruit) #its tuple comprahention
new_list={each_fruit for each_fruit in fruits if 'a' in each_fruit} #set comprehetion
new_list={each_fruit:'5' for each_fruit in fruits if 'a' in each_fruit} # dictionarty comprehetion
print(new_list)

print(next(new_list))
print(next(new_list))


# x = 123123121234

# # for i in str(x):
# #     print(i) 
# # list1 =tuple(int(i) if int(i)%2==0  else 'x' for i in str(x))
# # print(list1)


# v = {'a': 1, 'b': 2}
# x=v['b']
# del v['b']
# v['c']=x
# print(v)

# # Create a new dictionary with the key 'c' and the value associated with 'b'
# new_v = {key if key != 'b' else 'c': value for key, value in v.items()}

# # Print the new dictionary
# print(new_v)

# for key,value in v.items():

#     print(key,value)



# x={letter for letter in 'you are my best friend' if letter in 'mbest'}
# print(x)


# y={x:x*x for x in range(10)}
# print(y)













# Regular Expretion >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"|,\,?,$,^,+,.,*,(),{}"

import re
x = '^Q....P..H$'
z= 'QabchP23H'
y = re.match(x,z)
if y:
    print('successfull')
else:
    print('unsuccessfull')

#>>>>>>>>>>>>>>>>>match()
import re
input = 'you world you are my best friend'
result = re.match(r"[you]",input)
print(result) 

#>>>>>>>>>>>>>>>>search()
import re
input = 'you world you are my best friend'
result = re.search(r"[zi]",input)
print(result) 

#>>>>>>>>>>>>>>>>findall( )
import re

input = 'you world you are my best friend'
result = re.findall(r"[ra]",input)
print(result)


#>>>>>>>>>>>>>>>>>
import re

input = 'you world you are my best friend'
result = re.findall(r"..",input)
print(result)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ^ reprasenting starts with and exact
# $ representing ends with and exact

import re

input = 'your'
result = re.search(r"^y..r$",input)
print(result)


#>>>>>>>>>>>>>>>>>>>(*)
import re
input = 'yooooor'
result = re.search(r"^yo*r$",input)
print(result)


#>>>>>>>>>>>>>>>>>(+)
import re
input = 'yooooor'
result = re.search(r"^yo+r$",input)
print(result)


# #>>>>>>>>>>>>>>>>>(?)
import re
input = 'yasdor'
result = re.search(r"yasdo?r",input)
print(result)

#>>>>>>>>>>>>>>>>({})
import re
input = 'iam mam'
result = re.search(r"m{1,2}",input)
print(result)

#>>>>>>>>>>>>>>>([]{}) for find indiger number
import re
input = 'hi mom iam 262345asdf2345234'
result_one_digit = re.search(r"[0-9]{1,1}",input)
result_tree_digit = re.search(r"[0-9]{1,3}",input)
print(result_one_digit,'\n',result_tree_digit)

# >>>>>>>>>>>>>>>(\A,\b)
import re
# input = 'iam your son'
# result = re.search(r'\Aiam your',input)
# result2 = re.search(r'\byou',input)
# print(result,result2)

print(dir(re))





#serialization in python >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import pickle dumps, loads

# x = open("pickled.txt","wb")
# dic = {"name":"shammas","age":26}
# y = pickle.dump(dic,x)
# if y is None:
#     print("data is dumped u cannot see that")
# x.close()


# j = open("pickled.txt","rb")
# i = pickle.load(j)
# print(i)
# j.close()

# from pickle import dumps,loads
# dic = {"name":"shammas","age":26}
# dictstring=dumps(dic)
# print(dictstring)

# x=loads(dictstring)
# print(x)


#>>>>>>>>>>>>>>>>>>>>>>>>>


# import pickle
# def stordata(): #serialization

#     person1 ={"name":"shammas","age":24}
#     person2 ={"name":"vaishnav","age":23}

#     db ={}
#     db['person1'] = person1
#     db['person2'] = person2

#     dbfiel=open('examplepickle','ab')

#     dumpfiel = pickle.dump(db,dbfiel)
#     dbfiel.close()

#     print(dumpfiel)

# stordata()

# def LoadData():# deserialization
#     dbfile = open('examplepickle','rb')
#     loaded_file = pickle.load(dbfile)
#     for keys in loaded_file:
#         print(keys, '=>',loaded_file[keys])
#     # print(loaded_file)
#     dbfile.close()

# LoadData()    


# partial function>>>>>>>>>>>>>>>>>>>

# from functools import partial

# def power(base, exponent):
#     return base ** exponent

# square = partial(power,exponent=3)

# result = square(11)  

# print(result)  
    
#>>>>>>>>>>>>>>>>>>>>>>

# def sample_partial(a,b): 
#     return a+b

# x = partial(sample_partial,b=10)

# print(x(11,b=18))

# print(sample_partial(3,6))


# closures >>>>>>>>>>>>>>>>>>>>>>>>>>

# def outer(a):
#     a = a
#     def inner():
#         print(a)
#     inner()

# closure('shammas')

#>>>>>>>>>>>>>>>

# def outer(x):
#     x=x
#     def inner():
#         print(x) 
#     return inner

# myfunction=outer('shammas')
# myfunction()





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> decerator

# def outer(x):
    
#     print('outer x')
    
#     def inner():
#         print('inner x')
#         x()
#     return inner


# @outer
# def sample():
#     print('sample x')
    
# sample()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def i():

#     def j():
#         print('this is me j ')
#         print('thank for caling me')

#     print('this is the function i()')
#     print("iam callng function 'j()' now:\n")
#     j()

# i() # its first calling j function
#>>>>>>>>>>>>>>>>>

# def temprature(t):
#     def celsius(x):
#         return 9 * x / 5 + 32
    
#     result = "it is " + str(celsius(t)) + "degrees"
#     return result

# print(temprature(20))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# (1)>>>
# def factorial(n):
#     """
#     calculate the factorial of 'n'
#     n should be intiger and n<=0
#     """
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(4))


# # # #(2) modifide (1)  >>>>>>>

# def factorial(n):
    
#     if type(n) == int and n>=0:
#         if n==0:
#             return 1
#         else:
    
#             return n * factorial(n-1)
            
#     else:
#         return TypeError(" 'n' has to be a intiger and should a positive number")
    
# print(factorial(3))

# #(3) modifide (2)  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def factorial(n):

#     def inner_factorial(n):
            
       
#             if n==0:
#                 return 1
#             else:
        
#                 return n * factorial(n-1)
            
#     if type(n) == int and n>=0:
#           return inner_factorial(n)          
#     else:
#         return TypeError(" 'n' has to be a intiger and should a positive number")

   
# print(factorial(13))

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def factorial(n):

#     def inner_factorial(y):
            
#         def super_inner(n):
#             def very_inner(x):
                    
#                 if x==0:
#                     return 1
#                 else:
            
#                     return x * factorial(x-1)
#             return very_inner(n)
                
#         return super_inner(y)
           

#     if type(n) == int and n>=0:
#         return inner_factorial(int(n))          
#     else:
#         return TypeError(" 'n' has to be a intiger and should a positive number")   

# print(factorial(13))




# #polinomital>>>>>>>>>>>>>>>>>

# def x(a,b,c):
#     def y(n):
#         return a*(n**2)+(b*n)+c
#     return y

# result=x(1,2,3)
# print(result(1))
 