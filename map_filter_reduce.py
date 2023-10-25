# # Map....
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# # squared_numbers will be [1, 4, 9, 16, 25]


# # Redues....
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# total = reduce(lambda x, y: x + y, numbers)
# # total will be 15
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# # product will be 120




# # Filter...
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# # even_numbers will be [2, 4, 6]

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # with string methods..................

# # Map....
# text = "Hello, World!"
# result = ''.join(map(lambda char: char.upper(), text))
# # result will be "HELLO, WORLD!"

# words = ["hello", "world", "python"]
# capitalized_words = list(map(str.capitalize, words))
# # capitalized_words will be ["Hello", "World", "Python"]


# # Redues....
# from functools import reduce
# text = ["Python","shammas"]
# concatenated = reduce(lambda x, y: x + y, text)
# print(concatenated)
# # concatenated will be "Python"

# # Filter...
# text = "abc123xyz456"
# digits = ''.join(filter(lambda char: char.isdigit(), text))
# # digits will be "123456"

# names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# long_names = list(filter(lambda name: len(name) > 5, names))
# long_names will be ["Charlie", "David"]





# my practice section.......

# l1=[1,2,3,4,5]
# result=list(map(lambda x: x*2,l1))
# print(result)


# from functools import reduce
# result=reduce(lambda x,y: x*y,l1)
# print(result)


# result=list(filter(lambda x: x%2==0,l1))
# print(result)



# string_list=["shammas","yaseen","anuroop"]
# result=list(map(lambda x: x.upper(),string_list))
# print(result)


# from functools import reduce
# result=reduce(lambda x,y:x+y,string_list)
# print(result)

# result=list(filter(lambda x: len(x) > 6,string_list))
# print(result)



# def count_of_string(str):
#     dic={}

#     for i in str:
#         if i in dic:
#             dic[i] += 1
#         else:
#             dic[i] = 1

#     for i,count in dic.items():
        
#         result=print(i,":",count)
#     print(dic)    
#     return result

# count_of_string('shammass')




#....................................................................................................

# lis=[1,2,3,4,5,6,7,8,9,10]

# lis2=[]
# for i in lis:
#     lis2 = [i] + lis2

# print(lis2)


# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         merge_list=list1+list2
#         sort_list=sorted(merge_list)
#         return sort_list


# solution=Solution()
# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

# print(solution.mergeTwoLists(list1,list2))


