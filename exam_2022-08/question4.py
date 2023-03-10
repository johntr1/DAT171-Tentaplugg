
from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def escaped_name(self):
        s = ""
        for i in self.name:
            if i == "&":
                s += "&amp"
            elif i == '"':
                s += "&quot"
            elif i == "'":
                s += '&apos'
            elif i == "<":
                s += "&lt"
            elif i == ">":
                s += "&gt"
            else:
                s += i
        return s

    @abstractmethod
    def xml_structure(self, indent=0):
        pass

    @abstractmethod
    def __len__(self):
        pass


class Directory(Node):
    def __init__(self, name, nodes):
        super().__init__(name)
        self.nodes = nodes

    def xml_structure(self, indent=0):
        indents = ' ' * indent
        output = f'{indents}<directory name="{self.escaped_name()}"\n'
        for node in self.nodes:
            output += node.xml_structure(indent + 4)
        output += ' ' * indent + '</directory>\n'
        return output

    def add_node(self, node):
        return self.nodes.append(node)

    def __len__(self):
        return sum([len(n) for n in self.nodes]) + 1


class File(Node):
    def __init__(self, name, binary=True):
        super().__init__(name)
        self.binary = binary

    def __len__(self):
        return 1

    def xml_structure(self, indent=0):
        indents = ' ' * indent
        if self.binary is True:
            affirm = 'yes'
        else:
            affirm = 'no'
        output = f'{indents}<file name="{self.escaped_name()}" binary="{affirm}" />\n'
        return output


some_files = [File('Important data.dat', True), File('"Quotes" & jokes.txt', False)]
some_code = [File('important_python_code.py', False), File('cheat_sheet.py', False)]
code_dir = Directory('Code', some_code)
root = Directory('Directories can also have \'escaped\' characters', some_files)
root.add_node(code_dir)
print(root.xml_structure())
print("Total number of nodes in the tree is {}".format(len(root)))



