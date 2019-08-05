n=int(input())
q=input().split()
a=[]
b=[]
c=[]
for i in range(0,len(q)):
    a.append(q[i])
for i in range(0,len(a)):
    if(a.count(a[i])>1):
        b.append(a[i])
for i in range(0,len(a)):
    if(a.count(a[i])==1):
        c.append(a[i])
if(len(c)==len(a)):
    print("unique")
else:
    print(b[0])
