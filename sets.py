
a={"banana","apple","orange","mango"}
b={"kiwi","apple","orange"}

print(a.union(b)) # printing for add 2 set 
print(a.difference(b)) # printing unique elements in 'a' that's not in b
print(a.intersection(b)) # printing same element in 2 sets
print(a.symmetric_difference(b)) # printing uninque elelment in 'a' and 'b'

a.add("shammas")
print('After adding =', a)

a.remove("orange")
print("After removing =", a)

a.pop() #its for randomly removing in set

print(a)