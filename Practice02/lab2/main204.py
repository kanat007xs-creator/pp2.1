a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    if i>0:
        c+=1
print(c)