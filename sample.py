

#1
# n=5

# for i in range(n):
#     for j in range(i+1):
#         print('* ',end='')
#     print()

#2 left 
 
# for i in range(n):
#     for j in range(i,n):
#         print('  ',end='')
#     for k in range(i+1):
#         print('* ',end='')
#     print()

#3 piramid>>>>>>>>>>>>>>>>>>
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


# Diemond 
# for i in range(n-1):
#     for j in range(i,n):
#         print('  ',end='')
#     for j in range(i):
#         print('* ',end='')
#     for j in range(i+1):
#         print('* ',end='')
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print('  ',end='')
#     for j in range(i,n):
#         print('* ',end='')
#     for j in range(i,n-1):
#         print('* ',end='')
#     print()


# sand galss>>>>>>>>>>>>>>>>>>>>>
# for i in range(n):
#     for j in range(i):
#         print('  ',end='')
#     for j in range(2*(n-i)-1):
#         print('* ',end='')   
#     print()

# for i in range(n-2,-1,-1):
#     for j in range(i):
#         print('  ',end='')
#     for j in range(2*(n-i)-1):
#         print('* ',end='')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i==3 or j==3:
#             print('0 ',end='')
#         else:
#             print('1 ',end='')
#     print()        


# Butter fly >>>>>>>>>>>>>>>>>>>>>>>>

# for i in range(n-1):
#     for j in range(i+1):
#         print('* ',end='')
#     for j in range(((n-i)*2)-2):
#         print('  ',end='')
#     for j in range(i+1):
#         print('* ',end='')
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print('* ',end="")
#     for j in range(i*2):
#         print('  ',end='')
#     for j in range(i,n):
#         print('* ',end='')
#     print()    



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# find prime or non prime>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# num = int(input('enter a positive number '))

# if num>1:
#     for i in range(2,num):
#         if num % i == 0:
#             print(num,'is a not prime number')
#             break
#     else:
#         print(num,'is a prime number')

# find odd or even >>>>>>>>>>        
num = int(input('enter a positive number '))
if num>1:
    if num%2==0:
        print(num,'is even number')
        
    else:
        print(num,'is odd number')
else:       
    print('enter Greater than 1')

         