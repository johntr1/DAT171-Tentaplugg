import abc
from abc import ABC
import enum as Enum
from datetime import datetime


class Writer(metaclass=abc.ABCMeta):
    def __init__(self, file):
        self.file = file

    @abc.abstractmethod
    def write_line(self, text):
        pass

    @abc.abstractmethod
    def flush(self):
        pass


class DirectFileWriter(Writer, ABC):
    def __init__(self, file):
        super().__init__(file)
        self.file = open(file, mode='w')

    def write_line(self, text):
        return self.file.write(text + '\n')

    def flush(self):
        return self.file.flush()


class CircularWriter(Writer, ABC):
    def __init__(self, N, file):
        super().__init__(file)
        self.n = N
        self.pos = 0
        self.buffer = [None] * self.n

    def write_line(self, text):
        if self.pos == self.n:
            self.pos = 0
        self.buffer[self.pos] = text
        self.pos += 1

    def flush(self):
        with open(self.file, mode='w') as file:
            for line in self.buffer[self.pos:]:
                if line:
                    file.write(line + '\n')
            for line in self.buffer[:self.pos]:
                file.write(line + '\n')
            """
            for i in self.buffer:
                if i is not None:
                    file.write(i + '\n')
            """


class LogLevel(Enum.IntEnum):
    DEBUG = 0
    WARNING = 1
    ERROR = 2


class Logger:
    def __init__(self, name, level, date, writer):
        self.name = name
        self.level = level
        self.date = date
        self.writer = writer

    def log(self, level, msg):
        time_stamp = datetime.now()
        if level >= self.level:
            output = f'{time_stamp.strftime("%Y-%m-%dT%H:%M:%S")} Name::{self.name} - {msg}'
            return self.writer.write_line(output)
        else:
            return None


# Either writer should work for your logger:
use_circular = True
if use_circular:
    # We test it with a very small circular array:
    writer = CircularWriter(5, 'logfile.txt')
else:
    writer = DirectFileWriter('logfile.txt')
# We choose to store microseconds in this example since the test example is so brief:
logger = Logger('MyProgram', LogLevel.WARNING, '%Y-%m-%dT%H:%M:%S.%f', writer)
logger.log(LogLevel.DEBUG, 'This debug message should be ignored!')
for i in range(10):
    logger.log(LogLevel.WARNING, 'Testing {}'.format(i))
    logger.log(LogLevel.ERROR, 'This error should be printed last in the file.')
    logger.log(LogLevel.DEBUG, 'And this shouldn\'t be in the file at all.')
# Force flush the buffer before exiting to ensure everything is written to file:
writer.flush()
