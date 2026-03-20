from functools import reduce

numbers = [1, 2, 3, 4, 5]

#1 map
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

#1fil
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

#2red
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)