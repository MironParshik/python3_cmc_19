class LetterAttr:
    def __getattr__(self, name):
        if name in self.__dict__:
            pass
        else:
            self.__dict__[name] = name
        return self.__dict__[name]
    def __setattr__(self, name, val):
        s = ''
        for c in val:
            if c in name:
                s += c
        self.__dict__[name] = s
