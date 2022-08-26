def removeAllOccurrencesOfChar(string,c):    
    st=""
    for i in string:
        if(i==c):
            continue
        else:
            st+=i
    return st
string = input()
c = input()
output = removeAllOccurrencesOfChar(string,c)
print(output)
