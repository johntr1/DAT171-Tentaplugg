import numpy as np


class OneHotVector:
    def __init__(self, length, idx):
        self.length = length
        self.idx = idx
        self.li = []
        for i in range(length):
            self.li.append(0)
        self.li[idx] = 1

    def __repr__(self):
        return str(self.li)

    def __len__(self):
        return len(self.li)

    def __getitem__(self, item):
        if item >= 0:
            return self.li[item]
        elif item < 0:
            self.li.reverse()
            reversed_item = (item * -1) - 1
            output = self.li[reversed_item]
            self.li.reverse()
            return output

    def toarray(self, dtype=int):
        return np.array(self.li, dtype=dtype)

    def dot(self, M):
        return M[self.idx, :]


v = OneHotVector(3, 2)

w = OneHotVector(4, 1)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

assert w[0] == 0
assert w[1] == 1
assert w[2] == 0
assert w[-3] == 1
assert w[-2] == 0

print(f'v as np.array: {v.toarray()}')

print(f'w as float np.array: {w.toarray(dtype=float)}')

print('v . a =', v.dot(a))
print('w . b =', w.dot(b))