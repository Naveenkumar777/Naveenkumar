n=input()
q=input()
a=[]
b=[]
for i in range(0,len(n)):
    a.append(n[i])
for i in range(0,len(q)):
    b.append(q[i])
if(len(a)!=len(b)):
    if(len(b)>len(a)):
        x=len(b)-len(a)
        for i in range(0,x):
            a.append(" ")
for i in range(0,len(b)):
    print(b[i]+a[i])
