a=input()
b=[]
c=[]
d=[]
for i in range(0,len(a)):
    if(i%2==0):
        b.append(a[i])
    else:
        c.append(a[i])
for i in range(0,len(b)):
    d.append(c[i])
    d.append(b[i])
for i in range(0,len(d)):
    print(d[i],end="")
    
