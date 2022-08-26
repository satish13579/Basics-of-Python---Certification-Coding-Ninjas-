from sys import stdin
import re
def reverseEachWord(string) :
    li=re.split(" ",string)
    for i,ele in enumerate(li):
        li[i]=li[i][::-1]
    st=""
    for j,x in enumerate(li):
        st+=x
        if(j!=(len(li)-1)):
            st+=" "
    return st
string = stdin.readline().strip()
ans = reverseEachWord(string)
print(ans)
