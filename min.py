n,q=input().split()
n=int(n)
q=int(q)
a=list(map(int,input().split()))
for j in range(0,q):
    u,v=input().split()
    u=int(u)
    v=int(v)
    b=a[u-1:v]
    print(min(b))
    
