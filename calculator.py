
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "cant divide with zero"
    return x/y

while True:
    print("enter 'ADD' for addition")
    print("enter 'SUB' for addition")
    print("enter 'MULT' for addition")
    print("enter 'DIV' for addition")
    print("enter 'Q' to stop calulator")

    
    user_input = input(": ")
    if user_input == "Q":
        break

    elif user_input in ("ADD","SUB","MULT","DIV"):
        first_number= float(input('enter your first number:'))
        seceond_number=float(input('enter your seceond number:'))

        if user_input == "ADD":
            print("result: " + str(add(first_number,seceond_number)))
        elif user_input == "SUB":
            print("result: "+ str(subtract(first_number,seceond_number)))
        elif user_input == "DIV":
            print("result: "+ str(divide(first_number,seceond_number)))
        elif user_input == "MULT":
            print("result: "+ str(multiply(first_number,seceond_number)))
    else:
        print("unknow input")


    
    