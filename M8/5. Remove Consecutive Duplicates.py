from sys import stdin
def removeConsecutiveDuplicates(string) :
    st=""+string[0]
    for i in string:
        if(i==st[len(st)-1]):
            continue
        else:
            st+=i
    return st
string = stdin.readline().strip()
ans = removeConsecutiveDuplicates(string)
print(ans)
