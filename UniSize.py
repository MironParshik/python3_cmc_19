def sizer(args):
    class C(args):
        def __init__(self, val):
            if self:
                pass
            else:
                super().__init__(val)
            if '__len__' in dir(self):
                self.size = len(self)
            else:
                self.size = int(self)
        @property
        def size(self):
            return self._size
        @size.setter
        def size(self, val):
            self._size = val
        def __delitem__(self, key):
            super().__delitem__(key)
            if '__len__' in dir(self):
                self.size = len(self)
            else:
                self.size = int(self)
    return C

@sizer
class S(str): pass

@sizer
class N(float): pass

@sizer
class C(): pass
