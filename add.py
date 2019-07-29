n,q=input().split()
n=int(n)
q=int(q)
sum1=0
temp=0
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        sum1=a[i]+a[j]
        if(sum1==q):
            temp=1
            break
    if(temp==1):
        break
if(temp==1):
    print("yes")
else:
    print("no")
    
        
        
    
