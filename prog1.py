c=input()
a=[]
x=[]
for i in range(0,len(c)):
    a.append(c[i])
for i in range(0,len(c)):
    if(a.count(a[i])>1):
        x.append(a.count(a[i]))
g=list(set(x))
print(max(g))
                    
