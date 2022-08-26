class ComplexNumbers:
    def __init__(self,real,img):
        self.i=img
        self.r=real
    def add(self,x,y):
        self.r+=x
        self.i+=y
    def mul(self,x,y):
        self.a=((self.r*x)-(self.i*y))
        self.b=((self.r*y)+(self.i*x))
        self.r=self.a
        self.i=self.b
    def prit(self):
        print(self.r,"+","i{}".format(self.i))  
a,b=map(int,input().split())
c1=ComplexNumbers(a,b)
a,b=map(int,input().split())
c2=ComplexNumbers(a,b)
k=int(input())
if(k==1):
    c1.add(c2.r,c2.i)
elif(k==2):
    c1.mul(c2.r,c2.i)
c1.prit()
