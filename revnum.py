n=input()
s=int(n)
b=[]
for i in range(0,len(n)):
    b.append(n[i])
for i in range(len(b)-1,-1,-1):
    print(b[i],end="")
