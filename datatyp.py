t1=(1,2,3,4,5)
t2=(4,5,6,7,8)
print(t1)

print(t1+t2)
result= [x for x in t1 if x%2==0]
print(result)






# Create a list of your favorite fruits and print the second item.
# Given a list of numbers, find the sum and average of all the elements.
# Remove duplicates from a list without changing the order of elements.
# Reverse a list in-place without using any built-in functions.
# Given a list of strings, create a new list containing only the strings with more than 5 characters.
# Check if a list is empty.

li=[20,22,33,44]
list()
result=[]
for x in li:
    result.append(x+10)
print(result)



insert=li.insert(2,8)
print(li)
li.remove(8)
li.append(26)

l2=[x for x in li if x%2==0]
print(l2)
