def c():
    return 5
def f(a):
    b = a + c()
    return b
print(f(5))
