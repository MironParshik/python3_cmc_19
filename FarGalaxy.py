from math import sqrt
f = input()
d = dict()
while ' ' in f:
    f = f.split()
    if f[3] in d:
        d[f[3]].append([float(f[i]) for i in range(3)])
    else:
        d[f[3]] = [[float(f[i]) for i in range(3)]]
    f = input()
maxdist = 0
dist = 0
keys = list(d.keys())
for i in range(len(d)):
    for j in range(i,len(d)):
        for a in d[keys[i]]:
            for b in d[keys[j]]:
                if a != b:
                    dist = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
                    if dist > maxdist:
                        maxdist = dist
                        res = [keys[i], keys[j]]
print(' '.join(sorted(res)))
        
