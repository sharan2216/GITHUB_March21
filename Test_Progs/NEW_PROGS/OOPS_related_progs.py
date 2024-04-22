# class A:
#     x=10
#     print(x)
#     def method1():
#         print("Method1 gets called")
# class B(A):
#     y=20
#     print(y)
#     def method2():
#         print("Method2 gets called")
#
# obj2=B()
# obj2.method2()
# obj2.method1()


# Creating a simple class in Python
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f"{self.name} says hello!"
#
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks"
#
#
# obj = Dog("Jacky")
# obj2=Animal('Danny')
# print(obj.speak())
# print(obj2.speak())

# Using the super() function------------------
# class Animal:
#     def __init__(self,name):
#         self.name=name
#
#     def speaks(self):
#         return f"{self.name} says hello..!!"
#
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed
#
#     def species(self):
#         return f"{self.name} belongs to {self.breed}"
#
#
# dog = Dog("Charlie", "Bulldog")
# print(dog.species())



# 4. Creating a property -Protected
# #
# class Circle:
#     def __init__(self,radius):
#         self._radius=radius
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         if value >=0:
#             self._radius=value
#
#         else:
#             raise ValueError("Radius must be positive")
#
#
# obj=Circle(5)
# print(obj.radius)
# obj.radius=10
# print(obj.radius)

# 5. Encapsulation – Private members
#
# class Myclass:
#     def __init__(self):
#         self.public = "public"
#         self._protected = "Protected"
#         self.__private = "Private"
#
#
# obj=Myclass()
# print(obj.public)
# print(obj._protected)
# print(obj.__private)


# 6. Polymorphism – Using Inbuilt Abstract Base Classes (ABC)
#
# from collections.abc import Iterable
#
# def get_length(item):
#     if isinstance(item, Iterable):
#         return len(item)
#     else:
#         return "Not iterable"
#
# print(get_length("Hello"))
# print(get_length([1, 2, 3]))
# print(get_length(123))

# 7. Defining an Abstract Base Class (ABC)

# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         return "BOW WOW..!!!"
#
# obj=Dog()
# print(obj.speak())


# 8. Using class methods and static methods
# class MyClass:
#     @classmethod
#     def class_method(cls):
#         return "Class method called"
#
#     @staticmethod
#     def static_method():
#         return "Static method called"
#
# print(MyClass.class_method())
# print(MyClass.static_method())


# 9. Operator Overloading in Python

# class Mango:
#     def __init__(self,x):
#         self.x = str(x)
#     def __add__(self,y):
#         return self.x + y.x
# obj1 = Mango(7)
# obj2 = Mango('mangoes')
# print(obj1+obj2)

# 10. Using Special methods for string representations (repr and str)
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old."
#
#     def __repr__(self):
#         return f"Person('{self.name}', {self.age})"
#
# p = Person("Bob", 30)
# print(str(p))
# print(repr(p))


# 11. Using composition in Python OOP

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

s = Salary(15000, 5000)
e = Employee("Ashwin", s)
# print(e.salary)--gives error
print(e.name)
print(e.salary.pay)
print(e.salary.bonus)