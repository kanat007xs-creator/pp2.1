#2
with open("s.txt", "r") as file:
    con = file.read()

print("content:")
print(con)

#3
with open("s.txt", "a") as file:
    file.write("KAAANAAATTT NEW LINE.\n")

print("\nnew content:")
with open("s.txt", "r") as file:
    print(file.read())