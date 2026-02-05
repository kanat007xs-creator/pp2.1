#1
a=input()
for i in a:
    print(i)
    if i=="f" or i=="j":
        continue
#2
b=46
for i in range(b):
    print(i)
    if i==34 and i==23:
        continue
#3
c=["bmw","scoda","porshe","lexus"]
for i in c:
    if c=="lexus":
        continue
    print(i)