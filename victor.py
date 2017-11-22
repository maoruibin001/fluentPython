from math import hypot

class Victor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Victor(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __bool__(self):
        print(3333)
        return True

    def __mul__(self, other):
        return Victor(self.x * other, self.y * other)
    # def __str__(self):
    #     return 'hello world'

victor1 = Victor(1, 3)
victor2 = Victor(2, 5)

print(1 | 3)
