import math

import matplotlib.pyplot as plt
import numpy
import statistics
from math import comb
from scipy.stats import binom

import numpy as np
from scipy import stats
from scipy.stats import poisson, hypergeom, geom

def stichprobe():
    n, p = 1000, 0.005
    r = binom(n, p)
    print('Binomial-Verteilt: genau', r.pmf(0))  # von n mehr als x tritt ein (binomial)
    print('Binomial-Verteilt: mehr als', 1-r.cdf(1)) #von n mehr als x tritt ein (binomial)
    print('Binomial-Verteilt: weniger als', r.cdf(8)) #von n weniger als x tritt ein (binomial)
    print('Binomial-Verteilt: Erwartungswert bie n beobachtungen binomial:', n*p)
    print('Binomial-Verteilt Mittelwert:', r.mean())
    print('Binomial-Verteilt Varianz:', r.var())

    print()
    #Poisson Verteilung
    #Eintritte eines Ereignis innerhalb eines Intervalls (Popcornmaschine welche 3 mal Pro woche ausfällt, Z = Anzahl an Ausfällen pro Woche)
    x = 3.5
    z = poisson(x) # zwischen 20 und 21 Uhr rufen durchschnittlich x personen an,
    print('Poisson-Verteilt: genau', z.pmf(10)) # wie ist die Wahrscheinlichkeit dass genau z.B. 3 personen anrufen
    print('Poisson-Verteilt: mehr als', 1-z.cdf(0))
    print('Poisson-Verteilt: weniger inklusive', z.cdf(1))
    print('Poisson-Verteilt Mittelwert(Erwartungswert):', z.mean()) #E(B)
    print('Poisson-Verteilt Varianz:', z.var()) #Var(B)

    print()
    #geometrisch Verteilt
    #Anzahl an Wiederholungen bis 1 Ereignis mit Wahrscheinlichkeit p= z.B. 0.1 eintritt
    p = 0.15
    e = 3 #Anazahl Wiederholungen bis das erste Ereigniss eintritt
    g = geom(p)
    print('Geometrisch-Verteilt: genau e betrachten bis Ereignis eintritt', g.pmf(e))
    print('Geometrisch-Verteilt: höchstens e betrachten bis Ereignis eintritt', g.cdf(e))
    print('Geometrisch-Verteilt: Erwartungswert für n beobachtungen bis Ereignis p Eintritt:', 1/p)
    print('Geometrische Verteilung Varianz:', g.var())

#Ungleichung von Chebychev
# Liegt ein Schiff Außerhalb der Fahrrinne mit einer Abweichungsvarianz von z.B. Var(X) = 7?
def chebyev(var, k):
    return var/k**2 #k ist die ober und untergrenze

if __name__ == '__main__':
    stichprobe()
    print('chebyev wahrscheinlichkeit dass außerhalb varianz in Prozent:', chebyev(10, 5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
