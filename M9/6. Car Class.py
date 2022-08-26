from sys import stdin
class Car:
    def __init__(self,a,b):
        self.noOfGear=a
        self.color=b
    def printCarInfo(self):
        print("noOfGear:",self.noOfGear)
        print("color:",self.color)
class RaceCar(Car):
    def __init__(self,a,b,c):
        self.maxSpeed=c
        super().__init__(a,b)
    def printRaceCarInfo(self):
        super().printCarInfo()
        print("maxSpeed:",self.maxSpeed,end="")
noOfGear = int(stdin.readline().rstrip())
color = stdin.readline().rstrip()
maxSpeed = int(stdin.readline().rstrip())
raceCar = RaceCar(noOfGear,color,maxSpeed)
raceCar.printRaceCarInfo()
