n=int(input())
q=input().split()
a=[]
b=[]
for i in range(0,len(q)):
    a.append(q[i])
b=sorted(a)
if(a.count(a[0])==len(a)):
    print(a[0])
else:
    for i in range(len(b)-1,-1,-1):
        print(b[i],end="")
