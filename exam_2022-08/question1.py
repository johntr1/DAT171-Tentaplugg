# Question 1
# x[key] = value
from collections import *
from tabulate import tabulate


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


# Lär att använda help funktionen!
def read_groups(file):
    x = defaultdict(list)
    s = []
    with open(file, mode='r') as file:
        read_file = file.read()

    li = read_file.split('\n')
    li_split = [x.split(':') for x in li]
    for i, element in enumerate(li_split):
        names = element[3].split(',')
        for e in names:
            s.append([e, element[0]])

    for k, v in s:
        x[k].append(v)

    return x


def read_groups2(file):
    x = {}
    with open(file, mode='r') as file:
        read_file = file.read()
        name_list = []

    li = read_file.split('\n')
    li_split = [x.split(':') for x in li]
    for i, e in enumerate(li_split):
        names = e[3].split(',')
        for j in names:
            name_list.append(j)

    name_list = set(name_list)

    for i in name_list:
        value_list = []
        for j in li_split:
            if i in j[3].split(','):
                value_list.append(j[0])
        x[i] = value_list

    return x


names = read_users('passwd.txt')
y = names.keys()
# rint(y[0])
groups = read_groups2('group.txt')


def print_user_table(names, groups):
    li = names.items()
    li = sorted(li)
    group = sorted(groups.items())
    for i, e in enumerate(li):
        x = str(groups[li[i][0]])
        x = x.strip('[')
        x = x.strip(']')
        x = x.strip("'")
        x = x.strip("'")

        li[i] += x,

    print(li)


    return tabulate(li, headers=("User", "Name", "Groups"))


print(print_user_table(names, groups))
