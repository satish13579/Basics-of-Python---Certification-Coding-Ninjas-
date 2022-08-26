from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printMyType(self):
        pass
class Square(Shape):
    def calculateArea(self,s):
        return s*s
    def printMyType(self):
        print("square")
class Rectangle(Shape):
    def calculateArea(self,l,b):
        return l*b
    def printMyType(self):
        print("rectangle")
obj=Square()
obj.printMyType()
area=obj.calculateArea(5)
print(area)
obj=Rectangle()
obj.printMyType()
area=obj.calculateArea(5,4)
print(area)
