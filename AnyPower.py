a = int(input())
b = 2
while b <= a//2:
    i = 1
    while pow(b,i) < a:
        i+=1
    if pow(b,i) == a and i > 1 :
        print('YES')
        break;
    else:
        b+=1
else:
    print('NO')
