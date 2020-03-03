a = int(input())
if a % 10 == 0:
    print('NO')
else:
    while a >= 0:
        b = a
        i = 0
        while b >= 10:
            b = b // 10
            i += 1
        print(a, b, i)
        if a % 10 == b:
            a = (a//10) - b*(10**(i-1))
        else:
            print('NO')
            break;
    else:
        print('YES')

            
        
