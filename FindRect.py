flag = 0
stop = False
ids = []
count = 0
while flag!=2:
    s = input()
    if len(ids) > 0:
            for i in range(len(ids)):
                if s[ids[i]] != '#':
                    count += 1
            ids.clear()
    if s[0] == '.' and s[-1] == '.':
        for i in range(len(s)):
            if s[i] == '#' and s[i+1] == '.':
                ids.append(i)
    if s[0] == '-':
        for c in s:
            if c != '-':
                stop = True
                break
        flag += 1
    if stop:
        break
print(count)
