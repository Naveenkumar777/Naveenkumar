n,q=input().split()
n=int(n)
b=[]
c=[]
d=[]
for i in range(n):
    a=input().split()
    b.append(a)
for i in range(0,1):
    for o in range(0,len(b[i])):
        x=b[i][o]
        for j in range(1,len(b)):
            for k in range(0,len(b[j])):
                if(x==b[j][k]):
                    c.append(b[j][k])
for i in range(0,len(c)):
    if(c.count(c[i])>n-2):
        d.append(c[i])
e=list(set(d))
f=sorted(e)
for i in range(0,len(f)):
    print(f[i],end=" ")
