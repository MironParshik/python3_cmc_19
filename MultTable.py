from math import ceil
n, m = eval(input())
s = f"{n} * {n} = {n*n}"
l = len(s)
ind = s.index('=')
c = m // l
p = ceil(n/c)
tab = list()
image = [[(f"{i}".rjust(len(str(n))) + " * " + f"{j}".ljust(len(str(n)))+ f" = {i*j}").ljust(l) for i in range(1,n+1)] for j in range(1,n+1)]
while c*l+(c-1)*3 + 1 > m and n > 1:
    c -= 1
while c*p < n and n > 1:
    p += 1
for k in range(p):
    tab.append('='*m)
    for i in range(n):
        tab.append(' | '.join(image[i][c*k:(k+1)*c]))
tab.append('='*m)
print('\n'.join(tab))
