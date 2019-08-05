q=input()
a=[]
b=[]
for i in range(0,len(q)):
    a.append(q[i])
for i in range(0,len(a)):
    if(a.count(a[i])>1):
        b.append(a[i])
    else:
        b.append(a[i])
c=list(set(b))
if(len(c)!=len(a)):
    
    d=sorted(c)
    for i in range(0,len(d)):
        print(d[i],end="")
else:
    for i in range(0,len(b)):
        print(b[i],end="")
