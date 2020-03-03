from collections import deque
l = eval(input())
q = deque()
for c in l:
    if type(c) is tuple:
        for i in c:
            q.append(i)
    if type(c) is int:
        if len(q) < c:
            break
        tup = list()
        for i in range(c):
            tup.append(q.popleft())
        tup = tuple(tup)
        print(tup)

        
