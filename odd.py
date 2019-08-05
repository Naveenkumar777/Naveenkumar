n=int(input())
q=input().split()
a=[]
for i in range(0,len(q)):
    a.append(q[i])
for i in range(0,len(q)):
    if(a.count(a[i])==1):
        print(a[i])
