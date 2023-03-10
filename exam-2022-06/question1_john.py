def camel_caser(string):
    str_list = string.split('_')
    new_list = []
    for i, element in enumerate(str_list):
        letter = element.capitalize()
        new_list.append(letter)
    return ''.join(new_list)


input_file = 'student_code.py'
output_file = 'readable_file.py'

with open(input_file, mode='r') as inp:
    with open(output_file, mode='w') as out:
        line = inp.readline()
        while line:
            line_list = line.split(' ')
            if line_list[0] == 'class':
                line_list[1] = camel_caser(line_list[1])
                output_string = ' '.join(line_list)
                out.write(f'{output_string}\n')
                line = inp.readline()
            else:
                output_string = line
                out.write(f'{output_string}\n')
                line = inp.readline()
        out.close()
    inp.close()





