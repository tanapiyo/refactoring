from csv_reader import CSVTablePrinter
from csv_reader import CSVTreePrinter


def execute():
    printer = CSVTablePrinter(
        'おはよう,Good Morning\nこんにちは,Good Afternoon\nこんばんは,Good Evening')
    printer.print()
    printer.close()

    printer = CSVTreePrinter('sec15.csv')
    printer.print()
    printer.close()


if __name__ == "__main__":
    execute()
