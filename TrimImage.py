import time
coords = list()
s = input()
a = s.split()
if int(a[2]) != 0 and int(a[3]) != 0 and (32 < ord(a[4])) and (ord(a[4]) < 128):
    x1 = min(int(a[0]),int(a[0])+int(a[2]))
    x2 = max(int(a[0]),int(a[0])+int(a[2]))
    y1 = min(int(a[1]),int(a[1])+int(a[3]))
    y2 = max(int(a[1]),int(a[1])+int(a[3]))
while s.startswith("0 0 0 0") != True:
    s = s.split()
    if int(s[2]) != 0 and int(s[3]) != 0 and (32 < ord(s[4])) and (ord(s[4]) < 128):
        coords.append(s)
        x1 = min(x1, min(int(s[0]),int(s[0])+int(s[2])))
        x2 = max(x2, max(int(s[0]),int(s[0])+int(s[2])))
        y1 = min(y1, min(int(s[1]),int(s[1])+int(s[3])))
        y2 = max(y2, max(int(s[1]),int(s[1])+int(s[3])))
    s = input()
image = [['.' for j in range(x1, x2)] for i in range(y1,y2)]
a = x2 - x1
for c in coords:
    x3 = 0;
    y3 = 0;
    if int(c[2]) < 0:
        x3 += int(c[2])
    if int(c[3]) < 0:
        y3 += int(c[3])

    for j in range(abs(int(c[3]))):
        image[int(c[1])-y1+y3+j] = ''.join(image[int(c[1])-y1+y3+j][:int(c[0])-x1+x3]) + c[4]*abs(int(c[2])) + ''.join(image[int(c[1])-y1+y3+j][int(c[0])-x1+x3+abs(int(c[2])):])
for i in range(y2-y1):
    if type(image[i]) == list:
        image[i] = ''.join(image[i])
print('\n'.join(image))
