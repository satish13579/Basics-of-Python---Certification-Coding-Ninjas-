import re
def reverseStringWordWise(string): 
    li=re.split(" ",string)
    n=len(li)
    str=""
    for i in range(n-1,-1,-1):
        str=str+li[i]
        if(i!=0):
            str+=" "
    return str
string = input()
ans = reverseStringWordWise(string)
print(ans)
