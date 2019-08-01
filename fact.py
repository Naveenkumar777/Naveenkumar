n=int(input())
b=1
if(n==0):
    b=1
    print(b)
else:
    for i in range(1,n+1):
        b=b*i
    print(b)
