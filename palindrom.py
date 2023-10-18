# a = ['yaseen','malayalam','shammas','aaaaa','shammahs']
# l=[]
# b=''
# for i in a:
#     for j in i:
#         b = j + b     
#     if i == b:
#         l.append(i)
#     b = ''

# print(l)







# palindrom=[x for x in value if x == x[::-1]] #palindrom in listcomprehentioin
# print(palindrom)


# value = ['shammas','malayalam','shammahs']

# empty_list=[]
# empty_string=''


# for i in value:
#     for j in i:
#         empty_string = j + empty_string
#     if i == empty_string:
#         empty_list.append(i)
#     empty_string=''
# print(empty_list)


# a=["shammas","muhammed","malayalam"]

# empty_list=[]
# empty_string=''

# for i in a:
#     for j in i:
#         empty_string = j + empty_string
#     if empty_string == i:
#         empty_list.append(i)
#     empty_string=''

# print(empty_list)





# gap=li[0]-li[1]

# for i in range(1,len(li)-1):
#     if li[i+1] - li[i] != gap:
#         print("false")
#         break
#     else:
#         print("true")


    
# li.sort()
# # print(li[1])
# l1=[]
# for i in li:
#     if i not in l1:
#         l1.append(i)

# print(l1[1])


#........................
def palindrom(n):
    
    tr1=''

    for i in n:
        tr1 = i +tr1
    
    return n == tr1 

print(palindrom('malayalam'))