# 1
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# 2
nums = [10, 15, 20, 25]
greater_than_15 = list(filter(lambda x: x > 15, nums))
print(greater_than_15)

# 3
words = ["apple", "hi", "banana", "ok"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)

# 4
ages = [12, 18, 25, 16]
adults = list(filter(lambda x: x >= 18, ages))
print(adults)
