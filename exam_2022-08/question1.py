# Question 1
# x[key] = value
from collections import *

def read_users(file):
    with open(file, mode='r') as file:
        read_file = file.read()
    li = read_file.split('\n')
    li_split = [x.split(':') for x in li]
    x = {}
    for i, element in enumerate(li_split):
        test = int(element[2])
        if test >= 500:
            names = element[4]
            key = element[0]
            x[key] = names
    return x


def read_groups(file):
    x = {}
    with open(file, mode='r') as file:
        read_file = file.read()

    li = read_file.split('\n')
    li_split = [x.split(':') for x in li]
    for i, element in enumerate(names):
        names = element[3].split(',')
        for j in enumerate(li_split):
            return True



    return x

print(read_groups('group.txt'))
print(defaultdict)



