# # class method

# new comments added
# new comments added
class Employee:
    Company="INFY"
    def __init__(self,name,age,loc):
        self.name=name
        self.age=age
        self.loc=loc

    def meth1(self):
        print(f"name is {self.name} and age is {self.age} and location is {self.loc}")

    @classmethod
    def get_company(cls):
        print("Company name is:",cls.Company)

obj=Employee("Rahul",21,"Pune")
obj.meth1()
obj.get_company()
Employee.get_company()

# new comments added
# new comments added

# new comments added-4
# new comments adde-5
# new comments added-6
# new comments adde-7