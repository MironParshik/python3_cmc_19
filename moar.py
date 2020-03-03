def moar(a,b,n):
    acount, bcount = 0, 0
    for c in a:
        if c % n == 0:
            acount += 1
    for c in b:
        if c % n == 0:
            bcount += 1
    if acount > bcount:
        return True
    else:
        return False
        
        
