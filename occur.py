N=int(input())
a=[]
x=[]
for i in range(0,N):
    b=int(input())
    a.append(b)
for i in range(0,N):
    if(a.count(a[i])>1):
        x.append(a[i])
g=list(set(x))
for i in range(0,len(g)):
    print(g[i],end="")
                
                    
