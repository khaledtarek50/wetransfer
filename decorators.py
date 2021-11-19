def func(f):
    def wrapper():
        print('started')
        f()
        print('ended')
    return wrapper
def func2():
    print('i am func2')

x = func(func2)
print(x)
x()