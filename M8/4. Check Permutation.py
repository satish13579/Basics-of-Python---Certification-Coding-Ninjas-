def isPermutation(string1, string2) :
    s1=0
    for i in string1:
        s1+=ord(i)
    s2=0
    for j in string2:
        s2+=ord(j)
    if(s1==s2):
        return 1
    else:
        return 0
string1 = input()
string2 = input()
ans = isPermutation(string1, string2)
if ans :
    print('true')
else :
    print('false')
