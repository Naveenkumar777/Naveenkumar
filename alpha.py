q=input()
a=[]
for i in range(0,len(q)):
    a.append(q[i])
b=list(set(a))
c=sorted(b)
for i in range(0,len(c)):
    print(c[i],end="")
