def BinPow(a,n,f):
    if n == 1:
        return a
    return f(a,BinPow(a,n-1,f)) if n % 2 == 1 else f(BinPow(a,n/2,f),BinPow(a,n/2,f))
   
