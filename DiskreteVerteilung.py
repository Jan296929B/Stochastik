import math

import matplotlib.pyplot as plt
import numpy
import statistics
from math import comb
from scipy.stats import binom

import numpy as np
from scipy import stats
from scipy.stats import poisson, hypergeom, geom
#from icecream import ic

def stichprobe():
    # 1 ----- Bernoulli Verteilung ---------
    # --------------------------------------
    #
    #           Wurf einer Münze
    #           Verschicken von 50 Datenpaketen
    #
    #           p = Wahrscheinlichkeit, dass etwas eintritt
    #           X ~ Ber(p)
    p_1 = 0.7
    x_1 = 0

    print("BERNOULLI")
    print(
        "P(X = x)      --> Wahrscheinlichkeit, für genau X",
        stats.bernoulli(p_1).pmf(x_1),

        "\nP(X <= x)     --> Wahrscheinlichkeit, für mindestens",
        stats.bernoulli(p_1).cdf(x_1),
        "\nhöchstens X",
        1 - stats.bernoulli(p_1).cdf(x_1),

        "\nErwartungswert",
        stats.bernoulli(p_1).expect(),

        "\nVarianz",
        stats.bernoulli(p_1).var(),
    )
    #Binomial Verteilung
    n, p = 11, 0.55
    r = binom(n, p)
    print('\nBinomial-Verteilt: genau', r.pmf(0))  # von n mehr als x tritt ein (binomial)
    print('Binomial-Verteilt: mehr als', 1-r.cdf(1)) #von n mehr als x tritt ein (binomial)
    print('Binomial-Verteilt: weniger als', r.cdf(8)) #von n weniger als x tritt ein (binomial)
    print('Binomial-Verteilt: zwischen', r.cdf(8)-r.cdf(5))
    print('Binomial-Verteilt: Erwartungswert bie n beobachtungen binomial:', n*p)
    print('Binomial-Verteilt Mittelwert:', r.mean())
    print('Binomial-Verteilt Varianz:', r.var())

    print()
    #Poisson Verteilung
    #Eintritte eines Ereignis innerhalb eines Intervalls (Popcornmaschine welche 3 mal Pro woche ausfällt, Z = Anzahl an Ausfällen pro Woche)
    x = 7
    z = poisson(x) # zwischen 20 und 21 Uhr rufen durchschnittlich x personen an,
    print('Poisson-Verteilt: genau', z.pmf(1)) # wie ist die Wahrscheinlichkeit dass genau z.B. 3 personen anrufen
    print('Poisson-Verteilt: mehr als', 1-z.cdf(0))
    print('Poisson-Verteilt: weniger inklusive', z.cdf(8))

    print('Poisson-Verteilt: zwischen', z.cdf(8) - z.cdf(5))
    print('Poisson-Verteilt Mittelwert(Erwartungswert):', z.mean()) #E(B)
    print('Poisson-Verteilt Varianz:', z.var()) #Var(B)

    print()
    #geometrisch Verteilt
    #Anzahl an Wiederholungen bis 1 Ereignis mit Wahrscheinlichkeit p= z.B. 0.1 eintritt
    p = 0.34
    e = 2
    #Anazahl Wiederholungen bis das erste Ereigniss eintritt
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
