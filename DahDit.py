class morse:
    def __init__(self,s = 'di dit dah'):
        if ' ' in s:
            self.s = s.split(' ')
            if len(self.s) < 4:
                self.s.append('.')
            self.dels = [' ', ',']
        else:
            if len(s) > 3:
                self.s = s
            else:
                self.s = list(s) + ['']
                if len(s) < 3:
                    self.s = [s[0]]+self.s
            self.dels = ['', ' ']
        self.signs = ''
        self.res = []
    def __neg__(self):
        self.signs = '-' + self.signs
        return self
    def __pos__(self):
        self.signs = '+' + self.signs
        return self
    def __invert__(self):
        self.signs = '~' + self.signs
        return self
    def __str__(self):
        f1, f2, f3 = 1, False, False
        for i in range(len(self.signs)):
            if self.signs[i] == '-':
                self.res.append(self.s[2])
                f1 = 1
            if self.signs[i] == '+':
                if self.signs[i:i+3] == '+++':
                    f1 = 3
                if self.signs[i:i+2] == '++' and f1 != 3:
                    f1 = 2
                    f2 = True
                if f3:
                   self.res.append(self.s[0])
                   f3 = False
                   f2 = False
                   continue
                if f1 == 3:
                    self.res.append(self.s[0])
                if f1 == 2:
                    self.res.append(self.s[0])
                    f1 = 1
                    continue
                if f1 == 1:
                    self.res.append(self.s[1])
                    if f2:
                        f3 = True
            if self.signs[i] == '~':
                f1 = 1
                self.res[-1] += self.dels[1]
        return self.dels[0].join(self.res) + self.s[-1]
