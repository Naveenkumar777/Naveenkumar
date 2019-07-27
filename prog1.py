X=input()
Y=input()
a=[]
b=[]
s=[]
g=[]
for i in range(0,len(X)):
    a.append(X[i])
for i in range(0,len(Y)):
    b.append(Y[i])
if(len(a)<len(b)):
    
    for i in range(0,len(X)):
        if(X[i]==Y[i]):
            s.append(Y[i])
    f=len(b)-len(s)
    print(f)
else:
    for i in range(0,len(Y)):
        if(Y[i]==X[i]):
            g.append(Y[i])
    print(len(g))
                    
