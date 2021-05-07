class Printer(object):
    """docstring for Printer"""
    def log(self, *values):
        print(values)

class FormattedPrinter(Printer):
    """docstring for FormattedPrinter"""
    def log(self, *values):
        print(f'*'* 4 * len(values))
        print(f'* {values} *')
        print(f'*'* 4 * len(values))


R = FormattedPrinter()
R.log(1, 2, 3, 4, 5)