def statcounter():
    s = {}
    get = yield s
    def counter(func):
        def decor(*args):
            nonlocal s
            if func in s:
                s[func] += 1
            else:
                s[func] = 1
            return func(*args)
        return decor
    while get:
        get = yield counter(get)
