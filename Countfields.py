def fcounter(C, *args):
    c = C(*args)
    l = [list() for i in range(4)]
    for meth in dir(C):
        if not (meth.startswith('__') or meth.startswith('_')):
            if callable(getattr(C, meth)):
                l[0].append(meth)
            else:
                l[1].append(meth)
    for meth in dir(c):
        if not (meth.startswith('__') or meth.startswith('_')):
            if type(getattr(c, meth)) == 'method':
                l[2].append(meth)
            else:
                if not callable(getattr(c, meth)) and meth not in l[1]:
                    l[3].append(meth)
    return [sorted(i) for i in l]
