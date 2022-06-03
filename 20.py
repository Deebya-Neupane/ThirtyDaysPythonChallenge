# Example file for working with constructor in python.

# 1) Example for self keyword(The self in keyword in Python is used to all the instances in a class.):-

class Employee:

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}."
    
Deebya = Employee()
Deepika = Employee()

Deebya.name = "Deebya"
Deebya.salary = 500
Deebya.role = "Manager"

Deepika.name = "Deepika"
Deepika.salary = 600
Deepika.role = "Instructor"
 
print(Deepika.printdetails())


        


