li=[2,4,6,8,10]

def gaps(n):
    if len(n)<3:
        return True
    
    gap=n[1] - n[0]

    for i in range(1,len(n)-1):
        if n[i+1]-n[i] != gap:
            return False
    return True

print(gaps(li))



# finding a element that having user input.............
# lis1=["appel ","orange","bannana","kiwi",'1','1']
# lis2=[]
# inp=input("enter a character: ")
# for i  in lis1:
#     if inp in i:
#         lis2.append(i)

# if lis2:
#     print(lis2)
# else:
#     print(f'nothing with "{inp}" this input')


#printing commen element

# l1=[1,2,3,4,5]
# l2=[4,3,7,8,0]

# l3=[]

# for i in l1:
#     for j in l2:
#         if i == j:
#             l3.append(i)        

# print(l3)



# lis1=[1,2,3,4,5]

# def gaps(num):
#     if len(num)<3:
#         return True
    
#     gap=num[1]-num[0]

#     for i in range(1,len(num)-1):
#         if num[i+1] - num[i] != gap:
#             return False
#     return True

# print(gaps(lis1))


# n=int(input("enter your number"))
# new=[x for x in range(1,n+1)]
# print(new)




# def fibno(n):
#     new=[]
#     a,b=0,1
#     for i in range(n):
#         new.append(a)
#         a,b=b,a+b
#     return print(new)
# fibno(10)


# def fibnochi(n):
#     sequence=[0,1]
#     while len(sequence) < n :
#         result=sequence[-1] + sequence[-2]
#         sequence.append(result)
#     return print(sequence)

# fibnochi(5)