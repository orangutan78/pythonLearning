def a(x):
    print(x)
    print(x())
def b(y):
    print(y)
    try:
        print(y())
    except TypeError:
        raise TypeError('No ERROR!')
@b
@a
def c():
    print(1)
    return 2