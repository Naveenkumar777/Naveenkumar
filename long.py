from itertools import combinations
n,k=list(map(int,input().split()))
n=list(str(n))
nc=len(n)-k
a=list(combinations(n,nc))
minnum=min(a)
m="".join(minnum)
m=int(m)
print(m)
