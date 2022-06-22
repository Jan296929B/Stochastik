# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy

def print_hi():
    n = 33.3
    l = 1/2
    e = (n-0)**2*l+(n-1)**2*l+(n-99)**2*l
    k = (n - 25) ** 2 * l + (n - 30) ** 2 * l + (n - 45) ** 2 * l
    print('varianz', e)
    print('stdabweichung', numpy.sqrt(e))
    print('varianz', k)
    print('stdabweichung', numpy.sqrt(k))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
