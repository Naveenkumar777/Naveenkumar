N,Q=input().split()
N,Q=int(N),int(Q)
k=input().split()
l=[]
for i in range(0,Q):
    s=input().split()
    l.append(s)
for i in range(0,Q):
    b=[]
    c=0
    for j in range(int(l[i][0])-1,int(l[i][1])):
        b.append(k[j])
        c+=int(k[j])
    print(c)
