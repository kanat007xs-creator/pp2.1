# 1
def sum_all(*args):
    print(sum(args))

# 2
def show_numbers(*args):
    for num in args:
        print(num)

# 3
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

# 4
def full_info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


sum_all(1, 2, 3)
show_numbers(5, 6, 7)
show_info(name="Kanat", age=17)
full_info(1, 2, name="Kanat")
