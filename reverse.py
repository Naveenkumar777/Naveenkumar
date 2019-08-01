a=input()
b=[]
for i in range(0,len(a)):
    b.append(a[i])
for i in range(len(b)-1,-1,-1):
    print(b[i],end="")
