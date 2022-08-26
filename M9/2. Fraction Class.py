from math import gcd
class Fraction:
    def __init__(self,a,b):
        self.n=a
        self.d=b
    def add(self,n1,d1):
        if(self.d==d1):
            self.n+=n1
        else:
            self.lcm=self.d*d1
            self.n=((self.lcm//self.d)*self.n)+((self.lcm//d1)*n1)
            self.d=self.lcm
    def mul(self,n1,d1):
        self.n*=n1
        self.d*=d1
    def simplify(self):
        self.gcd=gcd(self.n,self.d)
        self.n//=self.gcd
        self.d//=self.gcd
    def prit(self):
        print(self.n,"/",self.d,sep="")
x,y=map(int,input().split())
f1=Fraction(x,y)
t=int(input())
for i in range(t):
    op,x,y=map(int,input().split())
    if(op==1):
        f1.add(x,y)
    elif(op==2):
        f1.mul(x,y)
    f1.simplify()
    f1.prit()
