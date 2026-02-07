n = int(input())

first_pos = {}

for i in range(1, n + 1):
    s = input()
    if s not in first_pos:
        first_pos[s] = i

keys = list(first_pos.keys())
keys.sort()

for k in keys:
    print(k, first_pos[k])
