def strtodiv(func):
    f = str(func).split(' ')[1]
    def meth(*args):
        if type(getattr(str, f)(*args)) == str:
            return DivStr(getattr(str, f)(*args))
        else:
            return getattr(str, f)(*args)
    return meth

class DivStr(str):
    for c in str.__dict__:
        if callable(getattr(str, c)) and c not in {'__class__', '__new__', '__getattribute__', '__getattr__', '__repr__', '__str__ '}:
            s = '''@strtodiv
def ''' + c + '''(*args):
    return None'''
            exec (s)
    def __truediv__(self, n):
        l = int(len(self)/n)
        return self[:l]
