a=int(input())
b=list(map(int,input().split()))
max=max(b)
min=min(b)
for i in range(a):
    if max==b[i]:
        b[i]=min
for v in b:
    print(v,end=" ")