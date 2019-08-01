n=int(input())
q=input().split()
a=[]
b=[]
c=[]
for i in range(0,len(q)):
    a.append(q[i])
for i in range(0,len(q)):
    b.append(str(i))
for i in range(0,len(q)):
    if(a[i]==b[i]):
        c.append(a[i])
    else:
        continue
d=sorted(c)
for i in range(0,len(d)):
    print(d[i],end="")
