X=input()
Y=input()
a=[]
b=[]
s=[]
for i in range(0,len(X)):
    a.append(X[i])
for i in range(0,len(Y)):
    b.append(Y[i])
for i in range(0,len(X)):
    if(X[i]==Y[i]):
        s.append(Y[i])
f=len(b)-len(s)
print(f)
                    
