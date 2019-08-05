n,q=input().split()
n=input().split()
q=int(q)
a=[]
for i in range(0,len(n)):
    a.append((int(n[i])))
b=sorted(a)
print(b[-q])
