c = 0
def randint(a, b):
    global c
    c += 1
    if (c-1) % 2 == 0:
        return a
    else:
        return b

p1 = p2 = p3 = p4 = None
i = 0
j = 0
flag = 1
def randrange(a, b=None, d=None, p=None):
    global p1,p2,p3,p4,i,j,flag
    if not (a == p1 and b == p2 and d == p3):
        i = j = 0
        flag = 1
    p1, p2, p3, p4 = a, b, d, p
    if b != None:
        if d < 0:
            a = -a
            b = -b
            d = -d
            flag = -1
        if a+d*i+j < b:
            i += 1
            return (a+d*(i-1)+j)*flag
        else:
            j = a+d*i+j - b
            i = 1
            return (a+j)*flag
    else:
        if i < a:
            i+=1
            return i-1
        else:
            i = 0
            return 0 



        
    
        
