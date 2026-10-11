def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
Add = add(1, 2, 3, 4, 5)
print(Add)