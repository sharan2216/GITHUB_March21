# #Access Specifiers---------------
# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self._rollno=rollno
#
#     def display(self):
#         print(f'name is {self.name} and rollno is {self._rollno}')
#
# obj=Student("Raj",121)
# print(obj.name)
# print(obj._rollno)
# obj.display()

# #Protected--------------------------------------------------
# using public function showdata also we can access protected memebers outside the class ,
# so nothing is protected in python-------------
# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self._rollno=rollno
#     def display(self):
#         print(f'name is {self.name} ans roll no is {self._rollno}')
#
# class Parents(Student):
#     pass
#
# p1 = Parents("Roy", 111)
# print(p1.name)
# print(p1._rollno)
# p1.display()
#
# def showdata():
#     p2= Parents("Roy", 111)
#     print(p2.name)
#     print(p2._rollno)
#     p2.display()
#
# showdata()
#
# # #-------------------------------------------------------------------------------------------------
# # # if we want to update the data of the class variables
# #
# s2=Student("RAJA",221)
# print(s2.name)
# s2.display()
# # #-------------------------------------------------------------------------------------------------

#PRIVATE ATTRIBUTE-------------------------

class Student:
    def __init__(self,name,age,loc):
        self.name=name
        self._age=age
        self.__loc=loc
    def __display(self):
        print(f'name is {self.name} ans age is {self._age} and loaction is {self.__loc}')

class Parents(Student):
    def show(self):
        print(f'name is {self.name} ans age is {self._age} and loaction is {self.__loc}')


p1=Parents("Raka",22,"Pune")
print(p1.name)
print(p1._age)
# print(p1.__loc) ------#cant access private attributes outside class
# p1.show() ------#cant access private attributes outside class

s1=Student("Rama",30,"Ayodhya")
print(s1.name)
print(s1._age)
# print(s1.__loc)  -----#cant access private attributes outside class
# s1.__display()   ------#cant access private attributes outside class