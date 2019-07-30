n=int(input())
s=[]
for i in range(0,n):
    b=input()
    s.append(b)
k=[]
for i in range(0,n):
    k.append(len(s[i]))
a=min(k)
k=s[0]
s.remove(s[0])
l=""
for i in range(0,n):
    c=0
    for j in range(0,len(s)):
        if(k[i]==s[j][i]):
            c+=1
    if(c==len(s)):
        l=l+k[i]
    else:
        break
print(l)
