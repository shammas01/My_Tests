
# def decorator(main):

#     def inner(*args):
#         result = 1
#         for i in args:
#             result *= i
#         print(result)

#         return main(*args)
    
#     return inner

# @decorator
# def shammas(*args):
#     c=sum(args)
#     return c

# print(shammas(1,2,3,4))



#.............................................
# def dec(main):

#     def inner(n):
#         print(n.upper())
#         return main(n)
    
#     return inner

# # @dec
# def first_fun(str):
#     return str

# # this is actually working here.
# result=dec(first_fun)
# print(result('shammas'))



#...................................
# from aiohttp_retry import List


# def longestCommonPrefix(strs: List[str]) -> str:
#         if not strs:
#             return ""
            
#         strs.sort()

#         first_str = strs[0]
#         last_str = strs[-1]

#         common_prefix = ""
#         min_len = min(len(first_str), len(last_str))

#         for i in range(min_len):
#             if first_str[i] == last_str[i]:
#                 common_prefix += first_str[i]
#             else:
#                 break

#         return common_prefix


# print(longestCommonPrefix(['shammas','shaminl','shais']))







