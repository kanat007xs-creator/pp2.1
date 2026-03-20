import os
from functools import reduce
#1dir
folder = "scores"
#папка соз
os.makedirs(folder, exist_ok=True)

data1 = "Alice,85\nBob,90\nCharlie,78"
data2 = "David,92\nEve,88\nFrank,75"
data3 = "Grace,95\nHannah,82\nIvan,89"

with open(os.path.join(folder, "class1.txt"), "w") as f:
    f.write(data1)

with open(os.path.join(folder, "class2.txt"), "w") as f:
    f.write(data2)

with open(os.path.join(folder, "class3.txt"), "w") as f:
    f.write(data3)

#список
files = os.listdir(folder)
#2hading
students = []

for file in files:
    path = os.path.join(folder, file)

    if file.endswith(".txt"):
        with open(path, "r") as f:
            for line in f:
                name, score = line.strip().split(",")
                students.append((name, int(score)))  

print("All students:")
print(students)
names = [s[0] for s in students]
scores = [s[1] for s in students]

# 1count
total_students = len(students)

# 2total
total_score = sum(scores)
highest = max(scores)
lowest = min(scores)

increased_scores = list(map(lambda x: x + 5, scores))

top_students = list(filter(lambda x: x[1] > 85, students))

product = reduce(lambda x, y: x * y, scores)

# 7Enu
print("\nStudents with index:")
for i, (name, score) in enumerate(students, start=1):
    print(i, name, score)

#8zip
zipped = list(zip(names, scores))
print("\nZipped:", zipped)

#9Sort students by score(decs)
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("\nSorted students:")
for name, score in sorted_students:
    print(name, score)

#4save

average = total_score / total_students

with open("report.txt", "w") as report:
    report.write(f"Total students: {total_students}\n")
    report.write(f"Average score: {average:.2f}\n")
    report.write(f"Highest score: {highest}\n")
    report.write(f"Lowest score: {lowest}\n\n")

    report.write("Top students (>85):\n")
    for name, score in top_students:
        report.write(f"{name} {score}\n")

print("\nReport saved to report.txt")