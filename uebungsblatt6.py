# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy
from math import comb

import numpy as np
from scipy import stats
from scipy.stats import poisson, hypergeom


def fuenfpunkteins():
#5.1
    #c)
    n, p = 5, 0.1
    x = stats.binom(n, p)
    print(x.cdf(2))
    print(1-x.cdf(2))
    #d)
    print("Erwartungswert???", x.mean()) #mean() Erwartungswert

def fuenfpunktdrei():
#5.3
    #a)
    n, p = 5, 1/5
    x = stats.binom(n, p)
    print("Genau 3 Kunden rufen an", x.pmf(3))
    #b)
    print("Die Hotline ist überlastet", 1-x.cdf(4))

#5.4
def fuenfpunktvier():
    n, p = 50, 0.1
    x = stats.binom(n, p)
    #a)
    print("mehr als 2 Fahrzeuge", 1-x.cdf(2))
    #b)
    print("Erwartungswert???", n*p)
    #c)???
    print("???", x.pmf(5))
    #d)???
    print("???", x.pmf(1))

#5.6
def fuenfpunktsechs():
    #a)
    n, p = 10, 0.3
    x = stats.binom(n, p)
    print("weniger als 3 strikes", x.cdf(2))
    #b)
    x, mu = 0, 1#x = Anzahl Ausfaelle/Bus kommt & mu = ca. wie offt es ausfaellt(Ausfallrate/wie offt der bus ca. kommt)
    print("Ein bus faellt zu", poisson.pmf(x, mu), "aus")
    #c)????
    n, p = 3, 0.2
    x = stats.binom(n, p)
    print("weniger als 4 Schachteln", 1-x.cdf(0))#?????
    #d)falsch
    r = hypergeom(60, 10, 3)
    print(r)
    #hypergeometrisch

#aufgabe 5.15 machen




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fuenfpunkteins()
    fuenfpunktdrei()
    fuenfpunktvier()
    fuenfpunktsechs()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
