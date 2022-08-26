class Person:
    def setValue(self,name,age):
        self.__name=name
        self.__age=age
    def GetValue(self):
        print("The name of the person is",self.__name,"and the age is {}.".format(self.__age))  
name=input()
age=input()
p=Person()
p.setValue(name,age)
p.GetValue()
