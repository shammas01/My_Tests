# Method overriding.........


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: "Woof!"
print(cat.speak())  # Output: "Meow!"



# Method overloading............

class Calculator:
    def add(self,*args, ):
        return sum(args)

calc = Calculator()
result1 = calc.add(2, 3)  # Calls add with two arguments
result2 = calc.add(2, 3, 4)  # Calls add with three arguments (default values)

print(result1)  # Output: 5
print(result2)  # Output: 9
