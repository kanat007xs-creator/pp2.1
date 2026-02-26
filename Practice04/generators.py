#t1
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input("Enter N: "))
for num in square_generator(n):
    print(num)
#t2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter n: "))
print(",".join(str(x) for x in even_numbers(n)))
#t3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))
for num in divisible_by_3_and_4(n):
    print(num)
#t4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for value in squares(a, b):
    print(value)
#t5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter n: "))
for num in countdown(n):
    print(num)