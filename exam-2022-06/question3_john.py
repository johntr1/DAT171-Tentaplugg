import numpy as np


class OuterMatrix:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1.copy()
        self.arr2 = arr2.copy()

    def toarray(self):
        return np.outer(self.arr1, self.arr2)

    def transpose(self):
        return OuterMatrix(self.arr2, self.arr1)

    def norm(self):
        return np.linalg.norm(self.arr1) * np.linalg.norm(self.arr2)

    def __getitem__(self, item):
        row, col = item
        if type(row) == slice and type(col) == slice:
            return OuterMatrix(self.arr1[row], self.arr2[col])
        else:
            return self.arr1[row] * self.arr2[col]

    def __mul__(self, other):
        if type(other) == np.ndarray:
            return np.dot((self.arr1*self.arr2), other)
        elif type(other) == int:
            return (self.arr1*self.arr2) * other
        else:
            raise TypeError("Wrong type")



a = np.array([9., 1., 2., 3., 4., 5., 6.])
b = np.array([2., 1., 4., 3., 6., 5., 7.])
c = np.array([1., 2., 1., 7., 8., 2., 4.])
m = OuterMatrix(a, b)
print("Expanded:\n{}".format(m.toarray()))
m_sub = m[1:3, 2:5] # This should also be a OuterMatrix.
print("Slicing (expanded):\n{}".format(m_sub.toarray()))
print("Slicing:", m[1:3, 5]) # slice + int -> ndarray
print("Slicing:", m[3, 2:5]) # int + slice -> ndarray
print("Item:", m[2, 4]) # int + int -> float
print("Norm:", m.norm())
m *= 2.0
print("Norm after scaling:", m.norm())
print("Multiplication with array:", m * c)
m_sub_t = m_sub.transpose()
print("Transpose (expanded):\n{}".format(m_sub_t.toarray()))

