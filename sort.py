k=int(input())
l=[]
for i in range(0,k):
    a=list(map(int,input().split()))
    l.append(a)
s=[]
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        x=l[i][j]
        s.append(x)
h=sorted(s)
for i in range(0,len(h)):
    print(h[i],end=" ")
    
    
        
        
    
