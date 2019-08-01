n,q=input().split()
n=int(n)
q=int(q)
c=0
for i in range(n,q+1):
    if (i > 1): 
       for n in range(2,i): 
           if (i%n)==0: 
               break
       else: 
           c=c+1
print(c)
