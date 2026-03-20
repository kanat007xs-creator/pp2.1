import os

#1
os.makedirs("test_dir/sub_dir", exist_ok=True)
print("creat dir")

#2
print("\ndir contents:")
for item in os.listdir("."):
    print(item)

#3
print("\n.txt files:")
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))