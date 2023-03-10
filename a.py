s=input()
a=[]
i=0
for i in range(len(s)):
    if s[i]!='B':
        a.append(s[i])
    else:
        if len(a)!=0:
            a.pop()
        else:
            pass

c=''
for i in a:
    c=c+str(i)    
print(c)            