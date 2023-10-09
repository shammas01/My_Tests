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























value = ['shammas','malayalam','shammahs']
empty_list=[]
empty_string=''

for i in value:
    for j in i:
        empty_string = j + empty_string
    if i == empty_string:
        empty_list.append(i)
    empty_string=''
print(empty_list)