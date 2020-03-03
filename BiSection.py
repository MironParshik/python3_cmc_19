from math import *
f = input()
a, b = eval(input())
x = 1/2*(a+b)
val = eval(f)
while abs(val) > 0.000001:
    x = a
    if val*eval(f) < 0:
        b = 1/2*(a+b)
        x = 1/2*(a+b)
        val = eval(f)
    else:
        x = b
        if val*eval(f) < 0:
            a = 1/2*(a+b)
            x = 1/2*(a+b)
            val = eval(f)
print(x)
    
