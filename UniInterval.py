s = eval(input())
s = sorted(s)
res = list(s[0])
reslen = 0
for i in s[1:]:
    if (i[0] <= res[1]) & (i[1] > res[1]):
        res[1] = i[1]
    elif i[1] <= res[1]:
        pass
    else:
        reslen += res[1]-res[0]
        res = list(i)
reslen += res[1]-res[0]
print(reslen)
    
    
