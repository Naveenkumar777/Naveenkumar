q=input().split()
a=[]
c=[]
for i in range(0,len(q)):
    a.append((q[i]))
for i in range(0,len(q)):
    b=a[i]
    for i in range(len(b)-1,-1,-1):
        c.append(b[i])
    c.append(" ")
for i in range(0,len(c)):
    print(c[i],end="")
