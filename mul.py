n=int(input())
q=input().split()
a=[]
b=1
for i in range(0,len(q)):
    a.append(int(q[i]))
for i in range(0,len(a)):
    b=b*a[i]
for i in range(0,len(a)):
    c=b//a[i]
    print(c,end=" ")
