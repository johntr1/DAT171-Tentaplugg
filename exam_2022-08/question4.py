class Node:
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
