import pprint
m, n = eval(input())
a = [[23]*m for i in range(n)]
l,k = 0,0
b = 0
s = 0
step = [(0,1),(1,0),(0,-1),(-1,0)]
for i in range(n):
    for j in range(m):
        a[l][k] = b
        b += 1
        if b == 10:
            b = 0
        if l+step[s][0] == n or k+step[s][1] == m or a[l+step[s][0]][k+step[s][1]] != 23:
            s += 1
            if s == 4:
                s = 0
        l += step[s][0]
        k += step[s][1]
for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()
