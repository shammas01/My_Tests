# tuple accessing 

# t1=(1,2,3,4,5)


# li=list(t1)
# li.append(26)
# tu=tuple(li)

# print(type(li))
# print(t1)
# print(li)
# print(tu)



# print(t1+t2)
# result= [x for x in t1 if x%2==0]
# print(result)






# Create a list of your favorite fruits and print the second item.
# Given a list of numbers, find the sum and average of all the elements.
# Remove duplicates from a list without changing the order of elements.
# Reverse a list in-place without using any built-in functions.
# Given a list of strings, create a new list containing only the strings with more than 5 characters.
# Check if a list is empty.

# ........list accecing.........

# input_list=[20,22,33,44,33]



#sum and avarage........
# sum=sum(input_list)
# print(sum)
# avrg= sum/len(input_list)
# print(avrg)

#remove dublucations in list.......
# def remove_dublications(value):
#     seen=set()
#     result=[]
#     for items in value:
#         if items not in seen:
#             seen.add(items)
#             result.append(items)
#     return print(result)
    
# remove_dublications(input_list)

# reverse_print........
# print(input_list[::-1])


# new list morthan 5 characters.........

# string_list=['shammas','uvais','thouseef']
# result2=[]

# result=[x for x in string_list if len(x) > 5] #with list comprehention
# print(result)

# for i in string_list: #with for loop
#         if len(i) > 5:
#             result2.append(i)

# print(result2)


#using python filter function.........


# result1=filter(lambda x: x %2==0, li) #even
# result2=[x for x in li if x%2==1] #odd

# print(list(result1))
# print(result2)


# if li:
#     print('list is not empty')
# else:
#     print('list is empty')



# li=[1,3,4,5,6,67,2]
# fixed=10
# print([fixed + x for x in li])

# nested=[[1,2,3,4],[5,6,7,8]]
# print([sum(row) for row in nested])
# print([sum(col) for col in zip(*nested)])



# print(nested[1][2])

# for i in nested:
#     for j in i:
#         sum=[]
#         if j is not None:
#             sum.append(j)
#         print(sum)

# new_list=[x**2 for x in li] #new list with squred value from existing list
# new=list(map(lambda x: x**2,li)) # with lampda function
# print(new)

# print(new_list)

# result=li[::-1] #reverse
# print(result)

# print(li[1::2]) #print all second element 


# li[1],li[5]=li[5],li[1] #swaping
# print(li)



# list1=[1,2,3,4,5,6,7]

# position_to_remove = int(input("Enter the position to remove: "))

# if 0 <= position_to_remove < len(list1):
#     list1 = list1[:position_to_remove] + list1[position_to_remove + 1:]
#     print("Updated list:", list1)
# else:
#     print("Invalid position. The list was not modified.")




# print(li.index(22))
# print(li[1])

# li.remove(20)
# print(li)

# result=[]
# for x in li:
#         result.append(x+1)
# print(result)


# insert=li.insert(2,8)
# print(li)
# li.remove(8)
# li.append(26)

# l2=[x for x in li if x%2==0]
# print(l2)




#12-10-23............................

x=(1,2,3)
y=x
x=(1,2,3,4,5)
print(x,y)
 
def sorting_number(number):
    number.sort()
    return number

number=[78,545,67,343,2,355,23,55]
print(number)
result=sorting_number(number)
print(number)


x=(1,2,3,4,5,6)
print(x.index(1))



# list_comprehention.......................

x=[[j for j in range(5)] for i in range(5) if i%2==0]

print(x)

# function_argument_accessing....................
def complicated_functio(x,z=10,y=None):
    print(x,y,z)
    pass

complicated_functio(2,6)

#>>>>>>>>>

def complicated_function(x,y, *args):
    print(x,y,args)
    pass


complicated_function(1,2,34,4,556,6,67,76,6,6)