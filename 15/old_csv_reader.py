from abc import ABCMeta, abstractmethod
import csv


class CSVReader(metaclass=ABCMeta):

    @abstractmethod
    def readCSV(self):
        pass

    @abstractmethod
    def close(self):
        pass


class CSVStringReader(CSVReader):

    def __init__(self, s):
        self._reader = csv.reader(s.strip().splitlines())

    def readCSV(self):
        return self._reader

    def close(self):
        pass


class CSVFileReader(CSVReader):

    def __init__(self, file_name):
        self._f = open(file_name, 'r')
        reader = csv.reader(self._f)
        lines = []
        for line in reader:
            lines.append(line)
        self._lines = lines
        self._line_counter = 0

    def readCSV(self):
        if len(self._lines) <= self._line_counter:
            return None
        line = self._lines[self._line_counter]
        self._line_counter += 1
        return line

    def close(self):
        self._f.close()


class CSVStringTablePrinter(CSVStringReader):

    def print(self):
        print('<table>')
        lines = self.readCSV()
        if lines is None:
            return
        for line in lines:
            print('<tr>')
            for element in line:
                print('<td>')
                print(element)
                print('</td>')
            print('</tr>')
        print('</table>')


class CSVFileTreePrinter(CSVFileReader):

    def print(self):
        prev_item = []
        while True:
            line = self.readCSV()
            if line is None:
                return
            just_print = False
            for i, item in enumerate(line):
                if just_print is True:
                    self.print_line(i, item)
                elif len(prev_item) <= i or item != prev_item[i]:
                    self.print_line(i, item)
                    just_print = True
            prev_item = line

    def print_line(self, indent, s):
        for _i in range(indent):
            print('    ', end='')
        print(s)
