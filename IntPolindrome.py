a = int(input())
if a % 10 == 0:
    print('NO')
else:
    while a > 0:
        b = a
        i = 0
        while b >= 10:
            b = b // 10
            i += 1
        if a % 10 == b:
            a = (a - b*(10**i)) // 10
        else:
            print('NO')
            break;
    else:
        print('YES')

            
        
