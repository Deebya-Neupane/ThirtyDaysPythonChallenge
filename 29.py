# Abstract Base Class.

from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
       self.length = 5
       self.breadth = 7

    def printarea(self):
        return self.length * self.breadth   

rect1 = Rectangle()
print(rect1.printarea())
