a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    b[i]*=b[i]
for x in b:
    print(x,end=" ")