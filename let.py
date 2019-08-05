n=input()
q=input()
if(len(n)>=len(q)):
    for i in range(0,len(n)):
        print(q[i]+n[i])
else:
    for i in range(0,len(q)):
        print(n[i]+q[i])
