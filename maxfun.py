def maxfun(s, f1, *args):
    if len(args) > 0:
        maxval = sum([f1(i) for i in s])
        maxf = f1
        for f in args:
            if sum([f(i) for i in s]) >= maxval:
                maxf = f
                maxval = sum([f(i) for i in s])
    else: maxf = f1
    return maxf
    
