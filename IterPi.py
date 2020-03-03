def pigen():
    i = 0
    j = 0
    a = 0
    while True:
        yield 4*(a+(-1)**i*(1/(1+j)))
        a = a + (-1)**i*(1/(1+j))
        i+=1
        j+=2
        
