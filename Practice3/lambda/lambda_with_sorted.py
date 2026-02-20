# 1
numbers = [5, 2, 8, 1]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)

# 2
words = ["apple", "kiwi", "banana"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)

# 3
students = [("Kanat", 90), ("Aida", 85), ("Ali", 95)]
sorted_by_score = sorted(students, key=lambda x: x[1])
print(sorted_by_score)

# 4
people = [{"name": "Kanat", "age": 17}, {"name": "Aida", "age": 16}]
sorted_by_age = sorted(people, key=lambda x: x["age"])
print(sorted_by_age)