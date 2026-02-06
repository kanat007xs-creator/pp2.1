a=int(input())
if a<=0:
    print("NO")
else:
    while(a%3==0):
        a//=3
if a==1:
    print("YES")
else:
    print("NO")
    
