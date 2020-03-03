class sausage:
    def __init__(self, f = 'pork!', v = 1):
        self.f = f
        self.s = '|' 
        j = 0
        if type(v) == str:
            v = eval(v)
        self.v = int(12*v)/12
        for i in range(int(12*v)):
            if i > 0 and i % 12 == 0:
                self.s += '||'
                j = 0
            self.s += f[j%len(f)]
            j += 1
        u = ''
        d = ''
        self.s += '|'
        j = 0
        for i in range(len(self.s)):
            if i > 0 and i % 14 == 0:
                j = 0
            if j == 0:
                u += '/'
                d += '\\'
                j += 1
                continue
            if j == 13:
                u += '\\'
                d += '/'
                j += 1
                continue
            if i+1 == len(self.s) and (i+1)%14 != 0:
                u += '|'
                d += '|'
                break
            u += '-'
            d += '-'
            j += 1
        d = '\n'+ d
        self.s = u + ('\n' + self.s)*3 + d

    def __bool__(self):
        if self.v == 0:
            return True
        else:
            return False
        
    def __str__(self):
        return self.s

    def __add__(self, obj):
        if type(obj) == sausage:
            return sausage(self.f, self.v+obj.v)

    def __sub__(self, obj):
        if type(obj) == sausage:
            return sausage(self.f, self.v-obj.v)

    def __mul__(self, i):
        return sausage(self.f, self.v * i)

    def __rmul__(self, i):
        return sausage(self.f, self.v * i)

    def __truediv__(self, i):
        return sausage(self.f, self.v / i)

    def __rtruediv__(self, i):
        return sausage(self.f, self.v / i)
    
        
        
    
