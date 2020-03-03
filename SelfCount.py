class WeAre:
    x = 0
    def __init__(self):
        WeAre.x += 1
    def __del__(self):
        WeAre.x -= 1

    @property
    def count(self):
        return self.x

    @count.setter
    def count(self, value):
        pass

    @count.deleter
    def count(self):
        pass
