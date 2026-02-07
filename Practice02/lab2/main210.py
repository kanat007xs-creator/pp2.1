a=int(input())
b=list(map(int,input().split()))
b.sort()
v=[]
for i in range(a-1,-1,-1):
    v.append(b[i])
for x in v:
    print(x,end=" ")