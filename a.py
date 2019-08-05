n=int(input())
q=input().split()
a=[]
b=[]
for i in range(len(q)-1,-1,-1):
    a.append(q[i])
for i in range(0,len(a)):
    b.append(a[i])
    b.append("->")
for i in range(0,len(b)-1):
    print(b[i],end="")
