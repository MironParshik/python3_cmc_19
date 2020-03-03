from time import *
t1 = process_time()
n = 0
d = dict()
b = list()
m = 0
while n < 2:
    f = input()
    if ' ' not in f:
        b.append(f)
        n += 1
    else:
        f = f.split()
        if f[0] in d:
            d[f[0]].add(f[1])
        else:
            d[f[0]] = {f[1]}
        if f[1] in d:
            d[f[1]].add(f[0])
        else:
            d[f[1]] = {f[0]}
if b[1] not in d or b[0] not in d:
    print('NO')
else:
    if b[0] in d[b[1]] or b[1] in d[b[0]]:
        print('YES')
    else:
        s1 = d[b[0]]
        s3 = s1
        while True:
            s2 = s1
            for c in s3:
                if not (d[c] & s1 == d[c]):
                    s1 = s1|d[c]|{c}
            if s2 == s1 or b[1] in s1:
                break
            s3 = s1 - s2
            if process_time() - t1 > 0.5:
                break
        if b[1] in s1:
            print('YES')
        else:
            print('NO')
