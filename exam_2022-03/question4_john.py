import abc


class TUIWidget(metaclass=abc.ABCMeta):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    @abc.abstractmethod
    def render(self):
        pass

    def show(self):
        for line in self.render():
            print(line)


class ProgressBar(TUIWidget):
    def __init__(self, columns, progress: float = 0):
        super().__init__(1, columns)
        self.progress = progress

    def set_progress(self, progress: float):
        self.progress = progress

    def render(self):
        tags = round((self.columns - 2) * self.progress)
        rest = self.columns - 2 - tags
        print(self.columns)
        print(tags)
        print(rest)
        return ['[' + tags * '#' + ' ' * rest + ']']


class TextField(TUIWidget):
    def __init__(self, rows, columns, text: str = ''):
        super().__init__(rows, columns)
        self.text = text

    def render(self):
        txt_li = []
        for i in range(self.rows):
            txt_li.append(self.text[self.columns*i:self.columns*(i+1)])
        return txt_li

    def


t = TextField(3, 20, 'Learning Python sure is fun. Even the exam is fun! Not all text fits')
t.show()

# Use Slicing!