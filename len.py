from random import choice
class A:
    def __init__(self, arr):
        self.count = arr
    def __len__(self):
        print('2222')
        return len(self.count)
    def __getitem__(self, position):
        print('bbb')
        return self.count[position + 1]

a = A([1, 3, 45])
print(a.__getitem__(1))
# print(a[1])