n=int(input())
q=input().split()
a=[]
b=[]
for i in range(0,len(q)):
    a.append(q[i])
for i in range(0,len(a)):
    if(a.count(a[i])>1):
        b.append(a[i])
print(b[0])
