# 1
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)

# 2
nums = [5, 6, 7]
squares = list(map(lambda x: x * x, nums))
print(squares)

# 3
temps = [0, 10, 20]
fahrenheit = list(map(lambda c: c * 9/5 + 32, temps))
print(fahrenheit)

# 4
names = ["kanat", "aida"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)
