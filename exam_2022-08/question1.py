# Question 1
# x[key] = value

def read_users(file):
    with open(file, mode='r') as file:
        read_file = file.read()

    li = read_file.split(':')
    key = [x for x in ]
    return li

print(read_users('passwd.txt'))