a,b,c=map(int,input().split())
d=list(map(int,input().split()))
b=b-1
c=c-1
while b<c:
    d[b],d[c]=d[c],d[b]
    b=b+1
    c=c-1
for x in d:
    print(x,end=" ")