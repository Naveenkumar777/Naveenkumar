n=int(input())
q=input().split()
a=[]
b=[]
for i in range(0,len(q)):
    a.append(int(q[i]))
for i in range(0,len(a)):
    if(a[i]%2==0):
        if(i%2==1):
            b.append(a[i])
    else:
        if(i%2==0):
            b.append(a[i])
for i in range(0,len(b)):
    print(b[i],end=" ")
