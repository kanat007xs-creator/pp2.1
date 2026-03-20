# 3. Use enumerate() and zip()
# 4. Type checking and conversions

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

#3enumer
print("Enumerate:")
for i, name in enumerate(names):
    print(i, name)

#3zip
print("\nZip:")
for name, score in zip(names, scores):
    print(name, score)

#4type 
value = "123"

print("\nType checking:")
print(isinstance(value, str))

converted = int(value)
print("Converted to int:", converted)