def func(a, b):
    while True:
        yield a
        a *= b


my_gen = func(-2, -5)
my_gen_2 = func(10, 3)

for item in range(6):
    print(next(my_gen))

print('*' * 100)

for item in range(6):
    print(next(my_gen_2))
