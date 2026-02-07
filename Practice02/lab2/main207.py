a=int(input())
b=list(map(int,input().split()))
max=max(b)
m=0
for i in range(a):
    if max>b[i]:
        m=m+1
    elif max==b[i]:
        m=m+1
        print(m)
        break
    else:
        print(m)