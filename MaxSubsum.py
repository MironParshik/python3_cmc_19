flag1 = True
flag2 = False
a = input()
subsum1 = 0
maxsubsum = int(a)
while a != '0':
    if a == '-0':
        break
    else:
        if flag1 & (int(a) < 0):
            if int(a) > maxsubsum:
                maxsubsum = int(a)
        else:
            flag1 = False
            subsum1 += int(a)
            if subsum1 > maxsubsum:
                maxsubsum = subsum1
        if subsum1 < 0:
            subsum1 = 0
            flag1 = True
    a = input()
print(maxsubsum)
        










    
