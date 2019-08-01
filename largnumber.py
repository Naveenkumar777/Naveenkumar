n=int(input())
q=input().split()
x=[]
y=[]
for i in range(0,len(q)):
    x.append(q[i])
y=sorted(x)
for i in range(len(y)-1,-1,-1):
    print(y[i],end="")
