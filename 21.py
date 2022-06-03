# Example file for working with constructor in python.

# 1) Example for __init__method(This method is called when an object is 
   # created from a class and it allows the class to initialize the attributes of the class.):-

class Employee:

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):  
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}."
    
Deebya = Employee("Deebya", 500, "Manager" )
 
print(Deebya.role)


        


