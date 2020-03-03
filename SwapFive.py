k = int(input())
i = 0
while True:
    b = k*(10**(i+1))//(10*k-1)
    if b*k == (b // 10 + k*(10**i)) and b % 10 == k:
        print(b)
        break
    else:
        i+=1
    
