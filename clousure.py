
def outer(a):
    def inner(b=1):
        nonlocal a
        a += b
        print(a)
    return inner

inner = outer(5)
inner(8)



