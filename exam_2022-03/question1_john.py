import os


def read_directory(directory):
    li = os.listdir(directory)
    x = {}
    for i in li:
        x[i] = os.path.getsize(f'{directory}/{i}')
    return x


path = 'example_directory'
dinfo = read_directory(path)
print(dinfo.items())


def format_bytes(byte):
    if 1024 <= byte < 1024 ** 2:
        output = byte / 1024
        if byte % 1024 == 0:
            return f'{int(output)}KiB'
        else:
            return f'{output:.2f}KiB'
    elif 1024 ** 2 <= byte < 1024 ** 3:
        output = byte / 1024 ** 2
        if byte % 1024 ** 2 == 0:
            return f'{int(output)}MiB'
        else:
            return f'{output:.2f}MiB'
    elif 1024 ** 3 <= byte:
        output = byte / 1024 ** 3
        if byte % 1024 ** 3 == 0:
            return f'{int(output)}GiB'
        else:
            return f'{output:.2f}GiB'
    else:
        return f'{byte}B'


def show_directory_info(path, dinfo):
    print(f'{path}: {format_bytes(sum(dinfo.values()))}')
    key_list = [x for x in dinfo.keys()]
    values = [x for x in dinfo.values()]
    values = sorted(values, reverse=True)
    for i in values:
        if i != values[-1]:
            print(f'|-- {list(dinfo.keys())[list(dinfo.values()).index(i)]}: {format_bytes(i)}')
        else:
            print(f'+-- {list(dinfo.keys())[list(dinfo.values()).index(i)]}: {format_bytes(i)}')

show_directory_info(path, dinfo)
