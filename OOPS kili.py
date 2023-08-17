# > scop concept <

# def Check_scope():
#     def do_local():
#         test = "local test"
#
#     def do_non_local():
#         nonlocal test
#         test = "non local test"
#
#     def do_global():
#         global test
#         test = "global test"
#
#     test = "default"
#     print("test value after do local :" + test)
#
#     do_non_local()
#     print("test value after non do local :" + test)
#
#     do_global()
#     print("test value after global :"+test)
#
#
#
# Check_scope()
# print("test value after main :"+test)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<
# class and object

# class MySampleClass:
#     def hello(self, nm):
#         self.name = nm
#
#     def print(self):
#         print("hallo "+self.name)
#
#
# x = MySampleClass()
# x.hello("shammas")
# x.print()
#
# y = MySampleClass()
# y.hello("fiyas")
# y.print()

#><>><><><><><>>>><><><><><><>>><><><><>

# class and function with costrector

# class Sample:
#     def __init__(self, name, age, place):
#         self.name = name
#         self.age = age
#         self.place = place

#     def add_age(self):
#         self.age = self.age+1

#     def relocate(self,place):

#         self.place = place



# a = Sample("shammas", 24, "vavad")
# b = Sample("fiyas", 23, "parappen poyil")

# a.add_age()
# b.add_age()
