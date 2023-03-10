
class RepeatedList:
    def __init__(self, li, n):
        self.n = n
        self.li = li
        self.repeated_li = self.li * self.n

    def __len__(self):
        return len(self.li * self.n)

    def __getitem__(self, item):
        if item < 0 or item > len(self.li):
            raise IndexError
        else:
            return self.repeated_li[item]

    def __str__(self):
        return f'{self.li}*{self.n}'

    def to_list(self):
        return self.repeated_li

    def __iter__(self):
        return RepeatedListIterator(self)


class RepeatedListIterator:
    def __init__(self, repeatedlist):
        self.repeatedlist = repeatedlist
        self.repetition = 0
        self.li_iterations = iter(self.repeatedlist.repeated_li)

    def __next__(self):
        if self.repetition < self.repeatedlist.n:
            return next(self.li_iterations)


repeated_list = RepeatedList([1, 2, 3], 3)

print("Test [1,2,3]x3")
x = RepeatedList([1,2,3], 3)
assert len(x) == 9  # Verify true length
assert len(x.to_list()) == 9  # Verify the length of the expanded list
print(x)  # Test printing
for i, v in enumerate(x):  # Iterate over entire sequence (9 elements)
    print(f'{i}: {v}')
print(x.to_list())  # Expand the list to verify the order is as expected
assert x.to_list() == [v for v in x]  # Verify that tolist and iterating are consistent
print("\nTest [4,5,6]x0")
y = RepeatedList([4,5,6], 0)
assert len(y) == 0
print(y)  # Test printing